#!/usr/bin/env python3
"""Behavioral tests for the local report validator."""

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_report.py"
SPEC = importlib.util.spec_from_file_location("validate_report", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def report(decision: str = "PASS", evidence: bool = True, outcome: str = "PASS — evidence E-1") -> str:
    row = "| E-1 | test fixture v1 | observed result | current | bounded fixture |" if evidence else ""
    return f"""# Report

## Decision summary

- **Decision:** {decision}

## Evidence register

| Evidence ID | Source and version | Observation | Integrity or freshness | Limitation |
| --- | --- | --- | --- | --- |
{row}

## Domain analysis

Observed facts cite E-1.

## Findings and decisions

| ID | Finding | Severity | Evidence | Action | Owner | Due or expiry |
| --- | --- | --- | --- | --- | --- | --- |
| F-1 | bounded fixture | low | E-1 | verify | owner | 2027-01-01 |

## Acceptance review

- {outcome}

## Residual risk and follow-up

Fixture only.
"""


class ReportValidatorTests(unittest.TestCase):
    def test_accepts_decided_evidenced_report(self):
        self.assertEqual([], MODULE.validate(report()))

    def test_rejects_empty_decision(self):
        self.assertIn("decision summary is empty", MODULE.validate(report(decision="")))

    def test_rejects_missing_evidence(self):
        self.assertIn("evidence register has no data row", MODULE.validate(report(evidence=False)))

    def test_rejects_unresolved_acceptance(self):
        errors = MODULE.validate(report(outcome="- [ ] unresolved"))
        self.assertIn("acceptance review contains unchecked items", errors)


if __name__ == "__main__":
    unittest.main()
