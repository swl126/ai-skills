---
name: api-contract-auditor
description: Audit OpenAPI or equivalent API contracts against implementation behavior, examples, errors, versioning, and compatibility expectations. Use before integration or release; do not infer implementation conformance from a specification alone.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Api Contract Auditor

## Purpose

Find contract defects that cause unsafe, ambiguous, or breaking client-server behavior.

## Required inputs

- API specification and version
- implementation or captured responses
- compatibility and consumer requirements

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Parse resources, operations, authentication, parameters, schemas, status codes, and examples.
2. Check internal consistency: required fields, nullability, formats, discriminator use, pagination, idempotency, and error envelopes.
3. Compare the contract with observed implementation behavior using authorized test cases.
4. Classify changes as compatible, conditionally compatible, or breaking for real consumers.
5. Inspect security declarations, authorization boundaries, sensitive fields, rate limits, and replay risks.
6. Return exact contract changes, implementation fixes, and consumer migration guidance.

## Output contract

- operation-level conformance matrix
- breaking-change report
- security and ambiguity findings
- prioritized remediation plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not send mutating requests to production without authorization.
- Redact tokens and sensitive response data.
- Separate spec defects from implementation defects.

