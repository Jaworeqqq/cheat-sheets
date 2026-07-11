---
title: "DORA & NIS2 (EU)"
category: "compliance"
tags: ["compliance", "dora", "nis2", "eu", "regulation"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# DORA & NIS2 (EU regulations)

## TL;DR
Two major EU cybersecurity laws. **DORA** targets financial entities' digital operational resilience (applies since 17 Jan 2025). **NIS2** broadens cybersecurity obligations across many "essential/important" sectors (national transposition ongoing since Oct 2024).

## DORA (Digital Operational Resilience Act)
```text
Who: banks, insurers, investment firms, crypto, and their critical ICT providers.
Pillars:
 1. ICT risk management framework (governance, controls)
 2. ICT incident management + reporting (classify, report major incidents)
 3. Digital operational resilience testing (incl. threat-led pentesting / TLPT)
 4. ICT third-party risk (contracts, register, oversight of critical providers)
 5. Information sharing (threat intel)
```

## NIS2 (Network and Information Security Directive 2)
```text
Who: "essential" & "important" entities across sectors (energy, transport, health,
     digital infra, ICT service management, public admin, manufacturing, etc.).
Key duties:
 - Risk management measures (Art. 21): policies, incident handling, BC/backup,
   supply chain security, crypto, access control, MFA, vuln handling.
 - Incident reporting: early warning within 24h, notification within 72h, final report 1 month.
 - Management accountability: leadership liable, must oversee & be trained.
 - Registration with national authority; supervision + significant fines.
```

## Overlap & approach
```text
- Both are risk-based and demand incident reporting + supply-chain diligence.
- An ISO 27001 ISMS + solid IR + vendor risk program covers much of both.
- Map obligations to existing controls; focus on incident reporting timelines and
  third-party/supply-chain requirements, which are stricter than many orgs expect.
```

## In practice
- Confirm applicability & national transposition (NIS2 varies by member state).
- Tighten incident classification/reporting (clocks: NIS2 24h/72h; DORA major-incident reports).
- Build/refresh the ICT third-party register (DORA) and supply-chain security (NIS2).

## Sources
- [DORA (EU 2022/2554)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [NIS2 (EU 2022/2555)](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
