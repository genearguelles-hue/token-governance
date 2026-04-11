# Token Governance

**Token Governance** is an operational extension of **Persona Engineering** into AI cost systems.

This repository contains:

- the **Token Governance** white paper
- the foundational **Persona Engineering** paper
- a Monte Carlo simulation for governed vs. ungoverned token burn
- archived first-batch simulation outputs
- an initial results note documenting the first simulation run

## Overview

Token Governance starts from a simple claim:

> Token cost is not just a pricing artifact or a prompt-length issue. It is an emergent property of interaction structure over time.

In sustained AI workflows, token burn compounds through:

- context carry-forward
- redundant and stale state
- verbose outputs that inflate future turns
- unnecessary tool-mediated state expansion
- repair loops caused by ambiguity, inconsistency, and drift

The central idea of this project is that these costs can be reduced by governing the **interactional identity** of the system itself through Persona Engineering. In this model, governance is not an after-the-fact optimization trick. It is built into the persona through:

- **axioms** as invariants
- **primitives** as trajectory constraints
- **engram schemas** as state-compression mechanisms

## Core Thesis

The repository explores the claim that:

- **ungoverned systems** tend toward compounding interaction-state growth
- **persona-governed systems** constrain context, bound trajectory evolution, and reduce cumulative token burn over time

The strongest gains are expected in long-horizon, context-heavy, and human-centered interaction settings.

## White Papers

### Token Governance
Primary paper:

- `docs/white-paper/Token_Governance_White_Paper.pdf`

### Persona Engineering
Foundational companion paper:

- `references/Persona_Engineering_White_Paper.pdf`

## Initial Simulation Results

The first archived results note is here:

- `docs/results/initial-simulation-results.md`

That note summarizes the first simulation batch across three scenarios:

1. short-horizon determinate task
2. long-horizon workflow collaboration
3. nonlinear human-centered mission

Headline first-batch results:

| Scenario | Ungoverned | Governed | Reduction |
|---|---:|---:|---:|
| Short-horizon determinate | 5,625 | 3,430 | 39.0% |
| Long-horizon workflow | 31,453 | 15,042 | 52.2% |
| Nonlinear human-centered | 54,199 | 21,227 | 60.8% |

## Simulation

Primary simulation script:

- `simulation/src/persona_token_governance_monte_carlo.py`

Archived outputs:

- `simulation/outputs/simulation_compare.csv`
- `simulation/outputs/simulation_summary.csv`
- `simulation/outputs/simulation_attribution.csv`
- `simulation/outputs/paper_benchmark_anchor.csv`

Charts:

- `simulation/outputs/chart_tokens_per_task.png`
- `simulation/outputs/chart_reduction_pct.png`
- `simulation/outputs/chart_turn_growth_workflow.png`
- `simulation/outputs/chart_turn_growth_humancentered.png`
- `simulation/outputs/chart_attribution.png`

## Reproducibility

Install dependencies:

```bash
python -m pip install -r requirements.txt
