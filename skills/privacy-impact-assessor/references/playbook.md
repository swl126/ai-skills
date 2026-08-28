# Operational playbook

Read this reference when planning or executing a substantive **privacy-impact-assessor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Screening: determine whether personal data and elevated privacy conditions are present.
- Full assessment: map lifecycle, purposes, actors, transfers, risks, and mitigations.
- Change review: identify how a proposed feature or vendor changes the approved data flow and residual risk.

## Minimum evidence record

- System purpose, users, data subjects, jurisdictions, owners, diagrams, vendors, and deployment model.
- Data categories, sources, collection, derivation, purposes, storage, access, transfers, retention, deletion, and rights handling.
- Sensitive-data flags, children or vulnerable groups, automated decisions, notices, asserted legal basis, incidents, and safeguards.

## Decision rules

- Map derived and inferred data, logs, backups, support access, and analytics, not only form fields.
- Assess necessity and proportionality before selecting controls.
- Separate engineering risk analysis from legal determinations requiring qualified counsel.
- Evaluate severity for affected people, including scale, reversibility, power imbalance, and subgroup effects.

## Common failure modes

- A data inventory with no purposes, retention, or recipients.
- Calling encrypted collection 'minimized' when the data is still unnecessary.
- Assuming vendor responsibility removes controller or product risk.
- Using consent language as a substitute for usable choice and rights handling.

## Acceptance checklist

- [ ] Every personal-data category has a source, purpose, location, recipients, retention, and deletion path.
- [ ] Elevated conditions and affected populations are identified.
- [ ] Risks link to design changes, controls, owners, and residual decisions.
- [ ] Required legal or executive decisions are clearly escalated.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
