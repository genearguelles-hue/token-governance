# Calibration Batch 04 Comparison

**Repository:** Token Governance  
**Document type:** Comparative analysis note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-batch-03-results.md`  
- `docs/results/calibration-batch-03-comparison.md`  
- `docs/results/calibration-batch-03-significance-report.md`  
- `docs/results/calibration-batch-04-results.md`  
- `docs/results/calibration-batch-04-parameter-plan.md`  
- `config/base_parameters.yaml`  
- `config/calibration_batch_03.yaml`  
- `config/calibration_batch_04.yaml`

## 1. Purpose

This document compares **Calibration Batch 04** against **Calibration Batch 03**.

Batch 03 established the first config-driven, explicitly parameter-controlled improvement cycle in the Token Governance project. Batch 04 was designed as a refinement batch to test whether a second small set of explicit overrides could continue moving the model in the same intended direction.

The purpose of this comparison is therefore to determine whether Batch 04:

- preserved the Batch 03 gains
- improved governed-vs-ungoverned separation further
- further reduced repair-driven distortion
- further strengthened context/state governance as the dominant source of savings
- did so without relying mainly on turn-count compression

## 2. Comparison set

### A. Batch 03
- archive: `simulation/outputs/calibration_batch_03_seed42/`
- override file: `config/calibration_batch_03.yaml`

### B. Batch 04
- archive: `simulation/outputs/calibration_batch_04_seed42/`
- override file: `config/calibration_batch_04.yaml`

## 3. Why this comparison matters

Batch 03 already showed two important things:

1. the config-driven method worked
2. the first explicit override state moved the model in the intended direction

Batch 04 matters because it tests whether that movement can be extended through a second, incremental, interpretable refinement pass.

That makes Batch 04 a more demanding test than Batch 03. It is no longer enough to show that one config-driven shift is possible. The question is whether the model can improve *again* without becoming unstable, opaque, or overly dependent on superficial effects.

## 4. Baseline expectations carried into Batch 04

Batch 04 should preserve the project’s structural expectations:

1. **Governed token burn remains lower than ungoverned token burn in all scenarios.**
2. **Short-horizon determinate remains the smallest governance-effect scenario.**
3. **Long-horizon workflow remains intermediate.**
4. **Nonlinear human-centered remains the largest governance-effect scenario.**
5. **Context/state governance remains the dominant source of savings.**
6. **Governance overhead remains much smaller than total avoided burn.**
7. **Turn-count changes remain secondary to repair/context improvements.**

These are the conditions under which Batch 04 should be interpreted as a successful refinement batch.

## 5. Headline Batch 03 → Batch 04 deltas

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

## 6. Repair-loop comparison

Repair loops declined again for both governed and ungoverned conditions.

### Governed repair-loop deltas
- short-horizon determinate: **-0.03225**
- long-horizon workflow: **-0.10375**
- nonlinear human-centered: **-0.14775**

### Ungoverned repair-loop deltas
- short-horizon determinate: **-0.03275**
- long-horizon workflow: **-0.09525**
- nonlinear human-centered: **-0.18650**

## Interpretation

This is one of the strongest signals in the comparison.

Batch 04 continued reducing repair pressure across the board, particularly in the more complex scenarios. That supports the interpretation that the override changes continued to improve the model through lower distortion dynamics, not merely through cosmetic changes to the output totals.

## 7. Turn-count comparison

Turn counts changed only minimally across all scenarios and both conditions.

### Interpretation

This matters because it shows that Batch 04, like Batch 03, did **not** mainly improve performance by reducing the number of turns.

Instead, the gains appear to come from:
- fewer repair loops
- less context inflation
- stronger governed state discipline
- lower burn at roughly similar interaction length

This remains consistent with the Token Governance thesis.

## 8. Attribution comparison

Batch 04 shifted the savings attribution structure further toward **context/state governance** in all three scenarios.

### Context/state share of savings increased by:
- short-horizon determinate: **+0.636 pct-pts**
- long-horizon workflow: **+0.189 pct-pts**
- nonlinear human-centered: **+0.172 pct-pts**

At the same time:
- output share fell
- tool share fell slightly
- turn share fell slightly

## Interpretation

This is theoretically important.

Batch 04 did not shift the model toward a weaker explanation such as simple output trimming. Instead, it further strengthened the same explanation already visible in Batch 03:

> **Savings are increasingly attributable to context/state discipline rather than output, tool, or turn effects.**

That is exactly the direction the framework is supposed to reward.

## 9. Overall comparison judgment

### Strong conclusions
- Batch 04 produced lower governed burn than Batch 03 in all scenarios.
- Batch 04 increased savings in all scenarios.
- Batch 04 improved reduction percentages in all scenarios.
- Batch 04 reduced repair loops in all scenarios and both conditions.
- Batch 04 further increased the context/state share of savings.
- Turn counts remained essentially stable.

### Moderate conclusions
- Batch 04 appears to be a successful refinement batch rather than a noisy deviation.
- The same parameter families that mattered in Batch 03 continue to matter in Batch 04.
- The model continues to improve in a coherent direction under explicit parameter control.

### Still-open conclusions
- Trial-level significance testing is still needed for Batch 03 vs Batch 04.
- The relative contribution of each individual Batch 04 override still needs finer attribution.
- It remains to be determined whether a Batch 05 is necessary or whether the model is approaching a stable calibration plateau.

## 10. What Batch 04 suggests about the model

Batch 04 suggests that the model is now behaving like a genuinely calibratable system.

That means:
- improvements can be produced intentionally
- improvements can be produced incrementally
- improvements remain interpretable
- improvements do not appear to depend on abrupt structural distortions

This is an important threshold. It means the project is no longer only demonstrating that governance *can* matter. It is now showing that governance effects can be *tuned* and *refined* in a disciplined way.

## 11. Recommendation for the next step

The next step should be **trial-level significance testing for Batch 03 vs Batch 04**.

That analysis should evaluate, per scenario × condition:

- `total_tokens`
- `repair_loops`
- `turns`

using:
- Welch’s t-test
- bootstrap 95% confidence intervals
- appropriate multiple-comparison correction

That will determine whether the Batch 04 refinements are merely directionally favorable or also statistically supported.

## 12. Working conclusion

Calibration Batch 04 should be understood as a successful second refinement pass.

Compared with Batch 03, it produced:
- lower governed burn
- higher savings
- higher reduction percentages
- fewer repair loops
- stronger context/state attribution
- stable turn counts

That means the Batch 03 gains were not isolated. They were extendable.

The most defensible overall conclusion is:

> **Batch 04 continues the same coherent improvement pattern established by Batch 03, strengthening the case that the Token Governance model is capable of incremental, interpretable refinement under explicit parameter control.**

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-04-comparison.md
```
