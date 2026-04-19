# Persona Token Governance Monte Carlo Results

- Trials per scenario-condition: 4000
- Master seed: 42

## Cross-scenario comparison

| scenario_label            |   ungoverned_avg_tokens_per_task |   governed_avg_tokens_per_task |   absolute_reduction_tokens |   reduction_pct |
|:--------------------------|---------------------------------:|-------------------------------:|----------------------------:|----------------:|
| short_horizon_determinate |                          6076.23 |                        3772.17 |                     2304.05 |         37.9191 |
| long_horizon_workflow     |                         28839    |                       15669.5  |                    13169.5  |         45.6656 |
| nonlinear_human_centered  |                         40731.8  |                       21463.3  |                    19268.6  |         47.3059 |

## Attribution

| scenario_label            |   context_share_pct |   output_share_pct |   tool_share_pct |   turn_share_pct |
|:--------------------------|--------------------:|-------------------:|-----------------:|-----------------:|
| short_horizon_determinate |             65.5418 |            16.6652 |          6.07408 |          11.7189 |
| long_horizon_workflow     |             69.63   |            13.4455 |          6.54601 |          10.3785 |
| nonlinear_human_centered  |             69.9412 |            14.0832 |          5.59607 |          10.3796 |

## Notes

- Trial-level outputs include context, output, tool, governance, and repair metrics.
- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.
- Output schema version: v1.
- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.