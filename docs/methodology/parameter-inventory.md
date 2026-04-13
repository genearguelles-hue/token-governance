# Parameter Inventory

**Repository:** Token Governance  
**Document type:** Methodology note  
**Status:** Draft v0.1  
**Source basis:** Direct inspection of `simulation/src/persona_token_governance_monte_carlo.py`

## 1. Purpose

This document inventories the tunable parameters currently embedded inside the Token Governance simulation engine.

Its purpose is to make explicit what has until now remained implicit:

- which parameters define baseline scenario behavior
- which parameters define governed vs. ungoverned behavior
- which parameters control experimental runs
- which parameters appear to exert the greatest influence on outputs
- how these parameters map to the archived CSV and chart outputs already produced

This note is the first step toward externalizing the model’s parameter layer so future calibration runs can be driven by explicit configuration rather than undocumented script-internal assumptions.

## 2. Key finding

The simulation already contains a real parameter layer.

That layer is currently embedded in three places:

1. the `Scenario` dataclass
2. the `GovernanceConfig` dataclass
3. the concrete values assigned in:
   - `SCENARIOS`
   - `UNGOVERNED`
   - `GOVERNED`

The project therefore does **not** lack parameters. It lacks an externalized and researcher-facing parameter interface.

## 3. Parameter classes

The parameters currently fall into three major classes:

### A. Scenario-level parameters
These define the baseline behavior of each scenario.

### B. Governance-level parameters
These define how governance modifies the baseline process.

### C. Run-level parameters
These define the execution of a run, such as seed, trial count, and output location.

## 4. Scenario dataclass parameters

The `Scenario` dataclass currently contains the following parameters:

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

### Functional interpretation

These variables collectively define the baseline process profile of a scenario.

They shape:
- interaction horizon
- typical context size
- typical output size
- likelihood of repair behavior
- likelihood of repeated stable-state carry-forward
- stale-state persistence
- oversized context admission
- verbosity
- rebriefing behavior
- base session-state burden

## 5. GovernanceConfig dataclass parameters

The `GovernanceConfig` dataclass currently contains the following parameters:

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

### Functional interpretation

These variables collectively define how the governance layer modifies the baseline scenario process.

They shape:
- governance direct cost
- context filtering
- suppression of redundant stable-state carry-forward
- stale-state pruning
- structured-state compression
- output control
- progressive disclosure
- tool restraint
- reduction of repair loops
- reduction of rebriefing
- turn efficiency

## 6. Run-level parameters

The current script also uses run-level controls:

- `seed`
- `trials`
- `outdir`

These are not behavior parameters in the same sense as the scenario and governance variables, but they are still important to reproducibility and archival discipline.

## 7. Concrete scenario values currently embedded in the script

## 7.1 Short-horizon determinate

- `base_turns = 6`
- `new_input_mean = 360`
- `new_input_sd = 45`
- `base_output_mean = 260`
- `base_output_sd = 40`
- `tool_need_prob = 0.12`
- `repair_prob = 0.16`
- `repeat_state_prob = 0.10`
- `stale_retention_prob = 0.08`
- `excess_context_prob = 0.12`
- `verbosity_prob = 0.18`
- `rebrief_prob = 0.05`
- `session_base_state = 180`
- `relevant_carry_forward = 120`

## 7.2 Long-horizon workflow

- `base_turns = 13`
- `new_input_mean = 620`
- `new_input_sd = 85`
- `base_output_mean = 430`
- `base_output_sd = 70`
- `tool_need_prob = 0.32`
- `repair_prob = 0.28`
- `repeat_state_prob = 0.38`
- `stale_retention_prob = 0.26`
- `excess_context_prob = 0.33`
- `verbosity_prob = 0.34`
- `rebrief_prob = 0.24`
- `session_base_state = 520`
- `relevant_carry_forward = 240`

## 7.3 Nonlinear human-centered

- `base_turns = 15`
- `new_input_mean = 700`
- `new_input_sd = 110`
- `base_output_mean = 520`
- `base_output_sd = 95`
- `tool_need_prob = 0.26`
- `repair_prob = 0.34`
- `repeat_state_prob = 0.42`
- `stale_retention_prob = 0.32`
- `excess_context_prob = 0.39`
- `verbosity_prob = 0.41`
- `rebrief_prob = 0.31`
- `session_base_state = 640`
- `relevant_carry_forward = 300`

## 8. Concrete governance values currently embedded in the script

## 8.1 Ungoverned

In the ungoverned configuration, all governance strengths are effectively zero:

- `governance_overhead_mean = 0.0`
- `governance_overhead_sd = 0.0`
- `context_filter_strength = 0.0`
- `repeat_block_strength = 0.0`
- `stale_prune_strength = 0.0`
- `compression_strength = 0.0`
- `output_bound_strength = 0.0`
- `progressive_disclosure_strength = 0.0`
- `tool_threshold_strength = 0.0`
- `tool_token_reduction = 0.0`
- `repair_reduction_strength = 0.0`
- `rebrief_reduction_strength = 0.0`
- `turn_efficiency_bonus = 0.0`

## 8.2 Governed

- `governance_overhead_mean = 36.0`
- `governance_overhead_sd = 6.0`
- `context_filter_strength = 0.52`
- `repeat_block_strength = 0.56`
- `stale_prune_strength = 0.58`
- `compression_strength = 0.44`
- `output_bound_strength = 0.34`
- `progressive_disclosure_strength = 0.22`
- `tool_threshold_strength = 0.47`
- `tool_token_reduction = 0.38`
- `repair_reduction_strength = 0.48`
- `rebrief_reduction_strength = 0.54`
- `turn_efficiency_bonus = 0.16`

## 9. Parameter-to-output mapping

The value of the inventory depends on linking parameters to observable outputs.

## 9.1 Turn count drivers

Primary parameters:
- `base_turns`
- `turn_efficiency_bonus`

Likely output impact:
- turn count
- average turns per task
- total token burn

## 9.2 Context-load drivers

Primary parameters:
- `new_input_mean`
- `new_input_sd`
- `relevant_carry_forward`
- `session_base_state`

Likely output impact:
- context token volume
- relevant context burden
- total token burn

## 9.3 Output-size drivers

Primary parameters:
- `base_output_mean`
- `base_output_sd`
- `verbosity_prob`
- `output_bound_strength`
- `progressive_disclosure_strength`

Likely output impact:
- output token volume
- output-excess burden
- total token burn

## 9.4 Repair-loop drivers

Primary parameters:
- `repair_prob`
- `repair_reduction_strength`

Likely output impact:
- repair-loop count
- future context burden
- future output burden
- total token burn

## 9.5 Context inflation / carry-forward drivers

Primary parameters:
- `repeat_state_prob`
- `stale_retention_prob`
- `excess_context_prob`
- `context_filter_strength`
- `repeat_block_strength`
- `stale_prune_strength`
- `compression_strength`

Likely output impact:
- redundant context
- stale context
- oversized context
- total context burden
- savings attribution structure

## 9.6 Tool burden drivers

Primary parameters:
- `tool_need_prob`
- `tool_threshold_strength`
- `tool_token_reduction`

Likely output impact:
- tool-token burden
- unnecessary tool usage burden
- total token burn

## 9.7 Rebrief drivers

Primary parameters:
- `rebrief_prob`
- `rebrief_reduction_strength`

Likely output impact:
- rebrief behavior
- repeated stable-state carry-forward
- future context burden

## 9.8 Governance direct-cost drivers

Primary parameters:
- `governance_overhead_mean`
- `governance_overhead_sd`

Likely output impact:
- governance token burden
- total token burn

## 10. Highest-leverage parameters for future calibration

Based on inspection of the script structure, the following appear to be the most important candidates for future true calibration.

## 10.1 First-tier parameters

- `repair_prob`
- `repair_reduction_strength`
- `excess_context_prob`
- `context_filter_strength`
- `compression_strength`
- `repeat_state_prob`
- `repeat_block_strength`
- `governance_overhead_mean`

These appear to be the strongest direct bridge between interaction degradation and compounding token burn.

## 10.2 Second-tier parameters

- `verbosity_prob`
- `output_bound_strength`
- `tool_need_prob`
- `tool_threshold_strength`
- `tool_token_reduction`
- `rebrief_prob`
- `rebrief_reduction_strength`

These are important, but appear more likely to support or refine the primary burn mechanisms rather than define them outright.

## 10.3 Structural scenario shapers

- `base_turns`
- `new_input_mean`
- `base_output_mean`
- `session_base_state`
- `relevant_carry_forward`

These define the shape of each scenario and should usually be changed more cautiously than the first-tier calibration parameters.

## 11. Methodological implication

This inventory clarifies a central methodological fact:

The project’s main limitation is **not** the absence of parameters.  
The limitation is the absence of an **externalized parameter interface**.

That means the simulation engine is already parameterized, but those parameters are still buried in code rather than being exposed through an explicit research-facing configuration layer.

## 12. Recommended next step

The next stage should create a formal parameter schema and then externalize these values.

Recommended follow-on artifacts:

1. `docs/methodology/parameter-schema.md`
2. `config/base_parameters.yaml`
3. `config/calibration_batch_03.yaml`

This would let future batches represent explicit model-state changes rather than repeated invocations of a fixed embedded parameter set.

## 13. Working conclusion

The Token Governance simulation now has an inspectable parameter inventory.

That is a major milestone.

It means the project can now move from:

- archived runs of an implicitly parameterized engine

to:

- explicit control of a defined model parameter set

This is the necessary bridge from proof-of-concept workflow discipline to research-grade model configuration.

---

## Suggested repository placement

Recommended path:

```text
docs/methodology/parameter-inventory.md
```
