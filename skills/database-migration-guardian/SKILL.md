---
name: database-migration-guardian
description: Plan and validate database schema migrations, backfills, compatibility windows, and rollback strategies. Use for changes that must preserve live data and mixed-version clients; do not approve irreversible operations without explicit recovery evidence.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Database Migration Guardian

## Purpose

Reduce data loss and downtime risk while moving a database between known states.

## Required inputs

- current and target schemas
- data volume and availability constraints
- application deployment sequence and rollback objective

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Classify changes by lock risk, rewrite cost, compatibility, data loss, and reversibility.
2. Design expand-migrate-contract sequencing for mixed-version operation.
3. Specify backfill batching, checkpoints, validation queries, throttling, and restart behavior.
4. Define backups, restore evidence, rollback limits, and the point of no return.
5. Test on representative volume and inspect locks, duration, replication lag, and application behavior.
6. Produce an ordered runbook with go/no-go gates and owners.

## Output contract

- migration dependency plan
- forward and rollback runbooks
- data reconciliation queries
- deployment gates and monitoring plan

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Never describe a backup as sufficient without a tested restore path.
- Flag destructive or lossy transformations explicitly.
- Stop when rollback assumptions conflict with the proposed change.

