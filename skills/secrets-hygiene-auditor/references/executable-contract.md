# Secrets Hygiene Engine executable contract

This package includes a dependency-free assessment engine at `scripts/assess.py`. It evaluates normalized, user-supplied evidence; it does not connect to or mutate production systems.

## Boundary

The engine requires evidence records for these categories: `repository`, `history`, `ci`, `logs`, `rotation`, `revocation`. Domain thresholds live in `engine-profile.json`, and the input shape is defined by `../schemas/assessment.schema.json`.

## Commands

```bash
python3 scripts/assess.py validate --input examples/fixtures/pass.json
python3 scripts/assess.py assess --input examples/fixtures/pass.json --out result.json --report report.md
python3 scripts/assess.py assess --input examples/fixtures/block.json --out result.json --fail-on-block
python3 tests/test_assess.py
```

Decisions are `PASS`, `REVIEW`, or `BLOCK`. Missing categories, missing evidence references, unverified evidence, and failed high-severity rules cannot produce a pass. Output includes canonical SHA-256 hashes for the profile and assessment.
+## Primary evidence collector

`python3 scripts/scan_secrets.py AUTHORIZED_ROOT --out findings.json --fail-on-findings` scans bounded local text files, skips common dependency/VCS directories, and emits only rule IDs, locations, and irreversible fingerprints. It never prints matched values. Heuristic findings require provider-aware confirmation before revocation.
