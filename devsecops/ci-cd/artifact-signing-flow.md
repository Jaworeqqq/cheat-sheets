---
title: "Artifact signing flow (end-to-end)"
category: "devsecops"
tags: ["ci-cd", "supply-chain", "sigstore", "slsa", "provenance"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Artifact signing flow (end-to-end)

## TL;DR
A complete, verifiable pipeline from build to deploy: generate an SBOM, sign the artifact (keyless via OIDC), attest its provenance (SLSA), and verify signature + provenance at admission. This closes the loop so only artifacts your pipeline built can run.

## The flow
```text
build  ──▶  SBOM  ──▶  sign (cosign/OIDC)  ──▶  attest provenance (SLSA)  ──▶  push
                                                                               │
deploy  ◀──  admission verify (signature + identity + provenance)  ◀──────────┘
```

## 1. Build + SBOM
```bash
docker build -t $REG/app:$SHA .
syft $REG/app:$SHA -o cyclonedx-json > sbom.json
```

## 2. Sign keyless (OIDC, no key management)
```bash
# In GitHub Actions/GitLab CI, cosign uses the workflow's OIDC identity.
# Requires: permissions: id-token: write (GitHub)
cosign sign --yes $REG/app@sha256:$DIGEST
# The signing identity = the CI workflow (recorded in the Rekor transparency log).
```

## 3. Attest SBOM + provenance (SLSA)
```bash
# Attach the SBOM as a signed attestation
cosign attest --yes --predicate sbom.json --type cyclonedx $REG/app@sha256:$DIGEST

# SLSA provenance – how/where/what built it (e.g. via slsa-github-generator)
# produces a signed provenance attestation tying the artifact to the build.
```

## 4. Verify (in CI gate AND at admission)
```bash
# Verify signature + the identity that signed it (pin to your workflow)
cosign verify $REG/app@sha256:$DIGEST \
  --certificate-identity-regexp "https://github.com/acme/.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# Verify the provenance attestation
cosign verify-attestation --type slsaprovenance $REG/app@sha256:$DIGEST \
  --certificate-identity-regexp "https://github.com/acme/.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

## 5. Admission enforcement (Kubernetes)
```text
- Kyverno verifyImages OR sigstore policy-controller:
    admit only images signed by your CI identity + valid SLSA provenance.
- Run in audit mode first, then enforce (fail closed).
```
```yaml
# Kyverno (concept)
verifyImages:
  - imageReferences: ["registry.acme.io/*"]
    attestors:
      - entries:
          - keyless:
              issuer: https://token.actions.githubusercontent.com
              subject: "https://github.com/acme/*"
```

## Why keyless
```text
- No long-lived signing keys to store/rotate/leak.
- Identity = the CI workflow, logged in Rekor (public transparency log) -> auditable.
- Verification pins the signer identity, so a stolen registry credential can't
  produce artifacts that pass admission.
```

## Detection (Blue Team)
- Admission logs: rejected unsigned/untrusted images; Rekor entries for unexpected identities.
- Alert on images deployed that bypass the verify gate.

## Best practices
- Sign by digest (immutable), not tag; verify at both CI gate and admission.
- Pin the allowed signer identity tightly; enforce SLSA provenance, not just a signature.
- Combine with [supply-chain/sbom-cosign](../supply-chain/sbom-cosign.md), [dependency-confusion](../supply-chain/dependency-confusion.md), and pipeline hardening ([github-actions-hardening](./github-actions-hardening.md)).

## Sources
- [Sigstore/cosign](https://docs.sigstore.dev/) · [SLSA](https://slsa.dev/) · [Kyverno verifyImages](https://kyverno.io/docs/writing-policies/verify-images/)
