# Calibration Batch 03 Results

**Repository:** Token Governance  
**Document type:** Calibration batch results note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-batch-02-results.md`  
- `docs/methodology/analytical-method-definition.md`  
- `docs/methodology/parameter-inventory.md`  
- `docs/methodology/parameter-schema.md`  
- `config/base_parameters.yaml`  
- `config/calibration_batch_03.yaml`

## 1. Purpose

This document records the outcome of **Calibration Batch 03**, the first archived calibration run executed through the new YAML configuration layer.

Batch 03 is important because it is the first run in the project that is explicitly driven by:

- a **base parameter file**
- a **batch-specific override file**

rather than only by parameter values embedded inside the simulation script.

In that sense, Batch 03 marks the transition from:

- archived runs of an implicitly parameterized engine

to:

- archived runs of an explicitly parameterized and researcher-visible model state

## 2. Batch identity

### Batch label
```text
calibration_batch_03_seed42
```

### Run mode
**First config-driven run**

### Run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --config config/base_parameters.yaml --override config/calibration_batch_03.yaml
```

### Archived output folder
```text
simulation/outputs/calibration_batch_03_seed42/
```

## 3. Position in the research sequence

Calibration Batch 03 follows this sequence:

1. **Baseline release**
   - `v0.1.0`

2. **Preserved post-release rerun**
   - `simulation/outputs/post_release_rerun_seed42/`

3. **Calibration Batch 01**
   - workflow-establishing calibration artifact

4. **Calibration Batch 02**
   - methodological clarification that explicit parameter control was missing

5. **Method codification**
   - analytical method definition
   - parameter inventory
   - parameter schema

6. **External config layer**
   - `config/base_parameters.yaml`
   - `config/calibration_batch_03.yaml`

7. **Calibration Batch 03**
   - first config-driven archived run

This makes Batch 03 the first batch whose analytical state is defined outside the simulation engine in a researcher-facing form.

## 4. Archived artifacts produced

The following artifacts were generated and archived for Batch 03:

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

## 5. What makes Batch 03 different

Batch 03 differs from all prior archived runs in one critical way:

### The parameter state is now explicit
Instead of relying only on values embedded inside `persona_token_governance_monte_carlo.py`, Batch 03 uses:

- `config/base_parameters.yaml`
- `config/calibration_batch_03.yaml`

This means the model state for the run is now:

- inspectable
- versionable
- externally defined
- easier to compare
- easier for other researchers to modify without changing engine logic

That is the major milestone achieved by Batch 03.

## 6. Batch 03 override intent

The Batch 03 override file introduced a first small set of explicit parameter changes relative to the base parameter state.

The override focused on:
- `repair_prob`
- `excess_context_prob`
- `repeat_state_prob`
- `governance_overhead_mean`
- `compression_strength`
- `repair_reduction_strength`
- `context_filter_strength`
- `repeat_block_strength`

The stated intention was to make Batch 03 the first genuinely parameter-adjusted calibration run while preserving the existing protocol and structural scenario expectations.

## 7. Immediate interpretation

### A. Batch 03 is the first true parameter-controlled batch
This is the most important conclusion.

Earlier batches helped stabilize the workflow and reveal the need for an explicit parameter layer. Batch 03 is the first batch that actually uses that layer.

### B. The simulation framework has crossed an important methodological threshold
Before Batch 03, calibration plans existed, but the parameter state remained largely implicit.

After Batch 03, the project now supports:
- explicit base model definition
- explicit override definition
- config-driven execution
- archived output tied to a named parameter state

That is a meaningful evolution of the research method.

### C. The project is now much more transferable
Other researchers can now inspect not only:
- the engine
- the notes
- the outputs

but also:
- the actual parameter state that defines a run

This is an important step toward making the approach extensible beyond the original author.

## 8. What Batch 03 establishes

Batch 03 establishes the following with confidence:

### 1. Config-driven execution works
The simulation engine successfully loaded YAML configuration inputs and produced a complete archived run.

### 2. The external parameter layer is now operational
The project is no longer limited to documentation about externalization. Externalization has now been used in practice.

### 3. Future calibration can now be meaningful in a stronger sense
From this point forward, a calibration batch can represent:
- same engine
- different explicit parameter state

That is far more analytically useful than repeating embedded-default runs.

### 4. The project now has the minimum viable architecture for research-grade experimentation
That architecture consists of:
- engine
- methodology
- parameter inventory
- parameter schema
- base config
- override config
- archived outputs

## 9. What still needs to be assessed

This note records the success of the first config-driven run, but it does not yet claim full quantitative interpretation of what changed in Batch 03 relative to prior batches.

The next comparison pass should explicitly assess:

1. Did Batch 03 preserve governed < ungoverned in all scenarios?
2. Did scenario ordering remain stable?
3. Did the override changes visibly affect token-burn behavior?
4. Did attribution remain led by context/state governance?
5. Did Batch 03 improve interpretability relative to Batch 02?
6. Which override dimensions appear most sensitive?

These are the questions that should be addressed in the next comparison note.

## 10. Why Batch 03 matters more than another nominal rerun

If Batch 03 had simply repeated a prior embedded-default run, its value would have been limited.

Instead, Batch 03 matters because it proves the project can now distinguish between:

- the **simulation engine**
- the **base model state**
- the **batch-specific override state**
- the **archived results of that explicit state**

That distinction is fundamental to any serious calibration program.

## 11. Recommended next step

The next step should be to interpret Batch 03 comparatively.

Recommended next artifact:

```text
docs/results/calibration-batch-03-comparison.md
```

That note should compare Batch 03 against:
- baseline context
- post-release rerun
- Batch 01
- Batch 02

with special attention to whether the new explicit override state produced analytically meaningful differences.

## 12. Recommended next implementation direction

After the Batch 03 comparison, the next likely steps should be:

1. refine the override design for Batch 04
2. continue using the config-driven method
3. tighten validation rules for config files
4. possibly introduce multi-seed runs after the parameter layer is stable

## 13. Working conclusion

Calibration Batch 03 is a major milestone for the Token Governance project.

Its most important contribution is not merely that another simulation run was archived. Its importance is that it is the first archived run whose model state is **explicitly externalized, inspectable, and versioned outside the engine**.

That changes the character of the project.

From Batch 03 onward, calibration can now be understood as a controlled comparison among explicit parameter states rather than only as repetition of a script with embedded assumptions.

That is the right foundation for all future refinement.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-03-results.md
```
