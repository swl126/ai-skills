#!/usr/bin/env python3
"""Verify that cataloged GitHub repositories expose their required public files."""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("SKILL.md", "README.md", "LICENSE", "VERSION")


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "swl126-ai-skills-validator"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def main():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    failures = []
    for skill in catalog["skills"]:
        slug = skill["repository"].removeprefix("https://github.com/")
        for path in REQUIRED:
            url = f"https://raw.githubusercontent.com/{slug}/main/{path}"
            try:
                content = fetch(url)
            except (urllib.error.URLError, TimeoutError) as exc:
                failures.append(f"{skill['id']}: cannot fetch {path}: {exc}")
                continue
            if not content.strip():
                failures.append(f"{skill['id']}: empty {path}")
            if path == "VERSION" and content.strip() != skill["version"]:
                failures.append(
                    f"{skill['id']}: catalog version {skill['version']} != repository {content.strip()}"
                )
            if path == "LICENSE" and "GNU GENERAL PUBLIC LICENSE" not in content:
                failures.append(f"{skill['id']}: LICENSE is not GNU GPL text")
        print(f"checked {skill['id']}")
    if failures:
        print("\n".join(f"ERROR: {item}" for item in failures), file=sys.stderr)
        raise SystemExit(1)
    print(f"Remote verification passed: {len(catalog['skills'])} skills")


if __name__ == "__main__":
    main()
