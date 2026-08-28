# Operational playbook

Read this reference when planning or executing a substantive **agent-permission-auditor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Static review: map configured tools, scopes, credentials, approvals, and delegation.
- Effective-authority test: verify harmless allowed and denied cases in an authorized environment.
- Redesign: propose least-privilege scopes, just-in-time grants, and revocation paths.

## Minimum evidence record

- Agent purpose, owners, deployment boundary, users, tenants, and permitted outcomes.
- Tool schemas, credential principals, scopes, network destinations, data stores, approval policy, and audit logs.
- Observed allowed/denied results, inherited roles, ambient credentials, rate limits, and revocation evidence.

## Decision rules

- Evaluate combinations of individually narrow tools because composition can create broad authority.
- Distinguish read, reversible write, consequential write, destructive action, delegation, and credential administration.
- A documented policy is not evidence of enforcement; require an observed denial for critical boundaries.
- Tie every retained permission to a concrete user outcome and accountable owner.

## Common failure modes

- Wildcard repository, tenant, storage, or cloud scopes justified by convenience.
- Approval requested after the consequential action instead of before it.
- Credentials shared between environments or agents with unrelated purposes.
- Audit logs that omit tool arguments, decision context, or acting identity.

## Acceptance checklist

- [ ] Every tool and credential has a purpose, scope, owner, and revocation path.
- [ ] Critical denied cases were observed or explicitly marked untested.
- [ ] Compound-authority paths and delegation are assessed.
- [ ] Exceptions have compensating controls and expiry dates.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
