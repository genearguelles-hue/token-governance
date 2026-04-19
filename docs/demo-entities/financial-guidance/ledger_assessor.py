#!/usr/bin/env python3
"""
Financial Guidance Persona Ledger Assessor

Assesses a ledger trajectory after persona definition updates and run assessments.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ledger_store import LedgerStore


@dataclass
class AssessmentReport:
    ledger_valid: bool
    total_entries: int

    persona_definition_updates: int
    run_events: int
    comparison_assessments: int

    max_axiom_pressure: int
    max_primitive_saturation: int

    first_axiom_pressure: int
    last_axiom_pressure: int
    pressure_delta: int
    pressure_trend: str

    first_primitive_saturation: int
    last_primitive_saturation: int
    saturation_delta: int
    saturation_trend: str

    drift_warnings: int
    stable_entries: int

    max_response_word_count: int
    average_response_word_count: float
    token_governance_warnings: int

    trajectory_status: str
    persona_valid: bool
    summary: str


class LedgerAssessor:
    def __init__(
        self,
        axiom_pressure_threshold: int = 3,
        primitive_saturation_threshold: int = 3,
        response_word_warning_threshold: int = 450,
    ) -> None:
        self.axiom_pressure_threshold = axiom_pressure_threshold
        self.primitive_saturation_threshold = primitive_saturation_threshold
        self.response_word_warning_threshold = response_word_warning_threshold

    def _classify_trend(self, delta: int) -> str:
        if delta < 0:
            return "improving"
        if delta > 0:
            return "worsening"
        return "stable"

    def _classify_trajectory_status(
        self,
        *,
        ledger_valid: bool,
        pressure_trend: str,
        saturation_trend: str,
        drift_warnings: int,
        token_governance_warnings: int,
    ) -> str:
        if not ledger_valid:
            return "invalid-ledger"

        if drift_warnings > 0:
            return "degrading"

        if pressure_trend == "worsening" or saturation_trend == "worsening":
            return "degrading"

        if token_governance_warnings > 0:
            return "token-governance-watch"

        if pressure_trend == "improving" or saturation_trend == "improving":
            return "stabilizing"

        return "stable"

    def assess(self, ledger_path: str | Path) -> AssessmentReport:
        ledger = LedgerStore.load(ledger_path)
        entries = ledger.entries()

        ledger_valid = ledger.verify()
        total_entries = len(entries)

        if total_entries == 0:
            return AssessmentReport(
                ledger_valid=ledger_valid,
                total_entries=0,
                persona_definition_updates=0,
                run_events=0,
                comparison_assessments=0,
                max_axiom_pressure=0,
                max_primitive_saturation=0,
                first_axiom_pressure=0,
                last_axiom_pressure=0,
                pressure_delta=0,
                pressure_trend="stable",
                first_primitive_saturation=0,
                last_primitive_saturation=0,
                saturation_delta=0,
                saturation_trend="stable",
                drift_warnings=0,
                stable_entries=0,
                max_response_word_count=0,
                average_response_word_count=0.0,
                token_governance_warnings=0,
                trajectory_status="stable",
                persona_valid=ledger_valid,
                summary="Ledger is empty. No persona trajectory to assess.",
            )

        persona_definition_updates = sum(1 for e in entries if e.event_type == "persona_definition_update")
        run_events = sum(1 for e in entries if e.event_type in {"governed_run", "ungoverned_run"})
        comparison_assessments = sum(1 for e in entries if e.event_type == "governed_vs_ungoverned_assessment")

        max_axiom_pressure = max(entry.axiom_pressure for entry in entries)
        max_primitive_saturation = max(entry.primitive_saturation for entry in entries)

        first_axiom_pressure = entries[0].axiom_pressure
        last_axiom_pressure = entries[-1].axiom_pressure
        pressure_delta = last_axiom_pressure - first_axiom_pressure
        pressure_trend = self._classify_trend(pressure_delta)

        first_primitive_saturation = entries[0].primitive_saturation
        last_primitive_saturation = entries[-1].primitive_saturation
        saturation_delta = last_primitive_saturation - first_primitive_saturation
        saturation_trend = self._classify_trend(saturation_delta)

        drift_warnings = sum(1 for entry in entries if "⚠️" in entry.drift_status or "warning" in entry.drift_status.lower())
        stable_entries = sum(1 for entry in entries if "✅" in entry.drift_status or "stable" in entry.drift_status.lower())

        word_counts = []
        for entry in entries:
            if "response_word_count" in entry.token_metrics:
                try:
                    word_counts.append(int(entry.token_metrics["response_word_count"]))
                except (TypeError, ValueError):
                    pass
            if "avg_governed_words" in entry.assessment_metrics:
                try:
                    word_counts.append(int(float(entry.assessment_metrics["avg_governed_words"])))
                except (TypeError, ValueError):
                    pass

        max_response_word_count = max(word_counts) if word_counts else 0
        average_response_word_count = sum(word_counts) / len(word_counts) if word_counts else 0.0
        token_governance_warnings = sum(1 for wc in word_counts if wc > self.response_word_warning_threshold)

        trajectory_status = self._classify_trajectory_status(
            ledger_valid=ledger_valid,
            pressure_trend=pressure_trend,
            saturation_trend=saturation_trend,
            drift_warnings=drift_warnings,
            token_governance_warnings=token_governance_warnings,
        )

        persona_valid = ledger_valid and trajectory_status not in {"invalid-ledger", "degrading"}

        summary = (
            f"Ledger valid: {ledger_valid}. "
            f"Entries: {total_entries}. "
            f"Definition updates: {persona_definition_updates}. "
            f"Comparison assessments: {comparison_assessments}. "
            f"Trajectory status: {trajectory_status}. "
            f"Persona valid: {persona_valid}."
        )

        return AssessmentReport(
            ledger_valid=ledger_valid,
            total_entries=total_entries,
            persona_definition_updates=persona_definition_updates,
            run_events=run_events,
            comparison_assessments=comparison_assessments,
            max_axiom_pressure=max_axiom_pressure,
            max_primitive_saturation=max_primitive_saturation,
            first_axiom_pressure=first_axiom_pressure,
            last_axiom_pressure=last_axiom_pressure,
            pressure_delta=pressure_delta,
            pressure_trend=pressure_trend,
            first_primitive_saturation=first_primitive_saturation,
            last_primitive_saturation=last_primitive_saturation,
            saturation_delta=saturation_delta,
            saturation_trend=saturation_trend,
            drift_warnings=drift_warnings,
            stable_entries=stable_entries,
            max_response_word_count=max_response_word_count,
            average_response_word_count=average_response_word_count,
            token_governance_warnings=token_governance_warnings,
            trajectory_status=trajectory_status,
            persona_valid=persona_valid,
            summary=summary,
        )
