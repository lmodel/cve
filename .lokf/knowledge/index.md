---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/cve/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: cve Knowledge Bundle
description: Common Vulnerabilities and Exposures (CVE) Record Format 5.2.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/cve/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# cve Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for cve. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/cve`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Datasets

* [cve LinkML schema](datasets/cve-linkml-schema.md) - The LinkML model of the CVE Record Format 5.2.0, `src/cve/schema/cve.yaml` (schema id `https://w3id.org/lmodel/cve`): an umbrella that holds only the tree root, `CveRecordRoot`, over the modules `cve_record` and `cve_cvss`.
* [Record module](datasets/record-module.md) - `src/cve/schema/cve_record.yaml`, the module that models a CVE record: its metadata, the assigning authority's container, other publishers' containers, products and versions, references, metrics and the tag lists.
* [CVSS module](datasets/cvss-module.md) - `src/cve/schema/cve_cvss.yaml`, the module with the score objects `CvssV20`, `CvssV30`, `CvssV31` and `CvssV40`, FIRST's property names as keys and each severity's score band. It imports only `linkml:types`, so that lmodel/nist-nvd can vendor it alone.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the cve schema: the projections in `project/`, the Python models in `src/cve/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: a valid example of each class, a counter-example for each constraint, and the rules no generated JSON Schema states, in `tests/data/valid/`, `invalid/` and `problem/`.
* [Sample of real records](datasets/real-record-sample.md) - The pinned sample of 421 real CVE records from cvelistV5 in `tests/data/cvelist/manifest.json`, with a small extract copied beside it, which `just test-cve-records` validates unchanged. No record departs from the schema.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/`, the files of `CVEProject/cve-schema` at the tag `v5.2.0`, each pinned by its git object hash: the format's JSON schema, its tag lists, its CVSS schemas, the example records and the licence.
* [Mapping term list](datasets/mapping-term-list.md) - `tests/upstream/mapping-terms.txt`, the classes and properties of Dublin Core, schema.org and the SEPSES CVE and CVSS ontologies, which `scripts/extract_mapping_terms.py` writes from each vocabulary's pinned file and `tests/test_mappings.py` holds each mapping to.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The seven released lmodel adapt copies in `tests/neighbours/` (slsa, github-actions, in-toto, oscal, spdx, stix and uco), each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/schema/cve.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: rooted on `CveRecord`, with eleven keys that LOKF also defines renamed with a `cve_` prefix, each keeping its IRI.
* [The upstream's basic example, as a concept](datasets/example-published-record.md) - The format's own basic example record, `upstream/schema/docs/full-record-basic-example.json`, written as a concept of type `CvePublishedRecord` in the adapt copy's keys. It shows that the domain schema admits a record as a concept. CVE-1900-1234 is the upstream's made-up identifier.

# References

* [CVE Record Format](references/cve-record-format.md) - The JSON format in which the CVE Program publishes a record of a vulnerability: `schema/CVE_Record_Format.json` in `CVEProject/cve-schema`, version 5.2.0, published on 29 October 2025 under CC0 1.0. The schema renders this edition.
* [CVSS schemas](references/cvss-schemas.md) - The JSON schemas of the Common Vulnerability Scoring System (CVSS), versions 2.0, 3.0, 3.1 and 4.0, which FIRST maintains and the CVE Program keeps as local modified copies in `schema/imports/cvss/`. The module follows the CVE Program's copies.
* [CVE list](references/cve-list.md) - `CVEProject/cvelistV5`, the repository that holds real CVE records in this format, where the sample of real records is pinned at one commit. It states no licence of its own and points to the CVE Program's Terms of Use.
* [CVE Program Terms of Use](references/cve-terms-of-use.md) - The terms real CVE records come under. They allow copies provided each reproduces MITRE's copyright designation and the licence, which NOTICE and `tests/data/cvelist/TERMS.txt` do. The watch reads the page's source file, because the page is written by script.

# Explanations

* [The upstream's keys and values](explanations/keys-and-values.md) - Why slots and permissible values keep the upstream's spelling, such as `cveMetadata`, `vectorString` and `NETWORK`, while classes take a `Cve` or `Cvss` prefix: a real record must validate unchanged, and `.linkmllint.yaml` says so.
* [Published or rejected](explanations/published-or-rejected.md) - Why a record has two classes under a base and a root that takes exactly one of them, so that a rejected state with a published container fails, and why a record has no identifier slot although `cveId` identifies it.
* [Rules the generators lose](explanations/rules-in-python.md) - Which of the upstream's rules `tests/cve_rules.py` checks in Python, because LinkML 1.12.1 cannot state them or its generators lose them: unique lists, extension keys, empty objects, the 0.1 score grid, lengths beside a pattern, and null.
* [Extension keys](explanations/extension-keys.md) - Why the three containers use `extra_slots` for keys beginning `x_`, what that opens, and what it costs: the JSON Schema passes a misspelled key, so a Python rule checks it, and the generated Python models refuse every such key.
* [Mappings](explanations/mappings.md) - Why the schema is the one home for mappings, each read at its source and held by a test, why the hand-kept SSSOM files went, and why the schema maps to no member of its family.
* [What the schema leaves out](explanations/scope.md) - What the schema does not claim: it says nothing about whether a record is true, it no longer imports lmodel/vulnerability-core, and the CVSS 4.0 threat and environmental score keys are absent because the upstream refuses them.

# Glossary

* [CVE record](glossary/cve-record.md) - A CVE record: one document in the CVE Record Format, about one CVE identifier, either published or rejected. It holds `dataType`, `dataVersion`, `cveMetadata` and `containers`.
* [CNA](glossary/cna.md) - A CVE Numbering Authority: the organisation that assigned a CVE identifier, and that provides a record's one `cna` container. The class is `CveCnaPublishedContainer` or `CveCnaRejectedContainer`, by the record's state.
* [ADP](glossary/adp.md) - An Authorized Data Publisher: an organisation other than the assigning authority that adds a container to a published record. The class is `CveAdpContainer`, and it must hold something beside its provider's metadata.
* [CVSS](glossary/cvss.md) - The Common Vulnerability Scoring System: a way to score a vulnerability from 0 to 10, in versions 2.0, 3.0, 3.1 and 4.0. A metric in a record may hold a score in any of them, as `CvssV20`, `CvssV30`, `CvssV31` or `CvssV40`.
* [Extension key](glossary/extension-key.md) - A key a publisher adds to a container, whose name begins `x_` and holds no full stop, such as `x_generator`. The upstream allows it on the three containers, and a tag may take the same `x_` form.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept` and each name LOKF also defines renamed.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/cve/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Validate a record](playbooks/validate-a-record.md) - How to check a real CVE record with `linkml-validate -s src/cve/schema/cve.yaml -C CveRecordRoot`, or with `project/jsonschema/cve.schema.json`, and which of the upstream's rules that leaves to `tests/cve_rules.py`.
* [Move to another edition](playbooks/update-upstream-pins.md) - How to answer the upstream watch when the CVE Program releases another edition of the format: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and let the coverage test say what else moved.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the format says, a rule states only what the upstream states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Licence and attribution](policies/license-and-attribution.md) - The repository's licences and what it takes from elsewhere: Apache-2.0 for the schema and code, CC BY 4.0 for the bundle, CC0 1.0 for the format's files, FIRST's licence on the CVSS files, and the Terms of Use for real records. No endorsement is implied.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A vulnerability a CVE record describes belongs with that record's publisher.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, lints the schema and checks the adapt copy on 3.13, and validates the pinned sample of real records in a job of its own.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another release of the format, a moved tag, a changed pinned file, a changed licence or changed Terms of Use fails the run and opens or updates an issue.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
