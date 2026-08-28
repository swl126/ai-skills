#!/usr/bin/env python3
"""Run every embedded skill's self-contained behavioral tests."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    manifest = json.loads((ROOT / "embedded-skills.json").read_text(encoding="utf-8"))
    failures = []
    for entry in manifest["skills"]:
        skill_root = (ROOT / entry["path"]).parent
        test_file = skill_root / "tests/test_validate_report.py"
        result = subprocess.run(
            [sys.executable, str(test_file)],
            cwd=skill_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            failures.append((entry["id"], result.stdout + result.stderr))
            continue
        example = subprocess.run(
            [sys.executable, str(skill_root / "scripts/validate_report.py"), str(skill_root / "examples/example-report.md")],
            cwd=skill_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if example.returncode:
            failures.append((entry["id"], example.stdout + example.stderr))
        else:
            print(f"passed {entry['id']}")
    if failures:
        for skill_id, output in failures:
            print(f"FAILED {skill_id}\n{output}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Embedded behavioral tests passed: {len(manifest['skills'])} skills")


if __name__ == "__main__":
    main()
