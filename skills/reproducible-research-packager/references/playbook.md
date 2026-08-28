# Operational playbook

Read this reference when planning or executing a substantive **reproducible-research-packager** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Inventory: map each published claim or artifact to data, code, parameters, environment, and execution step.
- Package: assemble lawful redistributable artifacts plus instructions for restricted dependencies.
- Reconstruct: execute in a clean environment and reconcile expected and observed outputs.

## Minimum evidence record

- Study and package identifiers, claims, outputs, source revisions, authors, license, and publication context.
- Input provenance, access restrictions, checksums, code, dependency locks, containers, platform, parameters, seeds, and external services.
- Ordered commands, expected intermediates, output hashes or tolerances, logs, deviations, nondeterminism, and reconstruction result.

## Decision rules

- A package is reproducible only for explicitly named claims and outputs.
- Never redistribute restricted data, credentials, proprietary software, or controlled artifacts without authority.
- Pin what can change and document unavoidable external services or nondeterminism.
- Record the clean-environment result; instructions alone are not reconstruction evidence.

## Common failure modes

- A requirements file without exact versions or platform information.
- Manual preprocessing absent from the execution chain.
- Expected output described visually with no machine-checkable reconciliation.
- Checksums created but not verified during reconstruction.

## Acceptance checklist

- [ ] Every target claim maps to inputs, code, parameters, environment, and expected output.
- [ ] Redistribution and license status are resolved or lawful acquisition steps are supplied.
- [ ] Ordered execution succeeds in a clean environment or the exact blocker is documented.
- [ ] Checksums, tolerances, logs, and deviations make reconstruction auditable.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
