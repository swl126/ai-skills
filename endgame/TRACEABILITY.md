# ENDGAME Traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Add `/ENDGAME` without duplicating the canonical skill | `ENDGAME.md` and pinned canonical source in `ENDGAME.json` | ENDGAME audit checks repository, version, commit, and entrypoint |
| Apply ENDGAME to the repository | Repository-wide acceptance gates and traceability record | `scripts/endgame_audit.py` |
| Ingest proposed skills without other repositories | Twenty complete v1.x packages under `skills/` plus package manifests and `embedded-skills.json` | `scripts/validate_embedded_skills.py`, `scripts/test_embedded_skills.py`, and unit tests |
| Preserve canonical released skills | ENDGAME remains linked and is not duplicated; proposed skills use an explicit embedded distribution | Audit rejects a root `SKILL.md` in the catalog hub |
| Preserve public/private boundary | Generic candidate admission process | Audit scans public governance documents for forbidden private identifiers |
| Test actual outputs | Catalog validator, 80 report-validator cases, 20 worked-report validations, 19 model-evaluation tests, 133 domain-engine tests, unit suite, link audit, JSON parsing, and remote verification | Local commands plus GitHub Actions |
| Make every embedded skill executable | Twenty version 1.1.0 packages with declared CLIs, strict schemas, fixtures, domain profiles, and fail-closed decisions | Package tests plus repository executable-coverage test |
| Prevent stale completion claims | Counts and versions are compared across README, catalogs, VERSION, and ledger | ENDGAME audit |
