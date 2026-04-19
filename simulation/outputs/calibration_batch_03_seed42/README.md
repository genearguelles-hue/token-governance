# Persona Token Governance Monte Carlo Results

- Trials per scenario-condition: 4000
- Master seed: 42

## Cross-scenario comparison

| scenario_label            |   ungoverned_avg_tokens_per_task |   governed_avg_tokens_per_task |   absolute_reduction_tokens |   reduction_pct |
|:--------------------------|---------------------------------:|-------------------------------:|----------------------------:|----------------:|
| short_horizon_determinate |                           6058.1 |                        3692.23 |                     2365.87 |         39.053  |
| long_horizon_workflow     |                          28660.5 |                       15175.8  |                    13484.7  |         47.0498 |
| nonlinear_human_centered  |                          40061.1 |                       20770.9  |                    19290.3  |         48.1521 |

## Attribution

| scenario_label            |   context_share_pct |   output_share_pct |   tool_share_pct |   turn_share_pct |
|:--------------------------|--------------------:|-------------------:|-----------------:|-----------------:|
| short_horizon_determinate |             66.1791 |            16.3864 |          6.02275 |          11.4117 |
| long_horizon_workflow     |             69.957  |            13.2896 |          6.48321 |          10.2703 |
| nonlinear_human_centered  |             70.2664 |            14.009  |          5.53194 |          10.1926 |

## Notes

- Trial-level outputs include context, output, tool, governance, and repair metrics.
- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.
- Output schema version: v1.
- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.