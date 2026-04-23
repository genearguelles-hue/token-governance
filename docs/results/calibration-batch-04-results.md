# Calibration Batch 04 Results

**Repository:** Token Governance  
**Document type:** Calibration batch results note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-batch-03-results.md`
- `docs/results/calibration-batch-03-comparison.md`
- `docs/results/calibration-batch-03-significance-report.md`
- `docs/results/calibration-batch-04-parameter-plan.md`
- `config/base_parameters.yaml`
- `config/calibration_batch_04.yaml`

## 1. Purpose

This document records the outcome of **Calibration Batch 04**, the second config-driven refinement batch in the Token Governance simulation program.

Batch 04 was designed as a **fine-tuning pass**, not a structural reset. Its purpose was to preserve the gains already demonstrated in Batch 03 while testing whether a second small set of parameter adjustments could:

- reduce governed token burn further
- improve reduction percentages further
- reduce repair loops further
- strengthen the context/state-governance explanation of savings
- do so without relying on turn-count compression

## 2. Batch identity

### Batch label
```text
calibration_batch_04_seed42
```

### Run mode
**Config-driven refinement batch**

### Run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --config config/base_parameters.yaml --override config/calibration_batch_04.yaml
```

### Archived output folder
```text
simulation/outputs/calibration_batch_04_seed42/
```

## 3. Position in the research sequence

Calibration Batch 04 follows this sequence:

1. **Baseline release**
   - `v0.1.0`

2. **Preserved post-release rerun**
   - `simulation/outputs/post_release_rerun_seed42/`

3. **Calibration Batch 01**
   - workflow-establishing calibration artifact

4. **Calibration Batch 02**
   - methodological clarification that explicit parameter control was missing

5. **Calibration Batch 03**
   - first config-driven run
   - first explicit parameter-controlled comparison
   - first statistically supported improvement report

6. **Calibration Batch 04**
   - second config-driven refinement run
   - incremental follow-on to Batch 03

This places Batch 04 as the first deliberate refinement pass built on both:
- a standardized config-driven execution path
- a statistically supported prior batch

## 4. Archived artifacts produced

The following artifacts were generated and archived for Batch 04:

### Core tables
- `simulation_compare.csv`
- `simulation_summary.csv`
- `simulation_attribution.csv`
- `simulation_trial_level.csv`
- `paper_benchmark_anchor.csv`

### Charts
- `chart_tokens_per_task.png`
- `chart_reduction_pct.png`
- `chart_attribution.png`
- `chart_turn_growth_short_horizon_determinate.png`
- `chart_turn_growth_long_horizon_workflow.png`
- `chart_turn_growth_nonlinear_human_centered.png`

### Supporting file
- `README.md`

## 5. Batch 04 override intent

Batch 04 was designed as a measured continuation of the Batch 03 direction.

The override focused on:
- `repair_prob`
- `excess_context_prob`
- `repeat_state_prob`
- `compression_strength`
- `repair_reduction_strength`
- `context_filter_strength`
- `repeat_block_strength`
- `governance_overhead_mean`

The intent was to:
- reduce repair-loop pressure slightly further
- reduce excess-context carry-forward slightly further
- strengthen governed state discipline slightly further
- keep governance overhead visible without allowing it to erode savings credibility

## 6. Headline Batch 03 → Batch 04 comparison

Batch 04 produced additional improvement relative to Batch 03.

### A. Governed burn decreased again in all scenarios
- short-horizon determinate: `3692.23 -> 3647.27` (**-44.95 tokens/task**)
- long-horizon workflow: `15175.79 -> 14905.89` (**-269.90 tokens/task**)
- nonlinear human-centered: `20770.85 -> 20346.27` (**-424.58 tokens/task**)

### B. Ungoverned burn also decreased in all scenarios
- short-horizon determinate: **-20.46**
- long-horizon workflow: **-165.43**
- nonlinear human-centered: **-281.63**

### C. Absolute savings increased in all scenarios
- short-horizon determinate: `2365.87 -> 2390.37` (**+24.49 tokens/task**)
- long-horizon workflow: `13484.68 -> 13589.15` (**+104.47 tokens/task**)
- nonlinear human-centered: `19290.29 -> 19433.24` (**+142.95 tokens/task**)

### D. Reduction percentage improved again in all scenarios
- short-horizon determinate: `39.053% -> 39.591%` (**+0.538 pct-pts**)
- long-horizon workflow: `47.050% -> 47.690%` (**+0.640 pct-pts**)
- nonlinear human-centered: `48.152% -> 48.852%` (**+0.700 pct-pts**)

## 7. Repair-loop interpretation

Repair loops declined again for both governed and ungoverned conditions across all scenarios.

### Governed repair-loop deltas
- short-horizon determinate: **-0.03225**
- long-horizon workflow: **-0.10375**
- nonlinear human-centered: **-0.14775**

### Ungoverned repair-loop deltas
- short-horizon determinate: **-0.03275**
- long-horizon workflow: **-0.09525**
- nonlinear human-centered: **-0.18650**

This is one of the clearest Batch 04 signals. The refinement continued to move the model in the same direction as Batch 03:
- fewer repair loops
- less distortion pressure
- less token burn driven by corrective interaction structure

## 8. Turn-count interpretation

Turn counts changed only minimally across all scenarios and both conditions.

This is important because it suggests Batch 04, like Batch 03, is **not** mainly working by shortening the interaction.

Instead, the gains appear to come from:
- lower repair frequency
- lower excess-context accumulation
- stronger context/state discipline
- lower burn at roughly similar interaction length

This remains strongly aligned with the Token Governance thesis.

## 9. Attribution interpretation

Batch 04 shifted the savings attribution structure further toward **context/state governance** in all three scenarios.

### Context/state share of savings increased by:
- short-horizon determinate: **+0.636 pct-pts**
- long-horizon workflow: **+0.189 pct-pts**
- nonlinear human-centered: **+0.172 pct-pts**

At the same time:
- output share fell
- tool share fell slightly
- turn share fell slightly

This means Batch 04 strengthened the same explanatory structure already visible in Batch 03:
savings are increasingly attributable to **context/state discipline**, not merely output trimming or shorter exchanges.

## 10. What Batch 04 establishes

Batch 04 establishes the following:

### 1. The config-driven refinement path is working
Batch 03 was not a one-off. A second incremental override batch also moved the model in the intended direction.

### 2. The highest-leverage parameters remain credible refinement targets
The Batch 04 changes further support the importance of:
- repair dynamics
- context inflation control
- repeat-state carry-forward control
- governed compression/filtering strength

### 3. The model can be improved without sacrificing interpretability
Batch 04 improved savings without relying on abrupt turn-count compression or a shift toward a weaker explanation of savings.

### 4. The refinement process remains coherent
Batch 04 looks like a **true refinement batch**, not a noisy or unstable deviation from Batch 03.

## 11. What still needs to be assessed

This results note records the main Batch 04 outcome, but it does not yet provide a trial-level significance test of Batch 03 vs Batch 04.

The next analysis pass should determine:

1. whether the Batch 04 improvements are statistically significant relative to Batch 03
2. which Batch 04 override dimensions contributed most to the observed gains
3. whether any effect-size tradeoff appears between governed and ungoverned movement
4. whether Batch 05 is justified, and if so, how small the next refinement step should be

## 12. Working conclusion

Calibration Batch 04 should be considered a successful refinement batch.

Compared with Batch 03, it produced:
- lower governed burn in all scenarios
- higher total savings in all scenarios
- higher reduction percentages in all scenarios
- fewer repair loops in all scenarios
- a further shift toward context/state-discipline attribution
- essentially stable turn counts

That means Batch 04 strengthened the same mechanisms already identified in Batch 03 and did so in a way that remains theoretically interpretable.

Batch 04 therefore supports the conclusion that the Token Governance model is not just moving in a favorable direction once, but is capable of **continued, coherent refinement under explicit parameter control**.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-04-results.md
```
