#!/usr/bin/env python3
"""List locally ingestible skills and their canonical paths."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "embedded-skills.json").read_text(encoding="utf-8"))
for skill in manifest["skills"]:
    print(f"{skill['id']}\t{skill['version']}\t{skill['path']}")
