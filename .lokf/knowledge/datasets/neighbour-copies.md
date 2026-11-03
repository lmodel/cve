---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The seven released lmodel adapt copies in `tests/neighbours/` (slsa, github-actions, in-toto, oscal, spdx, stix and uco), each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/cve/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and SHARED_WITH_NEIGHBOURS
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: neighbour_iris
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on a new key shared with a neighbour, and on any shared class, enum or type. The shared keys it lists today include `value` and `descriptions`, which are the upstream's own, so they are not renamed.[^test_schema_rules.py]

`tests/test_mappings.py` also reads these copies, to hold the mappings to SPDX and STIX.[^test_mappings.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
[^test_mappings.py]: tests/test_mappings.py, neighbour_iris
