# Security Policy

Report suspected vulnerabilities through GitHub's private vulnerability reporting feature for the affected repository. Do not open a public issue containing credentials, exploit details, personal information, or an unpatched vulnerability.

## Supported versions

Security fixes are provided for the current default-branch release. Older embedded packages and installation archives should be upgraded before use.

## Execution boundary

The hub executes bundled, dependency-free Python tools when requested. Every package manifest declares runtime, network, filesystem, external-write, and destructive-action boundaries. Current packages require no network access and may write only to explicit output paths.

Review a skill's instructions and scripts before granting an agent credentials or authority over external systems. Domain scanners operate only on user-supplied local paths. Secret findings are redacted and represented by fingerprints.

## Evidence integrity

`scripts/evidence_envelope.py` binds collected evidence to its artifact SHA-256, target, collector, method, and collection time. A digest verifies integrity, not the human or system identity of the collector. Use an external signing and identity system when non-repudiation is required.

## Disclosure

Include the affected version, component, reproduction conditions, impact, and a safe proof of concept. Do not include live credentials or unnecessary personal data. Maintainers should acknowledge a private report within seven days and coordinate disclosure after a fix is available.
