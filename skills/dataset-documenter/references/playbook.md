# Operational playbook

Read this reference when planning or executing a substantive **dataset-documenter** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Initial card: document a dataset before operational use or release.
- Version update: identify changes in collection, population, schema, labels, transformations, and limitations.
- Suitability review: evaluate a proposed use against documented scope and evidence gaps.

## Minimum evidence record

- Dataset identifier/version, owner, maintainers, storage, license, access, source, collection dates, and update cadence.
- Units, population, sampling, coverage, exclusions, schema, labels, missingness, sensitive attributes, and splits.
- Lineage, joins, filtering, deduplication, imputation, transformations, quality tests, drift, and known incidents.

## Decision rules

- Unknown provenance remains unknown; do not fill gaps with plausible narratives.
- Separate observed quality measures from suitability for a specific use.
- Document label creation, annotator instructions, disagreement, and uncertainty.
- Record both intended and unsuitable uses with the conditions that drive the boundary.

## Common failure modes

- Schema documentation presented as a dataset card.
- Representation statistics without comparison to the target population or use.
- Transforms listed without order, parameters, code version, or data loss.
- A static card with no dataset version or update responsibility.

## Acceptance checklist

- [ ] Identity, ownership, provenance, license, and access are recorded.
- [ ] Population, sampling, exclusions, missingness, and labels are described.
- [ ] Transformations and quality evidence are reproducible or explicitly limited.
- [ ] Uses, non-uses, biases, risks, and monitoring expectations are actionable.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
