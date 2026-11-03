---
type: Policy
id: https://w3id.org/lmodel/cve/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A vulnerability a CVE record describes belongs with that record's publisher.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/cve/knowledge/workflows/upstream-watch
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The release carries the adapt copy, the bundle as a zip and a Copilot skill zip, each with a checksum and a build-provenance attestation.[^security.md]

A CVE record is untrusted text from many publishers, and this repository treats it as data. Tests validate records, and nothing executes them.[^security.md]

The watch's token can write issues, and the script sends it to `api.github.com` alone.[^security.md]

A vulnerability that a record describes belongs with the publisher the record names, not here.[^security.md]

[^security.md]: SECURITY.md
