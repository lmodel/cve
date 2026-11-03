---
type: GlossaryTerm
id: https://w3id.org/lmodel/cve/knowledge/glossary/adp
title: ADP
description: "An Authorized Data Publisher: an organisation other than the assigning authority that adds a container to a published record. The class is `CveAdpContainer`, and it must hold something beside its provider's metadata."
definedBy:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
relatedTo:
  - https://w3id.org/lmodel/cve/knowledge/glossary/cve-record
sources:
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: CveAdpContainer
  - id: cve_rules.py
    resource: tests/cve_rules.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# ADP

An Authorized Data Publisher adds an `adp` container to a published record, beside the assigning authority's.[^cve_record.yaml]

The container must hold something beside its `providerMetadata`, which `tests/cve_rules.py` checks.[^cve_rules.py]

[^cve_record.yaml]: src/cve/schema/cve_record.yaml, CveAdpContainer
[^cve_rules.py]: tests/cve_rules.py, the docstring
