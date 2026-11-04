"""Coverage: the schema against the upstream's JSON schemas, in both directions.

These tests walk the copies in upstream/ beside the LinkML classes. They fail if
any definition, property, enum value or required key has no element here, if an
element has no counterpart there, or if a cardinality, pattern, bound or default
differs. Each departure is stated here with its reason:

- A CVSS 3.0, 3.1 or 4.0 score: the upstream lists 0.0 to 10.0 by 0.1, which no
  LinkML range states. The slot holds the bounds, and tests/cve_rules.py the grid.
- A key with both a pattern and lengths: LinkML has one pattern per slot, so
  tests/cve_rules.py holds the lengths.
- ``uniqueItems``, ``minProperties`` and ``patternProperties``: on the schema where
  the metamodel can say them, and checked in tests/cve_rules.py, since no
  generator writes them.
- An optional key may be null in the generated JSON Schema, and never upstream.
  tests/cve_rules.py refuses it.
- CVSS severity bands: rules on a mixin, not the upstream's score and severity
  definitions, which ``DEFINITIONS_WITHOUT_AN_ELEMENT`` lists.
- The upstream's cpe objects state no type, so a value that is not an object passes
  them. The generated class asks for an object, which no real record differs on.
"""

import re
from functools import cache
from pathlib import Path

import pytest
from linkml_runtime import SchemaView

from tests import upstream_schemas
from tests.cve_rules import (
    AT_LEAST_ONE_KEY,
    EXTENSION_CLASSES,
    GRID_CLASSES,
    LENGTH_BESIDE_PATTERN,
)

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cve" / "schema" / "cve.yaml"
RECORD = upstream_schemas.RECORD_FORMAT

# The roots of the walk: each is an object in the upstream's files and the class
# that renders it. The walk reaches everything else from these.
ROOTS = {
    f"{RECORD}#/oneOf/0": "CvePublishedRecord",
    f"{RECORD}#/oneOf/1": "CveRejectedRecord",
    "imports/cvss/cvss-v2.0.json#/": "CvssV20",
    "imports/cvss/cvss-v3.0.json#/": "CvssV30",
    "imports/cvss/cvss-v3.1.json#/": "CvssV31",
    "imports/cvss/cvss-v4.0.json#/": "CvssV40",
}

# Definitions with no element of their own, and why.
BANDS = "the rules of CvssSeverityBandsMixin state it"
DEFINITIONS_WITHOUT_AN_ELEMENT = {
    f"imports/cvss/cvss-v{version}.json#/definitions/{name}": BANDS
    for version in ("3.0", "3.1", "4.0")
    for name in (
        "noneScoreType",
        "lowScoreType",
        "mediumScoreType",
        "highScoreType",
        "criticalScoreType",
        "noneSeverityType",
        "lowSeverityType",
        "mediumSeverityType",
        "highSeverityType",
        "criticalSeverityType",
    )
}

LENGTH_TYPE = re.compile(r"^\^\[\\s\\S\]\{(\d+),(\d+)\}\$$")


@cache
def view():
    return SchemaView(str(SCHEMA))


def deref(node, path):
    """Follow a node's references, keeping the file each one lands in."""
    while "$ref" in node:
        ref = node["$ref"]
        if ref.startswith("file:"):
            path = ref.removeprefix("file:") + "#/"
        else:
            path = path.split("#")[0] + ref
        node = upstream_schemas.resolve_pointer(path)
    return node, path


def walk(node, class_name, path, problems):
    """Compare one upstream object with the class that renders it."""
    properties = node.get("properties", {})
    slots = {s.name: s for s in view().class_induced_slots(class_name)}
    cls = view().get_class(class_name)
    for key in properties.keys() - slots.keys():
        problems.append(f"{path}: {class_name} has no slot {key}")
    for key in slots.keys() - properties.keys():
        problems.append(f"{path}: {class_name}.{key} is not in the upstream")
    required = set(node.get("required", []))
    # A choice of shapes may state its required keys inside each branch; what
    # every branch requires is required. tests/test_data.py compares the choice
    # itself with the upstream's, for every mix of keys.
    if "oneOf" in node:
        required |= set.intersection(
            *(set(b.get("required", [])) for b in node["oneOf"])
        )
    for key in required ^ {name for name, slot in slots.items() if slot.required}:
        problems.append(f"{path}: {class_name}.{key} differs on required")
    open_here = bool(cls.extra_slots and cls.extra_slots.allowed)
    open_there = (
        node.get("additionalProperties") is not False or "patternProperties" in node
    )
    if open_here != open_there:
        problems.append(f"{path}: {class_name} differs on closure")
    if "patternProperties" in node:
        pattern = next(iter(node["patternProperties"]))
        if pattern != r"^x_[^.]*$" or class_name not in EXTENSION_CLASSES:
            problems.append(f"{path}: {class_name} has an unlisted patternProperties")
    if "minProperties" in node and class_name not in AT_LEAST_ONE_KEY | {
        "CveAdpContainer"
    }:
        problems.append(f"{path}: {class_name} has an unlisted minProperties")
    for key in properties.keys() & slots.keys():
        compare(
            properties[key],
            slots[key],
            class_name,
            f"{path}/properties/{key}",
            problems,
        )


def compare(node, slot, class_name, path, problems):
    """Compare one upstream property with the slot that renders it."""
    node, target = deref(node, path)
    name = f"{class_name}.{slot.name}"
    if node.get("type") == "array":
        if not slot.multivalued:
            problems.append(f"{path}: {name} is not multivalued")
        for up, here in (
            ("minItems", slot.minimum_cardinality),
            ("maxItems", slot.maximum_cardinality),
        ):
            if node.get(up) != here:
                problems.append(f"{path}: {name} {up} {node.get(up)} is {here} here")
        if bool(node.get("uniqueItems")) != bool(slot.list_elements_unique):
            problems.append(f"{path}: {name} differs on uniqueItems")
        compare_value(
            node["items"], slot, class_name, f"{target}/items", path, problems
        )
    else:
        if slot.multivalued:
            problems.append(f"{path}: {name} is multivalued here")
        compare_value(node, slot, class_name, target, path, problems)
    if "contains" in node:
        contained, _ = deref(node["contains"], target)
        if contained["required"] != ["lang"] or not slot.has_member:
            problems.append(f"{path}: {name} has lost its rule on English")
    elif slot.has_member:
        problems.append(f"{path}: {name} has a rule on its members the upstream lacks")


def compare_value(node, slot, class_name, target, path, problems):
    node, target = deref(node, target)
    name = f"{class_name}.{slot.name}"
    range_name = slot.range
    if "oneOf" in node and "properties" not in node:
        # Only a tag has this shape: the publisher's own form, or the upstream's list.
        alternatives = [deref(alt, target) for alt in node["oneOf"]]
        ranges = {alt.range for alt in slot.any_of}
        values = next(alt["enum"] for alt, _ in alternatives if "enum" in alt)
        enums = ranges & view().all_enums().keys()
        if len(enums) != 1 or "cve_tag_extension" not in ranges:
            problems.append(f"{path}: {name} is not an enum or an extension tag")
            return
        compare_values(values, next(iter(enums)), name, path, problems)
        return
    if "enum" in node and node.get("type") == "number":
        # The upstream lists 0.0 to 10.0 by 0.1, which no LinkML range states:
        # the bounds are on the slot, and tests/cve_rules.py checks the grid.
        if class_name not in GRID_CLASSES or (
            slot.minimum_value,
            slot.maximum_value,
        ) != (0, 10):
            problems.append(f"{path}: {name} has lost its grid of scores")
        return
    if node.get("type") == "number":
        for up, here in (
            ("minimum", slot.minimum_value),
            ("maximum", slot.maximum_value),
        ):
            if node.get(up) != here:
                problems.append(f"{path}: {name} {up} {node.get(up)} is {here} here")
        return
    if "enum" in node:
        if slot.equals_string is not None:
            if node["enum"] != [slot.equals_string]:
                problems.append(
                    f"{path}: {name} is {slot.equals_string}, not {node['enum']}"
                )
        elif range_name in view().all_enums():
            compare_values(node["enum"], range_name, name, path, problems)
        else:
            problems.append(f"{path}: {name} has no enum")
        compare_default(node, slot, range_name, name, path, problems)
        return
    if node.get("type") == "object" or "properties" in node:
        if range_name not in view().all_classes():
            problems.append(f"{path}: {name} does not range over a class")
            return
        walk(node, range_name, target, problems)
        return
    if node.get("type") == "boolean":
        if range_name != "boolean":
            problems.append(f"{path}: {name} is not boolean")
        compare_default(node, slot, range_name, name, path, problems)
        return
    if node.get("type") == "integer":
        if range_name != "integer" or node.get("minimum") != slot.minimum_value:
            problems.append(f"{path}: {name} differs on its integer")
        return
    compare_string(node, slot, class_name, path, problems)


def compare_values(values, enum_name, name, path, problems):
    here = set(view().get_enum(enum_name).permissible_values)
    if set(values) != here:
        problems.append(
            f"{path}: {name} {enum_name} differs: {sorted(set(values) ^ here)}"
        )


def compare_default(node, slot, range_name, name, path, problems):
    default = node.get("default")
    if default is None:
        if slot.ifabsent:
            problems.append(f"{path}: {name} has a default the upstream lacks")
        return
    expected = (
        f"{range_name}({default})"
        if range_name in view().all_enums()
        else str(default).lower()
    )
    if str(slot.ifabsent).lower() != expected.lower():
        problems.append(f"{path}: {name} default {default} is {slot.ifabsent} here")


def compare_string(node, slot, class_name, path, problems):
    name = f"{class_name}.{slot.name}"
    # The upstream states a default on some required strings, such as lang and
    # dataVersion. It can never apply, so no ifabsent says it here.
    if "default" in node and not slot.required:
        problems.append(f"{path}: {name} has a default on an optional string")
    type_def = view().get_type(slot.range) if slot.range in view().all_types() else None
    pattern_here = slot.pattern or (type_def.pattern if type_def else None)
    bounds = (node.get("minLength", 0), node.get("maxLength"))
    if "pattern" in node:
        if node["pattern"] != pattern_here:
            problems.append(f"{path}: {name} has another pattern")
        if (
            "maxLength" in node
            and LENGTH_BESIDE_PATTERN.get((class_name, slot.name)) != bounds
        ):
            problems.append(
                f"{path}: {name} lengths {bounds} are not in tests/cve_rules.py"
            )
    elif "maxLength" in node:
        match = LENGTH_TYPE.match(pattern_here or "")
        if not match or (int(match[1]), int(match[2])) != bounds:
            problems.append(f"{path}: {name} lengths {bounds} are not {pattern_here}")
    elif pattern_here:
        problems.append(f"{path}: {name} has a pattern the upstream lacks")
    if node.get("format") == "uri" and slot.range != "cve_uri":
        problems.append(f"{path}: {name} is not an address")
    if node.get("format") not in (None, "uri"):
        problems.append(f"{path}: {name} has format {node['format']}")


def all_annotated_paths():
    """Every upstream path that an element of the schema names."""
    found = set()
    elements = [
        *view().all_classes().values(),
        *view().all_slots().values(),
        *view().all_enums().values(),
        *view().all_types().values(),
    ]
    for cls in view().all_classes().values():
        elements += list(cls.attributes.values())
    for element in elements:
        annotation = element.annotations.get("upstream_path")
        if annotation:
            found |= set(annotation.value.split())
    return found


def test_every_upstream_object_is_rendered_in_both_directions():
    """The walk finds no property, value or required key without its element,
    and no element without its property."""
    problems = []
    for path, class_name in ROOTS.items():
        walk(upstream_schemas.resolve_pointer(path), class_name, path, problems)
    assert not problems, "\n".join(problems)


def test_a_record_is_exactly_one_of_two_kinds():
    """The upstream's oneOf has two members, and the tree root names both."""
    upstream = upstream_schemas.load(RECORD)
    assert [branch["title"] for branch in upstream["oneOf"]] == [
        "Published",
        "Rejected",
    ]
    root = view().get_class("CveRecordRoot")
    assert root.tree_root
    assert [c.is_a for c in root.exactly_one_of] == [
        "CvePublishedRecord",
        "CveRejectedRecord",
    ]


@pytest.mark.parametrize(
    "name",
    [
        RECORD,
        "imports/cvss/cvss-v2.0.json",
        "imports/cvss/cvss-v3.0.json",
        "imports/cvss/cvss-v3.1.json",
        "imports/cvss/cvss-v4.0.json",
    ],
)
def test_every_definition_has_an_element(name):
    """Every definition of each file is named by an element's upstream_path, or
    listed above with its reason."""
    annotated = all_annotated_paths()
    missing = [
        definition
        for definition in upstream_schemas.load(name)["definitions"]
        if f"{name}#/definitions/{definition}" not in annotated
        and f"{name}#/definitions/{definition}" not in DEFINITIONS_WITHOUT_AN_ELEMENT
    ]
    assert not missing, missing


def test_listed_definitions_exist():
    """Nothing is excused that the upstream does not define."""
    for path in DEFINITIONS_WITHOUT_AN_ELEMENT:
        upstream_schemas.resolve_pointer(path)


def test_every_annotated_path_exists():
    """An upstream_path names a real place in the upstream's files."""
    for path in all_annotated_paths():
        upstream_schemas.resolve_pointer(path)


def test_each_class_and_enum_names_its_upstream_path():
    """Every class and enum says what it renders, apart from the enum that gathers
    the two states for the base class."""
    missing = [
        name
        for name, element in {**view().all_classes(), **view().all_enums()}.items()
        if "upstream_path" not in element.annotations and name != "CveRecordState"
    ]
    assert not missing, missing


def test_tag_lists_are_rendered_whole():
    """Each tag file's values are one enum's permissible values."""
    for enum_name, name in (
        ("CveCnaTag", "tags/cna-tags.json"),
        ("CveAdpTag", "tags/adp-tags.json"),
        ("CveReferenceTag", "tags/reference-tags.json"),
    ):
        values = set(upstream_schemas.load(name)["enum"])
        assert values == set(view().get_enum(enum_name).permissible_values), enum_name


def test_the_score_rules_cover_the_bands_the_upstream_states():
    """The mixin's five rules give each severity the lowest and highest score the
    upstream's definitions list for it."""
    for version in ("3.0", "3.1", "4.0"):
        definitions = upstream_schemas.load(f"imports/cvss/cvss-v{version}.json")[
            "definitions"
        ]
        for rule in view().get_class("CvssSeverityBandsMixin").rules:
            severity = rule.preconditions.slot_conditions["baseSeverity"].equals_string
            scores = definitions[f"{severity.lower()}ScoreType"]
            low, high = (
                (min(scores["enum"]), max(scores["enum"]))
                if "enum" in scores
                else (scores["minimum"], scores["maximum"])
            )
            bound = rule.postconditions.slot_conditions["baseScore"]
            assert (bound.minimum_value, bound.maximum_value) == (low, high), severity
            assert definitions[f"{severity.lower()}SeverityType"]["const"] == severity


def test_version_four_has_no_keys_the_upstream_refuses():
    """CVSS 4.0's rules name four score and severity keys that its list of
    properties leaves out, and it refuses other keys. So they stay out here."""
    upstream = upstream_schemas.load("imports/cvss/cvss-v4.0.json")
    assert upstream["additionalProperties"] is False
    named = {
        key
        for group in upstream["allOf"][1:]
        for branch in group["anyOf"]
        for key in branch["properties"]
    }
    assert named == {
        "threatScore",
        "threatSeverity",
        "environmentalScore",
        "environmentalSeverity",
    }
    slots = {s.name for s in view().class_induced_slots("CvssV40")}
    assert not named & slots
    assert not named & set(upstream["properties"])
