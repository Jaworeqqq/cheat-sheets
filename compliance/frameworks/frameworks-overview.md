---
title: "Security frameworks – overview"
category: "compliance"
tags: ["compliance", "frameworks", "grc"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Security frameworks – overview

## TL;DR
A comparison cheat sheet of the most important standards: purpose, whether it's mandatory, who needs it. Many controls overlap — map once, satisfy many (crosswalk).

## Comparison
| Framework | Type | Who it applies to | Certification |
|-----------|------|-------------------|---------------|
| ISO/IEC 27001 | ISMS (management system) | any org | yes, external audit |
| SOC 2 | attestation (Trust Services) | SaaS/service providers (US) | auditor report (Type I/II) |
| NIST CSF 2.0 | voluntary framework | any org | no (self-assessment) |
| NIST 800-53 | control catalog | US federal agencies + contractors | via FedRAMP/RMF |
| PCI DSS v4.0 | industry requirement | anyone processing payment cards | yes (QSA/SAQ) |
| GDPR | law (EU) | anyone processing EU personal data | no (legal compliance) |
| HIPAA | law (US) | healthcare (PHI) | no (legal compliance) |
| CIS Controls v8 | control set (prioritized) | any org | no |

## NIST CSF 2.0 – functions
```text
GOVERN (new in 2.0) – oversight, roles, risk, policies
IDENTIFY – assets, risks
PROTECT  – preventive controls
DETECT   – detecting events
RESPOND  – incident response
RECOVER  – restoration
```

## In practice
- **Map controls across standards** (e.g. Secure Controls Framework, CIS crosswalk) — one implementation, many compliances.
- Start with CIS Controls (practical, prioritized), formalize via ISO 27001.

## Related
- [ISO 27001 Annex A](./iso27001-annex-a.md) · [NIST CSF](./nist-csf.md) · [PCI DSS](./pci-dss-v4.md)

## Sources
- [NIST CSF](https://www.nist.gov/cyberframework) · [CIS Controls](https://www.cisecurity.org/controls) · [ISO 27001](https://www.iso.org/standard/27001)
