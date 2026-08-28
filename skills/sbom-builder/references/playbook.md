# Operational playbook

Read this reference when planning or executing a substantive **sbom-builder** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Generate: derive SPDX or CycloneDX components and relationships from authoritative build evidence.
- Reconcile: compare multiple generators, lockfiles, images, and shipped artifacts.
- Validate: check schema, identifiers, relationships, hashes, licenses, and coverage limitations.

## Minimum evidence record

- Exact artifact name/version/hash, build identifier, source revision, target platform, and component boundary.
- Generator name/version/options and the lockfiles, package databases, image layers, or build records used.
- Component identifiers, package URLs, versions, suppliers, licenses, hashes, dependency edges, and unresolved fields.

## Decision rules

- Describe the shipped artifact, not merely the source checkout.
- Keep development-only and runtime scope explicit.
- Use `NOASSERTION` or an equivalent supported unknown value instead of inventing supplier or license data.
- Preserve stable document and component identifiers so relationships remain valid.

## Common failure modes

- SBOM generated from a stale lockfile rather than the release artifact.
- Missing operating-system packages in a container image.
- Components listed without dependency relationships or a root component.
- Schema-valid output claimed as complete without coverage reconciliation.

## Acceptance checklist

- [ ] Document validates against the declared specification version.
- [ ] Root artifact and every relationship reference resolve.
- [ ] Artifact hash and source/build identity are recorded.
- [ ] Unknowns and excluded component classes are reported.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
