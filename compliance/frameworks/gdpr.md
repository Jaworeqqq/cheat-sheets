---
title: "GDPR – basics"
category: "compliance"
tags: ["compliance", "gdpr", "privacy"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# GDPR

## TL;DR
The EU regulation on personal data protection. Applies to anyone processing the data of people in the EU. Fines up to €20M or 4% of global turnover. Security is Article 32; breach notification within 72h.

## Key principles (Art. 5)
```text
- Lawfulness, fairness, transparency
- Purpose limitation             - Data minimization
- Accuracy                       - Storage limitation
- Integrity and confidentiality (security)  - Accountability
```

## Lawful bases for processing (Art. 6)
```text
consent · contract · legal obligation · vital interests · public task · legitimate interest
```

## Data subject rights
```text
access · rectification · erasure ("right to be forgotten") ·
restriction · portability · objection · no automated decision-making
```

## Security (Art. 32) – "appropriate measures"
```text
- Pseudonymization and encryption
- Confidentiality, integrity, availability, resilience of systems
- Ability to restore quickly after an incident
- Regular testing of the effectiveness of measures
```

## Breaches (Art. 33/34)
```text
- Notify the supervisory authority (e.g. the local DPA) within 72h of becoming aware.
- Notify individuals if high risk to their rights.
- Breach register (even for non-reportable ones).
```

## In practice for tech teams
- Data mapping (RoPA – record of processing activities), DPIA for risky processing.
- Privacy by design/default, minimization, retention, DLP, encryption, access control.
- Processing agreements (DPAs) with processors, transfers outside the EEA (SCCs).

## Sources
- [GDPR text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [European Data Protection Board](https://edpb.europa.eu/)
