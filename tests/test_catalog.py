import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))

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


if __name__ == "__main__":
    unittest.main()
