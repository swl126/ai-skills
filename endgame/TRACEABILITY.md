# ENDGAME Traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Add `/ENDGAME` without duplicating the canonical skill | `ENDGAME.md` and pinned canonical source in `ENDGAME.json` | ENDGAME audit checks repository, version, commit, and entrypoint |
| Apply ENDGAME to the repository | Repository-wide acceptance gates and traceability record | `scripts/endgame_audit.py` |
| Ingest proposed skills without other repositories | Twenty complete v1.0.0 packages under `skills/` plus package manifests and `embedded-skills.json` | `scripts/validate_embedded_skills.py`, `scripts/test_embedded_skills.py`, and unit tests |
| Preserve canonical released skills | ENDGAME remains linked and is not duplicated; proposed skills use an explicit embedded distribution | Audit rejects a root `SKILL.md` in the catalog hub |
| Preserve public/private boundary | Generic candidate admission process | Audit scans public governance documents for forbidden private identifiers |
| Test actual outputs | Catalog validator, 80 package behavioral cases, 20 worked-report validations, unit suite, link audit, JSON parsing, and remote verification | Local commands plus GitHub Actions |
| Prevent stale completion claims | Counts and versions are compared across README, catalogs, VERSION, and ledger | ENDGAME audit |
