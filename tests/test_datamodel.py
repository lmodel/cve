"""Checks what the generated Python models do, as the docs say they do.

LinkML 1.12.1's dataclasses and Pydantic models ignore `extra_slots`, so docs/about.md
tells a user to validate real records with the JSON Schema. These tests hold that
sentence to the models: a record with no extension key loads into both, and one
with an extension key is refused by both.
"""

from pathlib import Path

import pytest
import yaml
from linkml_runtime.loaders import yaml_loader

from cve.datamodel import cve as dataclasses_module
from cve.datamodel import cve_pydantic

DATA = Path(__file__).parent / "data"
PLAIN = DATA / "valid" / "CvePublishedRecord-minimal.yaml"
EXTENDED = DATA / "problem" / "valid" / "CveCnaPublishedContainer-extension-key.yaml"


def test_a_plain_record_loads_into_the_dataclasses():
    record = yaml_loader.load(
        str(PLAIN), target_class=dataclasses_module.CvePublishedRecord
    )
    assert record.cveMetadata.cveId == "CVE-1900-1234"
    assert str(record.cveMetadata.state) == "PUBLISHED"


def test_a_plain_record_loads_into_the_pydantic_model():
    record = cve_pydantic.CvePublishedRecord(**yaml.safe_load(PLAIN.read_text()))
    assert record.cveMetadata.cveId == "CVE-1900-1234"
    assert record.containers.cna.providerMetadata.shortName == "example"


def test_the_dataclasses_refuse_an_extension_key():
    with pytest.raises(TypeError, match="x_generator"):
        yaml_loader.load(
            str(EXTENDED), target_class=dataclasses_module.CveCnaPublishedContainer
        )


def test_the_pydantic_model_refuses_an_extension_key():
    with pytest.raises(ValueError, match="x_generator"):
        cve_pydantic.CveCnaPublishedContainer(**yaml.safe_load(EXTENDED.read_text()))


def test_the_pydantic_model_holds_the_cvss_defaults():
    """The upstream's defaults for CVSS 4.0 reach the model through ifabsent."""
    score = cve_pydantic.CvssV40(
        version="4.0",
        vectorString="CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
        baseScore=9.3,
        baseSeverity="CRITICAL",
    )
    assert score.Safety == "NOT_DEFINED"
