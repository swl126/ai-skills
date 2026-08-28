#!/usr/bin/env python3
"""Query the AI skills catalog from a terminal or another agent."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_args():
    parser = argparse.ArgumentParser(description="Search the swl126 AI skills catalog")
    parser.add_argument("query", nargs="?", default="", help="text to match")
    parser.add_argument("--category", help="exact category filter")
    parser.add_argument("--status", choices=["candidate", "validated", "deprecated"])
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def select(skills, query="", category=None, status=None):
    needle = query.casefold()
    selected = []
    for skill in skills:
        searchable = " ".join(
            [skill["id"], skill["name"], skill["description"], skill["category"], *skill["tags"]]
        ).casefold()
        if needle and needle not in searchable:
            continue
        if category and skill["category"] != category:
            continue
        if status and skill["status"] != status:
            continue
        selected.append(skill)
    return selected


def main():
    args = parse_args()
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    skills = select(catalog["skills"], args.query, args.category, args.status)
    if args.as_json:
        print(json.dumps(skills, indent=2))
        return
    if not skills:
        print("No matching skills.")
        return
    for skill in skills:
        print(f"{skill['name']} {skill['version']} [{skill['status']}]")
        print(f"  {skill['description']}")
        print(f"  {skill['repository']}")
        print(f"  Install: {skill['install']}")


if __name__ == "__main__":
    main()
