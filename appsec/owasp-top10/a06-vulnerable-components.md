---
title: "A06 – Vulnerable and Outdated Components"
category: "appsec"
tags: ["owasp", "sca", "dependencies", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# A06 – Vulnerable and Outdated Components

## TL;DR
Using libraries, frameworks or runtimes with known vulnerabilities (CVEs). You inherit the security of everything you depend on — transitively.

## The problem
```text
- Outdated dependencies with public CVEs (log4shell, Struts, etc.)
- Unknown/unmanaged dependency inventory (no SBOM)
- Transitive deps you didn't choose but still ship
- End-of-life runtimes/frameworks without patches
```

## Detection / tooling (SCA)
```bash
trivy fs --scanners vuln .
grype dir:.
osv-scanner --lockfile package-lock.json
npm audit --production
# Generate an inventory (SBOM)
syft dir:. -o cyclonedx-json > sbom.json
```

## Prioritization
```text
- Severity (CVSS) + reachability (is the vulnerable code path actually used?)
- Exploited-in-the-wild (CISA KEV) -> patch first
- EPSS score for likelihood of exploitation
```

## Detection (Blue Team)
- Continuous dependency scanning (not just at build), alert on new CVEs in shipped versions.
- Monitor CISA KEV for components you run.

## Mitigation / Hardening
- Maintain an SBOM; automate updates (Dependabot/Renovate).
- Patch SLA by severity; remove unused dependencies.
- Pin versions + lockfiles; prefer maintained libraries.
- See also: [supply-chain/sbom-cosign](../../devsecops/supply-chain/sbom-cosign.md).

## Sources
- [OWASP A06:2021](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
