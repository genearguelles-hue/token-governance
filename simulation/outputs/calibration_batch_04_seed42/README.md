# Persona Token Governance Monte Carlo Results

- Trials per scenario-condition: 4000
- Master seed: 42

## Cross-scenario comparison

| scenario_label            |   ungoverned_avg_tokens_per_task |   governed_avg_tokens_per_task |   absolute_reduction_tokens |   reduction_pct |
|:--------------------------|---------------------------------:|-------------------------------:|----------------------------:|----------------:|
| short_horizon_determinate |                          6037.64 |                        3647.27 |                     2390.37 |         39.5911 |
| long_horizon_workflow     |                         28495    |                       14905.9  |                    13589.2  |         47.6895 |
| nonlinear_human_centered  |                         39779.5  |                       20346.3  |                    19433.2  |         48.8524 |

## Attribution

| scenario_label            |   context_share_pct |   output_share_pct |   tool_share_pct |   turn_share_pct |
|:--------------------------|--------------------:|-------------------:|-----------------:|-----------------:|
| short_horizon_determinate |             66.8151 |            15.9854 |          6.00474 |          11.1948 |
| long_horizon_workflow     |             70.1456 |            13.2523 |          6.47063 |          10.1315 |
| nonlinear_human_centered  |             70.4385 |            13.9334 |          5.5158  |          10.1124 |

## Notes

- Trial-level outputs include context, output, tool, governance, and repair metrics.
- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.
- Output schema version: v1.
- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.