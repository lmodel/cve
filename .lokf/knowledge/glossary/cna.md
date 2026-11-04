---
type: GlossaryTerm
id: https://w3id.org/lmodel/cve/knowledge/glossary/cna
title: CNA
description: "A CVE Numbering Authority: the organisation that assigned a CVE identifier, and that provides a record's one `cna` container. The class is `CveCnaPublishedContainer` or `CveCnaRejectedContainer`, by the record's state."
definedBy:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
relatedTo:
  - https://w3id.org/lmodel/cve/knowledge/glossary/cve-record
sources:
  - id: cve_record.yaml
    resource: src/cve/schema/cve_record.yaml
    title: the two container classes
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# CNA

A CVE Numbering Authority assigns a CVE identifier. A record holds one `cna` container, from that authority.[^cve_record.yaml]

A published record's container must hold `descriptions`, `affected` and `references`. A rejected record's holds `rejectedReasons`.[^cve_record.yaml]

[^cve_record.yaml]: src/cve/schema/cve_record.yaml, the two container classes
