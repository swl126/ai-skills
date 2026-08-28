# Operational playbook

Read this reference when planning or executing a substantive **release-readiness-gate** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Evidence collection: trace the release scope to required tests and operational proof.
- Decision review: apply predeclared mandatory gates and critical blockers.
- Conditional release: define narrowly bounded conditions, owners, expiry, rollback, and verification.

## Minimum evidence record

- Release identifier, exact change set, artifacts, environments, owners, schedule, and risk tolerance.
- Test results including failed, flaky, skipped, quarantined, and stale cases; security, migration, compatibility, and documentation evidence.
- Artifact hashes, deployment and rollback procedures, observability, support readiness, open findings, and exception approvals.

## Decision rules

- A missing mandatory artifact is not a pass.
- Critical security, safety, integrity, or unrecoverable-data risks cannot be averaged away.
- Conditional ship requires enforceable conditions and a named authority; it is not a euphemism for unresolved blockers.
- Tie every gate to the exact release evidence and its freshness.

## Common failure modes

- Reviewing only headline pass percentages.
- Rollback described but not tested or impossible after a data transition.
- Unknown ownership for post-release monitoring and incident response.
- Exceptions with no expiry, compensating control, or acceptance authority.

## Acceptance checklist

- [ ] Release scope and artifact identity are frozen.
- [ ] Every mandatory gate is pass, fail, or explicitly not applicable with rationale.
- [ ] Blockers and exceptions identify owners and decision authority.
- [ ] Rollback and post-release verification are executable and time-bounded.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
