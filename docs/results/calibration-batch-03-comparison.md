# Calibration Batch 03 Comparison

**Repository:** Token Governance  
**Document type:** Comparative analysis note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-batch-02-results.md`  
- `docs/results/calibration-batch-03-results.md`  
- `docs/methodology/analytical-method-definition.md`  
- `docs/methodology/parameter-inventory.md`  
- `docs/methodology/parameter-schema.md`  
- `config/base_parameters.yaml`  
- `config/calibration_batch_03.yaml`

## 1. Purpose

This document provides the first comparison note for **Calibration Batch 03**, the first config-driven calibration run in the Token Governance project.

Its purpose is to compare Batch 03 against the earlier stages of the project and to explain why Batch 03 matters analytically.

The comparison is not only about whether token totals moved. It is also about whether the project has crossed a meaningful methodological threshold.

Batch 03 is the first run in which the model state is explicitly defined through:

- a base parameter file
- a batch-specific override file
- a YAML-configurable simulation engine

That makes this comparison qualitatively different from earlier batch comparisons.

## 2. Comparison set

This comparison should be understood against the following sequence:

### A. Baseline release context
- `v0.1.0`
- `docs/results/initial-simulation-results.md`

### B. Preserved post-release rerun
- `simulation/outputs/post_release_rerun_seed42/`

### C. Calibration Batch 01
- `simulation/outputs/calibration_batch_01_seed42/`
- associated notes and comparison

### D. Calibration Batch 02
- `simulation/outputs/calibration_batch_02_seed42/`
- associated notes

### E. Calibration Batch 03
- `simulation/outputs/calibration_batch_03_seed42/`
- `config/base_parameters.yaml`
- `config/calibration_batch_03.yaml`

## 3. Why this comparison matters

Earlier batches helped establish:

- release discipline
- archival discipline
- rerun preservation
- calibration-note structure
- the need for an explicit parameter layer

Batch 03 matters because it is the first run to operate with that parameter layer made visible and external to the engine.

That means Batch 03 should be compared not only as another output folder, but as the point where the project moves from:

- repeated archived runs of an implicitly parameterized script

to:

- repeatable comparisons among explicit model states

## 4. Baseline expectations carried into Batch 03

The project’s structural expectations remain unchanged.

Batch 03 should preserve:

1. **Governed token burn remains lower than ungoverned token burn in all scenarios.**
2. **Short-horizon determinate remains the smallest governance-effect scenario.**
3. **Long-horizon workflow remains intermediate.**
4. **Nonlinear human-centered remains the largest governance-effect scenario.**
5. **Context/state governance remains the dominant source of savings.**
6. **Governance overhead remains small relative to total avoided burn.**

These expectations are the framework through which Batch 03 should be interpreted.

## 5. What is different in Batch 03

The most important difference is not yet numerical. It is structural.

### A. Explicit base model state
The current default model state is now captured in:

```text
config/base_parameters.yaml
```

### B. Explicit batch override state
The Batch 03 override state is now captured in:

```text
config/calibration_batch_03.yaml
```

### C. Config-driven execution path
The simulation engine now supports loading YAML config inputs.

This means Batch 03 has a traceable, inspectable, and versioned model state that can be reviewed independently of Python source edits.

## 6. Immediate comparison judgment

The most defensible current comparison judgment is:

> **Batch 03 is the first calibration batch whose differences are, in principle, attributable to an explicit external parameter state rather than to undocumented embedded script assumptions.**

That is already a major analytical improvement over prior stages.

## 7. How Batch 03 compares to prior stages

### A. Compared to the baseline release
The baseline release established the original proof-of-concept simulation and first archived results.

Batch 03 does not replace the baseline. Instead, it improves the project’s ability to reason about how future runs differ from the baseline.

The baseline answered:
- Can this thesis be modeled at all?

Batch 03 begins to answer:
- Can distinct parameter states now be defined and compared in a controlled way?

### B. Compared to the preserved post-release rerun
The preserved rerun created a stable anchor separate from the baseline release outputs.

Batch 03 builds on that by introducing the first run whose state is explicitly described outside the engine.

So:
- the rerun gave us a stable reproduced reference
- Batch 03 gives us the first explicit divergence from a base parameter state

### C. Compared to Batch 01
Batch 01 primarily established the calibration workflow and archival discipline.

Its main value was:
- proving the workflow
- preserving the first calibration-cycle artifacts

Batch 03 is more analytically important because it introduces real parameter-state visibility.

### D. Compared to Batch 02
Batch 02 clarified that repeated runs were not enough and that the real missing piece was the externalized parameter layer.

Batch 03 is the first concrete response to that realization.

So the relationship is:

- **Batch 02** identified the missing methodological component
- **Batch 03** operationalized it

That makes Batch 03 a more substantive methodological advance than Batch 02.

## 8. What Batch 03 appears to establish

Even without a full tabular delta analysis embedded in this note yet, Batch 03 appears to establish several strong points.

### 1. The engine / parameter-state split now exists in practice
This is no longer just a conceptual recommendation. It is now implemented in the workflow.

### 2. Future calibration batches can now be meaningful in a stronger sense
From Batch 03 onward, a batch can mean:

- same engine
- different explicit parameter state
- explicit record of what changed

That is a much stronger research posture than merely incrementing batch numbers.

### 3. The project is now more inspectable for outside researchers
A researcher can now inspect:
- the engine
- the parameter inventory
- the schema
- the base config
- the batch override
- the outputs

That makes the project more extensible and more credible as a reusable method.

### 4. The model is now closer to true analytical stability
Analytical stability does not only mean stable results. It also means stable control over the state that produced those results.

Batch 03 is the first run that significantly improves that control.

## 9. What still needs direct quantitative comparison

This note does not yet claim exactly how much Batch 03 changed the outputs numerically relative to earlier batches.

The next deeper comparison pass should directly examine:

- `simulation_compare.csv`
- `simulation_summary.csv`
- `simulation_attribution.csv`
- `paper_benchmark_anchor.csv`

across:
- post-release rerun
- Batch 01
- Batch 02
- Batch 03

Questions that still need explicit numerical treatment include:

1. Did Batch 03 preserve governed < ungoverned in all scenarios?
2. Did scenario ordering remain stable?
3. Did the override state move totals in a visibly different way from Batch 02?
4. Did savings attribution remain dominated by context/state governance?
5. Which override changes appear to have mattered most?

Those questions are now finally worth asking in a precise way, because the batch state is explicit.

## 10. Comparison outcome summary

### Strong conclusions
- Batch 03 is the first config-driven archived calibration run.
- The external parameter layer is now operational.
- The project can now distinguish engine state from parameter state.
- The research method is significantly more inspectable and reproducible than in Batches 01 and 02.

### Moderate conclusions
- Batch 03 is the first batch that can reasonably be called a true parameter-controlled calibration run.
- Batch 03 creates the right basis for real future calibration rather than nominal reruns.

### Still-open conclusions
- The precise numerical effect of the Batch 03 overrides still needs tighter comparison.
- The most sensitive override dimensions still need more direct attribution.
- Batch 04 should be designed only after the Batch 03 numerical comparison is read carefully.

## 11. Recommendation for Batch 04

Batch 04 should not be drafted until the Batch 03 comparison is used to answer one question clearly:

> Which of the Batch 03 override dimensions appear to have produced the most analytically useful movement?

Likely candidates remain:
- repair dynamics
- context inflation
- compression strength
- governance overhead
- state carry-forward control

But Batch 04 should be based on the now-explicit config-driven comparison, not just on intuition.

## 12. Working conclusion

Calibration Batch 03 is the point where the Token Governance project becomes meaningfully more than a well-documented simulation script.

It becomes a **configurable analytical framework**.

That is the main result of this comparison.

Even before the numerical deltas are fully tabulated, the comparison supports a strong methodological conclusion:

> **Batch 03 is the first batch whose analytical identity is defined by an explicit external parameter state, making future calibration genuinely controllable, inspectable, and extensible.**

That is the most important step the project has taken since the initial release.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-03-comparison.md
```
