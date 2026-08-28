# Operational playbook

Read this reference when planning or executing a substantive **database-migration-guardian** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Design review: classify risk and choose expand-migrate-contract sequencing.
- Rehearsal: run the migration on representative volume and observe locks, lag, and application behavior.
- Execution gate: produce a timed runbook, stop conditions, rollback limits, and post-checks.

## Minimum evidence record

- Current and target schema, engine/version, table sizes, traffic patterns, replicas, clients, and deployment order.
- Migration and backfill code, query plans, lock observations, duration, replication lag, and failure/restart behavior.
- Backup identifier, restore-test evidence, validation queries, owners, communications, and maintenance constraints.

## Decision rules

- A down migration is not a rollback plan when data has been transformed or discarded.
- Separate schema expansion, data migration, application cutover, and contract removal.
- Make backfills idempotent, resumable, bounded, observable, and safe under concurrent writes.
- Identify the point of no return and require explicit authority before crossing it.

## Common failure modes

- Adding a required field before all writers populate it.
- Long unbounded transactions or table rewrites on production-scale data.
- Assuming backups work without restore evidence.
- Contracting old schema while mixed-version clients remain.

## Acceptance checklist

- [ ] Mixed-version compatibility is demonstrated for the planned window.
- [ ] Representative rehearsal meets lock, lag, duration, and error thresholds.
- [ ] Rollback or forward-recovery is executable up to a named boundary.
- [ ] Go/no-go owners, stop conditions, and validation queries are explicit.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
