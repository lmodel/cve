---
type: Explanation
id: https://w3id.org/lmodel/cve/knowledge/explanations/scope
genre: explanation
title: What the schema leaves out
description: "What the schema does not claim: it says nothing about whether a record is true, it no longer imports lmodel/vulnerability-core, and the CVSS 4.0 threat and environmental score keys are absent because the upstream refuses them."
about:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: What is left out
  - id: changelog
    resource: CHANGELOG.md
    title: Removed
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# What the schema leaves out

The schema describes a record's shape. It says nothing about whether what a record claims is true.[^about.md]

The schema no longer imports lmodel/vulnerability-core, because its base classes fit none of the upstream's objects.[^changelog]

CVSS 4.0's rules name threat and environmental scores that its list of properties leaves out, so a score object cannot carry them and the class has no such slots.[^about.md]

[^about.md]: docs/about.md, What is left out
[^changelog]: CHANGELOG.md, Removed
