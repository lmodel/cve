---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/keys-and-values
genre: explanation
title: The upstream's keys and values
description: "Why slots and permissible values keep the upstream's spelling, such as `cveMetadata`, `vectorString` and `NETWORK`, while classes take a `Cve` or `Cvss` prefix: a real record must validate unchanged, and `.linkmllint.yaml` says so."
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: Keys
  - id: linkmllint
    resource: .linkmllint.yaml
    title: the comment
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_no_two_pages_differ_only_by_case
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# The upstream's keys and values

A key or a value in a schema is what a record holds. So a real record validates unchanged only if the schema spells them as the upstream does.[^about.md]

`.linkmllint.yaml` relaxes the naming rule for this, with a comment that says why. Class, enum and type names keep the rule's usual form.[^linkmllint]

A record never holds a class name, so classes carry a prefix to stay apart from those of other schemas. Two names that differed from a key only by case, one class and one type, were renamed, because their pages would be one file on a case-insensitive disk. One such name is left: the key `time`, beside the page of LinkML's own `Time` type.[^test_schema_rules.py]

[^about.md]: docs/about.md, Keys
[^linkmllint]: .linkmllint.yaml, the comment
[^test_schema_rules.py]: tests/test_schema_rules.py, test_no_two_pages_differ_only_by_case
