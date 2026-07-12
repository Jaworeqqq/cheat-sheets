---
title: "CIS Critical Security Controls v8"
category: "compliance"
tags: ["compliance", "cis-controls", "frameworks"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# CIS Critical Security Controls v8

## TL;DR
A prioritized, actionable set of 18 controls (down from 20) that defend against the most common attacks. More practical/tactical than ISO or NIST CSF — a great starting point: "do these, in roughly this order". Implementation Groups scale it to org size.

## The 18 controls
```text
 1. Inventory & control of enterprise assets
 2. Inventory & control of software assets
 3. Data protection
 4. Secure configuration of assets & software
 5. Account management
 6. Access control management
 7. Continuous vulnerability management
 8. Audit log management
 9. Email & web browser protections
10. Malware defenses
11. Data recovery
12. Network infrastructure management
13. Network monitoring & defense
14. Security awareness & skills training
15. Service provider management
16. Application software security
17. Incident response management
18. Penetration testing
```

## Implementation Groups (IG)
```text
IG1 – essential cyber hygiene; every org (small/limited resources). ~56 safeguards.
IG2 – orgs managing sensitive data / more resources. Builds on IG1.
IG3 – orgs with high-risk data / mature security. All safeguards.
Start with IG1 as a baseline; the first ~6 controls block a large share of attacks.
```

## Why CIS Controls
```text
- Prioritized & prescriptive (do this first) vs abstract frameworks.
- Each control has concrete "Safeguards" you can implement and measure.
- Maps to ISO 27001, NIST CSF, PCI (crosswalks) — implement once, satisfy many.
- Pairs with CIS Benchmarks (hardening configs) for control #4.
```

## Using them
```text
- Assess current state against IG1 safeguards; close gaps (asset inventory first — you can't
  protect what you don't know you have).
- Automate inventory (assets/software), vuln management, and logging early.
- Track maturity; use CIS-CAT / CSAT for measurement.
```

## Sources
- [CIS Controls v8](https://www.cisecurity.org/controls) · related: [frameworks-overview](./frameworks-overview.md), [cis-linux](../../blue-team/hardening/cis-linux.md)
