import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("api",ROOT/"scripts/audit_openapi.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
BASE={"paths":{"/users":{"get":{"responses":{"200":{}}}}},"components":{"schemas":{"User":{"properties":{"id":{"type":"string"}}}}}}
class Tests(unittest.TestCase):
    def test_identical_passes(self):self.assertEqual(M.audit(BASE,BASE)["decision"],"PASS")
    def test_removed_path_blocks(self):self.assertEqual(M.audit(BASE,{"paths":{},"components":{"schemas":{}}})["decision"],"BLOCK")
    def test_new_required_parameter_blocks(self):
        new={"paths":{"/users":{"get":{"parameters":[{"in":"query","name":"tenant","required":True}],"responses":{"200":{}}}}},"components":BASE["components"]}
        self.assertIn("REQUIRED_PARAMETER_ADDED",{x["code"] for x in M.audit(BASE,new)["findings"]})
if __name__=="__main__":unittest.main()
