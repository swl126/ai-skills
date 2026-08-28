# Embedded Skills

This directory contains 20 self-contained agent skills that can be ingested from one clone of swl126/ai-skills.

Each child directory is an installable unit whose canonical entry point is SKILL.md. The machine-readable index is [embedded-skills.json](../embedded-skills.json).

## Ingest all skills

Point the AI environment's skill loader at this skills directory, or copy its child directories into the environment's configured skill location.

```bash
git clone https://github.com/swl126/ai-skills.git
cd ai-skills
python3 scripts/validate_embedded_skills.py
```

No navigation to another repository is required for these 20 embedded skills. The separately released ENDGAME and Universal Spreadsheet Engine remain linked catalog releases and are not duplicated here.

## Maturity

Embedded version 0.1.0 means the skill has valid structure, task-specific instructions, and repository validation. It has not yet accumulated the independent usage history or separate release evidence required for the externally validated catalog.
