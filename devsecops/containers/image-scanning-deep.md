---
title: "Container image scanning – in depth"
category: "devsecops"
tags: ["containers", "scanning", "cve", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Container image scanning – in depth

## TL;DR
Image scanners detect known CVEs in OS packages and app dependencies, plus misconfig and secrets. Scan early (CI) and continuously (registry), gate on severity + reachability, and cut CVEs at the source with minimal base images.

## Tools
```bash
# Trivy – broad (OS + langs + IaC + secrets), fast
trivy image --scanners vuln,secret,misconfig myimage:tag
trivy image --severity HIGH,CRITICAL --ignore-unfixed myimage:tag

# Grype – focused vuln scanner, pairs with Syft SBOM
grype myimage:tag
grype sbom:sbom.json                      # scan a pre-generated SBOM

# Docker Scout – layer-aware, base image recommendations
docker scout cves myimage:tag
docker scout recommendations myimage:tag  # suggests better base images
```

## Where to scan: CI vs registry
```text
CI (build time)   – fast feedback, block a bad image before push. Point-in-time.
Registry (continuous) – re-scan stored images as NEW CVEs are disclosed (an image
                    clean yesterday may be vulnerable today without changing).
Admission (deploy) – last gate: block images with critical CVEs / unsigned.
Use all three — CVE disclosure is continuous, a single CI scan goes stale.
```

## Layer analysis – find where CVEs enter
```bash
# See which layer/package introduced a finding
trivy image --format json myimage:tag | jq '.Results[].Vulnerabilities[].PkgName'
docker scout cves --format only-packages myimage:tag
# dive – inspect layer contents and wasted space
dive myimage:tag
```

## Reduce base-image CVEs at the source
```text
- Distroless (gcr.io/distroless/*) – no shell/package manager -> tiny CVE surface.
- Chainguard/Wolfi images – near-zero-CVE, frequently rebuilt.
- Multi-stage builds – ship only the binary + runtime, not build tooling.
- Pin by digest, rebuild often (stale base = accumulating CVEs).
```

## Gating policy
```yaml
# CI: fail on fixable High/Critical only (avoid noise from unfixable)
- run: trivy image --exit-code 1 --severity HIGH,CRITICAL --ignore-unfixed myimage:tag
```
```text
- Block on: fixable Critical/High. Warn on: Medium/Low, unfixable.
- Allow-list with justification + expiry (.trivyignore with a reason), never blanket-ignore.
- Add reachability/EPSS + CISA KEV to prioritize what actually matters.
```

## False positives & reachability
```text
- FPs: wrong package version detection, backported fixes (distro patches CVE but
  keeps version) -> use distro-aware scanners, --ignore-unfixed.
- Reachability: is the vulnerable code path actually invoked? Tools adding reachability
  (e.g. commercial SCA) cut noise dramatically — don't chase unreachable CVEs first.
```

## Detection (Blue Team)
- Registry scan alerts on newly-vulnerable stored images; admission logs blocked pulls.
- Track fleet exposure to CISA KEV components; measure remediation SLA.

## Mitigation / Hardening
- Minimal/distroless base, rebuild + rescan continuously, digest pinning.
- Gate CI + admission on fixable Critical/High; SBOM for inventory (see [supply-chain/sbom-cosign](../supply-chain/sbom-cosign.md)).
- Pair with runtime detection ([containers/falco-runtime](./falco-runtime.md)) and [docker-hardening](./docker-hardening.md).

## Sources
- [Trivy](https://trivy.dev/) · [Grype](https://github.com/anchore/grype) · [Chainguard Images](https://www.chainguard.dev/chainguard-images)
