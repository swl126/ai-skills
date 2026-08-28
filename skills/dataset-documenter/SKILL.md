---
name: dataset-documenter
description: Create dataset cards describing provenance, population, collection, transformations, exclusions, limitations, intended use, and known bias. Use when publishing or operationalizing a dataset; do not infer missing provenance or represent documentation as quality proof.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Dataset Documenter

## Purpose

Make a dataset's origin, fitness, limitations, and responsible-use boundaries visible to downstream users.

## Required inputs

- source and collection records
- schema, transformations, quality results, and population details
- intended uses, prohibited uses, and governance constraints

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Identify dataset ownership, lineage, versions, licenses, consent or collection context, and update cadence.
2. Describe units of observation, population, sampling, coverage, exclusions, labels, and missingness.
3. Record transformations, joins, deduplication, imputation, filtering, and quality checks.
4. Analyze representation, measurement error, label uncertainty, temporal drift, leakage, and sensitive attributes.
5. Define suitable uses, unsuitable uses, access, retention, and monitoring expectations.
6. Mark unknowns and evidence gaps rather than filling them with plausible text.

## Output contract

- versioned dataset card
- lineage and transformation summary
- quality and bias limitations
- intended-use and governance boundaries

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not expose row-level personal or confidential data.
- Avoid unsupported fairness or representativeness claims.
- Preserve provenance and licensing uncertainty explicitly.

