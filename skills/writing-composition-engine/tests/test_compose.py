import importlib.util,json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("compose",ROOT/"scripts/compose.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def brief(self):return json.loads((ROOT/"examples/fixtures/brief.json").read_text())
    def test_fixture_composes_and_passes(self):
        draft=M.compose(self.brief());self.assertEqual(M.audit(draft)["decision"],"PASS");self.assertIn("[E-1]",draft)
    def test_unknown_evidence_is_rejected(self):
        data=self.brief();data["sections"][0]["claims"][0]["evidence_ids"]=["E-9"]
        with self.assertRaises(M.ContractError):M.validate_brief(data)
    def test_unknown_field_is_rejected(self):
        data=self.brief();data["typo"]=True
        with self.assertRaises(M.ContractError):M.validate_brief(data)
    def test_placeholder_blocks(self):self.assertEqual(M.audit("# X\n\n## A\n\nTODO\n\n## B\n\nDone.")["decision"],"BLOCK")
    def test_unresolved_citation_blocks(self):
        r=M.audit("# X\n\n## A\n\nClaim [E-9].\n\n## B\n\nConclusion.");self.assertIn("CITATION_UNRESOLVED",{x["code"] for x in r["findings"]})
    def test_unused_source_reviews(self):
        r=M.audit("# X\n\n## A\n\nText.\n\n## B\n\nText two.\n\n## Sources\n\n- [E-1] Source");self.assertEqual(r["decision"],"REVIEW")
    def test_long_paragraph_reviews(self):
        text="# X\n\n## A\n\n"+"word "*181+"\n\n## B\n\nShort.";self.assertEqual(M.audit(text)["decision"],"REVIEW")
    def test_cli_fail_on_block(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d,"audit.json");r=subprocess.run([sys.executable,str(ROOT/"scripts/compose.py"),"audit","--input",str(ROOT/"examples/fixtures/block.md"),"--out",str(out),"--fail-on-block"])
            self.assertEqual(r.returncode,1);self.assertEqual(json.loads(out.read_text())["decision"],"BLOCK")
if __name__=="__main__":unittest.main()
