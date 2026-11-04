---
type: GlossaryTerm
id: https://w3id.org/lmodel/cve/knowledge/glossary/cvss
title: CVSS
description: "The Common Vulnerability Scoring System: a way to score a vulnerability from 0 to 10, in versions 2.0, 3.0, 3.1 and 4.0. A metric in a record may hold a score in any of them, as `CvssV20`, `CvssV30`, `CvssV31` or `CvssV40`."
definedBy:
  - https://w3id.org/lmodel/cve/knowledge/references/cvss-schemas
sources:
  - id: cve_cvss.yaml
    resource: src/cve/schema/cve_cvss.yaml
    title: the four classes
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: CveMetric
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# CVSS

A score object holds a version, a vector string and a base score from 0 to 10. Versions 3.0, 3.1 and 4.0 also hold a base severity.[^cve_cvss.yaml]

A record's metric holds a score under the keys `cvssV2_0`, `cvssV3_0`, `cvssV3_1` and `cvssV4_0`.[^cve_record.yaml]

[^cve_cvss.yaml]: src/cve/schema/cve_cvss.yaml, the four classes
[^cve_record.yaml]: src/cve/schema/cve_record.yaml, CveMetric
