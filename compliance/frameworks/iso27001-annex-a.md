---
title: "ISO 27001:2022 – Annex A"
category: "compliance"
tags: ["compliance", "iso27001", "isms"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# ISO/IEC 27001:2022 – Annex A

## TL;DR
ISO 27001 is the standard for an information security management system (ISMS). Annex A (from ISO 27002) is a catalog of **93 controls** across 4 themes. Compliance = ISMS + Statement of Applicability + continual improvement (PDCA).

## Clause structure (4-10 = ISMS requirements)
```text
4  Context of the organization   5  Leadership
6  Planning (risk!)              7  Support (resources, awareness)
8  Operation                     9  Performance evaluation (audit, review)
10 Improvement (CAPA)
```

## Annex A – 4 themes (93 controls, 2022 version)
| Theme | # controls | Examples |
|-------|-----------|----------|
| A.5 Organizational | 37 | policies, roles, suppliers, threat intel*, incidents |
| A.6 People | 8 | screening, awareness, remote work, NDAs |
| A.7 Physical | 14 | zones, physical access, equipment, media |
| A.8 Technological | 34 | access control, crypto, logging, backups, secure dev |

\* New in 2022: threat intelligence, ICT readiness for BC, physical monitoring, config management, information deletion, data masking, DLP, web filtering, secure coding, cloud services.

## Path to certification
```text
1. ISMS scope + context
2. Risk assessment + risk treatment plan
3. Statement of Applicability (SoA) – which controls and why
4. Implement controls + evidence
5. Internal audit + management review
6. Certification audit (Stage 1 documents, Stage 2 implementation)
7. Surveillance annually, recertification every 3 years
```

## In practice
- The SoA is the heart — justify the inclusion/exclusion of each control against risk.
- Evidence: policies, logs, review records, test results. See [evidence-checklist](../audit/evidence-checklist.md).

## Sources
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) · [ISO 27002:2022 (controls)](https://www.iso.org/standard/75652.html)
