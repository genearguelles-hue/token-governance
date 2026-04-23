# Calibration Batch 04 Significance Analysis Report

**Repository:** Token Governance  
**Document type:** Statistical analysis report  
**Status:** Draft v0.1  
**Scope:** Comparison of `calibration_batch_03_seed42` vs `calibration_batch_04_seed42` using trial-level data

## 1. Purpose

This report documents the significance analysis performed on the Batch 03 and Batch 04 trial-level outputs.

The comparison evaluates **Batch 04 minus Batch 03** for the following variables, per **scenario × condition**:

- `total_tokens`
- `repair_loops`
- `turns`

The objective is to determine whether the directional improvements observed in the summary comparisons are supported by trial-level statistical evidence.

## 2. Data used

The analysis was based on the trial-level files for:

- `simulation/outputs/calibration_batch_03_seed42/simulation_trial_level.csv`
- `simulation/outputs/calibration_batch_04_seed42/simulation_trial_level.csv`

These were treated as **independent samples**, not paired observations.

## 3. Statistical methods

The following methods were used:

### A. Welch’s t-test
Used to compare mean differences between Batch 03 and Batch 04 under unequal-variance assumptions.

### B. Bootstrap 95% confidence intervals
Used to estimate uncertainty around the mean difference for each metric.

### C. Multiple-comparison correction
Holm adjustment was applied when interpreting p-values across related tests.

### D. Directional screening
The earlier Batch 03 vs Batch 04 summary comparison was treated as a directional screen only, not as a significance test.

## 4. Bottom line

The main result is:

> **There is statistically significant evidence that Batch 04 further reduced token burn and repair loops in several scenario/condition combinations, especially in the governed long-horizon workflow and governed nonlinear human-centered cases.**

There is **not** statistically significant evidence that Batch 04 changed turn counts.

This suggests that the Batch 04 improvement is being driven primarily by:

- lower burn per interaction structure
- fewer repair loops
- stronger state/context discipline

rather than by simply compressing the number of turns.

## 5. Total tokens: significance results

## 5.1 Governed condition

### Short-horizon determinate
- delta: **-44.95 tokens/task**
- 95% CI: **[-83.89, -4.13]**
- Holm-adjusted p ≈ **0.0721**
- interpretation: **not significant after Holm correction**
- interpretation note: **borderline / weak evidence**

### Long-horizon workflow
- delta: **-269.90 tokens/task**
- 95% CI: **[-355.68, -188.18]**
- Holm-adjusted p ≈ **1.54e-09**
- effect size: **small** (`d ≈ -0.141`)
- **statistically significant**

### Nonlinear human-centered
- delta: **-424.58 tokens/task**
- 95% CI: **[-526.87, -318.27]**
- Holm-adjusted p ≈ **6.67e-16**
- effect size: **small-to-moderate** (`d ≈ -0.186`)
- **statistically significant**

## 5.2 Ungoverned condition

### Short-horizon determinate
- delta: **-20.46**
- confidence interval crosses 0
- Holm-adjusted p ≈ **0.498**
- **not statistically significant**

### Long-horizon workflow
- delta: **-165.43**
- 95% CI: **[-304.31, -20.65]**
- Holm-adjusted p ≈ **0.0721**
- **not statistically significant after Holm correction**
- interpretation note: **borderline / weak evidence**

### Nonlinear human-centered
- delta: **-281.63**
- 95% CI: **[-452.68, -103.51]**
- Holm-adjusted p ≈ **0.00967**
- **statistically significant**

## 5.3 Interpretation for total tokens

The strongest statistical support for additional token-burn improvement is again in the more complex scenarios, especially:

- **governed long-horizon workflow**
- **governed nonlinear human-centered**

There is also statistically significant additional improvement in:

- **ungoverned nonlinear human-centered**

This supports the interpretation that Batch 04 extends the strongest gains where distortion pressure is highest.

## 6. Repair loops: significance results

## 6.1 Governed condition

### Short-horizon determinate
- delta: **-0.03225**
- 95% CI: **[-0.05850, -0.00700]**
- Holm-adjusted p ≈ **0.0252**
- **statistically significant**

### Long-horizon workflow
- delta: **-0.10375**
- 95% CI: **[-0.15150, -0.05524]**
- Holm-adjusted p ≈ **0.000103**
- **statistically significant**

### Nonlinear human-centered
- delta: **-0.14775**
- 95% CI: **[-0.20201, -0.09199]**
- Holm-adjusted p ≈ **9.97e-07**
- **statistically significant**

## 6.2 Ungoverned condition

### Short-horizon determinate
- delta: **-0.03275**
- confidence interval crosses 0 slightly
- Holm-adjusted p ≈ **0.0999**
- **not statistically significant**

### Long-horizon workflow
- delta: **-0.09525**
- 95% CI: **[-0.16304, -0.02074]**
- Holm-adjusted p ≈ **0.0252**
- **statistically significant**

### Nonlinear human-centered
- delta: **-0.18650**
- 95% CI: **[-0.26801, -0.10674]**
- Holm-adjusted p ≈ **2.53e-05**
- **statistically significant**

## 6.3 Interpretation for repair loops

This is one of the clearest findings in the analysis:

> **Batch 04 significantly reduced governed repair loops in all three scenarios, and also reduced ungoverned repair loops in the two more complex scenarios.**

This strongly supports the interpretation that Batch 04 continued improving the model through lower distortion dynamics rather than merely shifting top-line totals cosmetically.

## 7. Turns: significance results

Across **all** scenario/condition combinations:

- bootstrap confidence intervals include 0
- adjusted p-values are not statistically significant

## 7.1 Interpretation for turns

Batch 04 did **not** significantly change turn counts.

That is important because it suggests:

> **The Batch 04 improvement is not coming from simply shortening the interaction.**

Instead, the evidence points toward:

- lower repair frequency
- improved state/context discipline
- lower token burn at roughly similar turn counts

This remains strongly consistent with the Token Governance thesis.

## 8. Strongest conclusions

The strongest statistically supported conclusions are:

1. **Batch 04 significantly reduced governed token burn in the long-horizon workflow and nonlinear human-centered scenarios.**
2. **Batch 04 significantly reduced governed repair-loop frequency in all three scenarios.**
3. **Batch 04 significantly reduced ungoverned repair-loop frequency in the two more complex scenarios.**
4. **Turn counts did not significantly change, so the gain is not primarily a turn-compression effect.**

## 9. Careful phrasing of the result

A careful summary statement is:

> **Batch 04 shows statistically significant additional reductions in repair-loop frequency across the governed system and statistically significant further reductions in governed token burn in the long-horizon workflow and nonlinear human-centered scenarios, while turn counts remain statistically unchanged. This supports the interpretation that Batch 04 continues improving interaction-state discipline rather than merely shortening exchanges.**

## 10. Implications for further calibration

The Batch 04 refinement phase strengthens the case for continuing to focus on the mechanisms that now have both:

- **directional support**
- **statistical support**

These especially include:

- `repair_prob`
- `repair_reduction_strength`
- `excess_context_prob`
- `compression_strength`
- `context_filter_strength`
- `repeat_block_strength`

The significance results suggest these remain the most credible leverage points in the model.

## 11. Caveat on effect size

The effect sizes are mostly **small**, even when statistically significant.

That is not a problem. With approximately 4,000 trials per condition, small but consistent improvements can still be meaningful.

The right language is therefore:

- **statistically significant**
- **directionally coherent**
- **modest in magnitude**
- not “massive” or “transformational”

## 12. Working conclusion

The significance analysis supports a stronger version of the Batch 04 interpretation.

Batch 04 did not merely produce another directionally favorable pattern in the summary outputs. It also produced statistically significant additional reductions in repair loops and statistically significant further governed token-burn reductions in the more complex scenarios, without significantly changing turn counts.

That makes Batch 04 an important milestone in the Token Governance calibration program: it is a second config-driven refinement batch with evidence of **statistically supported additional improvement in the intended mechanisms**.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-04-significance-report.md