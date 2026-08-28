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

## Admission queue

The following repositories are not cataloged as validated until they are public, standardized, licensed, and tested:

- `swl126/paper-to-skill`
- `swl126/citation-to-formatter`

Their omission is deliberate and is not a judgment about their usefulness.
