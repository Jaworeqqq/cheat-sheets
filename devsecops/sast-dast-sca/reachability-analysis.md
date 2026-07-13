---
title: "Reachability analysis (SCA noise reduction)"
category: "devsecops"
tags: ["sca", "vulnerability-management", "reachability"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# Reachability analysis

## TL;DR
SCA tools flag every CVE in every dependency — most of which your code never actually calls. Reachability analysis determines whether the vulnerable function is genuinely invokable from your application, cutting the alert backlog dramatically so teams fix what matters. The key question: "does our code path reach the vulnerable code?"

## The problem it solves
```text
- A typical app has thousands of transitive dependencies -> hundreds of CVEs.
- Many are in code paths you never execute (unused features, dev-only, unreachable functions).
- Fixing everything is impossible; ignoring everything is dangerous. Reachability prioritizes.
```

## Levels of "does this matter"
```text
1. Is the vulnerable PACKAGE present?          (basic SCA — noisy)
2. Is the vulnerable VERSION present?          (version match)
3. Is the vulnerable FUNCTION/symbol imported/called? (reachability — call graph)
4. Is it reachable from an ENTRY POINT with attacker-controlled input? (exploitability)
5. Is it exploitable given mitigations/config? (highest confidence)
```

## How reachability works
```text
- Build a call graph of your code + dependencies.
- Check whether the specific vulnerable function (from the advisory) is on a path
  reachable from your application's entry points.
- Reachable + attacker-influenced input => prioritize; unreachable => deprioritize/defer.
```

## Tooling
```text
- Semgrep Supply Chain, Snyk (reachable vulns), Endor Labs, Socket, OSS analyses.
- Combine with EPSS (exploit likelihood) + CISA KEV (exploited in the wild) for prioritization.
```

## Using it well
```text
- Fix: reachable + high severity + KEV/high EPSS first.
- Defer (with tracking): unreachable low/medium — but re-check when code changes.
- Don't blanket-suppress by "unreachable" forever; reachability changes as your code evolves.
- Document decisions (VEX — Vulnerability Exploitability eXchange — standardizes "not affected").
```

## VEX (communicating exploitability)
```text
VEX statements assert a product's status for a CVE: affected / not affected / fixed / under investigation
(with justification, e.g. "vulnerable code not in the execution path"). Pairs with SBOM.
```

## Sources
- [CISA – VEX](https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-use-cases) · related: [sast-dast-sca](./sast-dast-sca.md), [a06-vulnerable-components](../../appsec/owasp-top10/a06-vulnerable-components.md)
