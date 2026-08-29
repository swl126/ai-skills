---
name: database-migration-guardian
description: Plan and validate database schema migrations, backfills, compatibility windows, and rollback strategies. Use for changes that must preserve live data and mixed-version clients; do not approve irreversible operations without explicit recovery evidence.
metadata:
  version: "1.1.0"
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

## Operating modes and local resources

- For substantive work, read [the operational playbook](references/playbook.md) before choosing tests, thresholds, or a decision.
- Use [the report template](assets/report-template.md) when a durable deliverable is requested. Preserve its evidence register and acceptance review even if the presentation format changes.
- Use [the example request](examples/request.md), [decision excerpt](examples/expected-output.md), and [validated worked report](examples/example-report.md) to calibrate scope and decisiveness, never as evidence for the current task.
- For a narrow question, apply only the relevant workflow steps and state which completion gates are outside scope.

## Executable engine

- Read [the executable contract](references/executable-contract.md) before supplying normalized evidence.
- Validate inputs with `python3 scripts/assess.py validate --input INPUT.json`.
- Produce a deterministic decision with `python3 scripts/assess.py assess --input INPUT.json --out RESULT.json --report REPORT.md`.
- Use `--fail-on-block` in automation. The engine analyzes supplied evidence and never connects to or mutates production systems.

## Evidence discipline

- Give material evidence stable identifiers and cite those identifiers in findings.
- Separate observed facts, interpretations, unknowns, and recommendations.
- Record the target version, environment, collection time, and tool or method when freshness or reproducibility matters.
- Never upgrade missing evidence into a passing result. Mark it blocked and name what would resolve it.

## Workflow

1. Classify changes by lock risk, rewrite cost, compatibility, data loss, and reversibility.
2. Design expand-migrate-contract sequencing for mixed-version operation.
3. Specify backfill batching, checkpoints, validation queries, throttling, and restart behavior.
4. Define backups, restore evidence, rollback limits, and the point of no return.
5. Test on representative volume and inspect locks, duration, replication lag, and application behavior.
6. Produce an ordered runbook with go/no-go gates and owners.

## Completion gates

- Scope, authority, target identity, and decision owner are explicit.
- Required inputs are present or their absence is recorded as a blocker.
- Material findings trace to reviewable evidence and distinguish inference from observation.
- Every applicable acceptance check in the local playbook has a recorded outcome.
- Critical failures remain visible in the decision and cannot be averaged away.
- Follow-up actions have an owner and an observable verification method.

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
