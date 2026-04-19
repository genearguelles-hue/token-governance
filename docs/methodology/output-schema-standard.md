# Output Schema Standard

**Repository:** Token Governance  
**Document type:** Methodology note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/methodology/analytical-method-definition.md`  
- `docs/methodology/parameter-inventory.md`  
- `docs/methodology/parameter-schema.md`

## 1. Purpose

This document defines the output schema standard for the Token Governance simulation framework.

Its purpose is to ensure that archived outputs remain directly comparable across:

- baseline runs
- preserved reruns
- calibration batches
- future multi-seed runs
- future sensitivity sweeps

The immediate motivation is practical: batch-to-batch numerical comparison should not require ad hoc normalization of merge keys or output formats.

## 2. Why a schema standard is needed

Earlier comparisons revealed that some output files could not be merged directly across batches because key fields were not stable.

The most obvious example was the `scenario` field, where one batch used human-readable labels such as:

- `Short-horizon determinate`
- `Long-horizon workflow`
- `Nonlinear human-centered`

while another batch used machine-stable labels such as:

- `short_horizon_determinate`
- `long_horizon_workflow`
- `nonlinear_human_centered`

This caused direct joins on `scenario` to fail.

The output schema standard therefore exists to ensure that comparison keys, row structure, and column definitions remain congruent across batches.

## 3. Core principle

The simulation outputs must distinguish between:

- **machine-stable keys**
- **human-readable labels**

Machine-stable keys should be used for:
- CSV merge fields
- downstream analysis
- automated batch comparison
- scripting
- archival consistency

Human-readable labels should be used for:
- charts
- markdown summaries
- presentation material
- reader-facing notes

These two purposes should not be conflated.

## 4. Required canonical keys

The following canonical keys should be enforced across output files.

### A. Scenario key
Use a machine-stable field:

- `short_horizon_determinate`
- `long_horizon_workflow`
- `nonlinear_human_centered`

Recommended field name:

```text
scenario
```

### B. Scenario label
Use a separate human-readable field:

- `Short-horizon determinate`
- `Long-horizon workflow`
- `Nonlinear human-centered`

Recommended field name:

```text
scenario_label
```

### C. Condition key
Use a machine-stable field:

- `ungoverned`
- `governed`

Recommended field name:

```text
condition
```

### D. Condition label
Use a separate human-readable field:

- `Ungoverned`
- `Governed`

Recommended field name:

```text
condition_label
```

## 5. Standard naming rules

To preserve comparison stability, output keys should follow these rules.

### Scenario key rules
- lowercase only
- words separated by underscores
- no spaces
- no hyphens
- no punctuation beyond underscore

### Condition key rules
- lowercase only
- no spaces
- no punctuation

### Label rules
- title-style or reader-friendly text is allowed
- labels must not be used as merge keys

## 6. Standard file purposes

Each output file should have a stable and explicit purpose.

### A. `simulation_compare.csv`
**Row granularity:** one row per `scenario`

**Purpose:** compare governed vs. ungoverned headline metrics at the scenario level

### B. `simulation_summary.csv`
**Row granularity:** one row per `scenario + condition`

**Purpose:** report summary statistics for each scenario-condition combination

### C. `simulation_attribution.csv`
**Row granularity:** one row per `scenario`

**Purpose:** report savings attribution shares for each scenario

### D. `simulation_trial_level.csv`
**Row granularity:** one row per trial instance (and any additional grouping fields used by the engine)

**Purpose:** provide detailed per-trial observations for deeper analysis

The row meaning of each file must remain stable across batches.

## 7. Standard merge keys by file

### A. `simulation_compare.csv`
Required merge key:
- `scenario`

Optional display field:
- `scenario_label`

### B. `simulation_summary.csv`
Required merge keys:
- `scenario`
- `condition`

Optional display fields:
- `scenario_label`
- `condition_label`

### C. `simulation_attribution.csv`
Required merge key:
- `scenario`

Optional display field:
- `scenario_label`

### D. `simulation_trial_level.csv`
Required merge keys should be explicitly defined once the trial-level schema is finalized. At minimum, the file should include stable scenario and condition keys if batch-level merging is expected.

## 8. Standard column stability requirements

Across batches, the following should remain stable unless a new schema version is explicitly introduced:

- column names
- column meanings
- data types
- row granularity
- merge-key definitions

If a field must be renamed, added, or removed, that should be treated as a schema change and documented explicitly.

## 9. Recommended metadata fields

To improve auditability and downstream analysis, output files or the output README should also include stable metadata such as:

- `schema_version`
- `batch_label`
- `config_label`
- `seed`
- `trials`
- `engine_version`

These can be added as columns or as documented metadata in the output folder README, depending on implementation preference.

## 10. Recommended schema versioning

A schema version should be defined once the standardized output logic is implemented.

Recommended field name:

```text
schema_version
```

Initial recommendation:

```text
v1
```

The purpose of schema versioning is to make later changes explicit rather than silently breaking comparison scripts.

## 11. Standardization requirements for charts

Charts do not need machine-stable merge keys in the same way as CSVs, but they should still follow consistent naming and label practices.

### Chart recommendations
- file names should remain stable across batches
- displayed labels may be human-readable
- scenario names on charts should be derived from `scenario_label`, not `scenario`
- chart titles and axis labels should remain stable enough for comparison

## 12. Standardization requirements for README outputs

Each output folder README should document at least:

- batch label
- config files used
- seed
- trials
- schema version
- generated files

This makes archived runs easier to interpret later without reverse-engineering the run context.

## 13. Minimum implementation requirements

To say the output schema has been standardized, the simulation engine should do all of the following:

1. always write canonical `scenario` keys
2. always write canonical `condition` keys
3. optionally write separate label fields for reader-facing use
4. preserve fixed column names and row meanings
5. emit outputs that can be merged across batches without manual normalization

## 14. What should be avoided

The following should be avoided going forward:

- using human-readable labels as merge keys
- changing scenario naming conventions between batches
- changing condition labels between batches
- changing file row granularity without documenting it
- renaming columns without a schema version change
- relying on ad hoc post-processing to make outputs mergeable

## 15. Why this matters

The project is now entering a phase where comparison across explicit parameter states is central.

That means output comparability is no longer optional. It is part of the analytical method itself.

Without an output schema standard:
- delta analysis becomes fragile
- automated comparisons break
- future researchers must normalize outputs by hand
- calibration becomes less inspectable

With an output schema standard:
- batch comparisons become native
- sensitivity sweeps become easier
- multi-seed analysis becomes easier
- the framework becomes more reusable and credible

## 16. Recommended next implementation step

The next implementation step should be to modify the simulation engine so that all exported CSVs use:

- canonical machine-stable keys for merge fields
- optional display-label fields for human readability
- stable column names across all files

That is the practical change needed to make this standard operational.

## 17. Working conclusion

The Token Governance simulation now has:
- a codified analytical method
- a documented parameter inventory
- a defined parameter schema
- a config-driven run path

The next necessary piece is a stable output schema.

This note defines that requirement so future batch comparisons can be performed directly, reliably, and without manual normalization of merge keys.

---

## Suggested repository placement

Recommended path:

```text
docs/methodology/output-schema-standard.md
```
