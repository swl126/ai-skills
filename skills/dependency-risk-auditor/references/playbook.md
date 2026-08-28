# Operational playbook

Read this reference when planning or executing a substantive **dependency-risk-auditor** engagement. Keep the main skill loaded; use this file for mode selection, evidence design, failure analysis, and completion review.

## Operating modes

- Inventory: resolve direct, transitive, development, build, and runtime dependencies from lock/build evidence.
- Risk triage: combine vulnerability, reachability, privilege, provenance, maintenance, and license information.
- Remediation: compare patch, upgrade, replacement, isolation, removal, and time-bound acceptance.

## Minimum evidence record

- Artifact boundary, ecosystems, lockfiles, build manifests, deployment form, platform, and runtime exposure.
- Package URL, exact resolved version, hashes or integrity data, dependency path, advisory identifiers, and fix versions.
- Reachability or call-path evidence, exploit prerequisites, privileges, mitigations, maintainer activity, and license obligations.

## Decision rules

- Use resolved versions, not loose manifest ranges, for the shipped artifact.
- Do not rank solely by advisory severity; include reachability, exposure, privilege, and consequence.
- Check dependency confusion, typosquatting, source registry, integrity pins, install scripts, and abandoned packages.
- Separate application risk from build-pipeline and developer-workstation risk.

## Common failure modes

- Counting vulnerabilities without identifying whether affected code ships or executes.
- Suggesting an upgrade without checking compatibility or transitive changes.
- Ignoring malicious-package and provenance risks because no CVE exists.
- Treating scanner absence as evidence of no vulnerability.

## Acceptance checklist

- [ ] All shipped ecosystems and dependency layers are inventoried.
- [ ] Each priority finding has a dependency path and contextual risk rationale.
- [ ] Remediation is actionable and verification is specified.
- [ ] Accepted risk has an owner, compensating control, and expiry.

If a checklist item is not met, mark it **failed**, **not applicable with rationale**, or **blocked with the missing evidence and owner**. Never silently omit it.
