---
title: "SLSA levels"
category: "devsecops"
tags: ["supply-chain", "slsa", "provenance"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# SLSA levels

## TL;DR
SLSA ("salsa", Supply-chain Levels for Software Artifacts) is a framework of increasing guarantees that an artifact was built from the source you think, in a tamper-resistant pipeline. The heart of it is **provenance**: signed, verifiable metadata about how an artifact was built.

## The build track levels (v1.0)
```text
L0 – no guarantees.
L1 – provenance exists: the build process is documented and produces provenance metadata.
L2 – signed provenance from a hosted build platform: harder to forge, tamper-evident.
L3 – hardened build: the platform prevents tampering and provenance forgery
     (isolated, ephemeral, non-falsifiable builds).
(Higher levels/tracks address source and dependency integrity as the spec evolves.)
```

## Provenance — what it attests
```text
- What was built (artifact digest).
- From what source (repo + commit).
- By what builder (the build platform identity).
- With what inputs/parameters.
-> A verifier can check the artifact matches signed provenance before deploying.
```

## Achieving it in practice
```text
L1 – generate provenance in CI (e.g. build metadata).
L2 – use a hosted builder that signs provenance (GitHub Actions + slsa-github-generator;
     sign with cosign / Sigstore keyless OIDC).
L3 – isolated, ephemeral, non-forgeable builds (reusable trusted workflows / dedicated builders).
```
```bash
# Verify SLSA provenance before deploy (slsa-verifier)
slsa-verifier verify-image myregistry/app@sha256:... \
  --source-uri github.com/org/repo
```

## Why it matters
```text
- Defends against build-system compromise (SolarWinds-style) and artifact tampering.
- Enables "only deploy artifacts with valid provenance from our pipeline" (admission control).
- Combined with SBOM (what's inside) + signing (authenticity) = end-to-end supply-chain integrity.
```

## Enforcement
```text
- Admission (Kyverno/policy-controller/Connaisseur): require signed provenance meeting a SLSA level.
- Gate deploys on slsa-verifier; reject unsigned/mismatched artifacts.
```

## Sources
- [SLSA](https://slsa.dev/) · [slsa-github-generator](https://github.com/slsa-framework/slsa-github-generator) · related: [sbom-cosign](./sbom-cosign.md), [artifact-signing-flow](../ci-cd/artifact-signing-flow.md)
