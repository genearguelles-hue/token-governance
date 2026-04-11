# Calibration Plan

**Repository:** Token Governance  
**Document type:** Post-release calibration note  
**Status:** Draft v0.1  
**Phase:** Post-release model refinement after `v0.1.0`

## 1. Purpose

This document defines the first calibration phase for the Token Governance simulation program following the publication of **v0.1.0**.

The initial release established three things:

- a theoretical basis for Token Governance
- a runnable Monte Carlo simulation framework
- a first archived results note demonstrating governed vs. ungoverned token-burn differences across multiple scenarios

That release was intended to serve as a **baseline research artifact**, not as a final calibrated forecasting system. The purpose of the present phase is to tighten the stochastic simulation so that its behavior is more rigorously aligned with the deterministic benchmark logic established in the Token Governance white paper and with the internal structural claims of Persona Engineering.

In short, the calibration phase begins the transition from:

- **foundational demonstration**
to
- **controlled model refinement**

## 2. Why calibration is needed

The initial simulation results were directionally successful: governed interaction reduced token burn across all tested scenarios, and the magnitude of benefit increased with interaction horizon and human-centered complexity.

However, the first Monte Carlo batch remains provisional in several important respects:

- stochastic assumptions are not yet empirically calibrated
- parameter values were selected to demonstrate structural behavior rather than final predictive accuracy
- attribution of savings across context, output, tool use, and turn reduction requires tighter control
- scenario dynamics should be better aligned with the deterministic benchmark in the white paper

This means the current model is useful as a **demonstration of plausibility**, but still requires calibration before it can support stronger quantitative claims.

## 3. Baseline artifacts carried into calibration

The calibration phase begins from the following published and archived baseline artifacts:

### Published baseline
- GitHub release: `v0.1.0`
- white paper in `docs/white-paper/`
- initial results note in `docs/results/initial-simulation-results.md`

### Baseline simulation artifacts
- `simulation/outputs/`
- archived first-batch outputs associated with the initial release

### Preserved post-release rerun
A new preserved post-release rerun has now been generated at:

```text
simulation/outputs/post_release_rerun_seed42/
```

This rerun is important because it establishes a **post-release stable rerun archive** that is separate from the original baseline release outputs.

## 4. Anchor rerun for calibration phase

The calibration phase is anchored to the following preserved command:

```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs/post_release_rerun_seed42
```

### Archived rerun output folder
```text
simulation/outputs/post_release_rerun_seed42/
```

### Archived artifacts observed in this rerun
- `simulation_compare.csv`
- `simulation_summary.csv`
- `simulation_attribution.csv`
- `simulation_trial_level.csv`
- `paper_benchmark_anchor.csv`
- chart images
- output `README.md`

This preserved rerun serves as the **starting calibration anchor** for Phase 2 work.

## 5. Calibration objectives

The first calibration phase has five main objectives.

### Objective 1: Align stochastic behavior with deterministic benchmark logic
The white paper provides a deterministic benchmark in which a representative ungoverned system consumes approximately **39.9 million tokens/month** and a governed system consumes approximately **15.9 million tokens/month**, implying a reduction of roughly **24 million tokens** or about **60%** under the benchmark assumptions.

The stochastic model should be tuned so that high-complexity scenarios are directionally and structurally consistent with this benchmark while still preserving scenario-specific variation.

### Objective 2: Improve parameter realism
The simulation should reduce reliance on illustrative parameter choices and move toward more disciplined parameter settings for:

- ambiguity
- persona inconsistency
- drift
- repair-loop frequency
- context inflation
- governance overhead
- compression strength
- tool invocation behavior

### Objective 3: Improve attribution discipline
The model should preserve the theoretical expectation that **context/state governance is the dominant source of savings**, rather than allowing savings to be driven primarily by output trimming alone.

### Objective 4: Improve repeatability and interpretability
Repeated runs with fixed seeds and stable parameters should produce behavior that is:

- understandable
- consistent
- scenario-sensitive
- easier to explain in research notes and releases

### Objective 5: Prepare for sensitivity analysis
Calibration is a prerequisite for meaningful sensitivity sweeps. A poorly calibrated base model makes subsequent sensitivity analysis less interpretable.

## 6. Parameters to tune

The first calibration batch should focus on the parameters most directly related to the causal structure of governed vs. ungoverned interaction.

### A. Ungoverned-side parameters
- probability of ambiguity
- probability of persona inconsistency
- probability of drift
- probability of repair loop
- context growth caused by repair loops
- stable-state repetition rate
- output verbosity multiplier
- unnecessary tool invocation rate

### B. Governed-side parameters
- governance overhead per turn
- ambiguity reduction factor
- inconsistency reduction factor
- drift reduction factor
- repair-loop reduction factor
- context-minimality enforcement strength
- output sufficiency / concise-by-default strength
- compression ratio of structured state relative to raw transcript carry-forward
- tool threshold strictness

### C. Scenario-shaping parameters
- average interaction horizon
- baseline context load
- baseline output load
- baseline tool-use load
- task-complexity multiplier
- re-brief frequency
- continuity benefit strength

## 7. Calibration targets

Calibration should be judged against explicit targets.

### Target 1: Benchmark proximity
The high-complexity governed vs. ungoverned relationship should remain broadly compatible with the deterministic benchmark direction and scale.

### Target 2: Stable directional ordering
Across scenarios, the model should continue to show:

- smaller governance effect in short-horizon determinate tasks
- larger governance effect in long-horizon workflow settings
- largest governance effect in nonlinear human-centered settings

### Target 3: Attribution plausibility
Savings attribution should continue to reflect the Token Governance thesis:

- context/state discipline as the dominant savings source
- output compression as secondary
- tool discipline as supportive rather than primary
- turn reduction as a meaningful but not sole driver

### Target 4: Repeatable seeded runs
Runs performed with the same seed and same parameter set should reproduce the same outputs.

### Target 5: Explainable causal structure
The tuned model should remain explainable in terms of the simple governed vs. ungoverned causal model:

**Ungoverned**
- higher ambiguity
- higher inconsistency
- higher drift
- more repair loops
- larger context inflation
- higher future token burn

**Governed**
- small governance overhead
- lower ambiguity
- lower inconsistency
- lower drift
- fewer repair loops
- less context inflation over time

## 8. Immediate calibration workflow

The next technical sequence should be:

1. preserve the post-release rerun archive
2. define the provisional parameter table currently in use
3. compare rerun behavior to benchmark expectations
4. adjust highest-leverage parameters first
5. rerun into a new archived output folder
6. compare outputs against:
   - baseline release outputs
   - post-release rerun anchor
   - deterministic benchmark
7. document the first calibration batch in a follow-on results note

## 9. Archival policy going forward

Calibration and post-release work should **not overwrite** baseline release outputs.

Every new run should be placed in a uniquely named output folder under:

```text
simulation/outputs/
```

### Recommended naming convention
Use run folders that encode purpose, batch, and seed.

Examples:
- `simulation/outputs/post_release_rerun_seed42/`
- `simulation/outputs/calibration_batch_01_seed42/`
- `simulation/outputs/calibration_batch_02_seed42/`
- `simulation/outputs/sensitivity_context_sweep_01/`

This preserves traceability and prevents loss of earlier result states.

## 10. Success criteria for Phase 2A

The first calibration phase should be considered successful if it produces:

- a preserved rerun anchor
- a documented parameter-tuning rationale
- at least one calibration batch archived separately from the baseline release
- clearer alignment between stochastic behavior and benchmark logic
- a cleaner basis for sensitivity analysis in the next phase

## 11. Next deliverables

The immediate deliverables following this plan should be:

1. **This calibration note**
   - `docs/results/calibration-plan.md`

2. **First calibration batch archive**
   - `simulation/outputs/calibration_batch_01_seed42/`

3. **Calibration summary note**
   - recommended future path:
     `docs/results/calibration-batch-01-results.md`

4. **Sensitivity analysis plan**
   - recommended future path:
     `docs/results/sensitivity-analysis-plan.md`

## 12. Working conclusion

The publication of `v0.1.0` established the baseline research artifact for Token Governance. The preserved post-release rerun in `simulation/outputs/post_release_rerun_seed42/` now provides a stable operational anchor for the next stage of work.

The calibration phase is therefore not a correction to the initial release. It is the intended next step in the research program: tightening the stochastic model, improving attribution discipline, and preparing the simulation framework for more rigorous expansion.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-plan.md
```
