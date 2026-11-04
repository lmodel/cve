# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.1.0] - 2026-11-04

### Added

- **A LinkML rendering of the CVE Record Format 5.2.0, with the CVSS 2.0, 3.0, 3.1 and 4.0 score objects in a module of their own, `cve_cvss`.** Keys and values are the upstream's own, so a real record validates unchanged, and every description is this project's.
- **The upstream's rules**: two kinds of record under one root, a description in English, a product's name and versions, a version entry's shapes, and each severity's score band. What LinkML cannot state, `tests/cve_rules.py` checks.
- **A test that walks the upstream's JSON schemas beside the classes**, and fails on anything missing, added or of another cardinality.
- **A pinned sample of 421 real records**, validated unchanged in a job of its own, and a small extract under the Terms of Use.
- **A weekly upstream watch** that reports a new edition, a changed file or licence, changed Terms of Use, or a check that could not finish.
- **Mappings to SEPSES, SPDX 3.0.1, lmodel/stix, Dublin Core, schema.org and Wikidata**, each held by a test to a pinned term list or a released copy.
- **`.lokf/cve.yaml`, the schema's `lokf adapt` copy, rooted on `CveRecord`.** The knowledge release attaches it as `schema-<tag>-cve.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The template moves to linkml-project-copier v0.5.0**, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `cve-linkml`. PyPI publishing stays off.
- **Slots take the upstream's keys**, such as `cveMetadata`, in place of the old snake_case slots with aliases, and classes take the `Cve` prefix.

### Removed

- **The import of lmodel/vulnerability-core**, whose base classes fit none of the upstream's objects.
- **The hand-kept SSSOM files under `src/cve/mappings/`.** No source confirmed their rows, and the schema is now the one home for mappings.
- **The invented subsets and abstract classes, the patched generator scripts, the PyPI publishing workflow and the mkdocs site.** The knowledge website replaces the site.
