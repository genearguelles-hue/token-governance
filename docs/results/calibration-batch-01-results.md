# Calibration Batch 01 Results

**Repository:** Token Governance  
**Document type:** Calibration batch results note  
**Status:** Draft v0.1  
**Related notes:**  
- `docs/results/calibration-plan.md`  
- `docs/results/calibration-batch-01-parameter-plan.md`

## 1. Purpose

This document records the outcome of **Calibration Batch 01**, the first archived calibration run executed after the publication of **v0.1.0**.

The goal of Batch 01 was not to fully calibrate the Token Governance simulation. It was to complete the first controlled post-release calibration cycle by:

- preserving a separately archived calibration run
- validating that the governed vs. ungoverned structure remains intact under the calibration workflow
- creating a documented basis for Batch 02 and later sensitivity analysis

In this sense, Batch 01 functions as the first formal bridge between the **baseline release artifact** and the **ongoing model-refinement program**.

## 2. Batch identity

### Batch label
```text
calibration_batch_01_seed42
```

### Run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs/calibration_batch_01_seed42
```

### Archived output folder
```text
simulation/outputs/calibration_batch_01_seed42/
```

## 3. Position in the research sequence

Calibration Batch 01 follows this progression:

1. **Baseline release**
   - GitHub release `v0.1.0`

2. **Initial results artifact**
   - `docs/results/initial-simulation-results.md`

3. **Post-release preserved rerun**
   - `simulation/outputs/post_release_rerun_seed42/`

4. **Calibration planning**
   - `docs/results/calibration-plan.md`
   - `docs/results/calibration-batch-01-parameter-plan.md`

5. **Calibration Batch 01**
   - `simulation/outputs/calibration_batch_01_seed42/`

This places Batch 01 as the first fully documented archived run in the post-release calibration phase.

## 4. Archived artifacts produced

The following artifacts were generated and archived for Batch 01:

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

## 5. What Batch 01 was intended to test

The parameter plan for Batch 01 emphasized the highest-leverage trajectory variables:

- ambiguity
- persona inconsistency
- drift
- repair-loop behavior
- context inflation
- governance overhead
- compression strength
- output inflation
- unnecessary tool use

The purpose was to preserve the core governed vs. ungoverned causal structure while establishing a clean archived calibration batch that can be compared against both the baseline release outputs and the post-release rerun anchor.

## 6. Batch 01 outcome summary

At the most basic level, Batch 01 was successful operationally.

### Operational success criteria achieved
- a dedicated archived output folder was created
- the batch completed successfully
- the expected output tables and charts were generated
- the batch is now committed and preserved in the repository
- the calibration workflow has moved from planning into documented execution

This matters because Batch 01 is not only a simulation run. It is the first complete demonstration that the post-release calibration process is now functioning as an organized research pipeline.

## 7. Structural interpretation

Even before a deeper comparative analysis is performed, Batch 01 supports several structural conclusions.

### A. Calibration workflow is now real, not merely planned
With Batch 01 archived, the project now contains:

- a baseline release
- a preserved rerun anchor
- a calibration plan
- a parameter-tuning plan
- a completed calibration batch

This means future calibration work can be compared against explicit prior artifacts rather than informal memory or overwritten outputs.

### B. Archival discipline is now established
Batch 01 confirms the archival policy introduced in the calibration plan:

- new runs should not overwrite the release baseline
- each run should have a distinct named output folder
- each calibration step should be documented as a separate research artifact

This is a significant improvement in methodological discipline.

### C. The project has entered Phase 2
The repository is no longer only a conceptual and demonstrative release. It has now entered **Phase 2: structured model refinement**.

## 8. What still needs to be assessed

This results note records the existence and role of Batch 01, but it does not yet claim that Batch 01 has fully improved benchmark alignment. That determination requires a tighter comparison against:

- the baseline release outputs
- the post-release rerun
- the deterministic benchmark anchor
- the intended attribution structure

The following questions remain for the next analysis pass:

1. Did Batch 01 preserve governed < ungoverned in all scenarios?
2. Did scenario ordering remain intact?
3. Did context/state governance remain the dominant source of savings?
4. Did Batch 01 move the higher-complexity scenarios closer to the white paper benchmark?
5. Which parameters appear most sensitive and should therefore be targeted in Batch 02?

These questions define the transition from **Batch 01 archival** to **Batch 01 comparative evaluation**.

## 9. Batch 01 limitations

Batch 01 should still be interpreted modestly.

### Key limitations
- It is the first archived calibration batch, not the final tuned model.
- The batch does not by itself prove improved benchmark fit.
- The note currently records process completion more strongly than full quantitative reinterpretation.
- A tighter comparative readout is still needed before strong claims are made about what changed.

These are acceptable limitations for this stage. Batch 01’s main contribution is that it creates the first stable calibration artifact from which disciplined comparison can proceed.

## 10. Recommended next step

The next step after this note should be one of two paths:

### Path A: Immediate comparative analysis
Perform a structured comparison between:

- `simulation/outputs/`
- `simulation/outputs/post_release_rerun_seed42/`
- `simulation/outputs/calibration_batch_01_seed42/`

and record the outcome in a more analytical follow-up note.

### Path B: Define Batch 02 tuning targets
Use Batch 01 as the organizational anchor, then refine the highest-leverage parameters for:

```text
simulation/outputs/calibration_batch_02_seed42/
```

The preferred route is likely:

1. compare Batch 01 against the rerun anchor and baseline
2. identify the clearest mismatch or instability
3. define Batch 02 tuning changes
4. run Batch 02 into a separately archived folder

## 11. Working conclusion

Calibration Batch 01 should be considered a successful **first calibration-cycle artifact**.

Its main achievement is not that it solves calibration. Its main achievement is that it establishes the post-release research workflow in concrete form:

- plan
- parameter plan
- archived run
- results note
- next-step transition

That is a real milestone for the Token Governance project. It means the simulation effort is no longer just demonstrating a thesis. It is now entering an auditable, iterative refinement process.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-01-results.md
```
