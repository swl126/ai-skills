# ENDGAME Traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Add `/ENDGAME` without duplicating the canonical skill | `ENDGAME.md` and pinned canonical source in `ENDGAME.json` | ENDGAME audit checks repository, version, commit, and entrypoint |
| Apply ENDGAME to the repository | Repository-wide acceptance gates and traceability record | `scripts/endgame_audit.py` |
| Ingest proposed skills without other repositories | Twenty-one complete packages under `skills/` plus package manifests and `embedded-skills.json` | `scripts/validate_embedded_skills.py`, `scripts/test_embedded_skills.py`, and unit tests |
| Preserve canonical released skills | ENDGAME remains linked and is not duplicated; proposed skills use an explicit embedded distribution | Audit rejects a root `SKILL.md` in the catalog hub |
| Preserve public/private boundary | Generic candidate admission process | Audit scans public governance documents for forbidden private identifiers |
| Test actual outputs | Catalog validator, 84 report-validator cases, 21 worked-report validations, 19 model-evaluation tests, 133 assessment-engine tests, 13 priority-domain tests, 8 writing-engine tests, 29 repository tests, link audit, JSON parsing, and remote verification | Local commands plus GitHub Actions |
| Make every embedded skill executable | Twenty-one packages with declared CLIs, strict contracts, fixtures, and fail-closed decisions | Package tests plus repository executable-coverage test |
| Install the super-repository as one skill | Root `SKILL.md` progressively routes to all twenty-one local child packages | Root-router unit test and clean installation smoke test |
| Add writing composition | Evidence-traceable brief, composer, source registry, structural auditor, and report workflow | Twelve package tests plus clean-install execution |
| Replace branded gates with real security tools | Five version 2.0.0 packages collect or analyze primary domain evidence before applying gates | Domain-specific tests executed by the embedded test runner |
| Make evidence tamper-evident | SHA-256 evidence envelope with target, collector, method, and collection time | Round-trip, tamper, and incomplete-identity tests |
| Publish a minimal consumer artifact | Deterministic distribution builder excludes repository administration and caches | Reproducibility and archive-content tests |
| Prevent stale completion claims | Counts and versions are compared across README, catalogs, VERSION, and ledger | ENDGAME audit |
