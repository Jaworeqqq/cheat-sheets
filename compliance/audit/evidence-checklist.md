---
title: "Audit – evidence checklist"
category: "compliance"
tags: ["compliance", "audit", "evidence"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Audit – evidence collection

## TL;DR
An auditor verifies that a control is **designed** and **operating**. Good evidence: current, complete, repeatable, tied to the audit period. Collect continuously, not the night before the audit.

## Types of evidence
```text
- Policies and procedures (approved, versioned, with a review date)
- Configuration screenshots (MFA on, encryption, log retention)
- Logs/records (access, changes, reviews) for the whole audit period
- Tickets (change management, incidents, access) with approvals
- Test results (vuln scans, pentests, DR test, backup restore)
- Registers (risks, assets, training, suppliers)
```

## Checklist by area
```text
Access control    – access reviews (quarterly), offboarding list, MFA enforcement
Change management – tickets with approval, CI/CD logs, no unapproved changes
Logging/monitoring – retention, alerts, samples of alert response
Backups           – schedule, backup success log, restore test evidence
Vuln management   – scans, remediation SLA, evidence criticals are patched
Incident response – runbooks, incident records, post-mortems
Suppliers         – DPAs/contracts, risk reviews, suppliers' SOC 2
HR/awareness      – training logs, screening, NDAs
```

## Best practices
- **Automate** collection (Drata/Vanta/Secureframe or your own scripts + evidence store).
- Sampling: the auditor will pick random cases — evidence must cover the whole period.
- Tie each piece of evidence to a specific control (control → evidence mapping).

## Sources
- [AICPA SOC 2](https://www.aicpa-cima.com/) · [ISO 27001 Annex A](../frameworks/iso27001-annex-a.md)
