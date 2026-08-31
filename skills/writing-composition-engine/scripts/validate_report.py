#!/usr/bin/env python3
"""Validate a completed writing-composition-engine Markdown report."""
import re,sys
from pathlib import Path
SKILL_ID="writing-composition-engine"
HEADINGS=("## Decision summary","## Evidence register","## Domain analysis","## Findings and decisions","## Acceptance review","## Residual risk and follow-up")
def section(text,start,end):
    if start not in text:return ""
    body=text.split(start,1)[1];return body.split(end,1)[0] if end in body else body
def validate(text):
    errors=[f"missing heading: {x}" for x in HEADINGS if x not in text]
    decision=re.search(r"^- \*\*Decision:\*\*[ \t]*([^\n]*)$",text,re.M)
    if not decision or not decision.group(1).strip():errors.append("decision summary is empty")
    evidence=section(text,"## Evidence register","## Domain analysis")
    rows=[x for x in evidence.splitlines() if x.startswith("|") and "---" not in x and "Evidence ID" not in x and x.count("|")>=5]
    if not rows:errors.append("evidence register has no data row")
    acceptance=section(text,"## Acceptance review","## Residual risk and follow-up")
    if "- [ ]" in acceptance:errors.append("acceptance review contains unchecked items")
    if not any(x in acceptance.upper() for x in ("PASS","FAIL","BLOCKED","NOT APPLICABLE")):errors.append("acceptance review has no recorded outcome")
    if re.search(r"\b(?:TODO|TBD|replace-with)\b",text,re.I):errors.append("report contains an unfinished marker")
    return errors
def main():
    if len(sys.argv)!=2:raise SystemExit(f"usage: {Path(sys.argv[0]).name} REPORT.md")
    p=Path(sys.argv[1]);errors=validate(p.read_text())
    if errors:
        for x in errors:print(f"ERROR: {x}",file=sys.stderr)
        raise SystemExit(1)
    print(f"{SKILL_ID} report valid")
if __name__=="__main__":main()
