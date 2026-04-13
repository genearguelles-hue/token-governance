# Persona Token Governance Monte Carlo Results

- Trials per scenario-condition: 4000
- Master seed: 42

## Cross-scenario comparison

| scenario                  |   ungoverned_avg_tokens_per_task |   governed_avg_tokens_per_task |   absolute_reduction_tokens |   reduction_pct |   ungoverned_avg_turns |   governed_avg_turns |   ungoverned_avg_repair_loops |   governed_avg_repair_loops |   ungoverned_avg_rebrief_rate |   governed_avg_rebrief_rate |   context_share_of_savings_pct |   output_share_of_savings_pct |   tool_share_of_savings_pct |   turn_share_of_savings_pct |
|:--------------------------|---------------------------------:|-------------------------------:|----------------------------:|----------------:|-----------------------:|---------------------:|------------------------------:|----------------------------:|------------------------------:|----------------------------:|-------------------------------:|------------------------------:|----------------------------:|----------------------------:|
| short_horizon_determinate |                           6058.1 |                        3692.23 |                     2365.87 |         39.053  |                6.01225 |               5.0775 |                       0.909   |                     0.3705  |                       0.05725 |                     0.0255  |                        66.1791 |                       16.3864 |                     6.02275 |                     11.4117 |
| long_horizon_workflow     |                          28660.5 |                       15175.8  |                    13484.7  |         47.0498 |               13.0145  |              10.9503 |                       3.3955  |                     1.39325 |                       0.2405  |                     0.10925 |                        69.957  |                       13.2896 |                     6.48321 |                     10.2703 |
| nonlinear_human_centered  |                          40061.1 |                       20770.9  |                    19290.3  |         48.1521 |               14.9995  |              12.5992 |                       4.64075 |                     1.8895  |                       0.29825 |                     0.143   |                        70.2664 |                       14.009  |                     5.53194 |                     10.1926 |

## Attribution

| scenario                  |   context_share_pct |   output_share_pct |   tool_share_pct |   turn_share_pct |
|:--------------------------|--------------------:|-------------------:|-----------------:|-----------------:|
| short_horizon_determinate |             66.1791 |            16.3864 |          6.02275 |          11.4117 |
| long_horizon_workflow     |             69.957  |            13.2896 |          6.48321 |          10.2703 |
| nonlinear_human_centered  |             70.2664 |            14.009  |          5.53194 |          10.1926 |

## Notes

- Trial-level outputs include context, output, tool, governance, and repair metrics.
- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.
- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.