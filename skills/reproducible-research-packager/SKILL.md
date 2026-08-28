---
name: reproducible-research-packager
description: Package research data, code, environments, parameters, provenance, checksums, and execution instructions for independent reconstruction. Use when preparing a study artifact or computational appendix; do not redistribute restricted data or software.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Reproducible Research Packager

## Purpose

Enable another authorized analyst to reconstruct results and identify where judgment or unavailable inputs affect reproducibility.

## Required inputs

- analysis code, data, outputs, and environment
- method, parameters, seeds, and transformation history
- sharing, licensing, and confidentiality constraints

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Define the exact claims and outputs the package must reconstruct.
2. Inventory inputs, code, dependencies, environments, parameters, seeds, and external services.
3. Separate redistributable artifacts from restricted inputs and provide lawful acquisition or substitution instructions.
4. Create ordered execution steps, checksums, expected intermediate outputs, and reconciliation checks.
5. Test reconstruction in a clean environment or document the precise untested dependency.
6. Record provenance, licenses, limitations, nondeterminism, and deviations from the reported analysis.

## Output contract

- structured research package
- environment and dependency lock information
- reconstruction guide and checksums
- provenance, restriction, and limitation report

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not package personal, confidential, proprietary, or licensed data without authority.
- Never fabricate unavailable inputs or successful reconstruction.
- Distinguish computational reproducibility from external scientific validity.

