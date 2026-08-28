#!/usr/bin/env python3
"""Validate a completed api-contract-auditor Markdown report."""

import re
import sys
from pathlib import Path

SKILL_ID = "api-contract-auditor"
REQUIRED_HEADINGS = (
    "## Decision summary",
    "## Evidence register",
    "## Domain analysis",
    "## Findings and decisions",
    "## Acceptance review",
    "## Residual risk and follow-up",
)
OUTCOMES = ("PASS", "FAIL", "BLOCKED", "NOT APPLICABLE")


def validate(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing heading: {heading}")

    decision = re.search(r"^- \*\*Decision:\*\*[ \t]*([^\n]*)$", text, re.MULTILINE)
    if not decision or not decision.group(1).strip():
        errors.append("decision summary is empty")

    evidence = section(text, "## Evidence register", "## Domain analysis")
    data_rows = [
        line for line in evidence.splitlines()
        if line.startswith("|")
        and "---" not in line
        and "Evidence ID" not in line
        and line.count("|") >= 5
    ]
    if not data_rows:
        errors.append("evidence register has no data row")

    acceptance = section(text, "## Acceptance review", "## Residual risk and follow-up")
    if "- [ ]" in acceptance:
        errors.append("acceptance review contains unchecked items")
    if not any(outcome in acceptance.upper() for outcome in OUTCOMES):
        errors.append("acceptance review has no recorded outcome")

    if re.search(r"\b(?:TODO|TBD|replace-with)\b", text, re.IGNORECASE):
        errors.append("report contains an unfinished marker")
    return errors


def section(text: str, start: str, end: str) -> str:
    if start not in text:
        return ""
    body = text.split(start, 1)[1]
    return body.split(end, 1)[0] if end in body else body


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} REPORT.md")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"report not found: {path}")
    errors = validate(path.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"{SKILL_ID} report valid")


if __name__ == "__main__":
    main()
