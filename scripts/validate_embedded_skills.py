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
REQUIRED_PACKAGE_FILES = (
    "agents/openai.yaml",
    "references/playbook.md",
    "assets/report-template.md",
    "examples/request.md",
    "examples/expected-output.md",
    "examples/example-report.md",
    "scripts/validate_report.py",
    "tests/test_validate_report.py",
)
EXPECTED_RESOURCES = {
    "playbook": "references/playbook.md",
    "report_template": "assets/report-template.md",
    "example_request": "examples/request.md",
    "example_output": "examples/expected-output.md",
    "example_report": "examples/example-report.md",
    "agent_metadata": "agents/openai.yaml",
}
EXPECTED_VALIDATION = {
    "command": "python3 scripts/validate_report.py REPORT.md",
    "test_command": "python3 tests/test_validate_report.py",
}
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

    if manifest.get("manifest_version") != "2.0.0":
        errors.append("embedded manifest version must be 2.0.0")
    if manifest.get("distribution") != "embedded":
        errors.append("embedded manifest distribution mismatch")
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
        expected_package_path = f"skills/{skill_id}/skill-package.json"
        if entry.get("path") != expected_path:
            errors.append(f"{skill_id}: manifest path is not canonical")
            continue
        if entry.get("package_path") != expected_package_path:
            errors.append(f"{skill_id}: package manifest path is not canonical")
        if entry.get("status") != "built":
            errors.append(f"{skill_id}: status must be built")
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

        skill_root = path.parent
        package_path = ROOT / expected_package_path
        if not package_path.is_file():
            errors.append(f"{skill_id}: missing skill-package.json")
            continue
        package = json.loads(package_path.read_text(encoding="utf-8"))
        if package.get("id") != skill_id or package.get("version") != version:
            errors.append(f"{skill_id}: package identity or version mismatch")
        if package.get("distribution") != "embedded":
            errors.append(f"{skill_id}: package distribution mismatch")
        if package.get("license") != "GPL-3.0-or-later":
            errors.append(f"{skill_id}: package license mismatch")
        if package.get("entrypoint") != "SKILL.md":
            errors.append(f"{skill_id}: package entrypoint mismatch")
        if package.get("resources") != EXPECTED_RESOURCES:
            errors.append(f"{skill_id}: package resource map mismatch")
        if package.get("validation") != EXPECTED_VALIDATION:
            errors.append(f"{skill_id}: package validation commands mismatch")
        for relative in REQUIRED_PACKAGE_FILES:
            resource = skill_root / relative
            if not resource.is_file():
                errors.append(f"{skill_id}: missing package resource {relative}")
        resources = package.get("resources", {})
        for relative in resources.values():
            if not (skill_root / relative).is_file():
                errors.append(f"{skill_id}: declared resource is missing: {relative}")
        expected_files = {"SKILL.md", "skill-package.json", *REQUIRED_PACKAGE_FILES}
        actual_files = {
            file.relative_to(skill_root).as_posix()
            for file in skill_root.rglob("*")
            if file.is_file() and "__pycache__" not in file.parts
        }
        if actual_files != expected_files:
            missing = sorted(expected_files - actual_files)
            unexpected = sorted(actual_files - expected_files)
            errors.append(
                f"{skill_id}: package file set mismatch; missing={missing}, unexpected={unexpected}"
            )
        for relative in ("references/playbook.md", "assets/report-template.md"):
            if relative not in text:
                errors.append(f"{skill_id}: SKILL.md does not route to {relative}")
        agent_yaml = (skill_root / "agents/openai.yaml").read_text(encoding="utf-8")
        if f"${skill_id}" not in agent_yaml:
            errors.append(f"{skill_id}: default prompt does not invoke the skill")
        report_template = (skill_root / "assets/report-template.md").read_text(encoding="utf-8")
        for heading in ("## Decision summary", "## Evidence register", "## Acceptance review"):
            if heading not in report_template:
                errors.append(f"{skill_id}: report template missing {heading}")

    discovered = sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))
    if discovered != sorted(ids):
        errors.append("manifest and embedded skill directories differ")

    if errors:
        fail(errors)
    print(f"Embedded skills valid: {len(entries)}")


if __name__ == "__main__":
    main()
