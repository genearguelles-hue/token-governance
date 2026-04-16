# Financial Guidance Demo Implementation

This directory contains the implementation-facing artifacts for the **Financial Guidance Demo Entity**.

The purpose of this folder is to support practical testing and demonstration of the entity after its persona specification has been defined in the documentation layer.

This implementation folder should not replace the formal persona specification. It translates the specification into runtime-facing artifacts that can be tested, revised, and evaluated.

---

## Directory Purpose

Use this folder to:

- run manual tests of the Financial Guidance Demo Entity
- stage the system prompt used for the demo
- stage the test prompts used for evaluation
- record test runs and observed failures
- track whether implementation behavior remains faithful to the persona specification

---

## Expected Files

```text
/implementation/demo-entities/financial-guidance/
├── README.md
├── system-prompt.md
├── test-prompts.md
└── run-log-template.md
```

## File Roles

### `system-prompt.md`
Implementation-facing system instruction derived from the persona specification.

This file expresses the entity’s:

- identity
- mission
- axioms
- primitives
- adaptation rules
- boundaries
- response style
- prohibited behaviors

### `test-prompts.md`
Structured prompt set for testing the entity across normal, emotional, sophisticated, adversarial, and boundary-stress scenarios.

### `run-log-template.md`
Template for recording model runs, scores, failures, drift observations, and revision recommendations.

---

## Source Design Artifacts

The implementation artifacts in this folder should be derived from the design documents located at:

```text
/docs/demo-entities/financial-guidance-demo-entity-spec.md

/docs/demo-entities/financial-guidance-demo-entity/
├── README.md
├── persona-profile.md
├── engram-schema.md
├── demo-script.md
├── evaluation-criteria.md
├── implementation-mapping.md
├── system-prompt.md
└── test-prompts.md
```

The documentation layer defines what the entity is.  
This implementation layer tests how well that entity can be expressed in a runtime environment.

---

## Manual Test Procedure

1. Open `system-prompt.md`.
2. Use it as the system instruction for the model or demo environment.
3. Open `test-prompts.md`.
4. Run prompts one at a time.
5. Record responses using `run-log-template.md`.
6. Score each response using the criteria in:

```text
/docs/demo-entities/financial-guidance-demo-entity/evaluation-criteria.md
```

7. Identify whether failures are specification-level, implementation-level, or test-level issues.

---

## Evaluation Focus

During testing, evaluate whether the entity:

- remains recognizably itself across prompts
- preserves its financial-guidance mission
- maintains explicit boundaries
- avoids individualized investment prescriptions
- avoids false certainty
- avoids emotional manipulation
- adapts to user context without identity drift
- remains useful without becoming over-cautious
- avoids generic chatbot collapse
- demonstrates token-governance discipline

---

## Revision Flow

Use this revision path:

```text
Observed behavior
    ↓
Run log entry
    ↓
Evaluation against criteria
    ↓
Diagnosis
    ↓
Revision target
```

### Revision Targets

If the failure is conceptual, revise:

```text
/docs/demo-entities/financial-guidance-demo-entity-spec.md
/docs/demo-entities/financial-guidance-demo-entity/persona-profile.md
/docs/demo-entities/financial-guidance-demo-entity/engram-schema.md
```

If the failure is implementation-specific, revise:

```text
/implementation/demo-entities/financial-guidance/system-prompt.md
```

If the failure is caused by incomplete testing, revise:

```text
/implementation/demo-entities/financial-guidance/test-prompts.md
```

---

## Common Failure Modes

Watch for:

- **generic chatbot collapse** — the entity becomes merely informative without stable advisory identity
- **advice overreach** — the entity gives specific individualized investment instructions
- **disclaimer bloat** — the entity becomes safe but verbose and unhelpful
- **emotional overreach** — the entity becomes therapeutic or overly intimate
- **sales drift** — the entity becomes persuasive, promotional, or hype-driven
- **forecast overclaim** — the entity speaks with false certainty about uncertain outcomes
- **over-caution** — the entity refuses valid educational or explanatory requests
- **token inefficiency** — the entity creates unnecessary length, ambiguity, or repair loops

---

## Success Condition

The implementation is successful when a user can interact with the entity and experience:

- a stable financial-guidance identity
- clear role boundaries
- useful explanatory guidance
- adaptive expression
- calm and prudent reasoning
- no pressure, hype, false certainty, or identity drift

The core question for every run is:

**Did the entity become better at serving the user as itself, or did it become a different entity?**

---

## Prospect Demo Readiness

The entity is ready for a prospect-facing demo only when:

- boundary stress tests pass
- direct prescription requests are handled correctly
- emotional prompts do not cause therapy drift
- sophisticated prompts receive appropriately deeper responses
- novice prompts receive clear and calm explanations
- responses remain concise enough to support token-governance claims
- the entity remains recognizably coherent across the full test set
