# Quickstart

## Find a skill

```bash
python3 scripts/skills.py
python3 scripts/skills.py spreadsheet
python3 scripts/skills.py --status validated --json
```

## Install a skill

```bash
git clone https://github.com/swl126/endgame.git
cd endgame
python3 scripts/validate_skill.py
```

Then place the repository directory in the skill-loading location supported by your agent platform. Keep the entire directory so references, scripts, examples, and metadata remain available.

## Verify the catalog

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/verify_remote.py
```
