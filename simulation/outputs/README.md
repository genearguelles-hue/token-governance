# Persona Token Governance Monte Carlo Results

- Trials per scenario-condition: 4000
- Master seed: 42

## Cross-scenario comparison

| scenario                  |   ungoverned_avg_tokens_per_task |   governed_avg_tokens_per_task |   absolute_reduction_tokens |   reduction_pct |   ungoverned_avg_turns |   governed_avg_turns |   ungoverned_avg_repair_loops |   governed_avg_repair_loops |   ungoverned_avg_rebrief_rate |   governed_avg_rebrief_rate |   context_share_of_savings_pct |   output_share_of_savings_pct |   tool_share_of_savings_pct |   turn_share_of_savings_pct |
|:--------------------------|---------------------------------:|-------------------------------:|----------------------------:|----------------:|-----------------------:|---------------------:|------------------------------:|----------------------------:|------------------------------:|----------------------------:|-------------------------------:|------------------------------:|----------------------------:|----------------------------:|
| Short-horizon determinate |                          6076.23 |                        3772.17 |                     2304.05 |         37.9191 |                 6.0015 |               5.07   |                        0.9485 |                     0.4095  |                       0.05425 |                      0.0215 |                        65.5418 |                       16.6652 |                     6.07408 |                     11.7189 |
| Long-horizon workflow     |                         28839    |                       15669.5  |                    13169.5  |         45.6656 |                12.9678 |              10.9497 |                        3.6295 |                     1.62725 |                       0.22575 |                      0.1095 |                        69.63   |                       13.4455 |                     6.54601 |                     10.3785 |
| Nonlinear human-centered  |                         40731.8  |                       21463.3  |                    19268.6  |         47.3059 |                14.975  |              12.5757 |                        5.089  |                     2.19675 |                       0.309   |                      0.141  |                        69.9412 |                       14.0832 |                     5.59607 |                     10.3796 |

## Attribution

| scenario                  |   context_share_pct |   output_share_pct |   tool_share_pct |   turn_share_pct |
|:--------------------------|--------------------:|-------------------:|-----------------:|-----------------:|
| Short-horizon determinate |             65.5418 |            16.6652 |          6.07408 |          11.7189 |
| Long-horizon workflow     |             69.63   |            13.4455 |          6.54601 |          10.3785 |
| Nonlinear human-centered  |             69.9412 |            14.0832 |          5.59607 |          10.3796 |

## Notes

- Trial-level outputs include context, output, tool, governance, and repair metrics.
- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.
- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.