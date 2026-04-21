# Calibration Batch 04 Parameter Plan

**Repository:** Token Governance  
**Document type:** Calibration batch working plan  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-batch-03-results.md`
- `docs/results/calibration-batch-03-comparison.md`
- `docs/methodology/output-schema-standard.md`
- `config/base_parameters.yaml`
- `config/calibration_batch_03.yaml`

## 1. Purpose

This document defines the parameter-tuning plan for **Calibration Batch 04**.

Batch 04 should build directly on the first standardized, config-driven comparison spine:

- `baseline_reference_seed42`
- `post_release_rerun_seed42`
- `calibration_batch_03_seed42`

Batch 03 already moved the model in the intended direction:
- lower governed token burn in all scenarios
- higher reduction percentages in all scenarios
- fewer repair loops in both governed and ungoverned conditions
- stronger context/state share of savings

Batch 04 should therefore be a **refinement batch**, not a structural reset.

## 2. Batch identity

### Batch label
```text
calibration_batch_04_seed42
```

### Recommended output folder
```text
simulation/outputs/calibration_batch_04_seed42/
```

### Recommended run mode
Config-driven run using:
- `config/base_parameters.yaml`
- `config/calibration_batch_04.yaml`

## 3. What Batch 03 revealed

Relative to the standardized baseline/reference set, Batch 03 showed:

### A. Governed burn decreased in all scenarios
- short-horizon determinate: `3772.17 -> 3692.23` (**-79.95**)
- long-horizon workflow: `15669.50 -> 15175.79` (**-493.71**)
- nonlinear human-centered: `21463.25 -> 20770.85` (**-692.40**)

### B. Ungoverned burn also decreased
- short-horizon determinate: **-18.13**
- long-horizon workflow: **-178.53**
- nonlinear human-centered: **-670.67**

### C. Governance savings increased
- short-horizon determinate: `2304.05 -> 2365.87` (**+61.82**)
- long-horizon workflow: `13169.51 -> 13484.68` (**+315.18**)
- nonlinear human-centered: `19268.56 -> 19290.29` (**+21.73**)

### D. Reduction percentage improved in all scenarios
- short-horizon determinate: `37.919% -> 39.053%` (**+1.134 pct-pts**)
- long-horizon workflow: `45.666% -> 47.050%` (**+1.384 pct-pts**)
- nonlinear human-centered: `47.306% -> 48.152%` (**+0.846 pct-pts**)

### E. Repair loops declined clearly
Both governed and ungoverned repair loops fell across all scenarios, with the largest reductions in:
- long-horizon workflow
- nonlinear human-centered

### F. Attribution became more context/state driven
Context/state share of savings increased in all scenarios:
- short-horizon determinate: **+0.637 pct-pts**
- long-horizon workflow: **+0.327 pct-pts**
- nonlinear human-centered: **+0.325 pct-pts**

This means Batch 03 improved the model in the intended theoretical direction.

## 4. What Batch 04 should preserve

Batch 04 must preserve:

1. **Governed token burn remains lower than ungoverned token burn in all scenarios.**
2. **Short-horizon determinate remains the smallest governance-effect scenario.**
3. **Long-horizon workflow remains intermediate.**
4. **Nonlinear human-centered remains the largest governance-effect scenario.**
5. **Context/state governance remains the dominant source of savings.**
6. **Governance overhead remains visible but much smaller than total avoided burn.**
7. **Standardized output keys and CSV structure remain unchanged.**

## 5. Batch 04 objective

Batch 04 should aim for a **second small directional improvement**, not a dramatic jump.

The objective is to:
- preserve the Batch 03 gains
- strengthen the causal bridge between repair/context inflation and burn
- improve the governed-vs-ungoverned spread slightly further
- avoid over-tightening the governed condition into something unrealistically frictionless

## 6. Recommended tuning focus

Based on the Batch 03 deltas, the highest-value next targets remain:

- `repair_prob`
- `excess_context_prob`
- `repeat_state_prob`
- `compression_strength`
- `repair_reduction_strength`
- `context_filter_strength`
- `repeat_block_strength`
- `governance_overhead_mean`

These are the parameters that most clearly moved the model in Batch 03.

## 7. Proposed Batch 04 directions

Batch 04 should make only **incremental** moves beyond Batch 03.

### A. Scenario-side adjustments

#### short_horizon_determinate
Keep changes very small. This scenario should remain the least governance-sensitive.

Suggested direction:
- `repair_prob`: small further decrease
- `excess_context_prob`: small further decrease

#### long_horizon_workflow
This scenario showed the clearest gain in absolute savings in Batch 03 and is a good place for another careful nudge.

Suggested direction:
- `repair_prob`: small further decrease
- `excess_context_prob`: small further decrease
- optionally very slight decrease in `repeat_state_prob`

#### nonlinear_human_centered
This scenario already carries the highest governance effect and strongest distortion profile.

Suggested direction:
- `repair_prob`: small further decrease
- `excess_context_prob`: small further decrease
- `repeat_state_prob`: small further decrease

### B. Governed-side adjustments

Suggested direction:
- `compression_strength`: small further increase
- `repair_reduction_strength`: small further increase
- `context_filter_strength`: small further increase
- `repeat_block_strength`: small further increase
- `governance_overhead_mean`: either hold constant or increase only minimally

## 8. Parameters Batch 04 should not aggressively change

To protect interpretability, Batch 04 should avoid large changes to:

- `base_turns`
- `new_input_mean`
- `base_output_mean`
- `session_base_state`
- `relevant_carry_forward`
- scenario definitions
- trial count
- output schema
- batch naming conventions

Those should remain stable unless there is a strong reason to revise the scenario architecture itself.

## 9. Suggested incremental override philosophy

Batch 04 should be treated as a **fine-tuning pass**.

That means:
- no sweeping scenario redesign
- no abrupt compression jump
- no major governance-overhead spike
- no aggressive output-bound changes unless needed later

A practical rule:
- prefer small directional deltas over large corrective moves

## 10. What would count as improvement in Batch 04

Batch 04 should be considered successful if it produces:

1. lower governed token burn than Batch 03 in at least the long-horizon and nonlinear scenarios
2. equal or slightly improved reduction percentages
3. stable scenario ordering
4. further decline in repair loops without collapsing turns unnaturally
5. context/state attribution share staying dominant or increasing slightly
6. no evidence that gains are coming primarily from output trimming

## 11. What would count as a warning sign

Batch 04 should be treated as analytically suspect if it causes any of the following:

- governed burn no longer lower than ungoverned burn
- short-horizon determinate becoming more governance-sensitive than long-horizon workflow
- output share of savings becoming the dominant driver
- dramatic turn-count compression with little other explanation
- governance overhead rising enough to erode the credibility of the constraint model

## 12. Recommended implementation artifact

Recommended override file:

```text
config/calibration_batch_04.yaml
```

That file should define only the changed values relative to:
```text
config/base_parameters.yaml
```

or, depending on workflow preference, relative to the Batch 03 override state.

## 13. Recommended next sequence

1. create `config/calibration_batch_04.yaml`
2. run `calibration_batch_04_seed42`
3. compare Batch 04 against:
   - standardized baseline reference
   - standardized post-release rerun
   - standardized Batch 03
4. record the result in:
   - `docs/results/calibration-batch-04-results.md`
   - `docs/results/calibration-batch-04-comparison.md`

## 14. Working conclusion

Batch 03 demonstrated that explicit override-driven calibration works and moves the model in the intended direction.

Batch 04 should therefore act as a **measured refinement batch**. Its purpose is not to reinvent the model, but to strengthen the same mechanisms that already showed useful movement:

- fewer repair loops
- less excess context accumulation
- stronger governed state discipline
- preserved interpretability of the Token Governance thesis

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-04-parameter-plan.md
```
