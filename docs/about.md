# About cve

This page is for anyone reading the schema's elements: it says how the classes fit together and what the model leaves out.

## How a record is shaped

The upstream's top level is a choice between two kinds of record, and the schema has one class for each. `CvePublishedRecord` and `CveRejectedRecord` both hold a `cveMetadata` and `containers`, typed for their state. `CveRecordRoot` is the tree root, which takes exactly one of the two. So a record with the rejected state and a published container fails at the root.

A published record's `containers` hold the assigning authority's `cna` container and any `adp` containers that others add. A rejected record has only a small `cna` container, which says why it was rejected.

The CVSS scores sit in their own module, `cve_cvss`, which imports only the LinkML types, so that lmodel/nist-nvd can take it alone. A name that recurs across CVSS versions, such as `attackVector`, is one slot that each class narrows, since the value lists differ.

## Keys

The keys and values are the upstream's own, such as `cveMetadata`, `vectorString` and `NETWORK`, and the classes carry a `Cve` or `Cvss` prefix. Each element's `upstream_path` annotation names the place in `upstream/schema/` that it renders.

A record's `cveId` sits inside `cveMetadata`, so no slot of the record is its identifier.

## What LinkML cannot say

The classes that hold a publisher's own keys beginning `x_` use `extra_slots`, which opens them to any key. The generated JSON Schema therefore passes a misspelled key there, and `tests/cve_rules.py` refuses it. The dataclasses and Pydantic models from LinkML 1.12.1 ignore `extra_slots`, so they refuse those keys, and most real records carry one. Validate real records with the JSON Schema.

## What is left out

CVSS 4.0's rules in the upstream name `threatScore`, `threatSeverity`, `environmentalScore` and `environmentalSeverity`, but its list of properties has none of them and it refuses any other key. A score object cannot carry them, so the class has no such slots.

The schema says nothing about whether what a record claims is true.
