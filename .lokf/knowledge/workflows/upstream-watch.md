---
type: Service
id: https://w3id.org/lmodel/cve/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: another release of the format, a moved tag, a changed pinned file, a changed licence or changed Terms of Use fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/cve/knowledge/references/cve-record-format
  - https://w3id.org/lmodel/cve/knowledge/references/cve-list
  - https://w3id.org/lmodel/cve/knowledge/references/cve-terms-of-use
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script asks the GitHub API about the format's repository, the record list and the website's source, compares files by git object hash, and reads at most 5 MB of an answer. It follows a redirect only over https to `api.github.com`, and quotes server text as code on one line.[^check_upstream_release.py]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
