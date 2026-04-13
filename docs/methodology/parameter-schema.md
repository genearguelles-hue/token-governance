# Parameter Schema

**Repository:** Token Governance  
**Document type:** Methodology note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/methodology/analytical-method-definition.md`  
- `docs/methodology/parameter-inventory.md`

## 1. Purpose

This document defines the proposed schema for externalizing the Token Governance simulation parameters.

Its purpose is to create a researcher-facing configuration layer that separates:

- the **simulation engine**
- the **parameter state of the model**
- the **batch-specific overrides used for calibration and exploration**

This schema is intended to let future runs represent explicit, inspectable model states rather than repeated invocations of parameters embedded only inside the Python script.

## 2. Why a parameter schema is needed

The parameter inventory established that the simulation already contains a real parameter layer. That layer currently lives inside:

- the `Scenario` dataclass
- the `GovernanceConfig` dataclass
- the hard-coded values assigned in `SCENARIOS`, `UNGOVERNED`, and `GOVERNED`

The problem is therefore not absence of parameters. The problem is absence of an **externalized parameter interface**.

A parameter schema is needed so that:

- future calibration batches correspond to explicit model states
- scenario definitions can be inspected without opening Python source
- governed vs. ungoverned parameter values can be compared directly
- researchers can extend the model without editing engine logic by hand
- archival runs can be traced to named config states

## 3. Design goals

The schema should satisfy the following goals:

1. **Human-readable**
2. **Easy to version**
3. **Explicit about scenarios and governance layers**
4. **Easy to override for calibration batches**
5. **Stable enough for future researchers to extend**
6. **Separated from secrets and environment-specific settings**

For these reasons, the preferred target format should be **YAML**, not `.env`.

## 4. Recommended directory structure

A suitable structure would be:

```text
config/
├── base_parameters.yaml
├── calibration_batch_03.yaml
├── calibration_batch_04.yaml
└── scenario_overrides.yaml
```

This is only a recommendation, but it captures the basic idea:

- one base parameter definition
- optional per-batch override files
- optional scenario-specific override files

## 5. Schema layers

The schema should be organized into the following layers.

### A. Run metadata
Defines the experiment identity.

### B. Run controls
Defines seed, trial count, and output settings.

### C. Scenario definitions
Defines baseline interaction behavior per scenario.

### D. Governance definitions
Defines governed vs. ungoverned modifiers.

### E. Optional batch overrides
Defines what differs in a particular batch relative to the base model.

## 6. Proposed top-level schema structure

A high-level config file should support sections like:

- `metadata`
- `run`
- `scenarios`
- `governance`
- `overrides`

A conceptual top-level structure would look like:

```yaml
metadata:
  label: calibration_batch_03_seed42
  description: First config-driven calibration batch

run:
  seed: 42
  trials: 4000
  outdir: simulation/outputs/calibration_batch_03_seed42

scenarios:
  short_horizon_determinate: ...
  long_horizon_workflow: ...
  nonlinear_human_centered: ...

governance:
  ungoverned: ...
  governed: ...

overrides:
  notes: "Batch-specific adjustments here"
```

## 7. Run metadata schema

The `metadata` section should describe the identity of the configuration.

### Required fields
- `label`
- `description`

### Recommended optional fields
- `created_from`
- `author`
- `date`
- `notes`

### Example
```yaml
metadata:
  label: calibration_batch_03_seed42
  description: First config-driven calibration batch
  created_from: calibration_batch_02_seed42
  notes: "Introduces explicit parameter changes to repair and compression dynamics"
```

## 8. Run control schema

The `run` section should define experiment controls.

### Required fields
- `seed`
- `trials`
- `outdir`

### Example
```yaml
run:
  seed: 42
  trials: 4000
  outdir: simulation/outputs/calibration_batch_03_seed42
```

These are not behavioral model parameters, but they are necessary for reproducibility.

## 9. Scenario schema

Each scenario entry should correspond to the current `Scenario` dataclass fields.

### Required fields per scenario
- `name`
- `base_turns`
- `new_input_mean`
- `new_input_sd`
- `base_output_mean`
- `base_output_sd`
- `tool_need_prob`
- `repair_prob`
- `repeat_state_prob`
- `stale_retention_prob`
- `excess_context_prob`
- `verbosity_prob`
- `rebrief_prob`
- `session_base_state`
- `relevant_carry_forward`

### Example
```yaml
scenarios:
  short_horizon_determinate:
    name: short_horizon_determinate
    base_turns: 6
    new_input_mean: 360
    new_input_sd: 45
    base_output_mean: 260
    base_output_sd: 40
    tool_need_prob: 0.12
    repair_prob: 0.16
    repeat_state_prob: 0.10
    stale_retention_prob: 0.08
    excess_context_prob: 0.12
    verbosity_prob: 0.18
    rebrief_prob: 0.05
    session_base_state: 180
    relevant_carry_forward: 120
```

## 10. Governance schema

The `governance` section should define both `ungoverned` and `governed` configurations corresponding to the current `GovernanceConfig` dataclass.

### Required fields per governance profile
- `label`
- `governance_overhead_mean`
- `governance_overhead_sd`
- `context_filter_strength`
- `repeat_block_strength`
- `stale_prune_strength`
- `compression_strength`
- `output_bound_strength`
- `progressive_disclosure_strength`
- `tool_threshold_strength`
- `tool_token_reduction`
- `repair_reduction_strength`
- `rebrief_reduction_strength`
- `turn_efficiency_bonus`

### Example
```yaml
governance:
  ungoverned:
    label: ungoverned
    governance_overhead_mean: 0.0
    governance_overhead_sd: 0.0
    context_filter_strength: 0.0
    repeat_block_strength: 0.0
    stale_prune_strength: 0.0
    compression_strength: 0.0
    output_bound_strength: 0.0
    progressive_disclosure_strength: 0.0
    tool_threshold_strength: 0.0
    tool_token_reduction: 0.0
    repair_reduction_strength: 0.0
    rebrief_reduction_strength: 0.0
    turn_efficiency_bonus: 0.0

  governed:
    label: governed
    governance_overhead_mean: 36.0
    governance_overhead_sd: 6.0
    context_filter_strength: 0.52
    repeat_block_strength: 0.56
    stale_prune_strength: 0.58
    compression_strength: 0.44
    output_bound_strength: 0.34
    progressive_disclosure_strength: 0.22
    tool_threshold_strength: 0.47
    tool_token_reduction: 0.38
    repair_reduction_strength: 0.48
    rebrief_reduction_strength: 0.54
    turn_efficiency_bonus: 0.16
```

## 11. Override schema

The `overrides` section should exist so that future calibration batches can define only what changes relative to a base parameter file.

### Purpose
This allows a batch to specify:
- “change only these 3 parameters”
rather than duplicating the entire model state.

### Example concept
```yaml
overrides:
  scenarios:
    nonlinear_human_centered:
      repair_prob: 0.31
      excess_context_prob: 0.36

  governance:
    governed:
      compression_strength: 0.48
      governance_overhead_mean: 38.0
```

This is useful for calibration research because it makes each batch more legible and easier to compare.

## 12. Required vs optional approach

The recommended approach is:

### Base file
Contains the full parameter state.

### Batch override file
Contains only the changed fields.

This gives the project:
- stable defaults
- explicit differences per batch
- cleaner version history
- easier comparison across runs

## 13. Validation expectations

A valid parameter schema should support at least the following checks:

1. every scenario has all required fields
2. every governance profile has all required fields
3. numeric probabilities remain in sensible ranges
4. output folder names are explicit
5. override files do not introduce unknown fields
6. missing fields in an override are inherited from the base file

## 14. What should not go in this schema

The parameter schema should not be overloaded.

Do **not** use it for:
- secrets
- tokens
- API keys
- local machine credentials
- unrelated environment setup

Those belong in `.env` or environment-specific tooling.

This schema is for the **model state**, not machine secrets.

## 15. Recommended implementation path

The practical next implementation sequence should be:

1. create `docs/methodology/parameter-schema.md`
2. create `config/base_parameters.yaml`
3. populate it with the current script-embedded values
4. modify the simulation engine so it can load config values
5. create `config/calibration_batch_03.yaml` as the first batch override
6. run the first truly config-driven calibration batch

## 16. Why this matters

Once this schema is implemented, future batches will finally mean something precise:

- same engine
- different explicit parameter state
- reproducible batch identity
- interpretable changes

That is the real transition from:
- proof-of-concept archival workflow
to
- research-grade configurable simulation framework

## 17. Working conclusion

The Token Governance simulation now has:

- a codified analytical method
- a documented parameter inventory
- a clear next step for externalization

This schema definition is the bridge between those things.

Its purpose is to make future calibration runs explicit, reproducible, inspectable, and extensible by researchers other than the original author.

---

## Suggested repository placement

Recommended path:

```text
docs/methodology/parameter-schema.md
```
