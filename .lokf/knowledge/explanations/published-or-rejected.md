---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/published-or-rejected
genre: explanation
title: Published or rejected
description: Why a record has two classes under a base and a root that takes exactly one of them, so that a rejected state with a published container fails, and why a record has no identifier slot although `cveId` identifies it.
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/record-module
  - https://w3id.org/lmodel/cve/knowledge/glossary/cve-record
sources:
  - id: about.md
    resource: docs/about.md
    title: How a record is shaped
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: the notes and the CveRecord comments
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_a_record_of_mixed_states_fails_against_the_file
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Published or rejected

The upstream's top level is a `oneOf` of two titled records. The schema has one class for each, and `CveRecordRoot` takes exactly one of them.[^about.md]

The state inside `cveMetadata` tells the two kinds apart, so LinkML's type designator cannot choose between them. A reader picks the class from the state, or validates against the root.[^cve_record.yaml]

Both are closed, so a record with one kind's state and the other kind's container fails at the root. `tests/test_generated_json_schema.py` checks this on the committed file.[^test_generated_json_schema.py]

`cveId` sits inside `cveMetadata`. An identifier there would make the metadata the thing `lokf adapt` must root on, which drops the key a real record needs. So the schema marks no identifier, and the type `cve_identifier` holds the pattern.[^cve_record.yaml]

[^about.md]: docs/about.md, How a record is shaped
[^cve_record.yaml]: src/cve/schema/cve_record.yaml, the notes and the CveRecord comments
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_a_record_of_mixed_states_fails_against_the_file
