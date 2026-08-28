# Operational playbook

Read this reference when planning or executing a substantive **row-level-security-auditor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Policy review: inspect protected relations, roles, ownership, bypass paths, USING, and WITH CHECK.
- Fixture test: execute positive and negative subject-action-object cases in an isolated authorized database.
- Regression design: produce a complete operation-by-role matrix for CI.

## Minimum evidence record

- Database engine/version, schema, policies, grants, role hierarchy, views, functions, triggers, and service accounts.
- Intended tenant and ownership rules expressed independently of current policy text.
- Isolated identities and rows, queries executed, affected-row counts, errors, and transaction cleanup evidence.

## Decision rules

- Test SELECT, INSERT, UPDATE, and DELETE separately; UPDATE requires both visible-row and new-row checks.
- Include null tenant IDs, tenant-key changes, joins, views, foreign keys, and security-definer functions.
- Table owners and bypass-RLS roles must be handled as explicit threat assumptions.
- Run write tests inside rollbackable fixtures unless persistence is specifically authorized.

## Common failure modes

- Testing only SELECT or only the nominal application role.
- Using the policy itself as the statement of intended behavior.
- Missing indirect exposure through views, functions, or service roles.
- A deny test that passes because the target row did not exist.

## Acceptance checklist

- [ ] Every protected operation and role has positive and negative coverage.
- [ ] Fixture preconditions prove that denied target data existed.
- [ ] Bypass roles and indirect access paths are documented.
- [ ] Corrective policy and regression cases are supplied for each exposure.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
