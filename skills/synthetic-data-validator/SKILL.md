---
name: synthetic-data-validator
description: Evaluate synthetic datasets for utility, leakage, duplication, bias, and re-identification risk against the intended use. Use before sharing or relying on synthetic data; do not treat synthetic generation as automatic anonymization.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Synthetic Data Validator

## Purpose

Determine whether synthetic data is useful enough for its purpose without reproducing unacceptable privacy or bias risks.

## Required inputs

- real reference data under authorized access
- synthetic dataset and generation method
- intended use and privacy/utility thresholds

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Confirm schema, types, constraints, support, and row-level validity.
2. Compare marginal, joint, conditional, temporal, and rare-event behavior relevant to the intended use.
3. Test downstream task performance and calibration against held-out real data.
4. Check exact and near duplicates, membership signals, attribute inference, memorization, and outlier leakage.
5. Compare subgroup representation and error to detect amplified or hidden bias.
6. Report tradeoffs and approve, restrict, regenerate, or reject against predeclared thresholds.

## Output contract

- utility and fidelity report
- privacy attack results
- subgroup and bias analysis
- use decision with thresholds and limitations

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Keep real reference data in its authorized environment.
- Do not publish attack examples that reveal actual records.
- Do not call a dataset anonymous without a justified threat model and evidence.

