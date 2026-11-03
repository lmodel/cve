<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# cve

Common Vulnerabilities and Exposures (CVE) Record Format 5.2.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/cve](https://lmodel.github.io/cve)

## What it models

The schema renders the [CVE Record Format](https://github.com/CVEProject/cve-schema), version 5.2.0, published on 29 October 2025, with the Common Vulnerability Scoring System (CVSS) schemas it imports. It keeps the format's own keys and values, so a real record validates unchanged.

`upstream/` holds the edition's files, pinned by hash, and `tests/test_coverage.py` holds the schema to them in both directions. A pinned sample of 421 real records from [cvelistV5](https://github.com/CVEProject/cvelistV5) validates with no departure. A weekly workflow opens an issue when a new edition appears, a pinned file or a licence changes, or the Terms of Use change. [docs/index.md](docs/index.md) says how to validate a record, and what LinkML cannot check.

## Mappings

The schema is the one home for mappings. The hand-kept SSSOM files that sat under `src/cve/mappings/` are gone, since no source confirmed their rows. The schema maps to no member of its own family: lmodel/nist-nvd and lmodel/kev-catalog map to it.

* **[SEPSES](https://www.sepses.org/vocab/ref/cve/) CVE and CVSS ontologies**: `close_mappings` for records, references, CVSS 2 and 3 scores and metrics, and `broad_mappings` for a CVSS 4.0 score. `tests/test_mappings.py` checks each against the term list from their pinned files.
* **[SPDX](https://spdx.github.io/spdx-spec/v3.0.1/) 3.0.1 Security and Software profiles**: `close_mappings` for a record, its dates, score, severity, vector and package address, `related_mappings` for its CVSS relationships, and `meaning` on each CVSS severity. `tests/test_mappings.py` checks each against lmodel/spdx's released copy.
* **[lmodel/stix](https://github.com/lmodel/stix)**: `close_mappings` for a record and a reference. `tests/test_mappings.py` checks each against its released copy.
* **[Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [schema.org](https://schema.org/)**: `close_mappings` for dates, titles, descriptions, references, languages and the repository address, and `narrow_mappings` for the CVE identifier. `tests/test_mappings.py` checks each against the term list from their pinned files.
* **[Wikidata](https://www.wikidata.org/wiki/Q631425) Q631425**, the idea of a vulnerability: `related_mappings` on a record. The term list names it by hand, as read on 3 November 2026.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch, the real-record fetch and the mapping term extractor
* [src/cve/schema/](src/cve/schema): the LinkML schema, `cve.yaml`, `cve_record.yaml` and `cve_cvss.yaml` (edit these)
* [src/cve/datamodel/](src/cve/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), the term list in [upstream/](tests/upstream) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the upstream's files at the pinned tag, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/cve.yaml`, is the copy `just lokf-adapt` writes from `src/cve/schema/cve.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-cve.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `CveRecord` on `Concept`, so a concept may be a record of either kind. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CvePublishedRecord, CveRejectedRecord
```

Containers, products and scores stay values inside a record. The copy renames each key LOKF also defines and keeps its IRI, with a `cve_` prefix: `at`, `description`, `name`, `references`, `source`, `status`, `tags`, `title`, `type`, `url` and `version`. A few keys, such as `value` and `descriptions`, are other lmodel copies' too, under another IRI there. `tests/test_schema_rules.py` lists them and fails on a new one.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The format is under CC0 1.0, its CVSS schemas are also under FIRST's licence, and real records come under the CVE Program's Terms of Use: see [NOTICE](NOTICE). This is not a project of the CVE Program, MITRE or FIRST, and its use implies no endorsement by any of them. CVE is a trademark of The MITRE Corporation.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
