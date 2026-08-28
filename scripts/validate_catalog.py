#!/usr/bin/env python3
"""Validate catalog invariants without third-party dependencies."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
PROPOSALS = ROOT / "proposals.json"
REQUIRED = {
    "README.md",
    "SKILLS.md",
    "STANDARD.md",
    "COMPATIBILITY.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "catalog.json",
    "schema/catalog.schema.json",
    "PROPOSED_SKILLS.md",
    "proposals.json",
    "schema/proposals.schema.json",
    "ENDGAME.md",
    "ENDGAME.json",
    "VERSION",
    "CHANGELOG.md",
    "schema/endgame.schema.json",
    "scripts/endgame_audit.py",
    "embedded-skills.json",
    "schema/embedded-skills.schema.json",
    "schema/skill-package.schema.json",
    "scripts/validate_embedded_skills.py",
    "scripts/test_embedded_skills.py",
    "scripts/list_embedded_skills.py",
    "skills/README.md",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    missing = sorted(path for path in REQUIRED if not (ROOT / path).is_file())
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    if data.get("license") != "GPL-3.0-or-later":
        fail("catalog license must be GPL-3.0-or-later")
    if not re.fullmatch(r"\d+\.\d+\.\d+", data.get("catalog_version", "")):
        fail("catalog_version must use semantic versioning")

    skills = data.get("skills")
    if not isinstance(skills, list) or not skills:
        fail("skills must be a non-empty list")

    ids = set()
    repositories = set()
    for skill in skills:
        required = {"id", "name", "repository", "entrypoint", "category", "version", "status", "license", "description", "tags", "install", "validation"}
        absent = sorted(required - set(skill))
        if absent:
            fail(f"skill entry missing fields: {', '.join(absent)}")
        if skill["id"] in ids:
            fail(f"duplicate skill id: {skill['id']}")
        if skill["repository"] in repositories:
            fail(f"duplicate repository: {skill['repository']}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill["id"]):
            fail(f"invalid skill id: {skill['id']}")
        if not skill["repository"].startswith("https://github.com/swl126/"):
            fail(f"repository is outside swl126: {skill['repository']}")
        if skill["entrypoint"] != "SKILL.md":
            fail(f"unsupported entrypoint for {skill['id']}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", skill["version"]):
            fail(f"invalid version for {skill['id']}")
        if skill["license"] != "GPL-3.0-or-later":
            fail(f"invalid license for {skill['id']}")
        if skill["status"] not in {"candidate", "validated", "deprecated"}:
            fail(f"invalid status for {skill['id']}")
        if not isinstance(skill["tags"], list) or not skill["tags"]:
            fail(f"missing tags for {skill['id']}")
        if len(skill["tags"]) != len(set(skill["tags"])):
            fail(f"duplicate tags for {skill['id']}")
        expected_install = f"git clone {skill['repository']}.git"
        if skill["install"] != expected_install:
            fail(f"invalid install command for {skill['id']}")
        ids.add(skill["id"])
        repositories.add(skill["repository"])

    print(f"Catalog valid: {len(skills)} skills")

    proposal_data = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    proposals = proposal_data.get("proposals")
    if not isinstance(proposals, list) or not proposals:
        fail("proposals must be a non-empty list")
    proposal_ids = [item.get("id") for item in proposals]
    if len(proposal_ids) != len(set(proposal_ids)):
        fail("proposal ids must be unique")
    priorities = [item.get("priority") for item in proposals]
    if priorities != list(range(1, len(proposals) + 1)):
        fail("proposal priorities must be contiguous and ordered from 1")
    if ids.intersection(proposal_ids):
        fail("a skill cannot be both cataloged and proposed")
    for proposal in proposals:
        if proposal.get("status") != "proposed":
            fail(f"invalid proposal status for {proposal.get('id')}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", proposal.get("id", "")):
            fail(f"invalid proposal id: {proposal.get('id')}")
    print(f"Proposal backlog valid: {len(proposals)} skills")


if __name__ == "__main__":
    main()
