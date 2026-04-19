# Financial Guidance Persona Ledger Management

This directory contains ledger-management utilities for the **Financial Guidance Demo Entity**.

The ledger records persona-governance events such as:

- runtime persona definition updates
- `system-prompt.md` revisions
- governed vs. ungoverned assessment results
- drift warnings
- token-governance metrics

## Files

```text
ledger_entry.py      # immutable hash-chain ledger event
ledger.py            # append-only ledger
ledger_store.py      # JSON persistence
ledger_assessor.py   # trajectory-level ledger assessment
ledger_manager.py    # CLI for recording updates and assessments
```

## Recommended Location

Place these files in:

```text
docs/demo-entities/financial-guidance/
```

or, if you prefer a subfolder:

```text
docs/demo-entities/financial-guidance/ledger_management/
```

If placed in a subfolder, run commands from that subfolder or adjust imports accordingly.

## Default Ledger Path

By default, `ledger_manager.py` writes to:

```text
docs/demo-entities/financial-guidance/ledger/financial-guidance-ledger.json
```

## Record a System Prompt Update

A change to `system-prompt.md` is a persona-definition ledger event because it changes the runtime compression of the Financial Guidance Persona.

```bash
python ledger_manager.py record-update \
  --artifact system-prompt.md \
  --summary "Added Conciseness Discipline and tightened Token Governance Behavior." \
  --source-file system-prompt.md \
  --notes "Runtime Persona definition changed; concision is now an explicit governed behavior."
```

## Record a Governed vs. Ungoverned Assessment

```bash
python ledger_manager.py record-assessment \
  --assessment-md assessments/assessment-governed-vs-ungoverned-2026-04-17_16-15-33.md \
  --assessment-csv assessments/assessment-governed-vs-ungoverned-2026-04-17_16-15-33.csv \
  --notes "Post-conciseness-update comparison run."
```

## Assess Ledger

```bash
python ledger_manager.py assess
```

## Conceptual Role

The ledger is the persistence layer for persona evolution.

It records:

- what changed
- why it changed
- what artifact changed
- which assessment followed
- whether drift or axiom pressure appeared
- whether token-governance behavior improved

This supports Persona Engineering as an auditable practice rather than an informal prompt-editing workflow.
