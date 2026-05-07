"""Validate official upstream CVE schema JSON examples against the LinkML schema.

These tests validate that the JSON example files from the CVEProject/cve-schema
repository (stored under tests/data/third_party/cveschema/) conform to the
LinkML CVE schema (src/cve/schema/cve.yaml).

The upstream JSON uses camelCase property names; the LinkML schema uses snake_case
slot names with camelCase aliases. A class-context-aware translator converts
the upstream keys before validation so that ``linkml.validator.validate()`` can
check them against the generated JSON Schema.

"""
import json
import pytest
from pathlib import Path
from typing import Any

from linkml.validator import validate
from linkml_runtime.utils.schemaview import SchemaView

THIRD_PARTY_DIR = Path(__file__).parent / "data" / "third_party" / "cveschema"
SCHEMA_PATH = Path(__file__).parent.parent / "src" / "cve" / "schema" / "cve.yaml"

# (filepath, target_class_name, json_extract_key_or_None)
# For cnaContainer-* files the JSON wraps the container under "cnaContainer".
CASES = [
    ("full-record-basic-example.json",        "CVERecord",             None),
    ("full-record-advanced-example.json",     "CVERecord",             None),
    # v5.0 archive examples: dataVersion "5.0", CVSS v3.1 only, no cpeApplicability
    ("full-record-v50-basic-example.json",    "CVERecord",             None),
    ("full-record-v50-advanced-example.json", "CVERecord",             None),
    # authored fixtures: gaps not covered by upstream examples
    ("full-record-rejected-example.json",     "CVERecord",             None),
    ("full-record-with-adp-example.json",     "CVERecord",             None),
    ("full-record-cvss30-example.json",       "CVERecord",             None),
    ("full-record-cvss20-example.json",       "CVERecord",             None),
    # authored: other metric type (SSVC) with arbitrary JSON content
    ("full-record-other-metric-example.json", "CVERecord",             None),
    # authored: x_* extension tags on cna.tags
    ("full-record-extension-tags-example.json", "CVERecord",           None),
    ("cnaContainer-basic-example.json",       "CnaPublishedContainer", "cnaContainer"),
    ("cnaContainer-advanced-example.json",    "CnaPublishedContainer", "cnaContainer"),
    ("cnaContainer-rejected-example.json",    "CnaRejectedContainer",  "cnaContainer"),
]


# ---------------------------------------------------------------------------
# Class-context-aware key translator
# ---------------------------------------------------------------------------

def _build_local_alias_map(sv: SchemaView, class_name: str) -> dict[str, str]:
    """Return {json_key: slot_name} for all slots induced by *class_name*.

    The induced slots include all slots declared on the class itself and on
    every ancestor (via is_a / mixins).  Each slot's ``aliases`` list provides
    the camelCase JSON keys that map to that slot.  Direct slot names are also
    included as identity entries so that keys already in snake_case pass through
    untouched.
    """
    alias_map: dict[str, str] = {}
    try:
        induced = sv.class_induced_slots(class_name)
    except Exception:
        return alias_map
    for slot in induced:
        alias_map[slot.name] = slot.name          # identity (snake_case key)
        for alias in slot.aliases or []:
            alias_map[alias] = slot.name          # camelCase alias → slot name
    return alias_map


def _range_classes(sv: SchemaView, class_name: str, slot_name: str) -> list[str]:
    """Return all possible range class names for *slot_name* on *class_name*.

    Collects the primary ``range`` (if it refers to a class) plus every
    class-range listed in ``any_of``.  This handles union-typed slots such as
    ``cve_metadata`` (CveMetadataPublished | CveMetadataRejected) and ``cna``
    (CnaPublishedContainer | CnaRejectedContainer).
    """
    try:
        induced = sv.class_induced_slots(class_name)
    except Exception:
        return []
    for slot in induced:
        if slot.name == slot_name:
            classes: list[str] = []
            if slot.range and sv.get_class(slot.range):
                classes.append(slot.range)
            for ao in slot.any_of or []:
                if ao.range and sv.get_class(ao.range):
                    classes.append(ao.range)
            return classes
    return []


def _combined_alias_map(sv: SchemaView, class_names: list[str]) -> dict[str, str]:
    """Build a merged alias map from all induced slots of every class in *class_names*."""
    alias_map: dict[str, str] = {}
    for cls in class_names:
        try:
            induced = sv.class_induced_slots(cls)
        except Exception:
            continue
        for slot in induced:
            alias_map.setdefault(slot.name, slot.name)
            for alias in slot.aliases or []:
                alias_map.setdefault(alias, slot.name)
    return alias_map


def _translate(data: Any, class_name: str, sv: SchemaView) -> Any:
    """Recursively translate *data* from upstream JSON keys to schema slot names."""
    if not isinstance(data, dict):
        return data
    return _translate_with_map(
        data, [class_name], _build_local_alias_map(sv, class_name), sv
    )


def _translate_with_map(data: dict, candidate_classes: list[str],
                        alias_map: dict[str, str], sv: SchemaView) -> dict:
    """Translate *data* using *alias_map*, resolving nested ranges from *candidate_classes*.

    For each key, after translating it to its slot name, the range is looked up
    in every candidate class in order.  This handles union-typed slots (any_of)
    where the abstract base class (e.g. CnaContainer) has no slots of its own.
    """
    result: dict[str, Any] = {}
    for key, value in data.items():
        translated_key = alias_map.get(key, key)

        # Find range by trying each candidate class until one has the slot
        range_cls_list: list[str] = []
        for cls in candidate_classes:
            range_cls_list = _range_classes(sv, cls, translated_key)
            if range_cls_list:
                break

        if range_cls_list and isinstance(value, dict):
            nested_candidates = range_cls_list
            nested_map = _combined_alias_map(sv, nested_candidates)
            value = _translate_with_map(value, nested_candidates, nested_map, sv)
        elif range_cls_list and isinstance(value, list):
            nested_candidates = range_cls_list
            nested_map = _combined_alias_map(sv, nested_candidates)
            value = [
                _translate_with_map(item, nested_candidates, nested_map, sv)
                if isinstance(item, dict) else item
                for item in value
            ]

        result[translated_key] = value
    return result


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    """Load the LinkML CVE schema once for all tests."""
    return SchemaView(str(SCHEMA_PATH.resolve()))


@pytest.fixture(scope="module")
def schema_def(schema_view):
    """Return the SchemaDefinition object for use with linkml.validator."""
    return schema_view.schema


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "filename,target_class,extract_key",
    CASES,
    ids=[c[0] for c in CASES],
)
def test_third_party_json_examples(filename, target_class, extract_key,
                                   schema_view, schema_def):
    """Upstream CVE JSON examples validate against the LinkML CVE schema.

    The upstream JSON is translated from camelCase to schema-native snake_case
    using a class-context-aware key translator before validation.
    """
    filepath = THIRD_PARTY_DIR / filename
    with filepath.open() as fh:
        data = json.load(fh)

    if extract_key:
        data = data[extract_key]

    translated = _translate(data, target_class, schema_view)

    report = validate(translated, schema_def, target_class=target_class)
    errors = report.results
    assert not errors, (
        f"{filename}: {len(errors)} validation error(s):\n"
        + "\n".join(f"  [{r.severity}] {r.message}" for r in errors)
    )
