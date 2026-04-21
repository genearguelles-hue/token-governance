# Batch 02 vs Batch 03 Significance Analysis Report

**Repository:** Token Governance  
**Document type:** Statistical analysis report  
**Status:** Draft v0.1  
**Scope:** Comparison of `calibration_batch_02_seed42` vs `calibration_batch_03_seed42` using trial-level data

## 1. Purpose

This report captures the statistical significance analysis performed on the Batch 02 and Batch 03 trial-level outputs.

The comparison evaluates **Batch 03 minus Batch 02** for the following variables, per **scenario × condition**:

- `total_tokens`
- `repair_loops`
- `turns`

The goal is to determine whether the directional improvements observed in the summary comparisons are supported by trial-level statistical evidence.

## 2. Data used

The analysis was based on the trial-level files for:

- `simulation/outputs/calibration_batch_02_seed42/simulation_trial_level.csv`
- `simulation/outputs/calibration_batch_03_seed42/simulation_trial_level.csv`

These files were treated as **independent samples** rather than paired observations.

## 3. Statistical methods

The following methods were used:

### A. Welch’s t-test
Used to compare mean differences between Batch 02 and Batch 03 under unequal variance assumptions.

### B. Bootstrap 95% confidence intervals
Used to estimate uncertainty around the mean difference for each metric.

### C. Multiple-comparison correction
Holm adjustment was applied when interpreting p-values across related tests.

### D. Directional screening
The earlier Batch 02 vs Batch 03 summary comparison was treated as a directional screen only, not as a significance test.

## 4. Bottom line

The main result is:

> **There is statistically significant evidence that Batch 03 reduced token burn and repair loops in several scenario/condition combinations, especially in the governed condition for long-horizon workflow and nonlinear human-centered cases.**

There is **not** statistically significant evidence that Batch 03 changed turn counts.

This suggests that the Batch 03 improvement is being driven primarily by:

- lower burn per interaction structure
- fewer repair loops
- stronger state/context discipline

rather than by simply compressing the number of turns.

## 5. Total tokens: significance results

## 5.1 Governed condition

### Short-horizon determinate
- delta: **-79.95 tokens/task**
- 95% CI: **[-121.95, -39.48]**
- Holm-adjusted p ≈ **0.0012**
- effect size: **small** (`d ≈ -0.086`)

### Long-horizon workflow
- delta: **-493.71 tokens/task**
- 95% CI: **[-576.88, -407.27]**
- Holm-adjusted p ≈ **1.24e-27**
- effect size: **small-to-moderate** (`d ≈ -0.250`)

### Nonlinear human-centered
- delta: **-692.40 tokens/task**
- 95% CI: **[-795.54, -590.27]**
- Holm-adjusted p ≈ **2.67e-37**
- effect size: **small-to-moderate** (`d ≈ -0.292`)

## 5.2 Ungoverned condition

### Short-horizon determinate
- delta: **-18.13**
- confidence interval crosses 0
- **not statistically significant**

### Long-horizon workflow
- delta: **-178.53**
- raw p < 0.05
- **not statistically significant after Holm correction**
- interpretation: **borderline / weak evidence only**

### Nonlinear human-centered
- delta: **-670.67**
- 95% CI: **[-854.39, -477.49]**
- Holm-adjusted p ≈ **2.57e-11**
- **statistically significant**

## 5.3 Interpretation for total tokens

The strongest statistical support for token-burn improvement is in the **governed** condition, especially:

- **long-horizon workflow**
- **nonlinear human-centered**

This supports the interpretation that Batch 03 improved the governed system in a real and measurable way.

## 6. Repair loops: significance results

## 6.1 Governed condition

### Short-horizon determinate
- delta: **-0.039**
- 95% CI: **[-0.065, -0.013]**
- Holm-adjusted p ≈ **0.0419**
- **statistically significant**

### Long-horizon workflow
- delta: **-0.234**
- 95% CI: **[-0.285, -0.184]**
- Holm-adjusted p ≈ **2.26e-18**
- **statistically significant**

### Nonlinear human-centered
- delta: **-0.307**
- 95% CI: **[-0.366, -0.252]**
- Holm-adjusted p ≈ **4.80e-24**
- **statistically significant**

## 6.2 Ungoverned condition

### Short-horizon determinate
- delta: **-0.0395**
- confidence interval touches or crosses 0 after correction
- **not statistically significant**

### Long-horizon workflow
- delta: **-0.234**
- 95% CI: **[-0.307, -0.162]**
- Holm-adjusted p ≈ **2.26e-09**
- **statistically significant**

### Nonlinear human-centered
- delta: **-0.448**
- 95% CI: **[-0.531, -0.369]**
- Holm-adjusted p ≈ **4.12e-25**
- **statistically significant**

## 6.3 Interpretation for repair loops

This is one of the clearest findings in the entire analysis:

> **Batch 03 significantly reduced repair loops in the governed system across all scenarios, and also in the ungoverned system for the two more complex scenarios.**

This strongly supports the conjecture that Batch 03 reduced distortion dynamics rather than merely shifting top-line totals cosmetically.

## 7. Turns: significance results

Across **all** scenario/condition combinations:

- bootstrap confidence intervals include 0
- adjusted p-values are not statistically significant

## 7.1 Interpretation for turns

Batch 03 did **not** significantly change turn counts.

That is important because it suggests:

> **The improvement is not coming from simply shortening the conversation.**

Instead, the evidence points toward:

- lower repair frequency
- improved state/context discipline
- lower token burn at roughly similar turn counts

This is highly consistent with the Token Governance thesis.

## 8. Strongest conclusions

The strongest statistically supported conclusions are:

1. **Batch 03 significantly reduced governed token burn in all three scenarios.**
2. **Batch 03 significantly reduced governed repair-loop frequency in all three scenarios.**
3. **The largest and most convincing significance signals are in long-horizon workflow and nonlinear human-centered settings.**
4. **Turn counts did not significantly change, so the gain is not primarily a turn-compression effect.**

## 9. Careful phrasing of the result

A careful summary statement is:

> **Batch 03 shows statistically significant reductions in governed token burn and repair-loop frequency, especially in the long-horizon workflow and nonlinear human-centered scenarios, while turn counts remain statistically unchanged. This supports the interpretation that the gains arise from improved interaction-state discipline rather than simply shorter exchanges.**

## 10. Implications for Batch 04

The Batch 04 refinement phase should remain focused on the mechanisms that now have both:

- **directional support**
- **statistical support**

These especially include:

- `repair_prob`
- `repair_reduction_strength`
- `excess_context_prob`
- `compression_strength`
- `context_filter_strength`
- `repeat_block_strength`

The significance results suggest that these are real leverage points in the model.

## 11. Caveat on effect size

The effect sizes are mostly **small to small-moderate**, even when highly significant.

That is not a problem. With approximately 4,000 trials per condition, small but consistent effects can still be meaningful.

The right language is therefore:

- **statistically significant**
- **directionally coherent**
- **modest in magnitude**
- not “massive” or “transformational”

## 12. Working conclusion

The significance analysis supports a more confident version of the Batch 03 interpretation.

Batch 03 did not simply produce a directionally favorable pattern in the summary outputs. It also produced statistically significant reductions in governed token burn and repair loops, especially in the more complex scenarios, without significantly changing turn counts.

That makes Batch 03 an important milestone in the Token Governance calibration program: it is the first config-driven batch with evidence of **statistically supported improvement in the intended mechanisms**.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-03-significance-report.md
```
