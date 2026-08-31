import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("dep",ROOT/"scripts/triage_dependencies.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
SB={"components":[{"purl":"pkg:pypi/demo@1.0"}]}
class Tests(unittest.TestCase):
    def test_unmatched_advisory_passes(self):self.assertEqual(M.triage(SB,[{"id":"X","purl":"pkg:pypi/other@1","severity":"critical"}])["decision"],"PASS")
    def test_reachable_critical_blocks(self):
        r=M.triage(SB,[{"id":"CVE-X","purl":"pkg:pypi/demo@1.0","severity":"critical","reachable":True}]);self.assertEqual(r["decision"],"BLOCK")
    def test_noncritical_requires_review(self):
        self.assertEqual(M.triage(SB,[{"id":"CVE-M","purl":"pkg:pypi/demo@1.0","severity":"medium"}])["decision"],"REVIEW")
if __name__=="__main__":unittest.main()
