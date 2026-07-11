---
title: "Supply chain – SBOM, signing, SLSA"
category: "devsecops"
tags: ["supply-chain", "sbom", "sigstore", "slsa"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Supply chain security

## TL;DR
Secure the chain from code to artifact: **SBOM** (what's inside), **signing** (authenticity, cosign), **provenance/SLSA** (how it was built). Protects against attacks like SolarWinds/dependency confusion.

## SBOM (Software Bill of Materials)
```bash
# Generation (CycloneDX / SPDX)
syft myimage:latest -o cyclonedx-json > sbom.json
trivy image --format cyclonedx -o sbom.json myimage:latest
# Scan the SBOM for CVEs
grype sbom:sbom.json
```

## Signing (Sigstore / cosign)
```bash
# Keyless (OIDC – no key management)
cosign sign myregistry/app@sha256:...
cosign verify myregistry/app@sha256:... \
  --certificate-identity=... --certificate-oidc-issuer=https://token.actions.githubusercontent.com

# Attach SBOM/attestations to the image
cosign attest --predicate sbom.json --type cyclonedx myregistry/app@sha256:...
```

## SLSA (provenance)
```text
SLSA levels:
 L1 – provenance exists   L2 – signed, hosted build
 L3 – hardened, non-forgeable build   L4/highest – reproducible, two-person review
Goal: be able to prove an artifact came from a given source in a given pipeline.
```

## Protection against attacks
```text
Dependency confusion – registry priority, scoping, package namespacing
Typosquatting        – lockfile + verification, allow-list
Build compromise     – hermetic build, pinned deps, provenance
```

## Admission (verification at deploy)
- Kyverno/Gatekeeper/Connaisseur: admit only signed images with valid provenance.

## Sources
- [Sigstore/cosign](https://docs.sigstore.dev/) · [SLSA](https://slsa.dev/) · [Syft](https://github.com/anchore/syft)
