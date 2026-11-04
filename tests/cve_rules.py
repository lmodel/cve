"""The upstream's rules that the generated JSON Schema does not check.

LinkML 1.12.1 cannot state these, or its generators lose them. The checks hold
the examples and the real records to them, and each returns a list of
``(pointer, message)`` pairs. None changes or strips the data it reads.

- ``uniqueItems``: ``list_elements_unique`` is on the slots, but no generator
  writes it (linkml issue 4194).
- ``patternProperties`` on the three containers: a key beyond the declared ones
  must match ``^x_[^.]*$``. ``extra_slots`` opens the class to every key, so the
  JSON Schema alone would pass a misspelled one.
- ``minProperties``: the source and metric content hold at least one key, and an
  ADP container holds something beside its provider's metadata.
- A CVSS 3.0, 3.1 or 4.0 score is a multiple of 0.1. The upstream lists those
  numbers, and a LinkML range can only bound them.
- ``minLength`` and ``maxLength`` beside a ``pattern``: LinkML has one pattern
  per slot, so ``LENGTH_BESIDE_PATTERN`` holds these five lengths.
- ``null``: the generator lets an optional key be null, and the upstream never
  does. Inside free-form content a null is the publisher's own business.
"""

import re
from decimal import Decimal
from functools import cache
from pathlib import Path

from linkml_runtime import SchemaView

SCHEMA = Path(__file__).parent.parent / "src" / "cve" / "schema" / "cve.yaml"

EXTENSION_KEY = re.compile(r"^x_[^.]*$")
EXTENSION_CLASSES = {
    "CveCnaPublishedContainer",
    "CveCnaRejectedContainer",
    "CveAdpContainer",
}
# Classes whose keys beyond the declared ones are the upstream's to leave open.
OPEN_CLASSES = {
    "CveCpeApplicabilityElement",
    "CveCpeNode",
    "CveOtherMetricContent",
    "CveSource",
}
AT_LEAST_ONE_KEY = {"CveOtherMetricContent", "CveSource"}
GRID_CLASSES = {"CvssV30", "CvssV31", "CvssV40"}
GRID_SLOTS = {"baseScore", "temporalScore", "environmentalScore"}

# (class, key): (shortest, longest) as the upstream states them, which
# tests/test_coverage.py checks against the upstream's files. A tag's bounds
# apply to the publisher's own tags, the upstream's tagExtension.
LENGTH_BESIDE_PATTERN = {
    ("CveProduct", "cpes"): (1, 2048),
    ("CveCpeMatch", "criteria"): (1, 2048),
    ("CveProblemTypeDescription", "cweId"): (5, 9),
    ("CveImpact", "capecId"): (7, 11),
    ("CveCnaPublishedContainer", "tags"): (2, 128),
    ("CveAdpContainer", "tags"): (2, 128),
    ("CveReference", "tags"): (2, 128),
}


@cache
def _view():
    return SchemaView(str(SCHEMA))


@cache
def _slots(class_name):
    """Each key a class declares, with its range and whether it is a list that
    the upstream holds unique."""
    view = _view()
    found = {}
    for slot in view.class_induced_slots(class_name):
        found[slot.name] = (
            slot.range,
            bool(slot.multivalued),
            bool(slot.list_elements_unique),
        )
    return found


def _escape(key):
    return str(key).replace("~", "~0").replace("/", "~1")


def _is_class(name):
    return name in _view().all_classes()


def _deep_key(value):
    """A value in a form that compares by content, whatever its key order."""
    if isinstance(value, dict):
        return ("object", tuple(sorted((k, _deep_key(v)) for k, v in value.items())))
    if isinstance(value, list):
        return ("array", tuple(_deep_key(v) for v in value))
    return (type(value).__name__ if isinstance(value, (bool, str)) else "number", value)


def _on_the_grid(number):
    return Decimal(str(number)) % Decimal("0.1") == 0


def rule_errors(instance, class_name, pointer=""):
    """Every rule of this module that an instance of a class breaks."""
    found = []
    if not isinstance(instance, dict):
        return found
    where = pointer or "/"
    slots = _slots(class_name)

    if class_name in AT_LEAST_ONE_KEY and not instance:
        found.append((where, "it must hold at least one key"))
    if class_name == "CveAdpContainer" and len(instance) < 2:
        found.append((where, "it must hold something beside providerMetadata"))

    for key, value in instance.items():
        here = f"{pointer}/{_escape(key)}"
        if key not in slots:
            if class_name in EXTENSION_CLASSES and not EXTENSION_KEY.match(key):
                found.append(
                    (
                        here,
                        "a key beyond the declared ones must begin x_ and hold no full stop",
                    )
                )
            continue
        if value is None:
            found.append((here, "the upstream never allows null"))
            continue
        range_name, multivalued, unique = slots[key]
        if multivalued and isinstance(value, list):
            found += _list_errors(class_name, key, value, here, range_name, unique)
            continue
        if class_name in GRID_CLASSES and key in GRID_SLOTS and not _on_the_grid(value):
            found.append((here, "the score must be a multiple of 0.1"))
        found += _length_errors(class_name, key, value, here)
        if _is_class(range_name):
            found += rule_errors(value, range_name, here)
    return found


def _list_errors(class_name, key, items, here, range_name, unique):
    found = []
    seen = set()
    for index, item in enumerate(items):
        at = f"{here}/{index}"
        mark = _deep_key(item)
        if unique and mark in seen:
            found.append((at, "the list holds this item twice"))
        seen.add(mark)
        found += _length_errors(class_name, key, item, at)
        if _is_class(range_name):
            found += rule_errors(item, range_name, at)
    return found


def _length_errors(class_name, key, value, here):
    bounds = LENGTH_BESIDE_PATTERN.get((class_name, key))
    if bounds is None or not isinstance(value, str):
        return []
    if key == "tags" and not value.startswith("x_"):
        return []
    shortest, longest = bounds
    if shortest <= len(value) <= longest:
        return []
    return [(here, f"it must hold {shortest} to {longest} characters")]


def record_class(record):
    """The class of a whole record, chosen by the state in its metadata."""
    state = (record.get("cveMetadata") or {}).get("state")
    return {"PUBLISHED": "CvePublishedRecord", "REJECTED": "CveRejectedRecord"}.get(
        state
    )
