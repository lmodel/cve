## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Real CVE records ============

# Download the pinned sample of real records into tmp/cvelist/, checking each
# against the size and hashes in tests/data/cvelist/manifest.json
[group('model development')]
fetch-cve-records:
  uv run scripts/fetch_cve_records.py

# Validate every record of the pinned sample unchanged, after fetching any that
# tmp/cvelist/ lacks
[group('model development')]
test-cve-records: fetch-cve-records
  CVE_RECORDS=1 uv run python -m pytest tests/test_cve_records.py
