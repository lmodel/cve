# Example data for cve

- `valid/` holds an example of each class that the generated dataclasses can load. `linkml-run-examples` and `tests/test_data.py` read it.
- `invalid/` holds a counter-example for each constraint the validator can state. Each file's first line, `# Fails at: <JSON pointer>`, names its one failing place, and `tests/test_data.py` holds it there.
- `problem/valid/` holds the valid examples that `linkml-run-examples` cannot load: the tree root, and whatever carries an extension key or free-form content, which LinkML 1.12.1's dataclasses refuse. `tests/test_data.py` validates them.
- `problem/invalid/` holds a counter-example for each rule the generated JSON Schema cannot state, which `tests/cve_rules.py` checks.
- `cvelist/` holds real records: see [its README](cvelist/README.md).

A file name is `ClassName-anything.yaml`, and the class is the part before the first hyphen. `tests/test_data.py` also asks the upstream's own schema about each file, so an example here says nothing the upstream does not.
