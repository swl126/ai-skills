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


if __name__ == "__main__":
    unittest.main()
