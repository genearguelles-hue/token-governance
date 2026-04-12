# Calibration Batch 01 Comparison

**Repository:** Token Governance  
**Document type:** Comparative analysis note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/initial-simulation-results.md`  
- `docs/results/calibration-plan.md`  
- `docs/results/calibration-batch-01-parameter-plan.md`  
- `docs/results/calibration-batch-01-results.md`

## 1. Purpose

This document provides the first comparative readout for **Calibration Batch 01**.

Its role is to compare three distinct simulation states:

1. the **baseline release outputs** associated with the initial release context
2. the **preserved post-release rerun** in `simulation/outputs/post_release_rerun_seed42/`
3. **Calibration Batch 01** in `simulation/outputs/calibration_batch_01_seed42/`

The purpose is not to claim that Batch 01 solved calibration. The purpose is to establish whether Batch 01:

- preserved the core governed vs. ungoverned pattern
- preserved scenario ordering
- maintained plausible attribution structure
- produced any meaningful change relative to the rerun anchor
- clarified what should be targeted in Batch 02

## 2. Comparison set

### A. Baseline release context
- release: `v0.1.0`
- supporting note: `docs/results/initial-simulation-results.md`

### B. Preserved post-release rerun
- archive: `simulation/outputs/post_release_rerun_seed42/`

### C. Calibration Batch 01
- archive: `simulation/outputs/calibration_batch_01_seed42/`

## 3. Why this comparison matters

The project now contains a full chain of artifacts:

- baseline release
- preserved rerun
- calibration plan
- calibration batch 01 parameter plan
- calibration batch 01 outputs
- calibration batch 01 results note

What is still needed is a direct interpretation of what Batch 01 means relative to prior states. Without this comparison, Batch 01 remains an archived run but not yet an analytically grounded step in the refinement program.

## 4. Baseline expectations carried into comparison

Before comparing outputs, the project established several expectations that should remain true across calibration unless the model is fundamentally broken.

### Structural expectations
1. **Governed token burn should remain lower than ungoverned token burn in all scenarios.**
2. **Governance effect should remain smallest in short-horizon determinate work.**
3. **Governance effect should remain larger in long-horizon workflow interaction.**
4. **Governance effect should remain largest in nonlinear human-centered interaction.**
5. **Context/state governance should remain the dominant source of savings.**
6. **Governance overhead should remain small relative to savings.**

These expectations provide the framework for interpreting Batch 01.

## 5. High-level comparison logic

The comparison should be read at three levels:

### Level 1: Stability
Did Batch 01 preserve the core qualitative structure already established by the baseline and preserved rerun?

### Level 2: Movement
Did Batch 01 materially shift totals, reductions, or attribution in any useful direction?

### Level 3: Guidance
Does Batch 01 tell us what to tune next, or does it mainly confirm pipeline stability?

## 6. Initial comparative interpretation

Based on the current state of the archived artifacts, the most defensible interpretation is as follows:

### A. Batch 01 successfully preserves the research workflow
This is the clearest conclusion.

Batch 01 demonstrates that the project now has a functioning refinement pipeline in which:

- baseline outputs are preserved
- reruns are separately archived
- calibration runs are separately archived
- notes are created for each stage
- future batches can be compared without overwriting prior states

This is a meaningful methodological advance.

### B. Batch 01 should currently be treated as a calibration-process milestone more than a strong behavioral shift milestone
At this stage, there is not yet evidence in the documentation that Batch 01 introduced dramatic or explicitly quantified parameter retuning relative to the preserved rerun. As a result, the most cautious reading is that Batch 01 currently functions as:

- the first organized calibration archive
- the first explicit calibration-cycle result
- the immediate platform for sharper Batch 02 tuning

This is still valuable. It means the refinement process is no longer implicit.

### C. The preserved rerun remains the most important operational anchor
The rerun in `post_release_rerun_seed42` serves as the clearest stable point of comparison because it separated post-release reproduction from release-baseline preservation.

Batch 01 gains its value largely by being positioned after that anchor and within the planned calibration sequence.

## 7. What Batch 01 appears to establish

Even without a full tabular delta analysis embedded in this note yet, Batch 01 appears to establish the following:

### 1. Calibration can now proceed without destroying baseline artifacts
This is operationally important. It means each calibration step can be treated as an auditable research object.

### 2. Scenario-based refinement is now possible
Because runs are archived separately, the project can now ask scenario-specific questions such as:

- Did long-horizon workflow change more than short-horizon determinate?
- Did nonlinear human-centered remain the strongest governance-benefit case?
- Did attribution shift away from context/state governance?

Those questions are now tractable within the repo structure.

### 3. Batch 01 creates the comparative basis needed for Batch 02
This is the most important forward-looking result. Batch 01 does not need to solve calibration fully to be valuable. It needs to make the next adjustment more targeted.

## 8. What still needs explicit numerical comparison

The next analysis pass should directly compare the following files across all three comparison states:

### Core tables
- `simulation_compare.csv`
- `simulation_summary.csv`
- `simulation_attribution.csv`
- `paper_benchmark_anchor.csv`

### Visuals
- token-burn comparison chart
- reduction percentage chart
- turn-growth charts
- attribution chart

### Questions to answer numerically
1. Did top-line average token burn per task change between rerun and Batch 01?
2. Did percent reduction from governance change materially?
3. Did any scenario move closer to or farther from the benchmark logic?
4. Did attribution shares remain dominated by context/state governance?
5. Did Batch 01 reduce or increase volatility in any scenario?

Until those are answered explicitly, Batch 01 should be interpreted as a successful calibration artifact, but not yet as a decisive quantitative recalibration.

## 9. Comparison outcome summary

The current comparison supports the following summary judgment:

### Strong conclusions
- The baseline release remains intact.
- The preserved rerun anchor exists and is stable.
- Calibration Batch 01 has been executed, archived, documented, and integrated into the repo.
- The project now has a valid iterative calibration workflow.

### Moderate conclusions
- Batch 01 appears to preserve the intended governed-vs-ungoverned structural logic.
- Batch 01 is a suitable platform for more focused parameter adjustment in Batch 02.

### Weak or still-open conclusions
- The degree to which Batch 01 improved benchmark alignment is not yet fully documented.
- The degree to which Batch 01 altered attribution balance is not yet fully documented.
- The highest-sensitivity parameters for Batch 02 still need sharper numerical justification.

## 10. Recommendation for Batch 02

The most sensible next step is **not** to broaden the model yet. It is to perform a tighter comparative read and then move into **Batch 02** with more specific tuning intent.

### Recommended Batch 02 focus
Target the highest-leverage parameters that directly shape the governed vs. ungoverned causal bridge:

- repair-loop probability
- context inflation per repair loop
- drift probability
- ambiguity probability
- compression ratio
- governance overhead

### Why these first
These parameters are the clearest bridge between:
- persona-level degradation
- context carry-forward
- compounding token burn

They are also the easiest to explain within the Persona Engineering and Token Governance framework, where drift, constraints, and trajectory-level state evolution are more central than isolated response trimming.

## 11. Recommended next artifacts

The next sequence should be:

1. **Batch 02 parameter plan**
   - `docs/results/calibration-batch-02-parameter-plan.md`

2. **Batch 02 archive**
   - `simulation/outputs/calibration_batch_02_seed42/`

3. **Batch 02 results note**
   - `docs/results/calibration-batch-02-results.md`

A more quantitative comparison addendum could also be added later if you want a fully tabulated delta note.

## 12. Working conclusion

Calibration Batch 01 should be understood primarily as the step that converted the Token Governance simulation effort from a released baseline plus ad hoc reruns into a **tracked calibration program**.

That is a significant transition.

The comparison at this stage does not need to overclaim. Its clearest and most defensible conclusion is:

> **Batch 01 successfully established the first archived calibration cycle and created the basis for more precise, explainable parameter tuning in Batch 02.**

That is exactly what the project needed at this point.

## 13. Theoretical grounding

This comparison remains grounded in the Persona Engineering view that sustained interaction should be reasoned about in terms of formally constrained identity, trajectories, drift, and state evolution rather than isolated outputs. That is what makes the preservation of scenario ordering, trajectory discipline, and drift-sensitive tuning a meaningful comparison target rather than a cosmetic reporting preference. fileciteturn6file0

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-01-comparison.md
```
