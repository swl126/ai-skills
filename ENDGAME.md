# ENDGAME Governance Profile

This repository uses [ENDGAME](https://github.com/swl126/endgame) as its high-rigor maintenance and release discipline.

The canonical skill remains in its own repository. This hub does not copy or fork `SKILL.md`; it pins the governing version and source commit in [`ENDGAME.json`](ENDGAME.json), records repository-specific gates here, and implements those gates through [`scripts/endgame_audit.py`](scripts/endgame_audit.py).

## Activation

Apply this profile when a maintainer invokes `/ENDGAME`, requests a release, changes the catalog contract, admits or removes a skill, changes validation behavior, or makes another substantial repository-wide change.

Routine typo corrections may use the normal validation workflow without the full evidence record.

## Repository workflow

1. **INTENT** — state the requested repository outcome and non-negotiable constraints.
2. **CONTEXT** — inspect the current default branch, catalog, proposals, standards, workflows, and relevant linked repositories.
3. **DECOMPOSE** — separate documentation, machine metadata, validation, security, and publication work.
4. **ASSUMPTIONS** — identify repository visibility, licensing, platform, branch, and external-access assumptions.
5. **ACCEPTANCE GATES** — use [`endgame/ACCEPTANCE_GATES.md`](endgame/ACCEPTANCE_GATES.md).
6. **BUILD** — make the smallest complete set of changes.
7. **TEST** — run the commands below against the actual repository.
8. **SPEC-CHECK** — compare results with the request and traceability record.
9. **ATTACK** — inspect for false validation claims, private-data disclosure, broken links, stale versions, unsafe automation, and incomplete artifacts.
10. **COMPLETE** — publish only when every required gate passes or record the precise blocker.

## Required commands

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/endgame_audit.py
python3 scripts/verify_remote.py
```

The remote check requires network access. Local structural and test gates must still run when the network is unavailable, and the remote gate must remain explicitly unresolved rather than silently skipped.

## Evidence

- [`ENDGAME.json`](ENDGAME.json) records the canonical source, profile version, gates, and most recent audited state.
- [`endgame/TRACEABILITY.md`](endgame/TRACEABILITY.md) connects user intent to implementation and verification.
- GitHub Actions provides independent default-branch execution evidence.
