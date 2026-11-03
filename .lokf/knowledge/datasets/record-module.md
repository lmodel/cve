---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/record-module
genre: reference
title: Record module
description: "`src/cve/schema/cve_record.yaml`, the module that models a CVE record: its metadata, the assigning authority's container, other publishers' containers, products and versions, references, metrics and the tag lists."
resource: src/cve/schema/cve_record.yaml
isPartOf:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
dependsOn:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cvss-module
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
sources:
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: the classes, types and enums
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Record module

The module holds a class per upstream object, each prefixed `Cve`. `CveRecord` is the abstract base of `CvePublishedRecord` and `CveRejectedRecord`, which narrow `cveMetadata` and `containers` for their state.[^cve_record.yaml]

It states these rules from the upstream:[^cve_record.yaml]

- a list of descriptions holds at least one member in English;
- a product has a vendor and a product name, or a collection address and a package name;
- a product has versions or a default status;
- a version entry with an upper limit has a version type and one limit, and status changes belong to a range;
- a metric holds at least one of CVSS 4.0, 3.1, 3.0, 2.0 and another format.

Its types hold the upstream's patterns, such as the form of a CVE identifier and of a timestamp. Types such as `cve_text_4096` state a length as a pattern.[^cve_record.yaml]

The enums come from the upstream too, including the tag lists in `schema/tags/`. A tag slot takes a value from the list or a tag of the publisher's own beginning `x_`.[^cve_record.yaml]

[^cve_record.yaml]: src/cve/schema/cve_record.yaml, the classes, types and enums
