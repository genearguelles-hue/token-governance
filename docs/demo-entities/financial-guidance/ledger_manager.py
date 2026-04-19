#!/usr/bin/env python3
"""
Financial Guidance Persona Ledger Manager

CLI utility for appending ledger events and assessing ledger state.

Expected location:
docs/demo-entities/financial-guidance/ledger_manager.py

Default ledger path:
docs/demo-entities/financial-guidance/ledger/financial-guidance-ledger.json

Examples:

1. Initialize or verify ledger:
   python ledger_manager.py assess

2. Record system prompt conciseness update:
   python ledger_manager.py record-update \
     --artifact system-prompt.md \
     --summary "Added Conciseness Discipline and tightened Token Governance Behavior." \
     --source-file system-prompt.md \
     --notes "Runtime Persona definition changed."

3. Record governed vs. ungoverned assessment:
   python ledger_manager.py record-assessment \
     --assessment-md assessments/assessment-governed-vs-ungoverned-2026-04-17_16-15-33.md \
     --assessment-csv assessments/assessment-governed-vs-ungoverned-2026-04-17_16-15-33.csv

4. Assess ledger:
   python ledger_manager.py assess
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List

from ledger import Ledger
from ledger_entry import LedgerEntry
from ledger_store import LedgerStore
from ledger_assessor import LedgerAssessor


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_LEDGER_PATH = BASE_DIR / "ledger" / "financial-guidance-ledger.json"


def parse_markdown_summary(path: Path) -> Dict[str, Any]:
    """
    Extract simple assessment summary metrics from an assessment Markdown file.
    """
    if not path.exists():
        raise FileNotFoundError(f"Missing assessment markdown: {path}")

    text = path.read_text(encoding="utf-8")

    def extract_int(label: str, default: int = 0) -> int:
        pattern = rf"{re.escape(label)}:\s*`?(-?\d+)`?"
        match = re.search(pattern, text)
        return int(match.group(1)) if match else default

    def extract_float(label: str, default: float = 0.0) -> float:
        pattern = rf"{re.escape(label)}:\s*`?(-?\d+(?:\.\d+)?)`?"
        match = re.search(pattern, text)
        return float(match.group(1)) if match else default

    return {
        "governed_stronger": extract_int("Governed stronger"),
        "ungoverned_stronger_or_more_concise": extract_int("Ungoverned stronger or more concise"),
        "ties": extract_int("Ties"),
        "avg_governed_words": extract_float("Avg governed words"),
        "avg_ungoverned_words": extract_float("Avg ungoverned words"),
        "avg_governed_characters": extract_float("Avg governed characters"),
        "avg_ungoverned_characters": extract_float("Avg ungoverned characters"),
        "avg_governed_overall_score": extract_float("Avg governed overall score"),
        "avg_ungoverned_overall_score": extract_float("Avg ungoverned overall score"),
    }


def read_assessment_csv_flags(path: Path) -> Dict[str, Any]:
    """
    Extract drift flags and basic row counts from assessment CSV.
    """
    if not path.exists():
        return {
            "rows": 0,
            "governed_drift_flags": [],
            "ungoverned_drift_flags": [],
        }

    governed_flags: List[str] = []
    ungoverned_flags: List[str] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        gf = (row.get("governed_drift_flags") or "").strip()
        uf = (row.get("ungoverned_drift_flags") or "").strip()
        if gf:
            governed_flags.extend([x for x in gf.split(";") if x])
        if uf:
            ungoverned_flags.extend([x for x in uf.split(";") if x])

    return {
        "rows": len(rows),
        "governed_drift_flags": governed_flags,
        "ungoverned_drift_flags": ungoverned_flags,
    }


def load_ledger(path: Path) -> Ledger:
    return LedgerStore.load(path)


def save_ledger(ledger: Ledger, path: Path) -> None:
    LedgerStore.save(ledger, path)


def append_entry(ledger_path: Path, entry: LedgerEntry) -> None:
    ledger = load_ledger(ledger_path)
    ledger.append(entry)
    save_ledger(ledger, ledger_path)


def record_update(args: argparse.Namespace) -> None:
    ledger_path = Path(args.ledger).resolve()
    ledger = load_ledger(ledger_path)

    entry = LedgerEntry.create(
        event_type="persona_definition_update",
        artifact_changed=args.artifact,
        change_summary=args.summary,
        state_snapshot={
            "artifact_changed": args.artifact,
            "change_type": "runtime_persona_definition_update",
        },
        engrams={
            "mission": 1,
            "axiom": 1,
            "primitive": 1,
            "token_governance": 1,
        },
        axiom_pressure=args.axiom_pressure,
        primitive_saturation=args.primitive_saturation,
        drift_status=args.drift_status,
        token_metrics={
            "token_governance_relevance": True,
            "response_word_count": None,
            "response_char_count": None,
        },
        assessment_metrics={},
        source_files=args.source_file,
        notes=args.notes,
        previous_hash=ledger.last_hash(),
    )

    ledger.append(entry)
    save_ledger(ledger, ledger_path)

    print("Ledger update recorded.")
    print(f"Ledger: {ledger_path}")
    print(f"Event hash: {entry.hash}")


def record_assessment(args: argparse.Namespace) -> None:
    ledger_path = Path(args.ledger).resolve()
    ledger = load_ledger(ledger_path)

    assessment_md = Path(args.assessment_md).resolve()
    assessment_csv = Path(args.assessment_csv).resolve() if args.assessment_csv else None

    summary_metrics = parse_markdown_summary(assessment_md)
    csv_metrics = read_assessment_csv_flags(assessment_csv) if assessment_csv else {}

    governed_flags = csv_metrics.get("governed_drift_flags", [])
    ungoverned_flags = csv_metrics.get("ungoverned_drift_flags", [])

    drift_status = "✅ stable"
    axiom_pressure = 0
    primitive_saturation = 0

    if governed_flags:
        drift_status = "⚠️ governed drift warning"
        axiom_pressure = 2
        primitive_saturation = 2

    if any(flag in {"advice_overreach", "weak_boundary_under_pressure"} for flag in governed_flags):
        axiom_pressure = 3
        drift_status = "⚠️ axiom pressure detected"

    entry = LedgerEntry.create(
        event_type="governed_vs_ungoverned_assessment",
        artifact_changed=None,
        change_summary="Recorded governed vs. ungoverned assessment results.",
        state_snapshot={
            "assessment_md": str(assessment_md),
            "assessment_csv": str(assessment_csv) if assessment_csv else None,
            "comparison_type": "governed_vs_ungoverned",
        },
        engrams={
            "assessment": 1,
            "token_governance": 1,
            "drift_monitoring": 1,
        },
        axiom_pressure=axiom_pressure,
        primitive_saturation=primitive_saturation,
        drift_status=drift_status,
        token_metrics={
            "avg_governed_words": summary_metrics.get("avg_governed_words"),
            "avg_ungoverned_words": summary_metrics.get("avg_ungoverned_words"),
            "avg_governed_characters": summary_metrics.get("avg_governed_characters"),
            "avg_ungoverned_characters": summary_metrics.get("avg_ungoverned_characters"),
        },
        assessment_metrics={
            **summary_metrics,
            **csv_metrics,
        },
        source_files=[str(assessment_md)] + ([str(assessment_csv)] if assessment_csv else []),
        notes=args.notes,
        previous_hash=ledger.last_hash(),
    )

    ledger.append(entry)
    save_ledger(ledger, ledger_path)

    print("Assessment ledger entry recorded.")
    print(f"Ledger: {ledger_path}")
    print(f"Event hash: {entry.hash}")
    print(f"Drift status: {entry.drift_status}")


def assess(args: argparse.Namespace) -> None:
    ledger_path = Path(args.ledger).resolve()
    report = LedgerAssessor().assess(ledger_path)

    print("Financial Guidance Persona Ledger Assessment")
    print("=" * 48)
    for key, value in asdict(report).items():
        print(f"{key}: {value}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Financial Guidance Persona Ledger Manager")
    parser.add_argument(
        "--ledger",
        default=str(DEFAULT_LEDGER_PATH),
        help=f"Path to ledger JSON. Default: {DEFAULT_LEDGER_PATH}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    update = subparsers.add_parser("record-update", help="Record a persona definition update.")
    update.add_argument("--artifact", required=True, help="Changed artifact, e.g. system-prompt.md")
    update.add_argument("--summary", required=True, help="Short summary of change.")
    update.add_argument("--source-file", action="append", default=[], help="Source file path. May be repeated.")
    update.add_argument("--notes", default="", help="Additional notes.")
    update.add_argument("--axiom-pressure", type=int, default=0)
    update.add_argument("--primitive-saturation", type=int, default=1)
    update.add_argument("--drift-status", default="✅ stable")
    update.set_defaults(func=record_update)

    assessment = subparsers.add_parser("record-assessment", help="Record governed-vs-ungoverned assessment.")
    assessment.add_argument("--assessment-md", required=True, help="Assessment markdown path.")
    assessment.add_argument("--assessment-csv", default="", help="Assessment CSV path.")
    assessment.add_argument("--notes", default="", help="Additional notes.")
    assessment.set_defaults(func=record_assessment)

    assess_cmd = subparsers.add_parser("assess", help="Assess the ledger trajectory.")
    assess_cmd.set_defaults(func=assess)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
