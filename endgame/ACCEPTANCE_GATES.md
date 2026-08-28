# Repository Acceptance Gates

| Gate | Passing evidence |
| --- | --- |
| Catalog valid | `scripts/validate_catalog.py` exits successfully |
| Proposal backlog valid | Exactly 20 unique, ordered proposals with no released-skill collisions |
| Embedded skills valid | Exactly 20 manifest-aligned, self-contained skill packages pass structural and content validation |
| Embedded behavioral tests pass | All 20 report validators pass four positive/negative unit cases and one complete worked report each |
| Unit tests pass | Test discovery exits successfully and the ledger count matches the suite |
| Local links resolve | Every relative Markdown link targets an existing repository path |
| License consistent | Root license contains GNU GPL text and released catalog entries declare GPL-3.0-or-later |
| Privacy preserved | Public governance files do not enumerate private repository names or private audit findings |
| Workflows present | Catalog validation and linked-skill verification workflows exist |
| ENDGAME pinned | Canonical repository, semantic version, and 40-character source commit are recorded |
| Version consistent | Root `VERSION` matches the ENDGAME ledger repository version |
| Remote verification passes | Required files and versions in linked public repositories are reachable and consistent |

Completion requires every local gate plus remote verification. A network failure is a blocker, not a passing result.
