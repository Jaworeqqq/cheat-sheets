---
title: "Third-party / vendor risk management"
category: "compliance"
tags: ["risk-management", "vendor-risk", "tprm", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Third-party / vendor risk management (TPRM)

## TL;DR
Your security posture inherits your vendors' weaknesses. TPRM assesses, contracts, and monitors third parties handling your data or systems. Increasingly mandated (DORA, NIS2, GDPR processors, SOC 2 CC9).

## Lifecycle
```text
1. Intake/tiering   – classify vendor by data access + criticality (Tier 1/2/3).
2. Due diligence    – assess before onboarding (questionnaire, evidence, scans).
3. Contracting      – security terms, DPA, right to audit, breach notification SLAs.
4. Ongoing monitoring – periodic reassessment, continuous ratings, alerting.
5. Offboarding      – revoke access, data return/deletion, confirm.
```

## Risk tiering (drives depth of review)
```text
Tier 1 (critical) – hosts/processes sensitive data, or business-critical availability
                    -> full assessment, SOC 2/ISO evidence, pentest, annual review.
Tier 2 (moderate) – limited data / integration -> questionnaire + key evidence.
Tier 3 (low)      – no sensitive data -> lightweight check.
```

## Due-diligence evidence to request
```text
- SOC 2 Type II report or ISO 27001 certificate (+ SoA/scope)
- Pentest summary, vuln management process, security whitepaper
- Data flows: what data, where stored, sub-processors, region (transfers)
- Incident history + breach notification commitments
- Questionnaire (SIG, CAIQ) for cloud/SaaS
```

## Contract must-haves
```text
- DPA (GDPR) if processing personal data; sub-processor controls
- Breach notification timelines (align to your regulatory clocks)
- Right to audit / evidence, security requirements, data return/deletion
- Liability, and for DORA: register entry + oversight for critical ICT providers
```

## Ongoing monitoring
```text
- Periodic reassessment by tier; re-collect SOC 2/ISO annually.
- Continuous monitoring (security ratings, breach news, CT/exposure).
- Track a vendor register/inventory (also a DORA/NIS2 requirement).
```

## Sources
- [Shared Assessments (SIG)](https://sharedassessments.org/) · [CSA CAIQ](https://cloudsecurityalliance.org/) · related: [dora-nis2](../frameworks/dora-nis2.md)
