---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/rules-in-python
genre: explanation
title: Rules the generators lose
description: "Which of the upstream's rules `tests/cve_rules.py` checks in Python, because LinkML 1.12.1 cannot state them or its generators lose them: unique lists, extension keys, empty objects, the 0.1 score grid, lengths beside a pattern, and null."
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/generated-artefacts
  - https://w3id.org/lmodel/cve/knowledge/datasets/example-data
sources:
  - id: cve_rules.py
    resource: tests/cve_rules.py
    title: the docstring
  - id: index.md
    resource: docs/index.md
    title: Validating a record
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Rules the generators lose

These rules are the upstream's, and the generated JSON Schema does not carry them, so `tests/cve_rules.py` checks them over the examples and the real records:[^cve_rules.py]

- `uniqueItems`: no generator writes `list_elements_unique`;
- `patternProperties` on the containers: an extra key must begin `x_` and hold no full stop;
- `minProperties` on the source, a metric's content and an ADP container;
- a CVSS 3.0, 3.1 or 4.0 score as a multiple of 0.1;
- a length beside a pattern, since LinkML has one pattern a slot;
- null, which the generator allows on an optional key and the upstream never does.

`tests/cve_rules.py` changes and strips nothing it reads.[^cve_rules.py]

`docs/index.md` lists these for a consumer who validates with the JSON Schema alone.[^index.md]

[^cve_rules.py]: tests/cve_rules.py, the docstring
[^index.md]: docs/index.md, Validating a record
