---
type: GlossaryTerm
id: https://w3id.org/lmodel/cve/knowledge/glossary/extension-key
title: Extension key
description: A key a publisher adds to a container, whose name begins `x_` and holds no full stop, such as `x_generator`. The upstream allows it on the three containers, and a tag may take the same `x_` form.
definedBy:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
sources:
  - id: cve_record_format.json
    resource: upstream/schema/CVE_Record_Format.json
    title: the containers and tagExtension
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Extension key

The upstream's `patternProperties` on the three containers allow a key that matches `^x_[^.]*$`.[^cve_record_format.json]

A tag has a form of the same kind: a value that begins `x_` is the publisher's own.[^cve_record_format.json]

[^cve_record_format.json]: upstream/schema/CVE_Record_Format.json, the containers and tagExtension
