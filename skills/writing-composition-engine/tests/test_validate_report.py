import importlib.util,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts/validate_report.py";S=importlib.util.spec_from_file_location("v",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def report(decision="PASS",row=True,outcome="PASS"):
    data="| E-1 | source | claim | verified | bounded |" if row else ""
    return f"""# Review

## Decision summary

- **Decision:** {decision}

## Evidence register

| Evidence ID | Source | Claim | Verification | Limitation |
| --- | --- | --- | --- | --- |
{data}

## Domain analysis

Analysis.

## Findings and decisions

Finding.

## Acceptance review

- {outcome}

## Residual risk and follow-up

Risk.
"""
class Tests(unittest.TestCase):
    def test_accepts(self):self.assertEqual(M.validate(report()),[])
    def test_empty_decision(self):self.assertIn("decision summary is empty",M.validate(report(decision="")))
    def test_missing_evidence(self):self.assertIn("evidence register has no data row",M.validate(report(row=False)))
    def test_unresolved(self):self.assertIn("acceptance review contains unchecked items",M.validate(report(outcome="- [ ] unresolved")))
if __name__=="__main__":unittest.main()
