---
type: Reference
id: https://w3id.org/lmodel/cve/knowledge/references/cvss-schemas
genre: reference
title: CVSS schemas
description: The JSON schemas of the Common Vulnerability Scoring System (CVSS), versions 2.0, 3.0, 3.1 and 4.0, which FIRST maintains and the CVE Program keeps as local modified copies in `schema/imports/cvss/`. The module follows the CVE Program's copies.
resource: https://www.first.org/cvss/data-representations
isPartOf:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
sources:
  - id: cvss-readme.md
    resource: upstream/schema/imports/cvss/README.md
  - id: notice
    resource: NOTICE
    title: The CVSS schemas
  - resource: upstream/schema/imports/cvss
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# CVSS schemas

The README beside the files says they are local modified versions of the schemas that the Forum of Incident Response and Security Teams (FIRST) maintains.[^cvss-readme.md]

Each file carries FIRST's licence as its first key: copyright 2017 for versions 2.0 and 3.0, 2021 for 3.1 and 2023 for 4.0. NOTICE repeats it and attributes the files to both.[^notice]

[^cvss-readme.md]: upstream/schema/imports/cvss/README.md
[^notice]: NOTICE, The CVSS schemas
