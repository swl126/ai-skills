---
name: sbom-builder
description: Build and validate a software bill of materials with components, versions, suppliers, provenance, licenses, hashes, and dependency relationships. Use for release evidence or supply-chain review; do not invent unresolved component metadata.
metadata:
  version: "0.1.0"
  distribution: embedded
---

# Sbom Builder

## Purpose

Create a traceable inventory that downstream security and compliance processes can reproduce.

## Required inputs

- build manifests and lockfiles
- built artifacts or container images
- target SBOM format and scope

If a required input is unavailable and materially changes the result, identify the blocker instead of inventing it.

## Workflow

1. Define the shipped artifact boundary and included development or runtime components.
2. Extract components from authoritative build and package metadata; reconcile duplicates and aliases.
3. Record versions, package URLs, suppliers, licenses, hashes, and dependency edges where supported.
4. Mark unknowns explicitly and preserve generator version and timestamp.
5. Validate schema, internal references, root component, and correspondence with the actual artifact.
6. Report coverage limitations and emit the requested SPDX or CycloneDX representation.

## Output contract

- machine-readable SBOM
- human coverage summary
- unresolved component register
- validation evidence

Separate verified observations, inference, uncertainty, and recommendations. Preserve enough evidence for another authorized analyst to review the result.

## Safety and authority

- Do not claim completeness when ecosystems or generated artifacts were not inspected.
- Avoid embedding credentials, internal URLs, or unnecessary personal data.
- Keep observed license metadata separate from legal conclusions.

