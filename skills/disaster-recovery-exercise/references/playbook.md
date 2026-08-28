# Operational playbook

Read this reference when planning or executing a substantive **disaster-recovery-exercise** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Tabletop: test decisions, coordination, dependencies, and information flow.
- Technical restoration: restore isolated systems or data and measure actual recovery.
- Regional or provider scenario: exercise dependency failure, failover, and degraded operations.

## Minimum evidence record

- Business services, criticality, RTO, RPO, minimum viable service, dependencies, owners, and approved scope.
- Scenario, injects, participant roles, observers, start/stop conditions, isolation, and safety controls.
- Observed timestamps, decisions, data-loss point, restored functions, validation results, communications, and deviations.

## Decision rules

- Keep scenario knowledge from participants when it would invalidate observation.
- Measure from disruption to validated service, not merely to infrastructure startup.
- RPO is an observed data-loss result, not a backup schedule.
- Any production disruption, failover, or destructive restoration requires separate explicit authorization.

## Common failure modes

- Calling a discussion a successful restore test.
- Testing backups without application-level validation or dependency recovery.
- Coaching participants through the expected runbook.
- Ignoring identity, DNS, certificates, secrets, vendors, and communication dependencies.

## Acceptance checklist

- [ ] Exercise scope and safety controls were honored.
- [ ] Observed RTO/RPO are compared with requirements.
- [ ] Restored service and data were functionally validated.
- [ ] Gaps have owners, priorities, due dates, and a scheduled retest.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
