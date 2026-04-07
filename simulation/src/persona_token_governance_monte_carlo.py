
"""
Persona Engineering / Token Governance Monte Carlo Simulation
------------------------------------------------------------

This script exports the simulation logic used to compare governed vs. ungoverned
AI interaction trajectories.

What it includes:
- parameter definitions
- RNG seed control
- scenario configs
- Monte Carlo loop
- output table generation
- chart generation

The model is intentionally structural rather than implementation-specific:
it treats token burn as a function of evolving interaction state, especially
context carry-forward, output feedback, tool expansion, repair loops, and
governance constraints.

Usage:
    python persona_token_governance_monte_carlo.py

Optional CLI:
    python persona_token_governance_monte_carlo.py --seed 42 --trials 5000 --outdir sim_outputs
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------
# Data model
# ---------------------------

@dataclass(frozen=True)
class Scenario:
    name: str
    base_turns: int
    new_input_mean: float
    new_input_sd: float
    base_output_mean: float
    base_output_sd: float
    tool_need_prob: float
    repair_prob: float
    repeat_state_prob: float
    stale_retention_prob: float
    excess_context_prob: float
    verbosity_prob: float
    rebrief_prob: float
    session_base_state: float
    relevant_carry_forward: float


@dataclass(frozen=True)
class GovernanceConfig:
    label: str
    # Governance overhead paid each turn for filtering / compression / validation
    governance_overhead_mean: float
    governance_overhead_sd: float
    # Context admission / carry-forward controls
    context_filter_strength: float      # lowers excess context
    repeat_block_strength: float        # lowers repeated stable info
    stale_prune_strength: float         # lowers stale carry-forward
    compression_strength: float         # compresses retained state
    # Output controls
    output_bound_strength: float        # lowers verbosity
    progressive_disclosure_strength: float
    # Tool controls
    tool_threshold_strength: float      # rejects unnecessary tool calls
    tool_token_reduction: float         # compresses accepted tool use
    # Interaction efficiency
    repair_reduction_strength: float
    rebrief_reduction_strength: float
    turn_efficiency_bonus: float        # makes earlier convergence slightly more likely


# ---------------------------
# Scenario definitions
# ---------------------------

SCENARIOS: Dict[str, Scenario] = {
    "short_horizon_determinate": Scenario(
        name="Short-horizon determinate",
        base_turns=6,
        new_input_mean=360,
        new_input_sd=45,
        base_output_mean=260,
        base_output_sd=40,
        tool_need_prob=0.12,
        repair_prob=0.16,
        repeat_state_prob=0.10,
        stale_retention_prob=0.08,
        excess_context_prob=0.12,
        verbosity_prob=0.18,
        rebrief_prob=0.05,
        session_base_state=180,
        relevant_carry_forward=120,
    ),
    "long_horizon_workflow": Scenario(
        name="Long-horizon workflow",
        base_turns=13,
        new_input_mean=620,
        new_input_sd=85,
        base_output_mean=430,
        base_output_sd=70,
        tool_need_prob=0.32,
        repair_prob=0.28,
        repeat_state_prob=0.38,
        stale_retention_prob=0.26,
        excess_context_prob=0.33,
        verbosity_prob=0.34,
        rebrief_prob=0.24,
        session_base_state=520,
        relevant_carry_forward=240,
    ),
    "nonlinear_human_centered": Scenario(
        name="Nonlinear human-centered",
        base_turns=15,
        new_input_mean=700,
        new_input_sd=110,
        base_output_mean=520,
        base_output_sd=95,
        tool_need_prob=0.26,
        repair_prob=0.34,
        repeat_state_prob=0.42,
        stale_retention_prob=0.32,
        excess_context_prob=0.39,
        verbosity_prob=0.41,
        rebrief_prob=0.31,
        session_base_state=640,
        relevant_carry_forward=300,
    ),
}

UNGOVERNED = GovernanceConfig(
    label="Ungoverned",
    governance_overhead_mean=0.0,
    governance_overhead_sd=0.0,
    context_filter_strength=0.0,
    repeat_block_strength=0.0,
    stale_prune_strength=0.0,
    compression_strength=0.0,
    output_bound_strength=0.0,
    progressive_disclosure_strength=0.0,
    tool_threshold_strength=0.0,
    tool_token_reduction=0.0,
    repair_reduction_strength=0.0,
    rebrief_reduction_strength=0.0,
    turn_efficiency_bonus=0.0,
)

GOVERNED = GovernanceConfig(
    label="Governed",
    governance_overhead_mean=36.0,
    governance_overhead_sd=6.0,
    context_filter_strength=0.52,
    repeat_block_strength=0.56,
    stale_prune_strength=0.58,
    compression_strength=0.44,
    output_bound_strength=0.34,
    progressive_disclosure_strength=0.22,
    tool_threshold_strength=0.47,
    tool_token_reduction=0.38,
    repair_reduction_strength=0.48,
    rebrief_reduction_strength=0.54,
    turn_efficiency_bonus=0.16,
)


# ---------------------------
# RNG utilities
# ---------------------------

def clipped_normal(rng: np.random.Generator, mean: float, sd: float, low: float = 0.0) -> float:
    val = rng.normal(mean, sd)
    return float(max(low, val))


def bernoulli(rng: np.random.Generator, p: float) -> bool:
    p = min(max(p, 0.0), 1.0)
    return bool(rng.random() < p)


# ---------------------------
# Turn / task simulation
# ---------------------------

def simulate_task(
    rng: np.random.Generator,
    scenario: Scenario,
    gov: GovernanceConfig
) -> Dict[str, float]:
    """
    Simulate one task/session.

    State representation:
    - relevant_state: task-relevant carry-forward
    - stable_state: repeated stable project info / durable state
    - stale_state: superseded residue
    - tool_artifacts: token residue from prior tool interactions
    """
    # Base number of turns; governance can reduce required turns.
    turn_efficiency = 1.0 - gov.turn_efficiency_bonus
    turns = max(2, int(round(clipped_normal(rng, scenario.base_turns * turn_efficiency, 1.2, low=2))))

    # Session-start state: rebriefing of stable project context
    stable_state = scenario.session_base_state
    if bernoulli(rng, scenario.rebrief_prob * (1.0 - gov.rebrief_reduction_strength)):
        stable_state += clipped_normal(rng, scenario.session_base_state * 0.65, scenario.session_base_state * 0.12)

    relevant_state = scenario.relevant_carry_forward
    stale_state = clipped_normal(rng, scenario.session_base_state * 0.18, scenario.session_base_state * 0.06)
    tool_artifacts = 0.0

    totals = {
        "turns": float(turns),
        "context_tokens": 0.0,
        "output_tokens": 0.0,
        "tool_tokens": 0.0,
        "governance_tokens": 0.0,
        "repair_loops": 0.0,
        "rebrief_events": 0.0,
        "context_relevant": 0.0,
        "context_redundant": 0.0,
        "context_stale": 0.0,
        "context_oversized": 0.0,
        "output_excess": 0.0,
        "tool_unnecessary": 0.0,
    }

    if stable_state > scenario.session_base_state:
        totals["rebrief_events"] += 1.0

    # Store per-turn cumulative total for charting
    cumulative_tokens = []
    running_total = 0.0

    for t in range(1, turns + 1):
        new_input = clipped_normal(rng, scenario.new_input_mean, scenario.new_input_sd, low=40)
        base_output = clipped_normal(rng, scenario.base_output_mean, scenario.base_output_sd, low=40)
        governance_tokens = clipped_normal(rng, gov.governance_overhead_mean, gov.governance_overhead_sd, low=0)

        # Relevant context always persists to some degree, though governance compresses it.
        relevant_component = relevant_state + new_input

        # Repeated stable info
        repeated_state = 0.0
        if bernoulli(rng, scenario.repeat_state_prob * (1.0 - gov.repeat_block_strength)):
            repeated_state = stable_state

        # Stale residue persists unless pruned
        stale_component = stale_state * (1.0 - gov.stale_prune_strength * 0.85)

        # Oversized context admission
        oversized_component = 0.0
        if bernoulli(rng, scenario.excess_context_prob * (1.0 - gov.context_filter_strength)):
            oversized_component = clipped_normal(rng, scenario.new_input_mean * 0.85, scenario.new_input_sd * 0.7, low=0)

        # Previously generated tool artifacts carried forward
        artifact_component = tool_artifacts

        context_tokens = relevant_component + repeated_state + stale_component + oversized_component + artifact_component
        context_tokens *= (1.0 - gov.compression_strength * 0.55)

        # Output generation
        verbose_excess = 0.0
        if bernoulli(rng, scenario.verbosity_prob * (1.0 - gov.output_bound_strength)):
            verbose_excess = clipped_normal(rng, scenario.base_output_mean * (0.55 - 0.25 * gov.progressive_disclosure_strength),
                                            scenario.base_output_sd * 0.35, low=0)

        output_tokens = base_output + verbose_excess
        output_tokens *= (1.0 - gov.output_bound_strength * 0.22)

        # Tool use
        tool_tokens = 0.0
        unnecessary_tool_tokens = 0.0
        if bernoulli(rng, scenario.tool_need_prob):
            # Necessary tool call
            tool_tokens += clipped_normal(rng, scenario.base_output_mean * 0.85, scenario.base_output_sd * 0.60, low=20)
        else:
            # Unnecessary tool use occurs more often when ungoverned
            unnecessary_prob = max(0.0, 0.18 - gov.tool_threshold_strength * 0.12)
            if bernoulli(rng, unnecessary_prob):
                unnecessary_tool_tokens = clipped_normal(rng, scenario.base_output_mean * 0.60, scenario.base_output_sd * 0.45, low=20)
                tool_tokens += unnecessary_tool_tokens

        tool_tokens *= (1.0 - gov.tool_token_reduction)

        # Repair loops / clarifications / reorientation
        repair_tokens = 0.0
        repair_prob = scenario.repair_prob * (1.0 - gov.repair_reduction_strength)
        if bernoulli(rng, repair_prob):
            totals["repair_loops"] += 1.0
            repair_tokens = clipped_normal(rng, scenario.new_input_mean * 0.55, scenario.new_input_sd * 0.40, low=25)
            # Repair loops often add output and context
            output_tokens += repair_tokens * 0.38
            context_tokens += repair_tokens * 0.62

        # Bookkeeping totals
        totals["context_tokens"] += context_tokens
        totals["output_tokens"] += output_tokens
        totals["tool_tokens"] += tool_tokens
        totals["governance_tokens"] += governance_tokens

        totals["context_relevant"] += relevant_component * (1.0 - gov.compression_strength * 0.20)
        totals["context_redundant"] += repeated_state * (1.0 - gov.compression_strength * 0.35)
        totals["context_stale"] += stale_component
        totals["context_oversized"] += oversized_component * (1.0 - gov.compression_strength * 0.35)
        totals["output_excess"] += verbose_excess
        totals["tool_unnecessary"] += unnecessary_tool_tokens * (1.0 - gov.tool_token_reduction)

        running_total += context_tokens + output_tokens + tool_tokens + governance_tokens
        cumulative_tokens.append(running_total)

        # State updates for next turn
        # Relevant state grows slowly, but governance compresses stored form.
        relevant_state = (scenario.relevant_carry_forward + 0.10 * new_input + 0.18 * output_tokens)
        relevant_state *= (1.0 - gov.compression_strength * 0.55)

        # Stable state grows when outputs are verbose or repeated state is carried around.
        stable_state = max(
            scenario.session_base_state * 0.55,
            (stable_state * 0.78 + repeated_state * 0.14 + verbose_excess * 0.10 + 0.04 * output_tokens)
            * (1.0 - gov.repeat_block_strength * 0.48)
        )

        # Stale state accumulates unless pruned.
        stale_state = max(
            0.0,
            stale_state * (0.85 - gov.stale_prune_strength * 0.40) + 0.08 * repeated_state + 0.06 * verbose_excess
        )

        # Tool artifacts persist unless governed.
        tool_artifacts = max(0.0, tool_tokens * (0.26 - gov.tool_threshold_strength * 0.10))

    totals["total_tokens"] = (
        totals["context_tokens"] + totals["output_tokens"] + totals["tool_tokens"] + totals["governance_tokens"]
    )
    totals["cumulative_curve"] = cumulative_tokens
    return totals


def monte_carlo(
    scenario: Scenario,
    gov: GovernanceConfig,
    trials: int,
    seed: int
) -> Tuple[pd.DataFrame, List[List[float]]]:
    """
    Run Monte Carlo trials for one scenario/governance condition.
    """
    rng = np.random.default_rng(seed)
    rows = []
    curves = []

    for i in range(trials):
        result = simulate_task(rng, scenario, gov)
        result["trial"] = i + 1
        result["scenario"] = scenario.name
        result["condition"] = gov.label
        rows.append(result)
        curves.append(result["cumulative_curve"])

    df = pd.DataFrame(rows)
    return df, curves


# ---------------------------
# Aggregation and attribution
# ---------------------------

def summarize_condition(df: pd.DataFrame) -> pd.Series:
    return pd.Series({
        "trials": len(df),
        "avg_tokens_per_task": df["total_tokens"].mean(),
        "median_tokens_per_task": df["total_tokens"].median(),
        "p95_tokens_per_task": df["total_tokens"].quantile(0.95),
        "avg_turns_per_task": df["turns"].mean(),
        "avg_repair_loops_per_task": df["repair_loops"].mean(),
        "avg_rebrief_rate": (df["rebrief_events"] > 0).mean(),
        "avg_context_tokens": df["context_tokens"].mean(),
        "avg_output_tokens": df["output_tokens"].mean(),
        "avg_tool_tokens": df["tool_tokens"].mean(),
        "avg_governance_tokens": df["governance_tokens"].mean(),
        "avg_context_relevant": df["context_relevant"].mean(),
        "avg_context_redundant": df["context_redundant"].mean(),
        "avg_context_stale": df["context_stale"].mean(),
        "avg_context_oversized": df["context_oversized"].mean(),
        "avg_output_excess": df["output_excess"].mean(),
        "avg_unnecessary_tool_tokens": df["tool_unnecessary"].mean(),
    })


def compare_conditions(ung_df: pd.DataFrame, gov_df: pd.DataFrame, scenario_name: str) -> pd.Series:
    ung = summarize_condition(ung_df)
    gov = summarize_condition(gov_df)

    delta_total = ung["avg_tokens_per_task"] - gov["avg_tokens_per_task"]
    reduction_pct = 100 * delta_total / ung["avg_tokens_per_task"]

    # Attribution of governed savings
    # Split savings into direct component deltas plus a convergence/turn-efficiency component.
    context_delta_raw = max(0.0, ung["avg_context_tokens"] - gov["avg_context_tokens"])
    output_delta_raw = max(0.0, ung["avg_output_tokens"] - gov["avg_output_tokens"])
    tool_delta_raw = max(0.0, ung["avg_tool_tokens"] - gov["avg_tool_tokens"])

    ung_per_turn = ung["avg_tokens_per_task"] / max(ung["avg_turns_per_task"], 1e-9)
    turn_delta_raw = max(0.0, (ung["avg_turns_per_task"] - gov["avg_turns_per_task"]) * ung_per_turn * 0.35)

    raw_sum = max(context_delta_raw + output_delta_raw + tool_delta_raw + turn_delta_raw, 1e-9)
    scale = delta_total / raw_sum if raw_sum > 0 else 0.0

    context_delta = context_delta_raw * scale
    output_delta = output_delta_raw * scale
    tool_delta = tool_delta_raw * scale
    turn_delta_proxy = turn_delta_raw * scale

    denom = max(delta_total, 1e-9)
    return pd.Series({
        "scenario": scenario_name,
        "ungoverned_avg_tokens_per_task": ung["avg_tokens_per_task"],
        "governed_avg_tokens_per_task": gov["avg_tokens_per_task"],
        "absolute_reduction_tokens": delta_total,
        "reduction_pct": reduction_pct,
        "ungoverned_avg_turns": ung["avg_turns_per_task"],
        "governed_avg_turns": gov["avg_turns_per_task"],
        "ungoverned_avg_repair_loops": ung["avg_repair_loops_per_task"],
        "governed_avg_repair_loops": gov["avg_repair_loops_per_task"],
        "ungoverned_avg_rebrief_rate": ung["avg_rebrief_rate"],
        "governed_avg_rebrief_rate": gov["avg_rebrief_rate"],
        "context_share_of_savings_pct": 100 * context_delta / denom,
        "output_share_of_savings_pct": 100 * output_delta / denom,
        "tool_share_of_savings_pct": 100 * tool_delta / denom,
        "turn_share_of_savings_pct": 100 * turn_delta_proxy / denom,
    })


# ---------------------------
# Plotting
# ---------------------------

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def save_bar_chart(compare_df: pd.DataFrame, outdir: Path) -> None:
    plt.figure(figsize=(8, 5))
    x = np.arange(len(compare_df))
    width = 0.36
    plt.bar(x - width / 2, compare_df["ungoverned_avg_tokens_per_task"], width=width, label="Ungoverned")
    plt.bar(x + width / 2, compare_df["governed_avg_tokens_per_task"], width=width, label="Governed")
    plt.xticks(x, compare_df["scenario"], rotation=15, ha="right")
    plt.ylabel("Average tokens per task")
    plt.title("Governed vs Ungoverned: Average Token Burn per Task")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "chart_tokens_per_task.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(compare_df["scenario"], compare_df["reduction_pct"])
    plt.ylabel("Percent reduction")
    plt.title("Percent Token Reduction from Governance")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(outdir / "chart_reduction_pct.png", dpi=180)
    plt.close()


def save_growth_chart(curves_u: List[List[float]], curves_g: List[List[float]], scenario_name: str, filename: Path) -> None:
    max_len = max(max(map(len, curves_u)), max(map(len, curves_g)))

    def pad_and_mean(curves):
        arr = np.full((len(curves), max_len), np.nan)
        for i, c in enumerate(curves):
            arr[i, :len(c)] = c
            if len(c) < max_len:
                arr[i, len(c):] = c[-1]
        return np.nanmean(arr, axis=0)

    mean_u = pad_and_mean(curves_u)
    mean_g = pad_and_mean(curves_g)

    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(1, max_len + 1), mean_u, label="Ungoverned")
    plt.plot(np.arange(1, max_len + 1), mean_g, label="Governed")
    plt.xlabel("Turn")
    plt.ylabel("Cumulative tokens")
    plt.title(f"Turn-level Token Growth: {scenario_name}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=180)
    plt.close()


def save_attribution_chart(compare_df: pd.DataFrame, outdir: Path) -> None:
    # average across scenarios
    avg_context = compare_df["context_share_of_savings_pct"].mean()
    avg_output = compare_df["output_share_of_savings_pct"].mean()
    avg_tool = compare_df["tool_share_of_savings_pct"].mean()
    avg_turn = compare_df["turn_share_of_savings_pct"].mean()

    labels = ["Context", "Output", "Tool", "Turn / convergence"]
    values = [avg_context, avg_output, avg_tool, avg_turn]

    plt.figure(figsize=(7, 5))
    plt.bar(labels, values)
    plt.ylabel("Share of total savings (%)")
    plt.title("Average Attribution of Governed Savings")
    plt.tight_layout()
    plt.savefig(outdir / "chart_attribution.png", dpi=180)
    plt.close()


# ---------------------------
# Main run logic
# ---------------------------

def run_batch(trials: int, seed: int, outdir: Path) -> None:
    ensure_dir(outdir)

    all_rows = []
    compare_rows = []
    attribution_rows = []

    growth_curves = {}

    # Deterministic benchmark from the Token Governance paper framing
    benchmark = pd.DataFrame([
        {
            "scenario": "Paper benchmark",
            "ungoverned_avg_tokens_per_task": 39900.0,
            "governed_avg_tokens_per_task": 15876.0,
            "absolute_reduction_tokens": 24024.0,
            "reduction_pct": 100 * (39900.0 - 15876.0) / 39900.0,
            "ungoverned_avg_turns": 14.0,
            "governed_avg_turns": 9.8,
            "ungoverned_avg_repair_loops": np.nan,
            "governed_avg_repair_loops": np.nan,
            "ungoverned_avg_rebrief_rate": np.nan,
            "governed_avg_rebrief_rate": np.nan,
            "context_share_of_savings_pct": 50.0,
            "output_share_of_savings_pct": 21.0,
            "tool_share_of_savings_pct": 12.0,
            "turn_share_of_savings_pct": 17.0,
        }
    ])
    benchmark.to_csv(outdir / "paper_benchmark_anchor.csv", index=False)

    for idx, (key, scenario) in enumerate(SCENARIOS.items(), start=1):
        ung_seed = seed + idx * 101
        gov_seed = seed + idx * 101 + 1

        ung_df, ung_curves = monte_carlo(scenario, UNGOVERNED, trials, ung_seed)
        gov_df, gov_curves = monte_carlo(scenario, GOVERNED, trials, gov_seed)

        all_rows.append(ung_df)
        all_rows.append(gov_df)

        comp = compare_conditions(ung_df, gov_df, scenario.name)
        compare_rows.append(comp)

        attribution_rows.append(pd.Series({
            "scenario": scenario.name,
            "context_share_pct": comp["context_share_of_savings_pct"],
            "output_share_pct": comp["output_share_of_savings_pct"],
            "tool_share_pct": comp["tool_share_of_savings_pct"],
            "turn_share_pct": comp["turn_share_of_savings_pct"],
        }))

        growth_curves[scenario.name] = (ung_curves, gov_curves)

    all_df = pd.concat(all_rows, ignore_index=True)
    compare_df = pd.DataFrame(compare_rows)
    attribution_df = pd.DataFrame(attribution_rows)

    # Summary by scenario x condition
    summary_rows = []
    for (scenario_name, condition), g in all_df.groupby(["scenario", "condition"]):
        row = summarize_condition(g).to_dict()
        row["scenario"] = scenario_name
        row["condition"] = condition
        summary_rows.append(row)
    summary_df = pd.DataFrame(summary_rows)

    # Save tabular outputs
    all_df.drop(columns=["cumulative_curve"]).to_csv(outdir / "simulation_trial_level.csv", index=False)
    summary_df.to_csv(outdir / "simulation_summary.csv", index=False)
    compare_df.to_csv(outdir / "simulation_compare.csv", index=False)
    attribution_df.to_csv(outdir / "simulation_attribution.csv", index=False)

    # Charts
    save_bar_chart(compare_df, outdir)
    save_attribution_chart(compare_df, outdir)

    for scenario_name, (u, g) in growth_curves.items():
        slug = scenario_name.lower().replace(" ", "_").replace("-", "_")
        save_growth_chart(u, g, scenario_name, outdir / f"chart_turn_growth_{slug}.png")

    # Simple markdown report
    report_lines = [
        "# Persona Token Governance Monte Carlo Results",
        "",
        f"- Trials per scenario-condition: {trials}",
        f"- Master seed: {seed}",
        "",
        "## Cross-scenario comparison",
        "",
        compare_df.to_markdown(index=False),
        "",
        "## Attribution",
        "",
        attribution_df.to_markdown(index=False),
        "",
        "## Notes",
        "",
        "- Trial-level outputs include context, output, tool, governance, and repair metrics.",
        "- Governance is modeled as structural constraint over context admission, carry-forward, verbosity, tool thresholds, and repair/rebrief rates.",
        "- The paper benchmark anchor is exported separately in `paper_benchmark_anchor.csv`.",
    ]
    (outdir / "README.md").write_text("\n".join(report_lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--trials", type=int, default=4000)
    p.add_argument("--outdir", type=str, default="sim_outputs")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    outdir = Path(args.outdir)
    run_batch(trials=args.trials, seed=args.seed, outdir=outdir)
    print(f"Simulation complete. Outputs written to: {outdir.resolve()}")
