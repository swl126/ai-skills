import importlib.util,tempfile,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("dist",ROOT/"scripts/build_distribution.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def test_minimal_archive_is_complete_and_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            a=Path(d,"a.zip");b=Path(d,"b.zip");ra=M.build(a);rb=M.build(b);self.assertEqual(ra["sha256"],rb["sha256"])
            with zipfile.ZipFile(a) as z:names=set(z.namelist())
            self.assertIn("ai-skills-hub/SKILL.md",names);self.assertIn("ai-skills-hub/skills/model-evaluation-harness/SKILL.md",names)
            self.assertFalse(any("/.github/" in x for x in names));self.assertFalse(any("__pycache__" in x for x in names))
if __name__=="__main__":unittest.main()
