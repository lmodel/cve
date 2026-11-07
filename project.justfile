## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/cve.yaml` is the copy `lokf adapt` writes from the schema so that it can
# sit beside `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The root is
# CveRecord, the abstract base of the two kinds of record, since a record is what
# a host's concept most naturally is. A concept names CvePublishedRecord or
# CveRejectedRecord as its `type`. The containers, products and CVSS scores stay
# values inside a record. The schema has no identifier slot, because cveId sits
# inside cveMetadata, so the concept's own `id` from LOKF stands beside it. The
# prefix names what the copy renames to keep apart from LOKF (cve_version,
# cve_type), each keeping its IRI. The recipes run the `lokf` the sidecar's floor
# pins (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root CveRecord --prefix cve"

# Rewrite .lokf/schema/cve.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/cve.yaml

# Fail when .lokf/schema/cve.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/cve.yaml --check

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

# ============ Artefacts gen-project does not write ============

# Write one LinkML YAML with every import merged, as the copier template's recipe does
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# Write the schema as RDF Turtle; gen-project's rdf generator is switched off in LinkML
[group('model development - extended')]
gen-rdf:
  mkdir -p {{dest}}/rdf
  uv run gen-rdf --mergeimports {{source_schema_path}} > {{dest}}/rdf/{{schema_name}}.ttl
