# Operational playbook

Read this reference when planning or executing a substantive **architecture-decision-recorder** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- New decision: record context and compare viable options before commitment.
- Review: test whether evidence, constraints, or consequences have changed.
- Supersession: create a linked new record while preserving the original decision context.

## Minimum evidence record

- Decision identifier, date, status, deciders, consulted stakeholders, scope, and deadline.
- Forces and constraints, current state, viable options, comparison criteria, evidence, uncertainty, and dissent.
- Chosen option, consequences, implementation plan, measures, revisit triggers, and reversal or migration path.

## Decision rules

- Include the status quo when it is viable.
- Write the decision before outcomes create hindsight bias.
- Separate fact, forecast, preference, and constraint.
- Never edit a historical ADR to make the original reasoning look better; supersede it.

## Common failure modes

- A decision log that records only the winning option.
- Criteria selected after the preferred option is known.
- No operational consequences, ownership, or reversal condition.
- Treating an ADR as permanent authority after its assumptions expire.

## Acceptance checklist

- [ ] Context and scope are understandable without meeting memory.
- [ ] At least two viable options or a justified single-option constraint are recorded.
- [ ] The selected option follows the stated criteria and acknowledges tradeoffs.
- [ ] Consequences, owner, adoption signals, and revisit triggers are explicit.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
