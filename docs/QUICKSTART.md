# Quickstart

## Find a skill

```bash
python3 scripts/skills.py
python3 scripts/skills.py spreadsheet
python3 scripts/skills.py --status validated --json
```

## Install a skill

To ingest all 20 built embedded skills from one clone:

```bash
git clone https://github.com/swl126/ai-skills.git
cd ai-skills
python3 scripts/validate_embedded_skills.py
python3 scripts/test_embedded_skills.py
```

Point the agent's skill loader at `skills/`, or use `embedded-skills.json` to enumerate canonical entrypoints and package manifests.

To install an independently validated release instead:

```bash
git clone https://github.com/swl126/endgame.git
cd endgame
python3 scripts/validate_skill.py
```

Then place the repository directory in the skill-loading location supported by your agent platform. Keep the entire directory so references, scripts, examples, and metadata remain available.

## Verify the catalog

```bash
python3 scripts/validate_catalog.py
python3 scripts/validate_embedded_skills.py
python3 scripts/test_embedded_skills.py
python3 -m unittest discover -s tests -v
python3 scripts/verify_remote.py
```
