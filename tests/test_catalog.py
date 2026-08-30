import json
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skills import select


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        cls.proposals = json.loads((ROOT / "proposals.json").read_text(encoding="utf-8"))
        cls.endgame = json.loads((ROOT / "ENDGAME.json").read_text(encoding="utf-8"))
        cls.embedded = json.loads((ROOT / "embedded-skills.json").read_text(encoding="utf-8"))

    def test_ids_are_unique(self):
        ids = [skill["id"] for skill in self.catalog["skills"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_repositories_are_unique(self):
        repos = [skill["repository"] for skill in self.catalog["skills"]]
        self.assertEqual(len(repos), len(set(repos)))

    def test_validated_skills_use_required_license(self):
        for skill in self.catalog["skills"]:
            if skill["status"] == "validated":
                self.assertEqual(skill["license"], "GPL-3.0-or-later")

    def test_versions_use_semver(self):
        for skill in self.catalog["skills"]:
            self.assertRegex(skill["version"], r"^\d+\.\d+\.\d+$")

    def test_search_matches_tags(self):
        matches = select(self.catalog["skills"], query="python")
        self.assertEqual([item["id"] for item in matches], ["universal-spreadsheet-engine"])

    def test_status_filter(self):
        matches = select(self.catalog["skills"], status="validated")
        self.assertEqual(len(matches), len(self.catalog["skills"]))

    def test_twenty_proposals_are_registered(self):
        self.assertEqual(len(self.proposals["proposals"]), 20)

    def test_proposals_do_not_duplicate_catalog(self):
        catalog_ids = {item["id"] for item in self.catalog["skills"]}
        proposal_ids = {item["id"] for item in self.proposals["proposals"]}
        self.assertFalse(catalog_ids & proposal_ids)

    def test_proposal_priorities_are_contiguous(self):
        priorities = [item["priority"] for item in self.proposals["proposals"]]
        self.assertEqual(priorities, list(range(1, 21)))

    def test_endgame_canonical_source_is_pinned(self):
        source = self.endgame["canonical_skill"]
        self.assertEqual(source["repository"], "https://github.com/swl126/endgame")
        self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
        self.assertEqual(source["entrypoint"], "SKILL.md")

    def test_endgame_counts_match_catalogs(self):
        audit = self.endgame["latest_audit"]
        self.assertEqual(audit["validated_skill_count"], len(self.catalog["skills"]))
        self.assertEqual(audit["proposal_count"], len(self.proposals["proposals"]))

    def test_repository_version_matches_endgame_ledger(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, self.endgame["repository_version"])

    def test_endgame_test_count_matches_suite(self):
        source = (ROOT / "tests/test_catalog.py").read_text(encoding="utf-8")
        count = len(__import__("re").findall(r"^\s+def test_", source, flags=__import__("re").MULTILINE))
        self.assertEqual(count, self.endgame["latest_audit"]["test_count"])

    def test_twenty_embedded_skills_are_installed(self):
        self.assertEqual(len(self.embedded["skills"]), 20)

    def test_embedded_ids_match_proposals(self):
        embedded_ids = [item["id"] for item in self.embedded["skills"]]
        proposal_ids = [item["id"] for item in self.proposals["proposals"]]
        self.assertEqual(embedded_ids, proposal_ids)

    def test_embedded_paths_exist(self):
        for item in self.embedded["skills"]:
            self.assertTrue((ROOT / item["path"]).is_file(), item["path"])

    def test_embedded_frontmatter_names_match(self):
        for item in self.embedded["skills"]:
            text = (ROOT / item["path"]).read_text(encoding="utf-8")
            self.assertIn(f"name: {item['id']}\n", text)

    def test_embedded_skills_are_built_version_one_packages(self):
        for item in self.embedded["skills"]:
            self.assertEqual(item["status"], "built")
            self.assertRegex(item["version"], r"^1\.\d+\.\d+$")

    def test_model_evaluation_harness_is_executable_gold_standard(self):
        item = next(skill for skill in self.embedded["skills"] if skill["id"] == "model-evaluation-harness")
        self.assertEqual(item["version"], "1.1.0")
        package_path = ROOT / item["package_path"]
        package = json.loads(package_path.read_text(encoding="utf-8"))
        extensions = package["extensions"]
        self.assertTrue((package_path.parent / extensions["executable"]).is_file())
        self.assertTrue((package_path.parent / extensions["test"]).is_file())

    def test_all_embedded_skills_have_executable_engines(self):
        for item in self.embedded["skills"]:
            self.assertEqual(item["version"], "1.1.0")
            package_path = ROOT / item["package_path"]
            package = json.loads(package_path.read_text(encoding="utf-8"))
            extensions = package["extensions"]
            for key in ("executable", "test", "reference"):
                self.assertTrue(
                    (package_path.parent / extensions[key]).is_file(),
                    f"{item['id']}: {key}",
                )
            if item["id"] != "model-evaluation-harness":
                self.assertTrue((package_path.parent / extensions["profile"]).is_file())
                self.assertEqual(len(extensions["schemas"]), 1)
                self.assertEqual(len(extensions["fixtures"]), 2)

    def test_repository_root_is_an_installable_router(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: ai-skills-hub\n", text)
        self.assertIn("embedded-skills.json", text)
        for item in self.embedded["skills"]:
            self.assertIn(item["path"], text)

    def test_embedded_package_manifests_match_index(self):
        for item in self.embedded["skills"]:
            package = json.loads((ROOT / item["package_path"]).read_text(encoding="utf-8"))
            self.assertEqual(package["id"], item["id"])
            self.assertEqual(package["version"], item["version"])
            self.assertEqual(package["license"], "GPL-3.0-or-later")

    def test_embedded_package_resources_resolve(self):
        for item in self.embedded["skills"]:
            package_path = ROOT / item["package_path"]
            package = json.loads(package_path.read_text(encoding="utf-8"))
            for relative in package["resources"].values():
                self.assertTrue((package_path.parent / relative).is_file(), f"{item['id']}: {relative}")

    def test_embedded_agent_prompts_invoke_their_skill(self):
        for item in self.embedded["skills"]:
            skill_root = (ROOT / item["path"]).parent
            metadata = (skill_root / "agents/openai.yaml").read_text(encoding="utf-8")
            self.assertIn(f"${item['id']}", metadata)

    def test_embedded_entrypoints_route_to_local_resources(self):
        for item in self.embedded["skills"]:
            text = (ROOT / item["path"]).read_text(encoding="utf-8")
            self.assertIn("references/playbook.md", text)
            self.assertIn("assets/report-template.md", text)


if __name__ == "__main__":
    unittest.main()
