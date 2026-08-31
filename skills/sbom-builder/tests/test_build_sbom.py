import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("sbom",ROOT/"scripts/build_sbom.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def test_python_and_npm_are_resolved(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/"requirements.txt").write_text("requests==2.32.3\n")
            (p/"package-lock.json").write_text('{"packages":{"node_modules/lodash":{"version":"4.17.21"}}}')
            b=M.build(p,"demo","1.0.0");self.assertEqual(len(b["components"]),2);self.assertEqual(b["bomFormat"],"CycloneDX")
    def test_unpinned_python_is_not_invented(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/"requirements.txt").write_text("requests>=2\n");self.assertEqual(M.build(p,"x","1")["components"],[])
if __name__=="__main__":unittest.main()
