---
type: Service
id: https://w3id.org/lmodel/cve/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
references:
  - https://w3id.org/lmodel/cve/knowledge/services/documentation-site
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment and the build job's steps
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:01:41Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

The `build` job runs the third-party tools, Hugo, Pagefind and the lokf toolkit, and the repository's own site code, under a read-only token. The `deploy` job holds the Pages scopes, runs for the default branch only, and waits for `KNOWLEDGE_WEBSITE_ENABLED`.[^knowledge-website.yaml]

The `build` job runs `website/scripts/build.sh`, which builds the site and checks its links, and uploads `website/dist` as the Pages artifact.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment and the build job's steps
