# Trust and Maturity Model

Catalog status communicates evidence, not popularity.

| Level | Meaning |
| --- | --- |
| Candidate | Potentially useful, but one or more admission gates remain unresolved |
| Validated | Required structure, licensing, local tests, documentation, and default-branch CI pass |
| Deprecated | Retained for traceability but no longer recommended for new use |

## What validation does prove

- required files and metadata exist;
- declared validation commands pass;
- licensing is internally consistent;
- the published default branch matches the cataloged version;
- required public files remain reachable.
- declared package execution boundaries are present and internally consistent;
- priority domain tools pass controlled positive and negative fixtures;
- evidence envelopes detect artifact tampering;
- the minimal installation archive is reproducible.

## What validation does not prove

- every output produced by an AI agent is correct;
- every platform interprets instructions identically;
- third-party services or dependencies remain available;
- a skill is safe when granted authority beyond its documented scope.
- an evidence digest proves the identity or honesty of its collector;
- normalized-evidence assessors collected or independently verified their inputs.

Users should review instructions and scripts before granting credentials, network access, external-write authority, or destructive capabilities.
