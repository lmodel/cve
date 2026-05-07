# Schema Directory

This folder contains the LinkML schema yaml files.

## Files

| File | Description |
|------|-------------|
| `cve.yaml` | Main CVE LinkML schema. Defines `CVERecord` (tree root), containers, metadata, affected products, metrics, and all supporting classes/slots/enums. Imports `vulnerability_core`. |
| `vulnerability_core.yaml` | Base schema with the abstract `Vulnerability` class and shared classes (`Product`, `AffectedProduct`, `Reference`, `Weakness`). Also maintained as a standalone schema in the `vulnerability-core` project. |
| `CVE_Record_Format_bundled.json` | Bundled upstream JSON Schema from MITRE (CVE Record Format). Used as a reference; validation tests use the LinkML schema instead. |

## Test Status (2026-05-07)

All 33 tests pass:

```
28 × test_data.py   — YAML fixture round-trip via yaml_loader
 5 × test_third_party.py — upstream MITRE JSON examples validated against LinkML schema
```

Run with:

```bash
just test-all
```

## Key Design Notes

- `CVERecord` uses `is_a: Vulnerability` (inherits `cve_id`, `description`, etc.) with those slots marked `recommended` on the base class and `required: false / identifier: false` overridden in `CVERecord.slot_usage`. This allows top-level CVE Records in the schema model to carry `cve_id` while upstream JSON examples (which put the ID in `cveMetadata`) still validate cleanly.
- `CveMetadata` and `CnaContainer` are slot-free abstract classes with `union_of`. Their concrete subclasses carry all slots. This prevents `gen-python` from emitting `@dataclass`-coercion code that would fail when instantiated with subclass-specific fields.
- Slots with `any_of` alternatives must also declare a parent `range:` pointing to the abstract union class; without it `gen-json-schema` falls back to `"type": "string"`, rejecting object values.

Upstream bugs / schema mismatches encountered
---------------------------------------------

1. **Abstract ``CveMetadata`` base class with own slots breaks ``gen-python``**
   When an abstract class has its own slots it becomes a ``@dataclass``.
   The generated ``__post_init__`` code in the parent class coerces the
   ``cve_metadata`` value with ``CveMetadata(**as_dict(value))``, which fails
   with ``TypeError: unexpected keyword argument`` for any key belonging only
   to a concrete subclass (e.g. ``published_state``).  Fixed by moving all
   slots into the concrete subclasses (``CveMetadataPublished``,
   ``CveMetadataRejected``) and leaving ``CveMetadata`` slot-free (mirroring
   the ``CnaContainer`` pattern).

2. **Inherited ``identifier`` slot forced ``required`` in JSON Schema**
   ``CVERecord`` inherits ``cve_id`` (marked ``identifier: true``) from the
   abstract ``Vulnerability`` class. In LinkML 1.10.0, ``required: false``
   alone in child ``slot_usage`` does not suppress inherited identifier
   requiredness; ``identifier: false`` is also needed. This caused full-record
   upstream examples (where the CVE ID lives inside ``cveMetadata``, not at the
   record root) to fail with ``'cve_id' is a required property`` until both
   overrides were applied.

3. **Translator recursion failed for union-typed slots with abstract range**
   The original translator passed only the abstract primary class
   (e.g. ``CnaContainer``) as the context when recursing into nested objects.
   Since ``CnaContainer`` has no own slots, its alias map was empty, so
   camelCase keys inside the ``cna`` container were left untranslated.  Fixed
   by passing *all* candidate classes (abstract + all concrete alternatives)
   and merging their alias maps, with range lookup falling through from the
   abstract class to the first concrete class that owns the slot.
