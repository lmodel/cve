"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/cve.schema.json is what a consumer without LinkML validates
with. It is read here under the draft it declares, and held to the generator's
settings in .linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "cve.schema.json"
SCHEMA = ROOT / "src" / "cve" / "schema" / "cve.yaml"
DATA = ROOT / "tests" / "data"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def validator():
    return jsonschema.validators.validator_for(schema())(schema())


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    assert args["include_range_class_descendants"] is True
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_the_choice_of_two_records():
    """The file's root takes a published or a rejected record, and nothing else."""
    assert schema()["title"] == "cve"
    branches = schema()["oneOf"]
    assert [b["anyOf"][0]["$ref"] for b in branches] == [
        "#/$defs/CvePublishedRecord",
        "#/$defs/CveRejectedRecord",
    ]
    assert not schema().get("properties")


def test_the_two_records_are_closed_and_typed_per_state():
    """Each kind of record refuses another key, and its metadata and containers
    are that kind's, not the abstract base's."""
    defs = schema()["$defs"]
    for kind, metadata, containers in (
        ("CvePublishedRecord", "CveMetadataPublished", "CvePublishedContainers"),
        ("CveRejectedRecord", "CveMetadataRejected", "CveRejectedContainers"),
    ):
        record = defs[kind]
        assert record["additionalProperties"] is False
        assert metadata in json.dumps(record["properties"]["cveMetadata"])
        assert containers in json.dumps(record["properties"]["containers"])
        assert 'CveMetadata"' not in json.dumps(record["properties"]["cveMetadata"])


@pytest.mark.parametrize("name", ["CveRecordRoot-published", "CveRecordRoot-rejected"])
def test_a_real_shape_validates_against_the_file(name):
    instance = _load(DATA / "problem" / "valid" / f"{name}.yaml")
    assert not list(validator().iter_errors(instance))


def test_the_fullest_example_validates_against_the_file():
    """Every key at once, with extension keys, passes."""
    instance = _load(DATA / "problem" / "valid" / "CvePublishedRecord-every-key.yaml")
    assert not list(validator().iter_errors(instance))


@pytest.mark.parametrize(
    "name",
    [
        "CveRecordRoot-rejected-state-published-container",
        "CveRecordRoot-published-state-rejected-container",
    ],
)
def test_a_record_of_mixed_states_fails_against_the_file(name):
    """A record with the state of one kind and the container of the other is
    neither kind, so the file's choice refuses it at the root."""
    found = list(validator().iter_errors(_load(DATA / "invalid" / f"{name}.yaml")))
    assert [list(e.absolute_path) for e in found] == [[]]
    assert found[0].validator == "oneOf"


def test_the_english_rule_reaches_the_file():
    """A list of descriptions needs a member in English: the generator writes this
    one rule as `contains`."""
    descriptions = schema()["$defs"]["CveCnaPublishedContainer"]["properties"][
        "descriptions"
    ]
    assert "contains" in descriptions
    assert "^en" in json.dumps(descriptions["contains"])


def test_the_extension_keys_are_open_in_the_file():
    """The three containers take other keys in the file, as extra_slots says, and
    tests/cve_rules.py is what holds them to the x_ form."""
    for name in (
        "CveCnaPublishedContainer",
        "CveCnaRejectedContainer",
        "CveAdpContainer",
    ):
        assert schema()["$defs"][name]["additionalProperties"] is True
