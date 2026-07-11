---
title: "Supply Chain – SBOM, podpisy, SLSA"
category: "devsecops"
tags: ["supply-chain", "sbom", "sigstore", "slsa"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Supply Chain Security

## TL;DR
Zabezpiecz łańcuch od kodu do artefaktu: **SBOM** (co jest w środku), **podpisy** (autentyczność, cosign), **provenance/SLSA** (jak zbudowano). Chroni przed atakami typu SolarWinds/dependency confusion.

## SBOM (Software Bill of Materials)
```bash
# Generowanie (CycloneDX / SPDX)
syft myimage:latest -o cyclonedx-json > sbom.json
trivy image --format cyclonedx -o sbom.json myimage:latest
# Skan SBOM pod CVE
grype sbom:sbom.json
```

## Podpisywanie (Sigstore / cosign)
```bash
# Keyless (OIDC – bez zarządzania kluczami)
cosign sign myregistry/app@sha256:...
cosign verify myregistry/app@sha256:... \
  --certificate-identity=... --certificate-oidc-issuer=https://token.actions.githubusercontent.com

# Dołącz SBOM/attestacje do obrazu
cosign attest --predicate sbom.json --type cyclonedx myregistry/app@sha256:...
```

## SLSA (provenance)
```text
Poziomy SLSA:
 L1 – jest provenance   L2 – podpisana, hostowany build
 L3 – zabezpieczony, nieforgeowalny build   L4/najwyższe – reprodukowalny, dwuosobowy review
Cel: móc udowodnić, że artefakt powstał z danego źródła w danym pipeline.
```

## Ochrona przed atakami
```text
Dependency confusion – priorytet rejestrów, scoping, namespacing paczek
Typosquatting        – lockfile + weryfikacja, allow-list
Kompromitacja buildu – hermetyczny build, pinned deps, provenance
```

## Admission (weryfikacja przy deployu)
- Kyverno/Gatekeeper/Connaisseur: dopuść tylko podpisane obrazy z ważną provenance.

## Źródła
- [Sigstore/cosign](https://docs.sigstore.dev/) · [SLSA](https://slsa.dev/) · [Syft](https://github.com/anchore/syft)
