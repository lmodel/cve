"""Data tests: every example against the JSON Schema the validator generates,
the rules no generator carries, and the upstream's own schemas."""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests import upstream_schemas
from tests.cve_rules import rule_errors

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cve" / "schema" / "cve.yaml"
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
PROBLEM_VALID = sorted((DATA / "problem" / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
PROBLEM_INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates.
    Generating it once keeps the run short; test_validator_agrees checks that
    linkml-validate gives the same answers."""
    generator = JsonSchemaGenerator(
        str(SCHEMA), mergeimports=True, include_range_class_descendants=True
    )
    return json.loads(generator.serialize())["$defs"]


def errors(instance, class_name):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions()}
    validator = jsonschema.validators.validator_for(schema)(schema)
    return list(validator.iter_errors(instance))


def pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


def class_of(path):
    return path.stem.split("-")[0]


def fails_at(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails"
    )
    return first.removeprefix("# Fails at: ").strip()


def places(error):
    """Where an error points: its own place, or, for an anyOf or oneOf that no
    branch met, the places inside each branch that could have been meant. An
    optional object's branches are the object and null, so its error points
    inside the object; the null branch is left aside. A choice whose branches
    are alternatives of a class, such as a record's two kinds, stays at its
    own place."""
    if error.validator not in ("anyOf", "oneOf") or not error.context:
        return {pointer(error)}
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    real = [
        subs
        for subs in branches.values()
        if not any(s.validator == "type" and s.validator_value == "null" for s in subs)
    ]
    if len(real) != 1:
        return {pointer(error)}
    found = set()
    for sub in real[0]:
        found |= places(sub)
    return found or {pointer(error)}


def upstream_path_of(class_name):
    """The part of the upstream's files that a class renders."""
    if class_name == "CveRecordRoot":
        return "CVE_Record_Format.json#/"
    annotation = (
        SchemaView(str(SCHEMA)).get_class(class_name).annotations["upstream_path"]
    )
    return annotation.value.split()[0]


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    assert len(VALID) >= 40, len(VALID)
    assert len(PROBLEM_VALID) >= 10, len(PROBLEM_VALID)
    assert len(INVALID) >= 180, len(INVALID)
    assert len(PROBLEM_INVALID) >= 20, len(PROBLEM_INVALID)


@pytest.mark.parametrize("path", VALID + PROBLEM_VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    """Every valid example passes the JSON Schema and the rules in Python."""
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    found = errors(instance, class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert not rule_errors(instance, class_of(path))


@pytest.mark.parametrize("path", VALID + PROBLEM_VALID, ids=lambda p: p.stem)
def test_the_upstream_accepts_each_valid_example(path):
    """The upstream's own schema accepts what this schema accepts."""
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    found = list(
        upstream_schemas.validator(upstream_path_of(class_of(path))).iter_errors(
            instance
        )
    )
    assert not found, [e.message[:200] for e in found]


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, and nowhere else but on the way to it, so a
    file that starts failing for another reason fails this test."""
    where = fails_at(path)
    found = errors(yaml.safe_load(path.read_text(encoding="utf-8")), class_of(path))
    assert found, "it validates"
    reached = set().union(*(places(e) for e in found))
    report = [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert where in reached, (sorted(reached), report)
    on_the_way = {
        p for p in reached if where == p or where.startswith(p.rstrip("/") + "/")
    }
    assert reached == on_the_way, (sorted(reached - on_the_way), report)


@pytest.mark.parametrize("path", PROBLEM_INVALID, ids=lambda p: p.stem)
def test_rule_counter_examples_fail_where_they_say(path):
    """A counter-example under problem/invalid/ passes the JSON Schema, which
    cannot state its rule, and fails only the rule its first line points to."""
    where = fails_at(path)
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    class_name = class_of(path)
    found = [e for e in errors(instance, class_name) if not _is_a_null(e)]
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert [p for p, _ in rule_errors(instance, class_name)] == [where]


def _is_a_null(error):
    return error.instance is None


@pytest.mark.parametrize("path", INVALID + PROBLEM_INVALID, ids=lambda p: p.stem)
def test_the_upstream_refuses_each_counter_example(path):
    """No counter-example asks for more than the upstream does: its own schema
    refuses each of them as well."""
    instance = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert not upstream_schemas.is_valid(instance, upstream_path_of(class_of(path)))


def test_validator_agrees():
    """linkml-validate, which the README tells a user to run, accepts a valid
    example and rejects a counter-example at the same place."""
    good = DATA / "problem" / "valid" / "CveRecordRoot-published.yaml"
    report = validate(yaml.safe_load(good.read_text()), SCHEMA, "CveRecordRoot")
    assert not report.results, [r.message for r in report.results]
    bad = DATA / "invalid" / "CvePublishedRecord-rejected-state.yaml"
    report = validate(yaml.safe_load(bad.read_text()), SCHEMA, "CvePublishedRecord")
    assert any("/cveMetadata" in r.message for r in report.results), [
        r.message for r in report.results
    ]


def test_every_concrete_class_has_an_example():
    """Each class a record can hold has a valid example, and so does the root."""
    view = SchemaView(str(SCHEMA))
    concrete = {
        name
        for name, cls in view.all_classes().items()
        if not cls.abstract and not cls.mixin
    }
    examples = {class_of(path) for path in VALID + PROBLEM_VALID}
    assert concrete == examples, sorted(concrete ^ examples)


def test_too_many_references_are_refused():
    """A record's references stop at 512, which is too long for an example file."""
    container = yaml.safe_load(
        (DATA / "valid" / "CveCnaPublishedContainer-minimal.yaml").read_text()
    )
    container["references"] = [{"url": f"https://example.org/{i}"} for i in range(512)]
    assert not errors(container, "CveCnaPublishedContainer")
    container["references"].append({"url": "https://example.org/one-more"})
    assert {pointer(e) for e in errors(container, "CveCnaPublishedContainer")} == {
        "/references"
    }


# The upstream's choice for one version entry names four shapes. Every mix of the
# optional keys is tried here against both schemas, so the rules on
# CveProductVersion cannot drift from it in a case no example shows.
VERSION_KEYS = {
    "versionType": "semver",
    "lessThan": "2.0",
    "lessThanOrEqual": "1.9",
    "changes": [{"at": "1.5", "status": "unaffected"}],
}


@pytest.mark.parametrize("mask", range(2 ** len(VERSION_KEYS)))
def test_version_rules_match_the_upstream_for_every_mix_of_keys(mask):
    entry = {"version": "1.0", "status": "affected"}
    for bit, (key, value) in enumerate(VERSION_KEYS.items()):
        if mask >> bit & 1:
            entry[key] = value
    ours = not errors(entry, "CveProductVersion")
    theirs = upstream_schemas.is_valid(
        entry, "CVE_Record_Format.json#/definitions/product/properties/versions/items"
    )
    assert ours == theirs, entry


# The same for a product's two choices, over the keys that decide them.
PRODUCT_KEYS = {
    "vendor": "Example Corp",
    "product": "Example Widget",
    "collectionURL": "https://example.org/packages",
    "packageName": "example-widget",
    "versions": [{"version": "1.0", "status": "affected"}],
    "defaultStatus": "unknown",
}


@pytest.mark.parametrize("mask", range(2 ** len(PRODUCT_KEYS)))
def test_product_rules_match_the_upstream_for_every_mix_of_keys(mask):
    product = {
        k: v for bit, (k, v) in enumerate(PRODUCT_KEYS.items()) if mask >> bit & 1
    }
    ours = not errors(product, "CveProduct")
    theirs = upstream_schemas.is_valid(
        product, "CVE_Record_Format.json#/definitions/product"
    )
    assert ours == theirs, product


@pytest.mark.parametrize(
    ("version", "low", "medium", "high", "critical"),
    [
        ("CvssV30", 3.9, 4.0, 7.0, 9.0),
        ("CvssV31", 3.9, 4.0, 7.0, 9.0),
        ("CvssV40", 3.9, 4.0, 7.0, 9.0),
    ],
)
def test_severity_bands_match_the_upstream_at_every_score(
    version, low, medium, high, critical
):
    """Every score on the 0.1 grid, with every severity, gets one answer from
    both schemas, so the rules cannot drift from the upstream's bands."""
    name = {"CvssV30": "3.0", "CvssV31": "3.1", "CvssV40": "4.0"}[version]
    vector = {
        "CvssV30": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "CvssV31": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
        "CvssV40": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
    }[version]
    path = f"imports/cvss/cvss-v{name}.json#/"
    upstream = upstream_schemas.validator(path)
    for tenths in range(101):
        for severity in ("NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"):
            score = {
                "version": name,
                "vectorString": vector,
                "baseScore": tenths / 10,
                "baseSeverity": severity,
            }
            assert (not errors(score, version)) == upstream.is_valid(score), score
