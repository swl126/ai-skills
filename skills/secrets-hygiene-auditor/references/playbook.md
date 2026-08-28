# Operational playbook

Read this reference when planning or executing a substantive **secrets-hygiene-auditor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Exposure review: scan authorized current files, history, logs, artifacts, and examples with redacted evidence.
- Credential posture: assess scope, lifetime, storage, delivery, rotation, and environment separation.
- Incident response: coordinate revoke, rotate, validate, and history-remediation decisions.

## Minimum evidence record

- Authorized repositories and systems, expected secret types, owners, environments, and approved storage mechanisms.
- Scanner name/version/configuration, redacted finding fingerprint, location, commit or artifact identifier, and confidence.
- Revocation timestamp, replacement validation, affected consumers, audit events, and residual copies.

## Decision rules

- Never print or store a complete discovered value; use a fingerprint or last four characters only when safe.
- For suspected live exposure, revoke and rotate before rewriting history.
- Distinguish examples and test tokens from live credentials using provider validation only when authorized.
- Treat logs, CI artifacts, packages, caches, tickets, and backups as separate exposure surfaces.

## Common failure modes

- Deleting a line while leaving the credential valid.
- Committing the replacement secret or remediation evidence back into the repository.
- Assuming private repository exposure is harmless.
- Broadly rewriting shared history without coordination and recovery planning.

## Acceptance checklist

- [ ] Every finding has a redacted identity, location, status, and owner.
- [ ] Live or uncertain credentials have a containment decision.
- [ ] Replacement operation and old-credential revocation are verified.
- [ ] Preventive controls cover local development, CI, logging, and examples.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
