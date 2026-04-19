#!/usr/bin/env python3
"""
Financial Guidance Persona Ledger Entry

Immutable hash-chain record for the Financial Guidance Demo Entity.

Supports three major event types:
- persona_definition_update
- governed_run
- governed_vs_ungoverned_assessment

The ledger is intentionally append-only. Any system-prompt.md revision,
engram-schema.md revision, run assessment, or drift finding should be recorded
as a new ledger event.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class LedgerEntry:
    """
    Immutable record of a single persona-governance event.
    """

    timestamp: float
    event_type: str
    persona_id: str
    persona_name: str

    artifact_changed: Optional[str]
    change_summary: str

    user_input: str
    response: str

    state_snapshot: Dict[str, Any]
    engrams: Dict[str, int]

    axiom_pressure: int
    primitive_saturation: int
    drift_status: str

    token_metrics: Dict[str, Any]
    assessment_metrics: Dict[str, Any]

    source_files: List[str]
    notes: str

    previous_hash: str
    hash: str = field(init=False)

    def __post_init__(self) -> None:
        self.hash = self.compute_hash()

    @classmethod
    def create(
        cls,
        *,
        event_type: str,
        persona_id: str = "financial-guidance-demo-entity",
        persona_name: str = "Financial Guidance Demo Entity",
        artifact_changed: Optional[str] = None,
        change_summary: str = "",
        user_input: str = "",
        response: str = "",
        state_snapshot: Optional[Dict[str, Any]] = None,
        engrams: Optional[Dict[str, int]] = None,
        axiom_pressure: int = 0,
        primitive_saturation: int = 0,
        drift_status: str = "✅ stable",
        token_metrics: Optional[Dict[str, Any]] = None,
        assessment_metrics: Optional[Dict[str, Any]] = None,
        source_files: Optional[List[str]] = None,
        notes: str = "",
        previous_hash: str = "GENESIS",
        timestamp: Optional[float] = None,
    ) -> "LedgerEntry":
        return cls(
            timestamp=timestamp if timestamp is not None else time.time(),
            event_type=event_type,
            persona_id=persona_id,
            persona_name=persona_name,
            artifact_changed=artifact_changed,
            change_summary=change_summary,
            user_input=user_input,
            response=response,
            state_snapshot=state_snapshot or {},
            engrams=engrams or {},
            axiom_pressure=axiom_pressure,
            primitive_saturation=primitive_saturation,
            drift_status=drift_status,
            token_metrics=token_metrics or {},
            assessment_metrics=assessment_metrics or {},
            source_files=source_files or [],
            notes=notes,
            previous_hash=previous_hash,
        )

    def to_hash_payload(self) -> Dict[str, Any]:
        """
        Return the canonical payload used for hashing.
        The computed hash field itself is intentionally excluded.
        """
        return {
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "persona_id": self.persona_id,
            "persona_name": self.persona_name,
            "artifact_changed": self.artifact_changed,
            "change_summary": self.change_summary,
            "user_input": self.user_input,
            "response": self.response,
            "state_snapshot": self.state_snapshot,
            "engrams": self.engrams,
            "axiom_pressure": self.axiom_pressure,
            "primitive_saturation": self.primitive_saturation,
            "drift_status": self.drift_status,
            "token_metrics": self.token_metrics,
            "assessment_metrics": self.assessment_metrics,
            "source_files": self.source_files,
            "notes": self.notes,
            "previous_hash": self.previous_hash,
        }

    def compute_hash(self) -> str:
        encoded = json.dumps(self.to_hash_payload(), sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def to_record(self) -> Dict[str, Any]:
        record = self.to_hash_payload()
        record["hash"] = self.hash
        return record

    @classmethod
    def from_record(cls, record: Dict[str, Any]) -> "LedgerEntry":
        entry = cls(
            timestamp=record["timestamp"],
            event_type=record["event_type"],
            persona_id=record.get("persona_id", "financial-guidance-demo-entity"),
            persona_name=record.get("persona_name", "Financial Guidance Demo Entity"),
            artifact_changed=record.get("artifact_changed"),
            change_summary=record.get("change_summary", ""),
            user_input=record.get("user_input", ""),
            response=record.get("response", ""),
            state_snapshot=record.get("state_snapshot", {}),
            engrams=record.get("engrams", {}),
            axiom_pressure=record.get("axiom_pressure", 0),
            primitive_saturation=record.get("primitive_saturation", 0),
            drift_status=record.get("drift_status", "✅ stable"),
            token_metrics=record.get("token_metrics", {}),
            assessment_metrics=record.get("assessment_metrics", {}),
            source_files=record.get("source_files", []),
            notes=record.get("notes", ""),
            previous_hash=record["previous_hash"],
        )

        if entry.hash != record["hash"]:
            raise ValueError("Ledger entry integrity failure: entry hash mismatch.")

        return entry
