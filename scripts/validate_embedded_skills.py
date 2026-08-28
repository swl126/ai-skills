#!/usr/bin/env python3
"""Validate embedded skills against their manifest and proposal provenance."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "embedded-skills.json"
PROPOSALS = ROOT / "proposals.json"
FRONTMATTER = re.compile(r"^---\n(?P<meta>.*?)\n---\n", re.DOTALL)
REQUIRED_HEADINGS = (
    "## Purpose",
    "## Required inputs",
    "## Workflow",
    "## Output contract",
    "## Safety and authority",
)
UNFINISHED = ("TODO", "TBD", "replace-with", "<skill-name>")


def fail(errors):
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def field(meta, name):
    match = re.search(rf"^\s*{re.escape(name)}:\s*(.+?)\s*$", meta, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    proposals = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    entries = manifest.get("skills", [])
    errors = []

    if len(entries) != 20:
        errors.append(f"expected 20 embedded skills, found {len(entries)}")
    ids = [entry.get("id") for entry in entries]
    if len(ids) != len(set(ids)):
        errors.append("embedded skill ids are not unique")
    proposal_ids = [entry.get("id") for entry in proposals.get("proposals", [])]
    if ids != proposal_ids:
        errors.append("embedded manifest order or ids differ from proposal provenance")

    for entry in entries:
        skill_id = entry.get("id", "")
        expected_path = f"skills/{skill_id}/SKILL.md"
        if entry.get("path") != expected_path:
            errors.append(f"{skill_id}: manifest path is not canonical")
            continue
        path = ROOT / expected_path
        if not path.is_file():
            errors.append(f"{skill_id}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            errors.append(f"{skill_id}: invalid YAML frontmatter boundary")
            continue
        meta = match.group("meta")
        if field(meta, "name") != skill_id:
            errors.append(f"{skill_id}: frontmatter name mismatch")
        description = field(meta, "description")
        if not description or len(description) < 80:
            errors.append(f"{skill_id}: description is not discriminating enough")
        version = field(meta, "version")
        if version != entry.get("version"):
            errors.append(f"{skill_id}: version differs from manifest")
        if field(meta, "distribution") != "embedded":
            errors.append(f"{skill_id}: distribution must be embedded")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{skill_id}: missing {heading}")
        if len(re.findall(r"^\d+\. ", text, re.MULTILINE)) < 5:
            errors.append(f"{skill_id}: workflow has fewer than five operational steps")
        for marker in UNFINISHED:
            if marker.casefold() in text.casefold():
                errors.append(f"{skill_id}: unfinished scaffold marker {marker}")

    discovered = sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))
    if discovered != sorted(ids):
        errors.append("manifest and embedded skill directories differ")

    if errors:
        fail(errors)
    print(f"Embedded skills valid: {len(entries)}")


if __name__ == "__main__":
    main()
