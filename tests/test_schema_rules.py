"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
import keyword
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
SOURCE_DIR = ROOT / "src" / "cve" / "schema"
COPY = ROOT / ".lokf" / "cve.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour, each under another IRI there. LinkML
# keeps one namespace, and the JSON-LD context gives each key one IRI across a
# composite, so in a host that imports both copies one of them projects under the
# other's IRI. These are the upstream's own keys, which a real record needs, so
# they are not renamed here; lokf issue #169 asks `lokf adapt` for a --beside
# option that would rename them in the copy. A new overlap fails this test. No
# class, enum or type is shared, since each carries the Cve or Cvss prefix or the
# cve_ prefix.
SHARED_WITH_NEIGHBOURS = {
    "github-actions.yaml": set(),
    "in-toto.yaml": {"content", "value"},
    "oscal.yaml": {"base64", "state", "value"},
    "slsa.yaml": {"content", "value"},
    "spdx.yaml": {"scope", "value", "vectorString"},
    "stix.yaml": {
        "content",
        "descriptions",
        "lang",
        "modules",
        "product",
        "value",
        "vendor",
    },
    "uco.yaml": {"dataType", "descriptions", "format", "state", "value"},
}

# The class `just lokf-adapt` re-roots on Concept. A concept names one of its two
# concrete kinds, which the README lists for the plugins' Known LOKF types setting.
ROOTS = {"CveRecord"}
CONCEPT_TYPES = {"CvePublishedRecord", "CveRejectedRecord"}

# What the copy renames because LOKF defines the name, each keeping the IRI the
# source gives it. The source makes each a top-level slot with its own slot_uri for
# this reason, since adapt never renames an attribute.
RENAMED = {
    name: f"cve_{name}"
    for name in (
        "at",
        "description",
        "name",
        "references",
        "source",
        "status",
        "tags",
        "title",
        "type",
        "url",
        "version",
    )
}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _load(path):
    return yaml.safe_load(path.read_text())


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _terms(doc):
    """The IRI of every class, slot, attribute, enum and type a schema file
    declares, each its own URI or the default prefix and its name."""
    expand = _expander(doc)
    default = doc.get("default_prefix")
    terms = set()
    for kind, uri_key in (
        ("classes", "class_uri"),
        ("slots", "slot_uri"),
        ("enums", "enum_uri"),
        ("types", "uri"),
    ):
        for name, element in (doc.get(kind) or {}).items():
            terms.add(expand((element or {}).get(uri_key) or f"{default}:{name}"))
    for cls in (doc.get("classes") or {}).values():
        for name, slot in ((cls or {}).get("attributes") or {}).items():
            terms.add(expand((slot or {}).get("slot_uri") or f"{default}:{name}"))
    return terms


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def _source():
    """The source's three modules, merged by element kind."""
    merged = {"classes": {}, "slots": {}, "prefixes": {}, "enums": {}, "types": {}}
    for path in sorted(SOURCE_DIR.glob("*.yaml")):
        doc = _load(path)
        for kind, elements in merged.items():
            elements.update(doc.get(kind) or {})
    return merged


def test_the_copy_renames_what_lokf_defines_and_keeps_the_iris():
    """Each slot LOKF also defines is renamed with its source IRI, and no other
    slot or class is renamed."""
    source, copy = _source(), _load(COPY)
    expand_source, expand_copy = _expander(source), _expander(copy)
    for old, new in RENAMED.items():
        assert new in copy["slots"] and old not in copy["slots"], old
        assert expand_copy(copy["slots"][new]["slot_uri"]) == expand_source(
            source["slots"][old]["slot_uri"]
        ), old
    assert set(copy["slots"]) == (set(source["slots"]) - set(RENAMED)) | set(
        RENAMED.values()
    )
    assert set(copy["classes"]) == set(source["classes"])


def test_every_key_lokf_defines_is_top_level_in_the_source():
    """adapt renames a top-level slot and never an attribute, so an attribute named
    like one of LOKF's slots would keep that name in the copy."""
    source = _source()
    lokf_slots = set(_load(LOKF)["slots"])
    assert set(RENAMED) == set(source["slots"]) & lokf_slots
    for name, cls in source["classes"].items():
        assert not set(cls.get("attributes") or {}) & lokf_slots, name


def test_the_real_records_keep_their_keys_in_the_source():
    """A renamed key is renamed in the copy alone: the source keeps the upstream's."""
    source = _source()
    for name in RENAMED:
        assert name in source["slots"], name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the record base on Concept, keeps its two kinds
    under it, leaves the tree root out of the concept types, and imports nothing
    but the LinkML types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    for name in CONCEPT_TYPES:
        assert doc["classes"][name]["is_a"] == "CveRecord", name
    assert doc["imports"] == ["linkml:types", "lokf"]
    assert not doc["classes"]["CveRecordRoot"].get("tree_root")


def test_the_readme_lists_the_concept_types():
    """The README's Known LOKF types block names each class a concept may use."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in CONCEPT_TYPES:
        assert name in readme, name


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_each_mapping_into_a_neighbour_names_a_term_it_declares():
    """A mapping into a released neighbour's own namespace names a term its copy
    declares. tests/test_mappings.py checks the rest against their files."""
    doc = _load(COPY)
    expand = _expander(doc)
    namespaces = {}
    for name in NEIGHBOURS:
        theirs = _load(NEIGHBOUR_DIR / name)
        default = theirs.get("default_prefix")
        namespace = (theirs.get("prefixes") or {}).get(default)
        if namespace:
            namespaces[namespace] = (name, _terms(theirs))
    mapped_into = 0
    for mapping in _mappings(doc):
        iri = expand(mapping)
        for namespace, (name, terms) in namespaces.items():
            if iri.startswith(namespace):
                assert iri in terms, (mapping, name)
                mapped_into += 1
    assert mapped_into >= 2


def _page_names(source):
    """The name of each page gen-doc writes for an element of the source."""
    names = set(source["classes"]) | set(source["enums"]) | set(source["slots"])
    names |= {
        "".join(part.title() for part in name.split("_")) for name in source["types"]
    }
    for cls in source["classes"].values():
        names |= set(cls.get("attributes") or {})
    return names


def test_no_two_pages_differ_only_by_case():
    """gen-doc writes a page per element, and two names that differ only by case
    are one file on a case-insensitive disk. A slot keeps the upstream's key, so a
    class or type gives way. The one left is `time`, a key of the upstream's, beside
    the `Time` page of LinkML's own types, which a schema cannot rename."""
    source = _source()
    names = _page_names(source) | {"Time"}
    lowered = {}
    for name in names:
        lowered.setdefault(name.lower(), set()).add(name)
    collisions = {key: found for key, found in lowered.items() if len(found) > 1}
    assert collisions == {"time": {"time", "Time"}}


def test_no_page_overwrites_the_index():
    """A slot named index would overwrite the docs site's index page."""
    assert "index" not in {name.lower() for name in _page_names(_source())}


def test_no_slot_is_a_python_keyword():
    """A slot named after a Python keyword breaks the generated dataclasses."""
    source = _source()
    slots = set(source["slots"])
    for cls in source["classes"].values():
        slots |= set(cls.get("attributes") or {})
    assert not {name for name in slots if keyword.iskeyword(name)}
