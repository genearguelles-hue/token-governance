# Calibration Batch 01 Parameter Plan

**Repository:** Token Governance  
**Document type:** Calibration batch working plan  
**Status:** Draft v0.1  
**Related note:** `docs/results/calibration-plan.md`

## 1. Purpose

This document defines the first parameter-tuning plan for **Calibration Batch 01** of the Token Governance simulation program.

The purpose of Batch 01 is not to redesign the model. It is to make a **first disciplined pass** at tuning the highest-leverage stochastic parameters so that the governed vs. ungoverned Monte Carlo behavior is more closely aligned with:

- the deterministic benchmark logic established in the Token Governance white paper
- the scenario ordering established in the first archived simulation results
- the causal interpretation documented in the calibration plan

This batch should be treated as a **controlled first adjustment**, not a full parameter sweep.

## 2. Batch identity

### Batch label
```text
calibration_batch_01_seed42
```

### Recommended output folder
```text
simulation/outputs/calibration_batch_01_seed42/
```

### Recommended run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs/calibration_batch_01_seed42
```

## 3. Starting point

Calibration Batch 01 begins from three reference points:

### A. Baseline release
- GitHub release: `v0.1.0`

### B. Initial archived results
- `docs/results/initial-simulation-results.md`

### C. Preserved post-release rerun
- `simulation/outputs/post_release_rerun_seed42/`

The preserved rerun is the immediate operational anchor for this batch.

## 4. What Batch 01 is trying to preserve

Before tuning anything, Batch 01 should preserve the following qualitative behavior:

1. **Governed token burn remains lower than ungoverned token burn in all scenarios.**
2. **Short-horizon determinate tasks remain the smallest governance-effect scenario.**
3. **Nonlinear human-centered tasks remain the largest governance-effect scenario.**
4. **Long-horizon workflow remains intermediate between those two.**
5. **Context/state governance remains the dominant source of savings.**
6. **Governance overhead remains small relative to total savings.**

These are the structural behaviors the simulation must not lose during early calibration.

## 5. Primary tuning strategy

Batch 01 should tune only the **highest-leverage parameters first**.

The overall idea is:

- reduce excessive volatility in ungoverned runs if needed
- keep governed runs meaningfully constrained without making them unrealistically frictionless
- preserve the causal story that repair loops and context carry-forward drive long-run token burn
- move the model closer to the benchmark without overfitting a single output number

## 6. Parameters to tune first

### A. Ungoverned-side parameters

#### 1. Ambiguity probability
Controls how often the system enters a state requiring clarification or misinterpretive repair.

**Why tune it:**  
Too high a value can cause unrealistically explosive repair behavior. Too low a value can flatten the difference between governed and ungoverned cases.

**Desired Batch 01 effect:**  
Keep ambiguity meaningfully present in ungoverned settings, especially in long-horizon and human-centered scenarios, but avoid making it the sole driver of cost inflation.

#### 2. Persona inconsistency probability
Controls how often the system produces responses that are weakly aligned with prior state or stance.

**Why tune it:**  
Inconsistency should contribute to repair and state expansion, but not dominate all other dynamics.

**Desired Batch 01 effect:**  
Maintain clear separation from governed behavior while making inconsistency one contributor among several, not the only explanation for rising burn.

#### 3. Drift probability
Controls how often persona behavior degrades across turns.

**Why tune it:**  
Drift is central to the thesis, but if it is too aggressive it can make all late-stage ungoverned runs collapse into the same failure mode.

**Desired Batch 01 effect:**  
Make drift visible and consequential, especially in nonlinear human-centered settings, while preserving meaningful scenario distinctions.

#### 4. Repair-loop probability
Controls how often ambiguity, inconsistency, or drift actually generate extra corrective turns.

**Why tune it:**  
Repair loops are one of the most important bridges between behavioral degradation and token burn.

**Desired Batch 01 effect:**  
Ensure repair loops remain frequent enough to explain context inflation, but not so frequent that every run turns into repetitive error correction.

#### 5. Context inflation per repair loop
Controls how much future context grows after a repair loop occurs.

**Why tune it:**  
This is one of the highest-leverage parameters in the whole model because it directly links bad interaction structure to future cost compounding.

**Desired Batch 01 effect:**  
Preserve context carry-forward as the dominant cost engine while preventing runaway growth that makes output inflation and tool behavior irrelevant.

#### 6. Output verbosity multiplier
Controls how much outputs inflate future context.

**Why tune it:**  
This should matter, but remain secondary to context/state carry-forward.

**Desired Batch 01 effect:**  
Keep verbosity as a supportive inflation mechanism, not the dominant explanation for savings.

#### 7. Unnecessary tool invocation rate
Controls how often tools are called when they are not needed.

**Why tune it:**  
Tool use should contribute to state expansion, but should not overpower context and repair-loop effects.

**Desired Batch 01 effect:**  
Keep tool-related cost noticeable, especially in workflow scenarios, without allowing it to become the principal cost driver.

### B. Governed-side parameters

#### 1. Governance overhead per turn
Represents the cost of governance itself.

**Why tune it:**  
Governed systems should not appear free. There should be a small but real overhead.

**Desired Batch 01 effect:**  
Maintain a visible overhead that is clearly outweighed by the savings from reduced repair and bounded state growth.

#### 2. Ambiguity reduction factor
Controls how much governance reduces ambiguity relative to the ungoverned case.

**Why tune it:**  
This is one of the primary benefits of governance.

**Desired Batch 01 effect:**  
Reduce ambiguity materially, but not to zero. Governed systems should still operate under uncertainty in hard scenarios.

#### 3. Inconsistency reduction factor
Controls how much governance reduces persona inconsistency.

**Why tune it:**  
Governance should reduce stance fragmentation and state incoherence.

**Desired Batch 01 effect:**  
Make governed runs visibly more coherent while preserving some residual variability.

#### 4. Drift reduction factor
Controls how strongly governance suppresses drift.

**Why tune it:**  
This is one of the most important governed-side parameters.

**Desired Batch 01 effect:**  
Keep governed drift low enough to bound trajectories over time, especially in long-horizon and human-centered conditions.

#### 5. Repair-loop reduction factor
Controls how strongly governance reduces the frequency of corrective loops.

**Why tune it:**  
This is the most direct way governance reduces future context burden.

**Desired Batch 01 effect:**  
Reduce repair loops substantially, but not so aggressively that governed runs appear unrealistically frictionless.

#### 6. Context-minimality enforcement strength
Controls how strictly the governed persona filters irrelevant or oversized context.

**Why tune it:**  
This is likely one of the strongest savings levers.

**Desired Batch 01 effect:**  
Keep context/state discipline as the dominant savings source.

#### 7. Compression ratio
Controls how much structured state compresses raw transcript carry-forward.

**Why tune it:**  
This parameter is central to the claim that engram-schema-style state representation reduces cost at the source.

**Desired Batch 01 effect:**  
Make compression strong enough to matter clearly, but still realistic enough that context never becomes trivial.

#### 8. Tool-threshold strictness
Controls how strongly governance resists unnecessary tool use.

**Why tune it:**  
This parameter should support savings without overshadowing context discipline.

**Desired Batch 01 effect:**  
Moderate reduction in unnecessary tools, especially in workflow scenarios.

## 7. Parameters not to aggressively tune in Batch 01

Batch 01 should avoid broad model reshaping.

Do **not** aggressively tune:

- number of scenarios
- scenario definitions
- total trials
- benchmark export logic
- reporting structure
- chart-generation logic
- naming conventions
- output schema

Those belong to later phases unless something is obviously broken.

## 8. Tuning principles for Batch 01

Use the following principles:

### Principle 1: Small moves first
Make moderate adjustments rather than sweeping changes. The goal is to observe direction and sensitivity, not force a desired number.

### Principle 2: Tune causal bridges, not just endpoints
Prefer tuning parameters that connect:
- ambiguity → repair loops
- repair loops → context inflation
- context inflation → future burn

rather than tuning only top-line totals.

### Principle 3: Preserve scenario differentiation
Do not flatten the model so all scenarios behave similarly.

### Principle 4: Protect attribution discipline
If calibration reduces the role of context/state governance and shifts savings almost entirely into output trimming, the batch should be considered suspect.

### Principle 5: Prefer interpretability over exact fit
A model that is slightly off in magnitude but clearly explainable is better than one that numerically matches the benchmark for opaque reasons.

## 9. Batch 01 success criteria

Calibration Batch 01 should be considered successful if it produces:

1. a separate archived output folder
2. governed < ungoverned in all scenarios
3. preserved scenario ordering
4. savings attribution still led by context/state governance
5. broad compatibility with benchmark scale in higher-complexity scenarios
6. a clearer explanation of which parameters exert the strongest influence

## 10. Batch 01 comparison checklist

After running Batch 01, compare it against:

### A. Baseline release outputs
- `simulation/outputs/`

### B. Preserved post-release rerun
- `simulation/outputs/post_release_rerun_seed42/`

### C. Deterministic benchmark
- `paper_benchmark_anchor.csv`

### D. Evaluation dimensions
- average token burn per task
- percent reduction from governance
- attribution of savings
- turn-growth behavior
- stability across scenarios

## 11. Recommended documentation after run

After Batch 01 is executed, the next note should be:

```text
docs/results/calibration-batch-01-results.md
```

That note should record:
- parameter changes made
- rationale for each change
- summary of outcome differences
- whether Batch 01 improved benchmark alignment
- what should be tuned next in Batch 02

## 12. Working conclusion

Calibration Batch 01 is the first controlled effort to move the Token Governance simulation from baseline demonstration toward disciplined refinement.

Its job is not to solve calibration completely. Its job is to make the **first interpretable, well-scoped parameter adjustments** while preserving the core governed vs. ungoverned causal structure already established in `v0.1.0` and anchored by `post_release_rerun_seed42`.

## 13. Theoretical grounding

This plan remains grounded in the Persona Engineering framework, which treats personas as formally governed composites of engrams, primitives, and axioms, with identity and coherence preserved across interaction trajectories rather than isolated responses. That framing is what justifies tuning trajectory-level parameters such as ambiguity, drift, repair loops, and state compression rather than treating token usage as only a local prompt problem. fileciteturn6file0

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-01-parameter-plan.md
```
