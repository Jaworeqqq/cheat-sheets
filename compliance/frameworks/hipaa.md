---
title: "HIPAA"
category: "compliance"
tags: ["compliance", "hipaa", "healthcare", "privacy"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# HIPAA

## TL;DR
US law protecting health information (PHI). Applies to covered entities (providers, plans, clearinghouses) and their business associates. The Security Rule defines safeguards for electronic PHI (ePHI); the Privacy Rule governs use/disclosure; the Breach Notification Rule sets reporting.

## Key rules
```text
Privacy Rule        – how PHI may be used/disclosed; patient rights (access, amendment).
Security Rule       – safeguards for ePHI (administrative, physical, technical).
Breach Notification – notify individuals/HHS (and sometimes media) after a breach.
Enforcement Rule    – investigations, penalties (OCR).
```

## Security Rule safeguards
```text
Administrative (largest set)
 - Risk analysis & management, sanction policy, workforce training
 - Access management, contingency plan (backup/DR), incident procedures
Physical
 - Facility access controls, workstation/device security, media disposal
Technical
 - Access control (unique IDs, auto-logoff, encryption)
 - Audit controls (logging), integrity, transmission security (encryption in transit)
```
Requirements are "Required" or "Addressable" (addressable = implement or document why an equivalent is used — not optional to ignore).

## Breach notification
```text
- Notify affected individuals without unreasonable delay, within 60 days.
- Notify HHS: <500 affected -> annual log; >=500 -> within 60 days (+ media).
- Business associates notify the covered entity.
```

## In practice (tech teams)
```text
- Encrypt ePHI at rest and in transit (encryption is an addressable safe harbor for breach).
- Unique user IDs, MFA, least privilege, audit logging of ePHI access.
- Business Associate Agreements (BAAs) with any vendor touching ePHI.
- Documented risk analysis is the #1 thing OCR asks for.
```

## Sources
- [HHS – HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html) · [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html)
