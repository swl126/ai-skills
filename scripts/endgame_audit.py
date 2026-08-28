#!/usr/bin/env python3
"""Run the repository-specific ENDGAME acceptance gates."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")

REQUIRED_PATHS = {
    ".github/CODEOWNERS",
    ".github/workflows/validate.yml",
    ".github/workflows/verify-linked-skills.yml",
    "CHANGELOG.md",
    "ENDGAME.md",
    "ENDGAME.json",
    "LICENSE",
    "README.md",
    "VERSION",
    "catalog.json",
    "endgame/ACCEPTANCE_GATES.md",
    "endgame/TRACEABILITY.md",
    "proposals.json",
    "embedded-skills.json",
    "schema/embedded-skills.schema.json",
    "scripts/validate_embedded_skills.py",
    "schema/endgame.schema.json",
}

PUBLIC_GOVERNANCE = {
    "CANDIDATES.md",
    "ENDGAME.md",
    "README.md",
    "ROADMAP.md",
    "SKILLS.md",
    "endgame/ACCEPTANCE_GATES.md",
    "endgame/TRACEABILITY.md",
}

# Private repository identities must not be disclosed by public governance files.
# Store only non-identifying sentinel patterns here; specific private names do not
# belong in this public repository or its validation source.
FORBIDDEN_PRIVACY_PATTERNS = (
    "private repository audit findings:",
    "private candidate repository:",
)


def fail(errors):
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def markdown_files():
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def main():
    errors = []
    missing = sorted(path for path in REQUIRED_PATHS if not (ROOT / path).is_file())
    if missing:
        errors.append("missing required paths: " + ", ".join(missing))

    if (ROOT / "SKILL.md").exists():
        errors.append("catalog hub must link the canonical ENDGAME skill, not vendor a root SKILL.md")

    catalog = read_json("catalog.json")
    proposals = read_json("proposals.json")
    embedded = read_json("embedded-skills.json")
    ledger = read_json("ENDGAME.json")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    if not SEMVER.fullmatch(version):
        errors.append("VERSION is not semantic versioning")
    if ledger.get("repository_version") != version:
        errors.append("ENDGAME repository_version does not match VERSION")

    canonical = ledger.get("canonical_skill", {})
    if canonical.get("repository") != "https://github.com/swl126/endgame":
        errors.append("canonical ENDGAME repository is incorrect")
    if not SEMVER.fullmatch(canonical.get("version", "")):
        errors.append("canonical ENDGAME version is invalid")
    if not SHA40.fullmatch(canonical.get("commit", "")):
        errors.append("canonical ENDGAME commit must be a full SHA")
    if canonical.get("entrypoint") != "SKILL.md":
        errors.append("canonical ENDGAME entrypoint must be SKILL.md")

    skills = catalog.get("skills", [])
    backlog = proposals.get("proposals", [])
    embedded_skills = embedded.get("skills", [])
    audit = ledger.get("latest_audit", {})
    if len(skills) != audit.get("validated_skill_count"):
        errors.append("validated skill count differs from ENDGAME audit ledger")
    if len(backlog) != audit.get("proposal_count"):
        errors.append("proposal count differs from ENDGAME audit ledger")
    if len(embedded_skills) != audit.get("embedded_skill_count"):
        errors.append("embedded skill count differs from ENDGAME audit ledger")
    if [item.get("id") for item in embedded_skills] != [item.get("id") for item in backlog]:
        errors.append("embedded skills differ from approved proposal provenance")
    test_source = (ROOT / "tests/test_catalog.py").read_text(encoding="utf-8")
    test_count = len(re.findall(r"^\s+def test_", test_source, flags=re.MULTILINE))
    if test_count != audit.get("test_count"):
        errors.append("unit-test count differs from ENDGAME audit ledger")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if f"| Validated skills | {len(skills)} |" not in readme:
        errors.append("README validated-skill count is stale")
    if f"| Approved proposals | {len(backlog)} |" not in readme:
        errors.append("README proposal count is stale")
    if f"| Embedded skills | {len(embedded_skills)} |" not in readme:
        errors.append("README embedded-skill count is stale")

    for markdown in markdown_files():
        text = markdown.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if relative:
                resolved = (markdown.parent / relative).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    errors.append(f"local link escapes repository in {markdown.relative_to(ROOT)}: {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"broken local link in {markdown.relative_to(ROOT)}: {target}")

    for relative in PUBLIC_GOVERNANCE:
        text = (ROOT / relative).read_text(encoding="utf-8").casefold()
        for pattern in FORBIDDEN_PRIVACY_PATTERNS:
            if pattern in text:
                errors.append(f"privacy boundary violation in {relative}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "GNU GENERAL PUBLIC LICENSE" not in license_text:
        errors.append("root LICENSE does not contain GNU GPL text")
    for skill in skills:
        if skill.get("license") != "GPL-3.0-or-later":
            errors.append(f"incompatible catalog license for {skill.get('id')}")

    validate_workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
    if "python3 scripts/endgame_audit.py" not in validate_workflow:
        errors.append("validation workflow does not run ENDGAME audit")
    if "python3 scripts/validate_embedded_skills.py" not in validate_workflow:
        errors.append("validation workflow does not validate embedded skills")

    if errors:
        fail(errors)
    print(
        f"ENDGAME audit passed: {len(skills)} validated releases, "
        f"{len(embedded_skills)} embedded skills"
    )


if __name__ == "__main__":
    main()
