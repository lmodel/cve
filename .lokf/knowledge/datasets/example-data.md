---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: a valid example of each class, a counter-example for each constraint, and the rules no generated JSON Schema states, in `tests/data/valid/`, `invalid/` and `problem/`."
resource: tests/data
references:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
sources:
  - id: tests-data-readme.md
    resource: tests/data/README.md
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstrings
  - resource: tests/cve_rules.py
    title: the rules no generated JSON Schema states
  - resource: tests/upstream_schemas.py
    title: the upstream schemas as validators
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Example data

`tests/data/` holds the examples, each named after its class, as `ClassName-anything.yaml`:[^tests-data-readme.md]

- `valid/` holds what the generated dataclasses can load;
- `invalid/` holds a counter-example for each constraint the validator can state;
- `problem/valid/` holds valid examples the dataclasses cannot load, such as the tree root and whatever carries an extension key;
- `problem/invalid/` holds a counter-example for each rule that only `tests/cve_rules.py` checks.

Each counter-example's first line, `# Fails at: <pointer>`, names its one failing place.[^tests-data-readme.md]

`tests/test_data.py` also asks the upstream's own schema about each file. So an example says nothing the upstream does not, and each counter-example is refused there as well.[^test_data.py]

The same file tries every mix of the keys that decide a version entry and a product, and every score on the 0.1 grid with every severity, against both schemas.[^test_data.py]

[^tests-data-readme.md]: tests/data/README.md
[^test_data.py]: tests/test_data.py, the docstrings
