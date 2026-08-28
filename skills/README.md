# Embedded Skills

This directory contains 20 self-contained agent skills that can be ingested from one clone of swl126/ai-skills.

Each child directory is an installable unit whose canonical entry point is SKILL.md. The machine-readable index is [embedded-skills.json](../embedded-skills.json).

## Ingest all skills

Point the AI environment's skill loader at this skills directory, or copy its child directories into the environment's configured skill location.

```bash
git clone https://github.com/swl126/ai-skills.git
cd ai-skills
python3 scripts/validate_embedded_skills.py
python3 scripts/test_embedded_skills.py
```

No navigation to another repository is required for these 20 embedded skills. The separately released ENDGAME and Universal Spreadsheet Engine remain linked catalog releases and are not duplicated here.

## Package anatomy

Each skill contains:

- `SKILL.md` — the canonical routing and workflow entrypoint;
- `references/playbook.md` — domain modes, evidence rules, failure modes, and acceptance checks;
- `assets/report-template.md` — a reusable evidence-backed deliverable;
- `examples/` — a realistic request, calibrated decision excerpt, and validator-clean worked report;
- `agents/openai.yaml` — discovery and invocation metadata;
- `scripts/validate_report.py` — deterministic completed-report validation;
- `tests/test_validate_report.py` — four behavioral regression tests;
- `skill-package.json` — machine-readable package identity and resource map.

## Maturity

Embedded version 1.0.0 means the package is operationally complete, self-contained, structurally validated, and covered by repository and package-level behavioral tests. It has not yet accumulated the independent usage history or separate release evidence required for the externally validated catalog.
