# Calibration Batch 02 Results

**Repository:** Token Governance  
**Document type:** Calibration batch results note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-plan.md`  
- `docs/results/calibration-batch-01-parameter-plan.md`  
- `docs/results/calibration-batch-01-results.md`  
- `docs/results/calibration-batch-01-comparison.md`  
- `docs/results/calibration-batch-02-parameter-plan.md`  
- `docs/methodology/analytical-method-definition.md`

## 1. Purpose

This document records the outcome of **Calibration Batch 02**, the second archived calibration run executed after the publication of **v0.1.0**.

The purpose of Batch 02 was to continue the calibration sequence established by:

- the baseline release
- the preserved post-release rerun
- Calibration Batch 01
- the codified analytical method

Batch 02 was intended to become the first calibration batch that is interpreted not merely as a workflow milestone, but as part of the transition toward a more explicit and stable parameter discipline.

At the same time, Batch 02 has made one important methodological fact clearer: the next major step in the project is not simply “more batches,” but the identification and externalization of the model’s actual tunable parameters.

## 2. Batch identity

### Batch label
```text
calibration_batch_02_seed42
```

### Run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs/calibration_batch_02_seed42
```

### Archived output folder
```text
simulation/outputs/calibration_batch_02_seed42/
```

## 3. Position in the research sequence

Calibration Batch 02 follows this sequence:

1. **Baseline release**
   - GitHub release `v0.1.0`

2. **Initial results note**
   - `docs/results/initial-simulation-results.md`

3. **Preserved post-release rerun**
   - `simulation/outputs/post_release_rerun_seed42/`

4. **Calibration Batch 01**
   - parameter plan
   - archived outputs
   - results note
   - comparison note

5. **Analytical method codification**
   - `docs/methodology/analytical-method-definition.md`

6. **Calibration Batch 02**
   - `docs/results/calibration-batch-02-parameter-plan.md`
   - `simulation/outputs/calibration_batch_02_seed42/`
   - this results note

This places Batch 02 at the point where the project begins to transition from workflow establishment into scrutiny of the model’s actual tunable structure.

## 4. Archived artifacts produced

The following artifacts were generated and archived for Batch 02:

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

## 5. Intended role of Batch 02

Batch 02 was intended to serve as the first calibration batch that more clearly targeted the highest-leverage bridge parameters between interaction distortion and token burn, especially:

- repair-loop probability
- context inflation per repair loop
- drift probability
- ambiguity probability
- compression ratio
- governance overhead

However, the analytical interpretation of Batch 02 now depends on an important clarification.

## 6. What Batch 02 has clarified

The most important result of Batch 02 is methodological clarity.

### A. The archival and documentation process is now stable
Batch 02 confirms that the project can now support repeated archived runs with a consistent research workflow:

- parameter plan
- archived outputs
- results note
- comparison logic
- methodological framing

This is a real achievement and should not be dismissed.

### B. The need for explicit parameter externalization is now unmistakable
Batch 02 has clarified that repeated batches do not become analytically meaningful simply by being numbered as separate calibration runs.

For calibration to become substantive rather than merely procedural, the project must now identify and externalize the simulation’s actual tunable parameters.

This is the key insight produced by reaching Batch 02.

### C. The project has now moved from “Can we run and archive this method?” to “How do we explicitly control the model state?”
That is the correct transition point.

The next meaningful phase is not just another nominal batch. It is the extraction of the real parameter layer from the simulation engine so that future batches represent explicit model changes rather than repeated invocations of an implicitly fixed script state.

## 7. What Batch 02 establishes

Batch 02 establishes several things with confidence.

### 1. The analytical method is now codified enough to reveal its own next requirement
This is a sign of maturation. The method is now stable enough that its next limitation is visible.

### 2. Separate archival batches are now easy to create and compare
The project no longer depends on overwriting outputs or relying on memory. Each step is now a distinct research artifact.

### 3. Batch numbering alone is not equivalent to true calibration
This is one of the most important lessons so far.

A genuine calibration batch should represent an identifiable shift in parameterization or model logic. Batch 02 helps make that requirement explicit.

### 4. The next phase should focus on the parameter layer
That is now more important than continuing to multiply nominal calibration runs without explicit parameter control.

## 8. How Batch 02 should be interpreted

Batch 02 should **not** be overclaimed as a decisive recalibration step.

It should be interpreted more carefully as:

- the second archived calibration-cycle artifact
- the point at which the project’s methodological discipline made the missing parameter layer impossible to ignore
- the final stage before moving from batch documentation to explicit model-state control

This makes Batch 02 a very important note in the project history, even if its greatest contribution is conceptual and methodological rather than purely numerical.

## 9. What remains unresolved after Batch 02

Several questions are now clearly open:

1. Where exactly are the current tunable parameters embedded in `persona_token_governance_monte_carlo.py`?
2. Which of those parameters should be extracted first into an external config layer?
3. What config structure should future runs use?
4. How should future batches distinguish:
   - engine changes
   - parameter changes
   - scenario changes
5. What should count as the first truly parameter-adjusted batch after externalization?

These questions define the real beginning of the next phase.

## 10. Recommended next step

The next step after Batch 02 should **not** be to continue running nominal batches under an implicitly fixed parameter state.

The next step should be:

### Step 1
Identify the tunable parameters currently embedded inside:

```text
simulation/src/persona_token_governance_monte_carlo.py
```

### Step 2
Define an external parameter schema for them.

### Step 3
Refactor the simulation so that future batches are driven by explicit config files rather than undocumented script-internal assumptions.

Only after that should the project proceed to the next meaningful calibration cycle.

## 11. Recommended next artifact sequence

The next documentation sequence should be:

1. **Parameter inventory note**
   - recommended path:
     `docs/methodology/parameter-inventory.md`

2. **External configuration schema note**
   - recommended path:
     `docs/methodology/parameter-schema.md`

3. **Config-driven batch plan**
   - recommended path:
     `docs/results/calibration-batch-03-parameter-plan.md`

4. **First truly parameter-adjusted archive**
   - recommended path:
     `simulation/outputs/calibration_batch_03_seed42/`

## 12. Working conclusion

Calibration Batch 02 is an important milestone, but not because it by itself solves the model.

Its importance is that it reveals the next real boundary of the current approach:

> **the simulation framework is now stable enough that the missing explicit parameter layer has become the central methodological issue.**

That is valuable progress.

Batch 02 therefore marks the point where the Token Governance project should shift from:
- repeatedly archiving runs of an implicitly parameterized engine

to:
- explicitly identifying, controlling, and documenting the model parameters that define each analytical state.

That is the correct next evolution of the project.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-02-results.md
```
