"""Checks the copy of the upstream, and that the schema names the same edition.

upstream/ holds files of CVEProject/cve-schema at the pinned tag. These tests hold
them to the git object hashes that scripts/check_upstream_release.py pins, and the
schema's headers to the edition that script watches. They run offline.
"""

import hashlib
import importlib.util
import json
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "cve" / "schema"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
MODULES = {
    path.stem: yaml.safe_load(path.read_text()) for path in SCHEMA_DIR.glob("*.yaml")
}


def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PINS = _watch()


def _blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_exactly_the_pinned_files():
    """Nothing is added to the copy, and nothing is missing from it."""
    held = {
        p.relative_to(UPSTREAM).as_posix() for p in UPSTREAM.rglob("*") if p.is_file()
    }
    assert held == set(PINS.PINNED_BLOBS)


@pytest.mark.parametrize("name", sorted(PINS.PINNED_BLOBS))
def test_each_copy_is_the_pinned_blob(name):
    """Each file is byte for byte its counterpart at the pinned tag."""
    assert _blob(UPSTREAM / name) == PINS.PINNED_BLOBS[name]


def test_every_module_names_the_pinned_edition():
    """Each module's version is the edition the watch pins."""
    for name, doc in MODULES.items():
        assert doc["version"] == PINS.PINNED_EDITION, name


def test_the_header_names_the_pinned_address():
    """The umbrella and the record module cite the record format at its tag, the
    CVSS module the folder of its copies at the same tag, and every licence is the
    project's."""
    assert MODULES["cve"]["source"] == PINS.PINNED_SOURCE
    assert MODULES["cve_record"]["source"] == PINS.PINNED_SOURCE
    assert PINS.PINNED_TAG in MODULES["cve_cvss"]["source"]
    assert MODULES["cve_cvss"]["source"].endswith("/schema/imports/cvss")
    for name, doc in MODULES.items():
        assert doc["license"] == "Apache-2.0", name
    assert MODULES["cve"]["annotations"]["upstream_commit"] == PINS.PINNED_COMMIT
    assert MODULES["cve"]["annotations"]["upstream_licence"] == PINS.PINNED_LICENCE


def test_the_upstream_schema_is_this_edition():
    """The upstream's default for dataVersion is the edition itself, so a copy of
    another edition cannot sit under this pin."""
    record = json.loads((UPSTREAM / "schema" / "CVE_Record_Format.json").read_text())
    assert record["definitions"]["dataVersion"]["default"] == PINS.PINNED_EDITION


def test_the_licence_file_is_cc0():
    assert "CC0 1.0 Universal" in (UPSTREAM / "LICENSE.txt").read_text()


@pytest.mark.parametrize("version", ["2.0", "3.0", "3.1", "4.0"])
def test_each_cvss_copy_carries_firsts_licence(version):
    """FIRST's licence stays with its file, and NOTICE repeats its first line."""
    path = UPSTREAM / "schema" / "imports" / "cvss" / f"cvss-v{version}.json"
    licence = json.loads(path.read_text())["license"]
    assert licence[0].endswith("FIRST.ORG, INC.")
    assert licence[0] in (ROOT / "NOTICE").read_text()


def test_notice_says_no_endorsement_and_names_each_party():
    notice = (ROOT / "NOTICE").read_text()
    assert "endorsement" in notice
    for name in ("The MITRE Corporation", "FIRST", "CVE Program", "CC0 1.0 Universal"):
        assert name in notice, name


def test_the_terms_are_beside_the_copies():
    """The Terms of Use ask each copy to reproduce the designation and licence."""
    terms = (ROOT / "tests" / "data" / "cvelist" / "TERMS.txt").read_text()
    assert "The MITRE Corporation" in terms
    assert "Any copy you make for such" in terms


def _texts(node):
    """Every description anywhere in a parsed JSON file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                yield value
            else:
                yield from _texts(value)
    elif isinstance(node, list):
        for item in node:
            yield from _texts(item)


def _words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def _runs(words, size):
    return {tuple(words[i : i + size]) for i in range(len(words) - size + 1)}


# A run this long cannot arise by chance in a short hint, though a shorter one can,
# such as "the date time the".
RUN = 6


def test_no_description_copies_the_upstreams_text():
    """A description here is this project's own: none shares a run of six words
    with a description in the upstream's files."""
    upstream = set()
    for path in (UPSTREAM / "schema").rglob("*.json"):
        if path.parent.name != "docs":
            for text in _texts(json.loads(path.read_text())):
                upstream |= _runs(_words(text), RUN)
    shared = []
    for name, doc in MODULES.items():
        for text in _yaml_descriptions(doc):
            found = _runs(_words(text), RUN) & upstream
            if found:
                shared.append((name, text, sorted(found)[:2]))
    assert not shared, shared


def _yaml_descriptions(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                yield value
            else:
                yield from _yaml_descriptions(value)
    elif isinstance(node, list):
        for item in node:
            yield from _yaml_descriptions(item)


def test_each_description_is_short():
    """A description fits a form's hint: one or two sentences, with caveats in
    comments and decisions in notes."""
    long = [
        text
        for doc in MODULES.values()
        for text in _yaml_descriptions(doc)
        if len(re.findall(r"[.!?](?:\s|$)", text)) > 2 or len(text) > 240
    ]
    assert not long, long
