---
type: Playbook
id: https://w3id.org/lmodel/cve/knowledge/playbooks/validate-a-record
genre: how-to
title: Validate a record
description: How to check a real CVE record with `linkml-validate -s src/cve/schema/cve.yaml -C CveRecordRoot`, or with `project/jsonschema/cve.schema.json`, and which of the upstream's rules that leaves to `tests/cve_rules.py`.
references:
  - https://w3id.org/lmodel/cve/knowledge/explanations/rules-in-python
  - https://w3id.org/lmodel/cve/knowledge/datasets/generated-artefacts
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a record
  - id: about.md
    resource: docs/about.md
    title: What LinkML cannot say
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Validate a record

1. Run `uv run linkml-validate -s src/cve/schema/cve.yaml -C CveRecordRoot record.yaml`.[^index.md]
2. Without LinkML, validate against `project/jsonschema/cve.schema.json`.[^index.md]
3. For the upstream's whole rule set, also run the checks in `tests/cve_rules.py`.[^index.md]

Do not use the generated Python models for a real record. They refuse the extension keys most records carry.[^about.md]

[^index.md]: docs/index.md, Validating a record
[^about.md]: docs/about.md, What LinkML cannot say
