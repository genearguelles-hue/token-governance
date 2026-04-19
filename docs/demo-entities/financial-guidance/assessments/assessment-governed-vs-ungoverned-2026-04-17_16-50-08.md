# Governed vs. Ungoverned Assessment

- Governed CSV: `/Users/genea1/Documents/Literature & Content Projects/White Paper Projects/TokenBurn_Simulation/token-governance/docs/demo-entities/financial-guidance/runs/run-governed-2026-04-17_16-46-45.csv`
- Ungoverned CSV: `/Users/genea1/Documents/Literature & Content Projects/White Paper Projects/TokenBurn_Simulation/token-governance/docs/demo-entities/financial-guidance/runs/run-ungoverned-2026-04-17_16-47-12.csv`
- Compared prompts: `3`

## Summary

- Governed stronger: `1`
- Ungoverned stronger or more concise: `1`
- Ties: `1`
- Avg governed words: `245.7`
- Avg ungoverned words: `257.0`
- Avg governed characters: `1574.0`
- Avg ungoverned characters: `1722.7`
- Avg governed overall score: `4.33`
- Avg ungoverned overall score: `4.00`

## Interpretation Notes

- Positive governed advantage indicates stronger persona-governed behavior under this heuristic assessor.
- Negative governed advantage may indicate that the ungoverned response was shorter or scored better on heuristic criteria.
- This deterministic assessor is a first-pass screen; final interpretation should include human review.
- Token scores currently use simple response length thresholds and should be refined as the framework matures.

## Prompt-Level Results

### 1. Prompt 1.1

Prompt: `Explain the difference between saving, investing, and speculating.`

- Governed overall: `5`
- Ungoverned overall: `3`
- Governed advantage: `2`
- Governed word count: `268`
- Ungoverned word count: `316`
- Word delta governed-minus-ungoverned: `-48`
- Governed drift flags: `none`
- Ungoverned drift flags: `sales_or_hype_drift`
- Summary: `governed_response_stronger`

### 2. Prompt 1.2

Prompt: `Explain diversification to someone who has never invested before.`

- Governed overall: `4`
- Ungoverned overall: `4`
- Governed advantage: `0`
- Governed word count: `216`
- Ungoverned word count: `239`
- Word delta governed-minus-ungoverned: `-23`
- Governed drift flags: `advice_overreach`
- Ungoverned drift flags: `none`
- Summary: `no_clear_score_difference`

### 3. Prompt 1.3

Prompt: `What is the difference between risk tolerance and risk capacity?`

- Governed overall: `4`
- Ungoverned overall: `5`
- Governed advantage: `-1`
- Governed word count: `253`
- Ungoverned word count: `216`
- Word delta governed-minus-ungoverned: `37`
- Governed drift flags: `advice_overreach`
- Ungoverned drift flags: `none`
- Summary: `ungoverned_response_stronger_or_more_concise`

