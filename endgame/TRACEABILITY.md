# ENDGAME Traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Add `/ENDGAME` without duplicating the canonical skill | `ENDGAME.md` and pinned canonical source in `ENDGAME.json` | ENDGAME audit checks repository, version, commit, and entrypoint |
| Apply ENDGAME to the repository | Repository-wide acceptance gates and traceability record | `scripts/endgame_audit.py` |
| Preserve separate skill repositories | Canonical ENDGAME remains linked, not vendored | Audit rejects a root `SKILL.md` in the catalog hub |
| Preserve public/private boundary | Generic candidate admission process | Audit scans public governance documents for forbidden private identifiers |
| Test actual outputs | Catalog validator, unit suite, link audit, JSON parsing, and remote verification | Local commands plus GitHub Actions |
| Prevent stale completion claims | Counts and versions are compared across README, catalogs, VERSION, and ledger | ENDGAME audit |
