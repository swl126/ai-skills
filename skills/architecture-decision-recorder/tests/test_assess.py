#!/usr/bin/env python3
"""Acceptance tests for the normalized-evidence assessment engine."""
import importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("assess",ROOT/"scripts/assess.py")
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
PROFILE=MOD.validate_profile(MOD.load_json(ROOT/"references/engine-profile.json"))
class AssessmentTests(unittest.TestCase):
    def fixture(self,name): return MOD.load_json(ROOT/"examples/fixtures"/name)
    def test_pass_fixture(self): self.assertEqual(MOD.assess(PROFILE,self.fixture("pass.json"))["decision"],"PASS")
    def test_block_fixture(self):
        result=MOD.assess(PROFILE,self.fixture("block.json"))
        self.assertEqual(result["decision"],"BLOCK"); self.assertIn(PROFILE["rules"][0]["id"],{x["code"] for x in result["findings"]})
    def test_missing_category_blocks(self):
        data=self.fixture("pass.json"); data["records"].pop(); self.assertEqual(MOD.assess(PROFILE,data)["decision"],"BLOCK")
    def test_missing_evidence_reference_blocks(self):
        data=self.fixture("pass.json"); data["records"][0]["evidence_ids"]=["absent"]
        self.assertIn("EVIDENCE-MISSING",{x["code"] for x in MOD.assess(PROFILE,data)["findings"]})
    def test_unknown_field_is_rejected(self):
        data=self.fixture("pass.json"); data["typo"]=True
        with self.assertRaises(MOD.ContractError): MOD.validate_assessment(data,PROFILE)
    def test_stale_evidence_requires_review(self):
        data=self.fixture("pass.json"); data["evidence"][0]["age_days"]=PROFILE["max_evidence_age_days"]+1
        self.assertEqual(MOD.assess(PROFILE,data)["decision"],"REVIEW")
    def test_cli_fail_on_block(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/"result.json"
            proc=subprocess.run([sys.executable,str(ROOT/"scripts/assess.py"),"assess","--input",str(ROOT/"examples/fixtures/block.json"),"--out",str(out),"--fail-on-block"],capture_output=True,text=True)
            self.assertEqual(proc.returncode,1); self.assertEqual(json.loads(out.read_text())["decision"],"BLOCK")
if __name__=="__main__": unittest.main()
