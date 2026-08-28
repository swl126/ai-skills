---
name: row-level-security-auditor
description: Audit database row-level security policies for cross-tenant exposure, privilege escalation, missing operation coverage, and unsafe defaults. Use for authorized schema and policy review; do not claim isolation from policy text without enforcement tests.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Row Level Security Auditor

## Purpose

Verify that each role can access only the rows and operations permitted by the tenancy model.

## Required inputs

- schema, roles, and tenancy model
- RLS policies and helper functions
- authorized test identities or fixtures

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Enumerate protected tables, views, operations, roles, ownership, security-definer functions, and bypass privileges.
2. Translate intended access rules into subject-action-object test cases.
3. Inspect USING and WITH CHECK logic for SELECT, INSERT, UPDATE, DELETE, joins, nulls, and tenant changes.
4. Test positive and negative cases with isolated fixtures where authorized.
5. Trace exposures through views, functions, service roles, foreign keys, and indirect references.
6. Deliver policy corrections and a regression matrix covering every protected operation.

## Output contract

- table-operation-role coverage matrix
- verified exposure findings
- corrected policy recommendations
- RLS regression cases

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Use non-production fixtures unless production testing is explicitly authorized.
- Never expose real tenant data in evidence.
- Do not confuse application filters with database-enforced isolation.

