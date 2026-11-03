"""Validates real CVE records unchanged.

The list is too large for git. The records in tests/data/cvelist/extract/ are always
checked. `just fetch-cve-records` downloads the rest of the pinned sample into
tmp/cvelist/, and `just test-cve-records` runs the others with CVE_RECORDS=1, as the
cve-records job of main.yaml does. Without that variable they skip, so `just test`
stays quick; with it, a missing record fails them.

Nothing here strips or rewrites a record. Each is checked in three ways: the
JSON Schema that this project commits, the rules in tests/cve_rules.py, and the
upstream's own schema, so a record that the upstream refuses shows up as a departure
of the record and not of this schema.
"""

import hashlib
import json
import os
from collections import Counter
from functools import cache
from pathlib import Path

import jsonschema
import pytest

from tests import upstream_schemas
from tests.cve_rules import record_class, rule_errors

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "cve.schema.json"
CVELIST = ROOT / "tests" / "data" / "cvelist"
MANIFEST = json.loads((CVELIST / "manifest.json").read_text(encoding="utf-8"))
EXTRACT = sorted((CVELIST / "extract").glob("*.json"))
DATA = Path(os.environ.get("CVE_RECORDS_DIR", ROOT / "tmp" / "cvelist"))
SAMPLE = sorted(MANIFEST["fetched"])
RECORD = f"{upstream_schemas.RECORD_FORMAT}#/"

# Records of the pinned sample that do not validate unchanged, by path, each with
# its reason and its count of failures. There are none: all 421 pass all three
# checks. A new sample that breaks a rule is listed here, not loosened for.
KNOWN_RECORD_DEPARTURES: dict[str, str] = {}

full_data = pytest.mark.skipif(
    os.environ.get("CVE_RECORDS") != "1",
    reason="the full sample is tested by `just test-cve-records`",
)


@cache
def validator():
    schema = json.loads(COMMITTED.read_text(encoding="utf-8"))
    return jsonschema.validators.validator_for(schema)(schema)


def problems(record):
    """What each of the three checks says about a record."""
    found = [f"schema: {e.message[:200]}" for e in validator().iter_errors(record)]
    found += [f"rule at {p}: {m}" for p, m in rule_errors(record, record_class(record))]
    if not upstream_schemas.is_valid(record, RECORD):
        found.append("the upstream's own schema refuses it")
    return found


def _pin_of(data):
    return {
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest(),
    }


def test_the_extract_holds_records():
    """The parametrized test below passes on an empty folder, so this one does not."""
    assert len(EXTRACT) >= 5, len(EXTRACT)
    assert {p.name for p in EXTRACT} == set(MANIFEST["copied"])


@pytest.mark.parametrize("path", EXTRACT, ids=lambda p: p.stem)
def test_each_copied_record_is_the_pinned_file(path):
    """A copy is byte for byte the record the manifest pins."""
    assert (
        _pin_of(path.read_bytes()) == MANIFEST["fetched"][MANIFEST["copied"][path.name]]
    )


@pytest.mark.parametrize("path", EXTRACT, ids=lambda p: p.stem)
def test_each_copied_record_validates_unchanged(path):
    record = json.loads(path.read_text(encoding="utf-8"))
    assert not problems(record)


def test_the_extract_shows_both_kinds_of_record():
    kinds = {
        json.loads(p.read_text(encoding="utf-8"))["cveMetadata"]["state"]
        for p in EXTRACT
    }
    assert kinds == {"PUBLISHED", "REJECTED"}


def test_the_upstream_examples_validate_unchanged():
    """The upstream's own example records pass, whole and as containers."""
    docs = upstream_schemas.UPSTREAM / "docs"
    for name in ("full-record-basic-example", "full-record-advanced-example"):
        record = json.loads((docs / f"{name}.json").read_text(encoding="utf-8"))
        assert not problems(record), name


def test_no_departure_is_stale():
    """A listed record is in the sample, so the list cannot outlive the sample."""
    assert set(KNOWN_RECORD_DEPARTURES) <= set(SAMPLE)


@cache
def _record(name):
    path = DATA / name
    if not path.is_file():
        pytest.fail(f"{path} is missing; run `just fetch-cve-records`")
    data = path.read_bytes()
    assert _pin_of(data) == MANIFEST["fetched"][name], f"{name} is not the pinned file"
    return json.loads(data)


@full_data
@pytest.mark.parametrize("name", SAMPLE)
def test_each_sampled_record_validates_unchanged(name):
    found = problems(_record(name))
    if name in KNOWN_RECORD_DEPARTURES:
        assert found, f"{name} passes now, so its departure is stale"
    else:
        assert not found, found


@full_data
def test_the_sample_spans_what_the_format_holds():
    """The sample stays varied: many years and publishers, both kinds of record,
    ADP containers, every score format and the extension keys."""
    records = [_record(name) for name in SAMPLE]
    seen = Counter()
    years, publishers = set(), set()
    for record in records:
        metadata = record["cveMetadata"]
        seen[metadata["state"]] += 1
        seen[f"data version {record['dataVersion']}"] += 1
        years.add(metadata["cveId"].split("-")[1])
        publishers.add(metadata.get("assignerShortName"))
        containers = record["containers"]
        seen["with an ADP container"] += "adp" in containers
        for container in [containers["cna"], *containers.get("adp", [])]:
            seen["with an extension key"] += any(k.startswith("x_") for k in container)
            for metric in container.get("metrics", []):
                for key in ("cvssV2_0", "cvssV3_0", "cvssV3_1", "cvssV4_0", "other"):
                    seen[key] += key in metric
    assert len(records) >= 400
    assert len(years) >= 25, sorted(years)
    assert len(publishers) >= 80, len(publishers)
    for key in (
        "PUBLISHED",
        "REJECTED",
        "data version 5.0",
        "data version 5.1",
        "data version 5.2",
        "with an ADP container",
        "with an extension key",
        "cvssV2_0",
        "cvssV3_0",
        "cvssV3_1",
        "cvssV4_0",
        "other",
    ):
        assert seen[key] >= 5, (key, seen[key])
