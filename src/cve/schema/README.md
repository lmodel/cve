# Schema Directory

This folder contains the LinkML schema yaml files.

## Files

| File | Description |
|------|-------------|
| `cve.yaml` | Main CVE LinkML schema. Defines `CVERecord` (tree root), containers, metadata, affected products, metrics, and all supporting classes/slots/enums. Imports `vulnerability_core`. |
| `vulnerability_core.yaml` | Base schema with the abstract `Vulnerability` class and shared classes (`Product`, `AffectedProduct`, `Reference`, `Weakness`). Also maintained as a standalone schema in the `vulnerability-core` project. |
| `CVE_Record_Format_bundled.json` | Bundled upstream JSON Schema from CVE (Record Format). Used as a reference; validation tests use the LinkML schema instead. |

## Test Status (2026-05-07)

All 41 tests pass:

```
28 × test_data.py        — YAML fixture round-trip via yaml_loader
13 × test_third_party.py — upstream CVE JSON examples + authored gap-coverage fixtures validated against LinkML schema
```

Run with:

```bash
just test-all
```

## Recent Changes (2026-05-07)

- **CVSS v3.x consolidation**: Merged `CvssV3_0` and `CvssV3_1` into a single `CvssV3` class. The two CVSS versions share an identical metric model (3.1 was a clarification, not a structural change), so the duplicate class was eliminated. The `cvss3_version` slot now ranges over a new `CvssV3Version`
  enum (`"3.0"` or `"3.1"`) to distinguish them. The `MetricEntry.cvss_v3_0` and `MetricEntry.cvss_v3_1` slots are replaced by a single `cvss_v3`. CVSS v2.0 and v4.0 are unchanged — their metric models genuinely differ from v3.x and from each other.
  Lint adds two warnings on `CvssV3Version` permissible values (`"3.0"`, `"3.1"`) flagged as non-`UPPER_SNAKE_CASE`; this is intentional — the values must round-trip with the literal CVSS spec strings.

## Why three CVSS classes? (`CvssV2_0`, `CvssV3`, `CvssV4_0`)

A single generic `Cvss` class — or keeping only the newest `CvssV4_0` — was rejected for four reasons:

1. **Upstream uses versioned keys, not a generic `cvss` field.** [upstream/cve-schema/schema/CVE_Record_Format.json](../../../upstream/cve-schema/schema/CVE_Record_Format.json) defines `metrics[]` items via `anyOf` over fixed property names `cvssV2_0`, `cvssV3_0`, `cvssV3_1`, `cvssV4_0`, `other`. Producing valid CVE records requires emitting the version-specific key — there is no `cvss` key.

2. **Real records mix versions in one entry.** [upstream/cve-schema/schema/docs/full-record-advanced-example.json](../../../upstream/cve-schema/schema/docs/full-record-advanced-example.json) shows a single `metrics` item populated with both `cvssV4_0` and `cvssV3_1` simultaneously. CNAs publish v4.0 alongside v3.1 during the transition; NVD re-scores legacy CVEs in newer versions. A single `Cvss` field cannot represent both at once.

3. **Metric models genuinely differ across major versions** — collapsing them would lose validation precision:
   - **v2.0** uses `accessVector`/`accessComplexity`/`authentication`, lacks `scope` and `baseSeverity`. No severity-tier enum; ranges and value sets are incompatible with v3/v4.
   - **v3.x** introduces `scope`, `privilegesRequired`, `userInteraction`, and `baseSeverity` (`NONE`/`LOW`/`MEDIUM`/`HIGH`/`CRITICAL`).
   - **v4.0** adds six structurally new metrics (`attackRequirements`, `Safety`, `Automatable`, `Recovery`, `valueDensity`, `providerUrgency`) and splits CIA impact into vulnerable-system (`VC`/`VI`/`VA`) and subsequent-system (`SC`/`SI`/`SA`) variants.

   A single class with every metric optional would silently accept impossible combinations (e.g. v2.0 with `attackRequirements`) and make `baseSeverity` ambiguously typed.

4. **Historical coverage requires v2.0.** ~80,000 CVEs published 2007–2015 are scored only in CVSS v2.0. Dropping v2.0 means the schema cannot represent the bulk of historical NVD data.

**What we *did* consolidate (and why it was safe):** CVSS 3.0 and 3.1 share an identical metric model — same slots, same enums, same required fields. The 3.1 spec was a clarification, not a structural change. Distinguishing them at the class level was pure duplication; using a `cvss3_version` enum (`"3.0"` | `"3.1"`) within a single `CvssV3` class preserves all validation power with zero loss.

## Upstream JSON Schema Coverage

The LinkML schema targets full semantic coverage of `CVE_Record_Format.json` (v5.2.0). Some upstream JSON Schema constraints have no LinkML equivalent and are documented as feature gaps in `ISSUE.md`.

| Upstream constraint | Status |
|---|---|
| `cweId` pattern `^CWE-[1-9][0-9]*$` | ✅ `pattern:` on `cwe_id` slot |
| `x_*` tag extension strings on `cnaTags`/`adpTags` (`^x_.*$`) | ✅ `any_of: [{range: CNATag}, {range: string, pattern: "^x_.*$"}]` |
| `VersionEntry`: `lessThan` / `lessThanOrEqual` mutually exclusive | ✅ class-level `none_of` with `slot_conditions` |
| `VersionEntry`: `versionType` required when `lessThan` or `lessThanOrEqual` present | ✅ class-level `rules:` preconditions/postconditions |
| `AffectedProduct` co-requirements: (vendor+product ∨ collectionURL+packageName) ∧ (versions ∨ defaultStatus) | ✅ class-level `all_of` / `any_of` with `slot_conditions` |
| `MetricEntry`: at least one of cvssV4_0/cvssV3_1/cvssV3_0/cvssV2_0/other required | ✅ class-level `any_of` with `slot_conditions` (CvssV3_0+CvssV3_1 unified as `CvssV3`; version distinguished via `cvss3_version` enum) |
| `references` max 512 items | ✅ `maximum_cardinality: 512` on `cve_references` slot |
| `shortName` length 2–32 characters | ✅ `pattern: "^.{2,32}$"` on `short_name` + `assigner_short_name` slots |
| `other_metric_content` arbitrary JSON object | ✅ `range: Any` (`class_uri: linkml:Any`) |
| `descriptions` must contain ≥1 English-language entry (`contains`) | ❌ no `contains` constraint in LinkML |
| `x_*` vendor-extension `patternProperties` on CNA/ADP containers | ❌ no open/pattern-property concept in LinkML |
| `AdpContainer` must have ≥1 property beyond `providerMetadata` (`minProperties: 2`) | ❌ no minimum-property-count rule in LinkML |

## Key Design Notes

- `CVERecord` uses `is_a: Vulnerability` (inherits `cve_id`, `description`, etc.) with those slots marked `recommended` on the base class and `required: false / identifier: false` overridden in `CVERecord.slot_usage`. This allows top-level CVE Records in the schema model to carry `cve_id` while upstream JSON examples (which put the ID in `cveMetadata`) still validate cleanly.
- `CveMetadata` and `CnaContainer` are slot-free abstract classes with `union_of`. Their concrete subclasses carry all slots. This prevents `gen-python` from emitting `@dataclass`-coercion code that would fail when instantiated with subclass-specific fields.
- Slots with `any_of` alternatives must also declare a parent `range:` pointing to the abstract union class; without it `gen-json-schema` falls back to `"type": "string"`, rejecting object values.

Upstream bugs / schema mismatches encountered
---------------------------------------------

1. **Abstract ``CveMetadata`` base class with own slots breaks ``gen-python``**
   When an abstract class has its own slots it becomes a ``@dataclass``.
   The generated ``__post_init__`` code in the parent class coerces the
   ``cve_metadata`` value with ``CveMetadata(**as_dict(value))``, which fails with ``TypeError: unexpected keyword argument`` for any key belonging only to a concrete subclass (e.g. ``published_state``).  Fixed by moving all slots into the concrete subclasses (``CveMetadataPublished``, ``CveMetadataRejected``) and leaving ``CveMetadata`` slot-free (mirroring the ``CnaContainer`` pattern).

2. **Inherited ``identifier`` slot forced ``required`` in JSON Schema**
   ``CVERecord`` inherits ``cve_id`` (marked ``identifier: true``) from the abstract ``Vulnerability`` class. In LinkML 1.10.0, ``required: false`` alone in child ``slot_usage`` does not suppress inherited identifier requiredness; ``identifier: false`` is also needed. This caused full-record upstream examples (where the CVE ID lives inside ``cveMetadata``, not at the record root) to fail with ``'cve_id' is a required property`` until both overrides were applied.

3. **Translator recursion failed for union-typed slots with abstract range**
   The original translator passed only the abstract primary class
   (e.g. ``CnaContainer``) as the context when recursing into nested objects. Since ``CnaContainer`` has no own slots, its alias map was empty, so camelCase keys inside the ``cna`` container were left untranslated.  Fixed by passing *all* candidate classes (abstract + all concrete alternatives) and merging their alias maps, with range lookup falling through from the abstract class to the first concrete class that owns the slot.
