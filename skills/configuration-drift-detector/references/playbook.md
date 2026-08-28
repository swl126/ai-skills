# Operational playbook

Read this reference when planning or executing a substantive **configuration-drift-detector** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Snapshot: capture redacted, typed configuration from declared and observed sources.
- Compare: normalize representations and classify semantic differences.
- Reconcile: choose a direction, owner, verification step, and exception expiry for each material drift.

## Minimum evidence record

- Environment identities, configuration sources, collection timestamps, versions, and declared baseline authority.
- Normalized key path, typed redacted values or fingerprints, source, scope, inheritance, and default behavior.
- Change history, approval record, owner, behavioral impact, reconciliation action, and verification result.

## Decision rules

- Preserve types; string `false`, boolean `false`, null, absent, and inherited are not equivalent.
- Redact values but compare secret presence, provider, version, scope, and rotation metadata.
- Do not assume the majority environment is correct; reconcile to an authorized baseline.
- Ignore volatile fields only through explicit, versioned comparison rules.

## Common failure modes

- Dumping live secrets into the comparison report.
- Flattening structured configuration until scope and inheritance are lost.
- Automatically overwriting production to match a lower environment.
- Permanent ignore rules with no owner or rationale.

## Acceptance checklist

- [ ] Sources, collection times, and baseline authority are stated.
- [ ] Every material difference has a classification and behavioral impact.
- [ ] Reconciliation preserves secrets and includes verification.
- [ ] Exceptions have an owner, reason, and expiry.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
