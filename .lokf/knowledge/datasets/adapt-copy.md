---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/cve.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CveRecord`, with eleven keys that LOKF also defines renamed with a `cve_` prefix, each keeping its IRI."
resource: .lokf/cve.yaml
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
about:
  - https://w3id.org/lmodel/cve/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: RENAMED
  - resource: .lokf/cve.yaml
  - resource: .lokf/justfile
    title: the schema line
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/cve.yaml` from `src/cve/schema/cve.yaml` with `--root CveRecord --prefix cve`, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

A concept may name `CvePublishedRecord` or `CveRejectedRecord` as its `type`. Containers, products and scores stay values inside a record.[^readme.md]

The copy renames `at`, `description`, `name`, `references`, `source`, `status`, `tags`, `title`, `type`, `url` and `version` with a `cve_` prefix, and each keeps its IRI. The source makes each of them a top-level slot for this reason, since `lokf adapt` never renames an attribute.[^test_schema_rules.py]

A release attaches the copy as `schema-<tag>-cve.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, RENAMED
