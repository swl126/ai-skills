import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("env",ROOT/"scripts/evidence_envelope.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d,"evidence.json");p.write_text('{"ok":true}')
            e=M.create(p,"target","1","test","collector","1","offline");M.verify(e,p)
    def test_tamper_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d,"evidence.json");p.write_text("before");e=M.create(p,"target","1","test","collector","1","offline");p.write_text("after")
            with self.assertRaises(ValueError):M.verify(e,p)
    def test_identity_is_required(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d,"evidence.json");p.write_text("x");e=M.create(p,"target","1","test","collector","1","offline");e["collector"]["id"]=""
            with self.assertRaises(ValueError):M.verify(e,p)
if __name__=="__main__":unittest.main()
