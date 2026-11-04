---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/cvss-module
genre: reference
title: CVSS module
description: "`src/cve/schema/cve_cvss.yaml`, the module with the score objects `CvssV20`, `CvssV30`, `CvssV31` and `CvssV40`, FIRST's property names as keys and each severity's score band. It imports only `linkml:types`, so that lmodel/nist-nvd can vendor it alone."
resource: src/cve/schema/cve_cvss.yaml
isPartOf:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/references/cvss-schemas
sources:
  - id: cve_cvss.yaml
    resource: src/cve/schema/cve_cvss.yaml
    title: the header comments and the classes
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# CVSS module

The module imports only the LinkML types, and its id is `https://w3id.org/lmodel/cve/cve_cvss`. lmodel/nist-nvd vendors the file by its git object hash.[^cve_cvss.yaml]

A name that recurs across CVSS versions, such as `attackVector`, is a top-level slot that each class narrows with `slot_usage`, since the value lists differ. A key that one version alone uses is an attribute of its class.[^cve_cvss.yaml]

`CvssSeverityBandsMixin` holds five rules that tie a base severity to its score band, for versions 3.0, 3.1 and 4.0. Version 2.0 has no severity.[^cve_cvss.yaml]

The upstream's CVSS 4.0 rules name `threatScore`, `threatSeverity`, `environmentalScore` and `environmentalSeverity`. Its list of properties has none of them and it refuses other keys, so `CvssV40` has no such slots.[^cve_cvss.yaml]

[^cve_cvss.yaml]: src/cve/schema/cve_cvss.yaml, the header comments and the classes
