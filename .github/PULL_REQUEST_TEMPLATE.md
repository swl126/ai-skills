## Summary

Describe the catalog or standard change.

## Validation

- [ ] `python3 scripts/validate_catalog.py` passes
- [ ] `python3 scripts/validate_embedded_skills.py` passes
- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] `python3 scripts/endgame_audit.py` passes for substantial or release-affecting changes
- [ ] Linked skill repository passes its own validation
- [ ] Licensing and documentation are consistent
- [ ] No credentials, private data, or generated caches are included
- [ ] `ENDGAME.json` and traceability evidence are updated when catalog counts, versions, or acceptance results change
