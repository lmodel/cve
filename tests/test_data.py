"""Data test."""
import os
import glob
import pytest
from pathlib import Path
import re

import cve.datamodel.cve
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(cve.datamodel.cve, target_class_name, None)
    if tgt_class is None:
        # Generated Python classes flatten CVSS version underscores (e.g., CvssV4_0 -> CvssV40).
        fallback_name = re.sub(r"V(\d+)_(\d+)", r"V\1\2", target_class_name)
        tgt_class = getattr(cve.datamodel.cve, fallback_name)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj
