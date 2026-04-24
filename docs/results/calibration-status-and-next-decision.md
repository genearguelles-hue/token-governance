# Calibration Status and Next Decision

**Repository:** Token Governance  
**Document type:** Status and decision note  
**Status:** Draft v0.1  
**Related artifacts:**  
- `docs/results/batch-03-and-04-milestone-summary.md`
- `docs/results/calibration-batch-03-significance-report.md`
- `docs/results/calibration-batch-04-significance-report.md`
- `docs/results/calibration-batch-04-comparison.md`
- `docs/methodology/analytical-method-definition.md`
- `docs/methodology/parameter-schema.md`
- `docs/methodology/output-schema-standard.md`

## 1. Purpose

This note records the current calibration status of the Token Governance simulation program and defines the decision frame for what should happen next.

At this point, the project has completed:

- baseline release and post-release anchor work
- parameter inventory and schema definition
- externalized config-driven execution
- output-schema standardization
- Batch 03 refinement and significance analysis
- Batch 04 refinement and significance analysis
- a milestone summary consolidating the two-batch improvement cycle

The question is no longer whether the model can be run, documented, and compared. The question is:

> **Is Batch 05 necessary, and if so, what threshold would justify it?**

## 2. Current calibration status

The project is now beyond proof-of-concept execution.

It has established:

### A. A stable analytical method
The repo now contains:
- explicit method definition
- parameter inventory
- parameter schema
- output schema standard
- reproducible archival structure

### B. A working config-driven model
The simulation engine can now run from:
- `config/base_parameters.yaml`
- batch-specific override files

This means calibration is no longer implicit.

### C. Standardized output structure
Outputs now support cleaner comparison across batches through:
- stable scenario keys
- stable condition keys
- stable merge structure

### D. Two successive refinement batches
Batch 03 and Batch 04 both moved the model in the intended direction.

## 3. What is now established

The following can now be treated as established findings of the current calibration program.

### 1. Config-driven calibration works
The model can be adjusted through explicit parameter states rather than hidden script edits.

### 2. Improvement is repeatable
Batch 03 showed the first config-driven improvement.
Batch 04 extended that improvement.

### 3. The main mechanism remains stable
Across both refinement batches, the strongest explanation for the gains remains:
- fewer repair loops
- lower distortion pressure
- stronger context/state discipline
- stable turn counts

### 4. The strongest effects remain in the more complex scenarios
The largest and clearest improvements continue to appear in:
- `long_horizon_workflow`
- `nonlinear_human_centered`

### 5. Statistical support now exists in key places
The strongest statistically supported results include:
- governed token-burn reduction in key scenarios
- governed repair-loop reduction across all scenarios
- stable turn counts, indicating gains are not mainly coming from shorter exchanges

## 4. What remains uncertain

Even with these gains, some things are still unresolved.

### A. Diminishing returns threshold
It is not yet fully clear whether another refinement batch would produce enough additional information to justify the work.

### B. Small-effect regime
The statistically significant gains are generally modest in magnitude, not transformative. That means further refinement may continue to help, but likely in smaller increments.

### C. Batch 05 value proposition
A new batch is only justified if it is likely to clarify something materially new rather than merely repeat the same pattern at slightly smaller scale.

## 5. Current decision frame

The current decision is best framed as:

### Option 1: Consolidate and pause
This would treat Batch 03 and Batch 04 as a meaningful milestone and pause further calibration until a new reason for refinement appears.

### Option 2: Proceed to Batch 05
This would authorize one more very small and selective refinement batch.

The burden of proof is now on Batch 05.

## 6. Recommendation

The recommended default is:

> **Pause and consolidate unless Batch 05 is expected to produce materially new insight.**

This recommendation is based on the fact that the project already has:

- two config-driven refinement batches
- repeatable directional improvement
- statistically supported gains in the intended mechanisms
- standardized outputs
- a mature enough methodology for external communication

That is already a substantial milestone.

## 7. When Batch 05 would be justified

Batch 05 should be run only if at least one of the following is true:

### A. Mechanism clarification
A new batch is needed to distinguish more clearly among:
- repair reduction
- context inflation control
- repeat-state carry-forward control
- compression/filtering strength

### B. Marginal-gain verification
A new batch is needed to test whether the model is approaching a stable calibration plateau.

### C. External communication need
A new batch would materially improve the strength of a white paper, release note, investor/client communication, or research-facing summary.

### D. Comparative decision need
A new batch is needed to decide whether the model should:
- remain in the current scope
- move into sensitivity analysis
- move into multi-seed robustness testing
- expand into a new scenario family

## 8. When Batch 05 would not be justified

Batch 05 should **not** be run if it would only provide:

- another modestly favorable result of the same type
- no clearer attribution among leverage points
- no materially stronger evidence than Batch 03 and Batch 04 already provide
- no decision-relevant new information

In that case, more batching would risk looking repetitive rather than analytically meaningful.

## 9. Best next step if pausing

If the project pauses here, the best next actions are:

1. consolidate repo-facing conclusions
2. prepare external summary material
3. preserve the current framework as a stable checkpoint
4. define the next research phase deliberately rather than reflexively

That next research phase might be:
- sensitivity analysis
- multi-seed robustness testing
- parameter-ablation analysis
- scope expansion to a more complex scenario family

## 10. Best next step if proceeding

If Batch 05 is authorized, it should be:

- smaller than Batch 04
- tightly focused
- explicitly justified
- aimed at clarifying a specific remaining uncertainty

Likely candidate parameters would remain:
- `repair_prob`
- `repair_reduction_strength`
- `excess_context_prob`
- `compression_strength`
- `context_filter_strength`
- `repeat_block_strength`

But the adjustment sizes should be minimal, and the objective should be sharper than “improve things again.”

## 11. Practical recommendation

The most practical recommendation is:

> **Treat the project as being at a consolidation checkpoint, not at an automatic next-batch point.**

That means:
- the current status is strong enough to summarize externally
- the evidence base is now meaningful
- the next move should be a deliberate decision, not a habitual continuation

## 12. Working conclusion

The Token Governance simulation program has now reached a stage where:

- the method is codified
- the model is configurable
- outputs are standardized
- improvement is repeatable
- key gains are statistically supported
- the strongest mechanisms are identifiable

That is enough to justify a pause for consolidation.

The correct next decision is therefore not “run Batch 05 by default,” but:

> **Run Batch 05 only if it is expected to produce materially new insight beyond what Batch 03 and Batch 04 already established.**

---

## Suggested repository placement

Recommended path:

```text
docs/results/calibration-status-and-next-decision.md
```
