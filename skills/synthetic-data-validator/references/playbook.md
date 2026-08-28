# Operational playbook

Read this reference when planning or executing a substantive **synthetic-data-validator** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Structural validation: test schema, types, constraints, support, and row-level validity.
- Utility validation: compare relevant distributions and downstream task performance.
- Disclosure assessment: test memorization, duplicates, membership, attribute inference, outliers, and subgroup risk.

## Minimum evidence record

- Real reference data governance and split, synthetic generator/version/settings, seeds, privacy method, and intended use.
- Predeclared metrics, thresholds, subgroup definitions, holdout logic, statistical uncertainty, and downstream tasks.
- Exact/near-match results, attack assumptions, adversary knowledge, rare-record analysis, utility results, and decision.

## Decision rules

- Keep a held-out real set that was unavailable to generator training when the method requires it.
- Choose metrics from the intended use and risk model, not from convenience.
- Report privacy and utility separately; neither compensates automatically for the other.
- Synthetic data is not anonymous by definition and must retain governance until risk is demonstrated acceptable.

## Common failure modes

- Only comparing univariate distributions.
- Training and evaluating against the same real records.
- No analysis of rare combinations or high-risk subgroups.
- Declaring safe because exact duplicates were not found.

## Acceptance checklist

- [ ] Structural validity meets predeclared constraints.
- [ ] Utility is demonstrated for the named use with uncertainty and subgroup results.
- [ ] Disclosure tests match a stated adversary model.
- [ ] Decision thresholds, limitations, and governance conditions are explicit.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
