# Contributing

## Add a skill

1. Publish the skill in its own public repository.
2. Conform it to [STANDARD.md](STANDARD.md).
3. Add one entry to `catalog.json` and one human-readable entry to `SKILLS.md`.
4. Run `python3 scripts/validate_catalog.py`.
5. Open a pull request using the supplied template.

## Acceptance requirements

- the repository is controlled by or intentionally accepted into this catalog;
- the skill solves a defined task rather than offering vague prompting advice;
- instructions disclose important assumptions and failure conditions;
- validation is reproducible;
- the license is GPL-3.0-or-later;
- links and catalog metadata are accurate.

Catalog changes should not silently alter the linked skill. Modify the individual skill repository first, validate it, and then update its catalog entry.
