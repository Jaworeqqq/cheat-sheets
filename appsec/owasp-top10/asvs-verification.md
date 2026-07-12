---
title: "ASVS – using it to verify"
category: "appsec"
tags: ["owasp", "asvs", "verification", "testing"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# ASVS – using it to verify

## TL;DR
The OWASP Application Security Verification Standard (ASVS) is a catalog of testable security requirements. Where the Top 10 is awareness ("watch out for these risks"), ASVS is verification ("prove the app meets these controls"). Use it to define requirements, drive testing, and structure pentests. Practical companion to [asvs-overview](./asvs-overview.md).

## From risk to verifiable requirement
```text
Top 10 A01 (Broken Access Control) -> ASVS gives concrete, checkable requirements, e.g.:
  "Verify that access controls fail securely including when an exception occurs."
  "Verify that the application enforces access control rules on a trusted service layer."
Each requirement is a yes/no test with a level (L1/L2/L3).
```

## Choosing a level
```text
L1 – basic; achievable via black-box testing. Minimum for all apps.
L2 – most apps handling sensitive data (recommended default). Needs some design/code insight.
L3 – high-value/critical (finance, health, life-safety). Rigorous.
Pick the level per the app's risk, then verify every requirement in scope.
```

## Using ASVS in the SDLC
```text
Requirements  – select ASVS level -> those requirements become security acceptance criteria.
Design/threat model – map controls to ASVS chapters (authn, session, access control, crypto...).
Development   – checklist for code review; write tests for requirements.
Testing/pentest – structure the engagement around ASVS (coverage, not ad hoc).
Evidence      – track which requirements pass -> a verification report (great for audits/customers).
```

## Chapters (V1-V14, overview)
```text
V1 Architecture · V2 Authentication · V3 Session Mgmt · V4 Access Control ·
V5 Validation/Encoding · V6 Cryptography · V7 Error/Logging · V8 Data Protection ·
V9 Communications · V10 Malicious Code · V11 Business Logic · V12 Files/Resources ·
V13 API/Web Service · V14 Configuration.
```

## Practical tips
```text
- Don't verify all 280+ requirements blindly — scope to the chosen level + relevant chapters.
- Automate what you can (SAST/DAST mapped to requirements); manual-test the rest.
- Produce a coverage report: requirement -> pass/fail/N/A + evidence.
```

## Sources
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · related: [asvs-overview](./asvs-overview.md), [owasp-top10-2021](./owasp-top10-2021.md)
