import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];S=importlib.util.spec_from_file_location("rls",ROOT/"scripts/audit_rls.py");M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
class Tests(unittest.TestCase):
    def test_missing_rls_blocks(self):self.assertEqual(M.audit("CREATE TABLE public.jobs(id int);")["decision"],"BLOCK")
    def test_tenant_policy_passes(self):
        sql="CREATE TABLE jobs(id int); ALTER TABLE jobs ENABLE ROW LEVEL SECURITY; ALTER TABLE jobs FORCE ROW LEVEL SECURITY; CREATE POLICY p ON jobs FOR ALL USING (tenant_id=current_setting('app.tenant')::uuid) WITH CHECK (tenant_id=current_setting('app.tenant')::uuid);"
        self.assertEqual(M.audit(sql)["decision"],"PASS")
    def test_using_true_blocks(self):
        sql="CREATE TABLE jobs(id int); ALTER TABLE jobs ENABLE ROW LEVEL SECURITY; CREATE POLICY p ON jobs FOR SELECT USING (true);"
        self.assertEqual(M.audit(sql)["decision"],"BLOCK")
if __name__=="__main__":unittest.main()
