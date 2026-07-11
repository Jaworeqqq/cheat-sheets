---
title: "OWASP ASVS – overview"
category: "appsec"
tags: ["owasp", "asvs", "requirements", "sdlc"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# OWASP ASVS – overview

## TL;DR
The Application Security Verification Standard is a catalog of **verifiable** security requirements. Where the Top 10 is an awareness list of risks, ASVS is a checklist you build and test against — a measurable definition of "secure enough" for your app.

## Top 10 vs ASVS
```text
Top 10  – the 10 most critical risk categories (awareness, prioritization).
ASVS    – hundreds of specific, testable requirements across all security areas.
Use both: Top 10 to communicate risk; ASVS to define & verify controls.
```

## Levels
```text
L1 – Baseline. Achievable via black-box/pentest. Minimum for any app.
L2 – Standard. For apps handling sensitive data (most business apps). Recommended target.
L3 – Advanced. For high-value/critical apps (health, finance, life-safety).
Higher levels ADD requirements (they're cumulative), and demand more design/code evidence.
```

## Chapters (V1–V14)
```text
V1  Architecture, design & threat modeling
V2  Authentication
V3  Session management
V4  Access control
V5  Validation, sanitization & encoding (injection)
V6  Stored cryptography
V7  Error handling & logging
V8  Data protection
V9  Communication (TLS)
V10 Malicious code
V11 Business logic
V12 Files & resources
V13 API & web service
V14 Configuration
```
(Chapter numbering evolves between ASVS versions; check the version you adopt.)

## Using ASVS in the SDLC
```text
- Pick a target level (usually L2) per app based on data sensitivity.
- Turn applicable requirements into acceptance criteria / security user stories.
- Map each requirement to a control + a test (SAST/DAST/manual) -> verifiable.
- Use as a pentest scope and a code-review checklist.
- Track coverage; gaps become backlog items.
```

## Relation to other sheets
- Risk framing: [owasp-top10-2021](./owasp-top10-2021.md); design: [threat-modeling/stride](../threat-modeling/stride.md).
- Requirements often map to specific defenses (auth, injection, crypto) covered across `appsec/`.

## Sources
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [ASVS GitHub](https://github.com/OWASP/ASVS)
