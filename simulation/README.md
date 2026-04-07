# Simulation

This directory contains the Token Governance Monte Carlo simulation and related artifacts.

## Contents

- `src/` — primary simulation script
- `outputs/` — generated CSVs, charts, and reports
- `notebooks/` — optional notebook versions and exploratory analysis

## Run

```bash
python simulation/src/persona_token_governance_monte_carlo.py --seed 42 --trials 4000 --outdir simulation/outputs
```

## Expected Outputs

Typical outputs include:
- `simulation_trial_level.csv`
- `simulation_summary.csv`
- `simulation_compare.csv`
- `simulation_attribution.csv`
- scenario comparison charts
- growth charts
- benchmark anchor exports
- a local README or manifest from the script
