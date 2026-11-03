# cve

This project is a LinkML model of the CVE Record Format, version 5.2.0, the JSON form in which the CVE Program publishes a record of a vulnerability. It keeps the format's own keys and values, so a real record validates unchanged.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together and what the model leaves out
- [`cve.yaml`](schema/cve.yaml): the schema, with its modules merged

## Validating a record

```bash
uv run linkml-validate -s src/cve/schema/cve.yaml -C CveRecordRoot record.yaml
```

This checks a file against the JSON Schema generated from the schema. `project/jsonschema/cve.schema.json` is the same schema for anyone without LinkML. A consumer that wants the upstream's whole rule set also runs the checks in `tests/cve_rules.py`, because LinkML 1.12.1 cannot state them:

- that a key beyond the declared ones in a container begins `x_` and holds no full stop;
- that a list the upstream holds unique repeats no item;
- that a CVSS 3.0, 3.1 or 4.0 score is a multiple of 0.1;
- that the source, a metric's content and an ADP container are not empty;
- that a key is not null;
- the lengths of a CPE name, a CWE identifier and an extension tag.

## What was checked

A pinned sample of 421 real records validates unchanged, with no departure. `tests/test_coverage.py` walks the upstream's JSON schemas beside the classes and fails on anything missing, added or of another cardinality.
