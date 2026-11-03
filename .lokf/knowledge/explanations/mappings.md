---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: Why the schema is the one home for mappings, each read at its source and held by a test, why the hand-kept SSSOM files went, and why the schema maps to no member of its family.
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
  - https://w3id.org/lmodel/cve/knowledge/datasets/mapping-term-list
sources:
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: the docstring and FAMILY_NAMESPACES
  - id: changelog
    resource: CHANGELOG.md
    title: Removed
  - id: readme.md
    resource: README.md
    title: Mappings
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Mappings

Each mapping names its target by a CURIE whose prefix its module binds, and `tests/test_mappings.py` holds it to a pinned term list or a released neighbour copy.[^test_mappings.py]

The hand-kept SSSOM files under `src/cve/mappings/` are gone. No source confirmed their rows.[^changelog]

The targets are the SEPSES CVE and CVSS ontologies, SPDX 3.0.1, lmodel/stix, Dublin Core, schema.org and Wikidata. The README names each with its kind and its test.[^readme.md]

The schema maps to no member of its own family, because mappings point downstream to upstream: lmodel/nist-nvd and lmodel/kev-catalog map to it.[^test_mappings.py] [^readme.md]

[^test_mappings.py]: tests/test_mappings.py, the docstring and FAMILY_NAMESPACES
[^changelog]: CHANGELOG.md, Removed
[^readme.md]: README.md, Mappings
