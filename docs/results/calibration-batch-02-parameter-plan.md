# Calibration Batch 02 Parameter Plan

**Repository:** Token Governance  
**Document type:** Calibration batch working plan  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/calibration-plan.md`  
- `docs/results/calibration-batch-01-parameter-plan.md`  
- `docs/results/calibration-batch-01-results.md`  
- `docs/results/calibration-batch-01-comparison.md`  
- `docs/methodology/analytical-method-definition.md`

## 1. Purpose

This document defines the parameter-tuning plan for **Calibration Batch 02** of the Token Governance simulation program.

Where **Batch 01** primarily established the calibration workflow and preserved the first archived calibration cycle, **Batch 02** is intended to become the first more intentionally steered calibration pass.

Its purpose is to make a **targeted second adjustment** to the highest-leverage parameters so that the simulation moves closer to an analytically stable and more interpretable governed-vs-ungoverned model while preserving the existing protocol.

Batch 02 is therefore not a change in methodology. It is a continuation of the same method under more deliberate parameter discipline.

## 2. Batch identity

### Batch label
```text
calibration_batch_02_seed42
```

### Recommended output folder
```text
simulation/outputs/calibration_batch_02_seed42/
```

### Recommended run command
```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs/calibration_batch_02_seed42
```

## 3. Starting point for Batch 02

Batch 02 begins from the full chain now established in the repository:

1. **Baseline release**
   - `v0.1.0`

2. **Preserved post-release rerun**
   - `simulation/outputs/post_release_rerun_seed42/`

3. **Calibration Batch 01 archive**
   - `simulation/outputs/calibration_batch_01_seed42/`

4. **Batch 01 documentation**
   - parameter plan
   - results note
   - comparison note

The key conclusion from the Batch 01 comparison is that Batch 01 should be treated primarily as a **workflow-establishing calibration artifact**, not yet as a decisive quantitative recalibration. Batch 02 therefore becomes the first batch that should attempt more explicit behavioral improvement.

## 4. What Batch 02 must preserve

Batch 02 should **not** sacrifice the core structural behavior of the model.

The following must remain true:

1. **Governed token burn remains lower than ungoverned token burn in all scenarios.**
2. **Short-horizon determinate remains the smallest governance-effect scenario.**
3. **Long-horizon workflow remains intermediate.**
4. **Nonlinear human-centered remains the largest governance-effect scenario.**
5. **Context/state governance remains the dominant source of savings.**
6. **Governance overhead remains meaningfully smaller than total avoided burn.**
7. **The analytical protocol remains unchanged.**

These are non-negotiable structural expectations for Batch 02.

## 5. Batch 02 objective

Batch 02 should attempt to improve the model along three axes:

### Objective 1: Sharpen causal discipline
The governed vs. ungoverned difference should be more clearly attributable to the intended bridge variables:

- ambiguity
- drift
- repair loops
- context inflation
- compression
- governance overhead

### Objective 2: Reduce unnecessary looseness
If any parameters currently allow the model to appear too diffuse, too arbitrary, or too weakly coupled to the causal story, Batch 02 should tighten them.

### Objective 3: Prepare for eventual calibration stability
Batch 02 should move the project closer to a state where later batches are smaller and more corrective rather than still foundational.

## 6. Primary Batch 02 tuning focus

Based on the Batch 01 comparison, the most sensible parameters to prioritize next are:

- repair-loop probability
- context inflation per repair loop
- drift probability
- ambiguity probability
- compression ratio
- governance overhead

These remain the best bridge parameters between:
- interaction degradation
- state carry-forward
- compounding token burn
- constrained governance effects

## 7. Proposed parameter directions

Batch 02 should not make sweeping changes. It should make **moderate, interpretable directional adjustments**.

### A. Repair-loop probability
**Reason to tune:**  
Repair loops are one of the clearest translation mechanisms from behavioral degradation to token inflation.

**Batch 02 direction:**  
Tighten the relationship between ambiguity/inconsistency/drift and repair loops so that repair remains a strong inflation driver, but does not become indiscriminate.

**Desired effect:**  
A more interpretable and controlled contribution of repair loops to long-run burn.

### B. Context inflation per repair loop
**Reason to tune:**  
This is likely one of the most leverage-rich parameters in the entire model.

**Batch 02 direction:**  
Adjust context inflation so that it remains dominant as a cost mechanism, but avoid runaway escalation that obscures all other contributions.

**Desired effect:**  
Clearer demonstration that governance mainly saves tokens by constraining future context burden.

### C. Drift probability
**Reason to tune:**  
Drift is central to the theoretical framing, but if too aggressive it can flatten scenario differentiation.

**Batch 02 direction:**  
Keep drift structurally important, especially in the nonlinear human-centered scenario, while reducing the risk that all ungoverned late-stage behavior collapses into the same pattern.

**Desired effect:**  
More meaningful scenario differentiation without losing the drift thesis.

### D. Ambiguity probability
**Reason to tune:**  
Ambiguity is a strong upstream driver but should not behave as the sole explanation for burn differences.

**Batch 02 direction:**  
Slightly tighten ambiguity behavior so it remains important yet balanced with drift and repair-loop dynamics.

**Desired effect:**  
Clearer causal balance across the ungoverned distortion mechanisms.

### E. Compression ratio
**Reason to tune:**  
Compression is one of the most direct governance-side expressions of the engram-schema/state-discipline thesis.

**Batch 02 direction:**  
Strengthen or clarify compression enough that governed state discipline remains visibly dominant in savings attribution, but not so strong that governed context becomes unrealistically trivial.

**Desired effect:**  
Preserve context/state discipline as the primary explanation for governed savings.

### F. Governance overhead
**Reason to tune:**  
Governed systems should not appear to produce savings at zero cost.

**Batch 02 direction:**  
Keep governance overhead visible and credible, but bounded well below the scale of avoided distortion burn.

**Desired effect:**  
A more defensible claim that governance costs something small in order to save something larger.

## 8. Parameters Batch 02 should avoid changing aggressively

To preserve interpretability, Batch 02 should avoid major changes to:

- scenario definitions
- total trial count
- file schema
- chart-generation logic
- benchmark export logic
- naming conventions
- batch archival structure
- reporting structure

The method should remain stable while parameter behavior becomes more precise.

## 9. Batch 02 tuning principles

### Principle 1: Preserve protocol
No change to the research protocol, archival discipline, or document sequence.

### Principle 2: Adjust bridges, not cosmetics
Prioritize parameters that govern how interaction distortions become token burn.

### Principle 3: Prefer moderate directional moves
Batch 02 should not attempt a final fit. It should make clearer, well-explained second-order adjustments.

### Principle 4: Protect scenario ordering
If a parameter change threatens the established scenario ordering, treat that as a warning sign.

### Principle 5: Protect attribution discipline
If savings begin to appear driven mainly by output trimming rather than context/state governance, the batch should be considered analytically suspect.

## 10. What would count as improvement in Batch 02

Batch 02 should be considered an improvement over Batch 01 if it produces:

1. governed < ungoverned in all scenarios
2. preserved scenario ordering
3. more interpretable relationship between distortion variables and burn
4. context/state discipline still dominant in savings attribution
5. more plausible balance between governance overhead and avoided burn
6. clearer justification for what to tune next, with fewer foundational ambiguities left in the model

Batch 02 does **not** need to be perfect. It needs to be more intentional and more analytically legible than Batch 01.

## 11. Batch 02 comparison targets

After Batch 02 is run, compare it directly against:

### A. Baseline release context
- initial released outputs

### B. Preserved rerun anchor
- `simulation/outputs/post_release_rerun_seed42/`

### C. Calibration Batch 01
- `simulation/outputs/calibration_batch_01_seed42/`

### D. Primary evaluation dimensions
- average token burn per task
- percent reduction from governance
- attribution of savings
- turn-growth shape
- scenario differentiation
- apparent stability of the governed-vs-ungoverned causal structure

## 12. Recommended follow-on artifact

After running Batch 02, the next note should be:

```text
docs/results/calibration-batch-02-results.md
```

That note should record:
- which parameter directions were applied
- what changed relative to Batch 01
- whether the model became more stable or more interpretable
- whether Batch 03 should be narrower, smaller, or unnecessary

## 13. Working conclusion

Calibration Batch 02 should be the first batch that deliberately shifts the model from **workflow establishment** toward **behavioral refinement**.

Its job is not to finish the research program. Its job is to make the model:

- more interpretable
- more disciplined
- more causally legible
- better positioned for eventual stabilization

That makes Batch 02 the first calibration batch whose success should be judged not just by being archived, but by whether it improves the explanatory quality of the governed-vs-ungoverned comparison.

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-batch-02-parameter-plan.md
```
