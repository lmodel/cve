---
type: Service
id: https://w3id.org/lmodel/cve/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, lints the schema and checks the adapt copy on 3.13, and validates the pinned sample of real records in a job of its own."
resource: .github/workflows/main.yaml
references:
  - https://w3id.org/lmodel/cve/knowledge/playbooks/regenerate-and-test
  - https://w3id.org/lmodel/cve/knowledge/datasets/real-record-sample
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Build and test (main.yaml)

The `test` job runs on Python 3.10 to 3.14. It installs with `uv sync --locked`, and runs `just test`. On Python 3.13 it also runs `just lint` and `just lokf-adapt-check`.[^main.yaml]

The `cve-records` job fetches the sample and validates each record with `just test-cve-records`. A cache keeps the records until the manifest moves.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml
