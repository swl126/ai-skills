#!/usr/bin/env python3
"""List locally ingestible skills, entrypoints, and package manifests."""

import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--json", action="store_true", help="emit the complete machine-readable skill list")
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "embedded-skills.json").read_text(encoding="utf-8"))
if args.json:
    print(json.dumps(manifest["skills"], indent=2))
else:
    for skill in manifest["skills"]:
        print(
            f"{skill['id']}\t{skill['version']}\t{skill['status']}\t"
            f"{skill['path']}\t{skill['package_path']}"
        )
