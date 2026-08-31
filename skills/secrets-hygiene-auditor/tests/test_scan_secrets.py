import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; S=importlib.util.spec_from_file_location("scanner",ROOT/"scripts/scan_secrets.py"); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def test_clean_tree_passes(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d,"app.py").write_text("value = 'safe-placeholder'\n")
            self.assertEqual(M.scan(Path(d))["decision"],"PASS")
    def test_secret_is_redacted_and_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            raw="AKIAABCDEFGHIJKLMNOP"; Path(d,"bad.txt").write_text(raw)
            result=M.scan(Path(d)); self.assertEqual(result["decision"],"BLOCK")
            self.assertNotIn(raw,str(result)); self.assertTrue(result["findings"][0]["redacted"])
if __name__=="__main__": unittest.main()
