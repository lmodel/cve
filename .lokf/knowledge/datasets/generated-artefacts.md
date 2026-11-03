---
type: Dataset
id: https://w3id.org/lmodel/cve/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the cve schema: the projections in `project/`, the Python models in `src/cve/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/cve/knowledge/datasets/cve-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: the docstring
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the jsonschema settings
  - id: about.md
    resource: docs/about.md
    title: What LinkML cannot say
  - resource: project
  - resource: src/cve/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:18:39Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/cve/datamodel/`. `just gen-doc` writes the merged schema to `docs/schema/cve.yaml` and the element pages to `docs/elements/`, which git ignores.[^justfile]

`project/jsonschema/cve.schema.json` is what a consumer without LinkML validates with. `tests/test_generated_json_schema.py` holds it to the generator's output.[^test_generated_json_schema.py]

The generators' settings sit in `.linkml/generators.yaml`. `include_range_class_descendants` is on, so a slot ranged over an abstract base accepts its concrete classes.[^generators.yaml]

The Python models refuse the extension keys and free-form objects most real records carry, because LinkML 1.12.1's generators for them ignore `extra_slots`.[^about.md]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, the docstring
[^generators.yaml]: .linkml/generators.yaml, the jsonschema settings
[^about.md]: docs/about.md, What LinkML cannot say
