---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/real-record-sample
genre: reference
title: Sample of real records
description: The pinned sample of 421 real CVE records from cvelistV5 in `tests/data/cvelist/manifest.json`, with a small extract copied beside it, which `just test-cve-records` validates unchanged. No record departs from the schema.
resource: tests/data/cvelist
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-list
references:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
sources:
  - id: manifest.json
    resource: tests/data/cvelist/manifest.json
  - id: cvelist-readme.md
    resource: tests/data/cvelist/README.md
  - id: test_cve_records.py
    resource: tests/test_cve_records.py
    title: the docstring and the departures
  - resource: scripts/fetch_cve_records.py
    title: what it downloads and keeps
  - resource: tests/test_fetch.py
    title: the fetch against stubbed downloads
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Sample of real records

`tests/data/cvelist/manifest.json` pins each record's path at one commit of `CVEProject/cvelistV5`, with its size, its SHA-256 and its git object hash. The manifest's `selection` key says how they were chosen.[^manifest.json]

`extract/` holds a few of them, so `just test` validates real records with no network. `TERMS.txt` carries MITRE's copyright designation and licence beside the copies.[^cvelist-readme.md]

`just fetch-cve-records` runs `scripts/fetch_cve_records.py`, which downloads only from `raw.githubusercontent.com` and keeps a file only when its size and hashes match. `just test-cve-records` validates each record against the committed JSON Schema, the rules in Python and the upstream's own schema, and nothing strips or rewrites a record.[^test_cve_records.py]

`KNOWN_RECORD_DEPARTURES` in that test is empty: all 421 pass.[^test_cve_records.py]

[^manifest.json]: tests/data/cvelist/manifest.json
[^cvelist-readme.md]: tests/data/cvelist/README.md
[^test_cve_records.py]: tests/test_cve_records.py, the docstring and the departures
