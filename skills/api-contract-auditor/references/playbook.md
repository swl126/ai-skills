# Operational playbook

Read this reference when planning or executing a substantive **api-contract-auditor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Static contract lint: inspect schema consistency, examples, security declarations, and error models.
- Conformance: compare authorized implementation behavior with the declared contract.
- Compatibility: classify a proposed diff for existing consumers and produce migration guidance.

## Minimum evidence record

- Versioned API contract, server/build identifier, base URL, auth model, and consumer assumptions.
- Request and response samples for success, validation, authorization, rate-limit, and failure paths.
- Observed status, headers, body, latency, pagination, idempotency, and correlation behavior.

## Decision rules

- Treat omitted fields, null fields, and empty values as distinct when consumers can observe the difference.
- Assess both source compatibility and behavioral compatibility.
- Test authorization with separate identities and negative cases; never infer it from OpenAPI security blocks.
- Preserve exact JSON paths and operations in every finding.

## Common failure modes

- Only testing happy-path examples.
- Calling a change additive when it changes defaults, ordering, limits, or error semantics.
- Sending destructive requests to production without explicit approval and cleanup.
- Reporting a contract defect without stating whether contract or implementation should change.

## Acceptance checklist

- [ ] Every operation has an auth, success, validation, and error assessment.
- [ ] Breaking and conditional changes identify affected consumers.
- [ ] Observed behavior is tied to an environment and build.
- [ ] Remediation names the exact contract path or implementation behavior.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
