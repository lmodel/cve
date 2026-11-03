---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/`, the files of `CVEProject/cve-schema` at the tag `v5.2.0`, each pinned by its git object hash: the format's JSON schema, its tag lists, its CVSS schemas, the example records and the licence."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
  - https://w3id.org/lmodel/cve/knowledge/references/cvss-schemas
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: PINNED_COMMIT and PINNED_BLOBS
  - id: notice
    resource: NOTICE
    title: The CVE Record Format and The CVSS schemas
  - resource: tests/test_upstream.py
    title: the copy held to its pins
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Copy of the upstream

`upstream/` holds fifteen files of the format's repository at the tag `v5.2.0`, commit `5533f6038cc0`. `PINNED_BLOBS` in `scripts/check_upstream_release.py` names each with its git object hash, and `tests/test_upstream.py` holds the folder to that list.[^check_upstream_release.py]

Each file is unchanged. The CVSS files keep FIRST's licence as their first key.[^notice]

[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_COMMIT and PINNED_BLOBS
[^notice]: NOTICE, The CVE Record Format and The CVSS schemas
