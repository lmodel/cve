---
type: Policy
id: https://w3id.org/lmodel/cve/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The repository's licences and what it takes from elsewhere: Apache-2.0 for the schema and code, CC BY 4.0 for the bundle, CC0 1.0 for the format's files, FIRST's licence on the CVSS files, and the Terms of Use for real records. No endorsement is implied."
resource: NOTICE
references:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-terms-of-use
  - https://w3id.org/lmodel/cve/knowledge/references/cvss-schemas
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
sources:
  - id: readme.md
    resource: README.md
    title: License
  - id: notice
    resource: NOTICE
    title: every section
  - resource: LICENSE
    title: the Apache License 2.0
  - resource: website/NOTICE
    title: the adapted graph explorer
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Licence and attribution

The code is under the Apache License 2.0, and the bundle under CC BY 4.0.[^readme.md]

NOTICE states each upstream's terms:[^notice]

- the format's files are under CC0 1.0 Universal;
- the CVSS schemas keep FIRST's licence, and are attributed to FIRST and the CVE Program;
- the copied records reproduce MITRE's copyright designation and licence, as the Terms of Use ask.

None of the parties has endorsed this project.[^notice]

[^readme.md]: README.md, License
[^notice]: NOTICE, every section
