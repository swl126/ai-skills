# Executable composition contract

The dependency-free engine accepts a strict JSON brief defined by `schemas/composition-brief.schema.json`. It creates Markdown without inventing prose beyond the supplied paragraphs and claims, then audits the result.

## Commands

```bash
python3 scripts/compose.py compose --brief examples/fixtures/brief.json --out draft.md --audit audit.json
python3 scripts/compose.py audit --input draft.md --out audit.json --fail-on-block
python3 tests/test_compose.py
```

Audit decisions are `PASS`, `REVIEW`, or `BLOCK`. Unresolved citations, unfinished markers, missing titles, or missing substantive sections block. Excessive paragraph length, repeated sentences, and unused registered sources require review.
