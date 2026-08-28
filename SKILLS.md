# Skill Catalog

## ENDGAME

- Repository: <https://github.com/swl126/endgame>
- Entry point: `SKILL.md`
- Category: orchestration and verification
- Use when: work is substantial, multi-stage, consequential, or easy to leave partially complete
- Core behavior: routes only necessary modules, defines acceptance gates, builds, tests, adversarially reviews, and proves completion
- Validation: `python3 scripts/validate_skill.py`
- Status: validated

## Universal Spreadsheet Engine

- Repository: <https://github.com/swl126/Spreadsheet_runner>
- Entry point: `SKILL.md`
- Category: spreadsheets and reproducible computation
- Use when: an agent must create, modify, validate, or reproduce spreadsheet work with Python or R
- Core behavior: separates workbook intent from deterministic recipe execution and validation
- Validation: `python3 -m unittest discover -s tests -v`
- Status: validated

## Admission policy

Only public repositories that satisfy [STANDARD.md](STANDARD.md) appear in this released-skill catalog. Planned capabilities are tracked separately in [PROPOSED_SKILLS.md](PROPOSED_SKILLS.md).
