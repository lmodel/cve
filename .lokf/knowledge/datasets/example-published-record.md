---
type: CvePublishedRecord
id: https://w3id.org/lmodel/cve/knowledge/datasets/example-published-record
genre: reference
title: The upstream's basic example, as a concept
description: The format's own basic example record, `upstream/schema/docs/full-record-basic-example.json`, written as a concept of type `CvePublishedRecord` in the adapt copy's keys. It shows that the domain schema admits a record as a concept. CVE-1900-1234 is the upstream's made-up identifier.
resource: upstream/schema/docs/full-record-basic-example.json
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/datasets/upstream-copy
about:
  - https://w3id.org/lmodel/cve/knowledge/glossary/cve-record
dataType: CVE_RECORD
dataVersion: "5.2"
cveMetadata:
  cveId: CVE-1900-1234
  assignerOrgId: b3476cb9-2e3d-41a6-98d0-0f47421a65b6
  state: PUBLISHED
containers:
  cna:
    providerMetadata:
      orgId: b3476cb9-2e3d-41a6-98d0-0f47421a65b6
    problemTypes:
      - descriptions:
          - lang: en
            cve_description: CWE-78 OS Command Injection
    affected:
      - vendor: Example.org
        product: Example Enterprise
        versions:
          - cve_version: 1.0.0
            cve_status: affected
            lessThan: 1.0.6
            versionType: semver
        defaultStatus: unaffected
    descriptions:
      - lang: en
        value: "OS Command Injection vulnerability parseFilename function of example.php in the Web Management Interface of Example.org Example Enterprise on Windows, MacOS and XT-4500 allows remote unauthenticated attackers to escalate privileges.\n\nThis issue affects:\n  *  1.0 versions before 1.0.6\n  *  2.1 versions from 2.16 until 2.1.9."
    cve_references:
      - cve_url: https://example.org/ESA-22-11-CVE-1900-1234
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: full-record-basic-example.json
    resource: upstream/schema/docs/full-record-basic-example.json
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:17:36Z"
status: draft
---

# The upstream's basic example, as a concept

This concept shows how a host writes a record in its bundle. Its type is `CvePublishedRecord`, and `lokf validate` checks it against `.lokf/schema/cve.yaml`.[^readme.md]

It holds the upstream's example unchanged, apart from the keys the copy renames, such as `references`, which this concept writes as `cve_references`.[^full-record-basic-example.json]

It describes no real vulnerability.

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^full-record-basic-example.json]: upstream/schema/docs/full-record-basic-example.json
