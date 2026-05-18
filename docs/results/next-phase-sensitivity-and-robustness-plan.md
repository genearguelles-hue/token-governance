# Next-Phase Sensitivity and Robustness Plan

**Repository:** Token Governance  
**Document type:** Research-phase planning note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-status-and-next-decision.md`
- `docs/results/batch-03-and-04-milestone-summary.md`
- `docs/results/calibration-batch-03-significance-report.md`
- `docs/results/calibration-batch-04-significance-report.md`
- `docs/methodology/parameter-inventory.md`
- `docs/methodology/parameter-schema.md`
- `docs/methodology/output-schema-standard.md`
- `config/base_parameters.yaml`
- `config/calibration_batch_03.yaml`
- `config/calibration_batch_04.yaml`

## 1. Purpose

This note defines the next research phase for the Token Governance simulation program.

The project has now completed two config-driven refinement batches with statistically supported improvements in the intended mechanisms. The next phase should therefore shift away from another immediate refinement batch and toward a stronger question:

> **How robust are the observed gains, and which parameters are truly doing the most work?**

This note frames that next phase in two linked parts:

- **sensitivity analysis**
- **multi-seed robustness testing**

## 2. Why this phase is next

Batch 03 and Batch 04 established that:

- config-driven calibration works
- the model is incrementally refinable
- statistically significant gains appear in key governed conditions
- repair-loop reduction and context/state discipline remain the main explanatory mechanisms
- turn counts remain largely stable

The next valuable contribution is not merely showing one more favorable batch. It is showing that the result is:

- stable across random variation
- not overly dependent on one hand-tuned parameter set
- interpretable in terms of real leverage points

## 3. Phase objectives

This phase should answer four questions:

### 1. Robustness
Do the main Batch 03 / Batch 04 gains persist across multiple random seeds?

### 2. Sensitivity
Which parameters have the strongest effect on:
- governed token burn
- reduction percentage
- repair loops
- context/state share of savings

### 3. Fragility
Which parameters destabilize the model if nudged too far?

### 4. Plateau
Are the model improvements now in a diminishing-returns regime?

## 4. Recommended phase structure

The next phase should have two workstreams.

### Workstream A: Multi-seed robustness testing
Run the current preferred parameter state across multiple seeds.

### Workstream B: One-parameter-at-a-time sensitivity analysis
Perturb selected high-leverage parameters while holding the rest fixed.

These two workstreams complement each other:
- multi-seed testing assesses stability under stochastic variation
- sensitivity testing assesses leverage and fragility under parameter variation

## 5. Recommended reference state

Use the **current best config-driven state** as the default reference point.

Recommended comparison baseline for this phase:
- `config/base_parameters.yaml`
- `config/calibration_batch_04.yaml`

This treats Batch 04 as the current leading refinement state.

## 6. Workstream A: Multi-seed robustness testing

## 6.1 Purpose

The goal is to test whether the observed Batch 04 gains are robust to random initialization and trial variation.

## 6.2 Recommended seeds

A practical starting set:

- `11`
- `42`
- `101`
- `314`
- `777`

This is enough to move beyond a single-seed narrative without immediately exploding workload.

## 6.3 Recommended output structure

Use a clear archive layout such as:

```text
simulation/outputs/robustness_batch04_seed11/
simulation/outputs/robustness_batch04_seed42/
simulation/outputs/robustness_batch04_seed101/
simulation/outputs/robustness_batch04_seed314/
simulation/outputs/robustness_batch04_seed777/
```

## 6.4 Core robustness questions

For each seed, ask:

- Does governed remain lower burn than ungoverned in all scenarios?
- Does scenario ordering remain stable?
- Do reduction percentages remain in the same general range?
- Does context/state attribution remain dominant?
- Do turn counts remain roughly stable?
- Do long-horizon workflow and nonlinear human-centered remain the strongest-effect scenarios?

## 6.5 Robustness success criteria

The model should be considered robust if:

1. governed < ungoverned remains true in all scenarios for all seeds
2. scenario ordering remains stable
3. reduction percentages do not vary wildly across seeds
4. the strongest attribution remains context/state governance
5. significance patterns do not collapse under seed variation

## 7. Workstream B: Sensitivity analysis

## 7.1 Purpose

The goal is to determine which parameters most strongly affect the model and which ones have little marginal effect.

## 7.2 Recommended initial parameter set

Start with the parameters already supported by directional and statistical evidence:

- `repair_prob`
- `repair_reduction_strength`
- `excess_context_prob`
- `compression_strength`
- `context_filter_strength`
- `repeat_block_strength`
- `repeat_state_prob`
- `governance_overhead_mean`

## 7.3 Sensitivity design

Use **one-parameter-at-a-time perturbations** first.

For each chosen parameter:
- hold all other values fixed at the Batch 04 state
- test a small negative adjustment
- test the current value
- test a small positive adjustment

This gives a local sensitivity profile without introducing combinatorial explosion.

## 7.4 Suggested perturbation logic

### Probabilities
For parameters like:
- `repair_prob`
- `excess_context_prob`
- `repeat_state_prob`

test:
- current value minus a small increment
- current value
- current value plus a small increment

### Governance strengths
For parameters like:
- `compression_strength`
- `context_filter_strength`
- `repeat_block_strength`
- `repair_reduction_strength`

test:
- slightly weaker
- current value
- slightly stronger

### Governance overhead
For:
- `governance_overhead_mean`

test:
- slightly lower
- current value
- slightly higher

## 7.5 Suggested output structure

A clean archive layout would be:

```text
simulation/outputs/sensitivity_repair_prob_low/
simulation/outputs/sensitivity_repair_prob_high/
simulation/outputs/sensitivity_compression_strength_low/
simulation/outputs/sensitivity_compression_strength_high/
...
```

Or, if you want a more structured hierarchy:

```text
simulation/outputs/sensitivity/
  repair_prob_low/
  repair_prob_high/
  compression_strength_low/
  compression_strength_high/
```

## 8. Metrics to prioritize

Both workstreams should focus on the same core outputs:

### Primary
- `avg_tokens_per_task`
- `reduction_pct`
- `repair_loops`

### Secondary
- `turns`
- `context_share_pct`
- `output_share_pct`
- `tool_share_pct`
- `turn_share_pct`

### Interpretation metrics
- effect size relative to Batch 04 reference
- sign stability
- scenario-order stability
- attribution stability

## 9. What counts as a meaningful sensitivity result

A parameter should be treated as **high leverage** if small perturbations produce noticeable movement in:

- governed burn
- reduction percentage
- repair loops
- context/state attribution

A parameter should be treated as **fragility-prone** if small perturbations produce:

- unstable scenario ordering
- collapse of governed advantage
- abrupt changes in turn counts
- attribution shifts away from context/state discipline

A parameter should be treated as **low leverage** if perturbations produce only minimal movement across core outputs.

## 10. What this phase should not do

To keep the phase interpretable, avoid:

- immediate multi-parameter sweeps
- scenario redesign during sensitivity testing
- schema changes mid-phase
- mixing robustness and sensitivity results without labeling them clearly
- introducing Batch 05 logic before robustness/sensitivity conclusions are read

## 11. Recommended documentation sequence

The next phase would be best documented through a small note set:

1. `docs/results/next-phase-sensitivity-and-robustness-plan.md`
2. `docs/results/multi-seed-robustness-results.md`
3. `docs/results/sensitivity-analysis-results.md`
4. optional:
   `docs/results/post-robustness-batch-05-decision.md`

## 12. Practical recommendation

The recommended order is:

### Step 1
Run multi-seed robustness testing on the Batch 04 state.

### Step 2
Review whether the main conclusions remain stable.

### Step 3
Run one-parameter-at-a-time sensitivity tests on the highest-leverage candidates.

### Step 4
Only then decide whether Batch 05 is justified.

This order is preferable because it strengthens the evidence base before more hand-tuned refinement.

## 13. Working conclusion

The Token Governance simulation program has now reached the point where the next best question is not “Can another batch improve the result?” but:

> **How stable and how interpretable are the improvements already achieved?**

That makes sensitivity analysis and multi-seed robustness testing the correct next phase.

This phase should determine:
- whether the current gains are robust
- which parameters matter most
- which parameters risk fragility
- whether another refinement batch would add meaningful knowledge

---

## Suggested repository placement

Recommended path:

```text
docs/results/next-phase-sensitivity-and-robustness-plan.md
```
