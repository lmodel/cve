# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/cve/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Validate a record](validate-a-record.md) - How to check a real CVE record with `linkml-validate -s src/cve/schema/cve.yaml -C CveRecordRoot`, or with `project/jsonschema/cve.schema.json`, and which of the upstream's rules that leaves to `tests/cve_rules.py`.
* [Move to another edition](update-upstream-pins.md) - How to answer the upstream watch when the CVE Program releases another edition of the format: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let the coverage test say what else moved.
* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
