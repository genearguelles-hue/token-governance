#!/usr/bin/env python3
"""
Financial Guidance Persona Ledger Store

Save/load ledger JSON files.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from ledger import Ledger
from ledger_entry import LedgerEntry


class LedgerStore:
    """
    Save and load Ledger objects as JSON.
    """

    @staticmethod
    def save(ledger: Ledger, filepath: str | Path) -> None:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)

        records: List[Dict[str, Any]] = [entry.to_record() for entry in ledger.entries()]

        with path.open("w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

    @staticmethod
    def load(filepath: str | Path) -> Ledger:
        path = Path(filepath)

        if not path.exists():
            return Ledger()

        with path.open("r", encoding="utf-8") as f:
            records = json.load(f)

        ledger = Ledger()

        for record in records:
            entry = LedgerEntry.from_record(record)
            ledger.append(entry)

        return ledger
