---
title: "Continuous third-party monitoring"
category: "compliance"
tags: ["risk-management", "tprm", "vendor-risk", "monitoring"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Continuous third-party monitoring

## TL;DR
A point-in-time vendor assessment is stale the day after it's done. Continuous monitoring tracks a vendor's risk posture between formal reviews — catching breaches, deteriorating security, and exposure in near-real-time. Increasingly expected by regulators (DORA, NIS2) that emphasize ongoing oversight of critical providers.

## Why continuous (vs annual questionnaires)
```text
- A vendor assessed as "secure" in January can be breached in March.
- Fourth-party (your vendor's vendors) risk changes constantly.
- Questionnaires are self-reported snapshots; continuous signals are external + timely.
```

## What to monitor
```text
Security ratings   – external scan-based scores (exposed services, patching, cert hygiene) trending down.
Breach news        – the vendor (or their sub-processors) appearing in breach reports / leak sites.
Attack surface     – new exposed assets, expired certs, leaked credentials tied to the vendor.
Compliance status  – lapsed SOC 2 / ISO certs; overdue reassessments.
Concentration risk – over-reliance on one critical provider (DORA concern).
Financial/news     – business viability signals for critical vendors.
```

## How to operationalize
```text
1. Tier vendors (see vendor-risk); monitor Tier 1/critical most intensively.
2. Use security-rating services + threat intel + your own attack-surface monitoring on vendor domains.
3. Set thresholds/alerts (rating drop, breach mention) -> trigger reassessment or escalation.
4. Maintain a live vendor register (also a DORA/NIS2 requirement) with current status.
5. Contractually require timely breach notification + right to reassess.
```

## From signal to action
```text
- Rating drop / new exposure -> ad-hoc reassessment; request remediation evidence.
- Vendor breach -> assess YOUR exposure (what data/access they hold); IR if impacted.
- Repeated issues -> risk-accept with sign-off, add compensating controls, or offboard.
```

## Tooling
```text
Security ratings (SecurityScorecard/BitSight-style), CTI feeds, ASM on vendor domains,
GRC platforms that track vendor status + evidence + reassessment cadence.
```

## Sources
- [Shared Assessments](https://sharedassessments.org/) · related: [vendor-risk](./vendor-risk.md), [dora-nis2](../frameworks/dora-nis2.md), [continuous-compliance](../audit/continuous-compliance.md)
