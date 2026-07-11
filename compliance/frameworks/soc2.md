---
title: "SOC 2"
category: "compliance"
tags: ["compliance", "soc2", "attestation"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SOC 2

## TL;DR
An AICPA attestation report (not a certification) where an independent auditor evaluates a service organization's controls against the Trust Services Criteria. Common ask from B2B/SaaS customers in the US.

## Trust Services Criteria (TSC)
```text
Security (Common Criteria) – REQUIRED baseline for every SOC 2
Availability   – system uptime/SLA, DR
Processing Integrity – complete, accurate, timely processing
Confidentiality – protection of confidential info
Privacy        – handling of personal information (notice, choice, etc.)
```
You choose which criteria apply beyond Security.

## Type I vs Type II
```text
Type I  – controls suitably DESIGNED at a point in time.
Type II – controls OPERATED EFFECTIVELY over a period (typically 3–12 months). More valued.
```

## Common Criteria (CC) areas
```text
CC1 Control environment      CC2 Communication & information
CC3 Risk assessment          CC4 Monitoring activities
CC5 Control activities       CC6 Logical & physical access
CC7 System operations (incident/vuln)  CC8 Change management
CC9 Risk mitigation (vendors)
```

## Path to a report
```text
1. Scope (which TSC, which systems), gap assessment.
2. Implement controls, define policies, start collecting evidence.
3. Type I (optional) to show design.
4. Observation period (Type II), continuous evidence.
5. Auditor testing -> report (with any exceptions noted).
```

## In practice
- Evidence discipline is everything — see [audit/evidence-checklist](../audit/evidence-checklist.md).
- Automate evidence (Vanta/Drata/Secureframe) mapped to CC controls.
- Maps closely to ISO 27001 controls — do both efficiently via a crosswalk.

## Sources
- [AICPA – SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) · [Trust Services Criteria](https://www.aicpa-cima.com/)
