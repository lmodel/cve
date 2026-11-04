---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/extension-keys
genre: explanation
title: Extension keys
description: "Why the three containers use `extra_slots` for keys beginning `x_`, what that opens, and what it costs: the JSON Schema passes a misspelled key, so a Python rule checks it, and the generated Python models refuse every such key."
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/record-module
  - https://w3id.org/lmodel/cve/knowledge/glossary/extension-key
sources:
  - id: real-sample
    resource: tests/data/cvelist/extract/CVE-2016-10784.json
    title: x_legacyV4Record
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: the container comments
  - id: about.md
    resource: docs/about.md
    title: What LinkML cannot say
  - id: test_cve_records.py
    resource: tests/test_cve_records.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Extension keys

Real records carry keys of the publisher's own, such as `x_generator` and `x_legacyV4Record`, where the upstream's `patternProperties` allow them.[^real-sample]

A closed class refuses such a key, so `CveCnaPublishedContainer`, `CveCnaRejectedContainer` and `CveAdpContainer` use `extra_slots`. That opens each to any key, and LinkML 1.12.1 cannot state a rule on a key's name. So `tests/cve_rules.py` refuses a key that does not begin `x_` or that holds a full stop.[^cve_record.yaml]

The dataclasses and Pydantic models ignore `extra_slots`, so they refuse those keys, and most real records carry one. The README and the about page tell a user to validate real records with the JSON Schema.[^about.md]

No test strips a key to make a record pass.[^test_cve_records.py]

[^real-sample]: tests/data/cvelist/extract/CVE-2016-10784.json, x_legacyV4Record
[^cve_record.yaml]: src/cve/schema/cve_record.yaml, the container comments
[^about.md]: docs/about.md, What LinkML cannot say
[^test_cve_records.py]: tests/test_cve_records.py, the docstring
