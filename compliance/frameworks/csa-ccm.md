---
title: "CSA Cloud Controls Matrix (CCM)"
category: "compliance"
tags: ["compliance", "cloud", "csa", "ccm"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# CSA Cloud Controls Matrix (CCM)

## TL;DR
The Cloud Security Alliance's Cloud Controls Matrix is a cloud-specific control framework: a catalog of controls across domains, mapped to other standards (ISO 27001, NIST, PCI, SOC 2), with a shared-responsibility lens. The companion CAIQ questionnaire is how cloud customers assess providers.

## What it is
```text
- A cloud-focused control framework (CCM v4): ~197 controls across 17 domains.
- Each control maps to major standards (ISO 27001/27017/27018, NIST 800-53, PCI, SOC 2, etc.)
  -> assess once, demonstrate multiple.
- Explicit shared-responsibility guidance (what the CSP vs the customer owns).
```

## Domains (examples)
```text
IAM (identity & access), DSP (data security & privacy), CEK (cryptography & key mgmt),
IVS (infra & virtualization), TVM (threat & vuln mgmt), LOG (logging & monitoring),
IPY (interoperability/portability), GRC (governance), BCR (business continuity),
AIS (application & interface security), SEF (incident response), STA (supply chain/3rd party)... (17 total)
```

## CAIQ (the assessment tool)
```text
Consensus Assessments Initiative Questionnaire – a set of yes/no questions per CCM control.
- CSPs complete it to document their control implementation.
- Customers use it in vendor due diligence (see risk-management/vendor-risk).
- Published CAIQs live in the CSA STAR registry.
```

## CSA STAR
```text
Security, Trust, Assurance and Risk registry:
 Level 1 – self-assessment (CAIQ published).
 Level 2 – third-party audit/certification (STAR Certification/Attestation, often with ISO 27001 or SOC 2).
```

## How to use it
```text
- Cloud provider: implement CCM controls; publish a CAIQ / pursue STAR to reduce customer questionnaires.
- Cloud customer: request the provider's CAIQ/STAR entry; use CCM to define YOUR cloud controls
  and understand the shared-responsibility split.
- Leverage mappings to avoid duplicating work across ISO/SOC 2/PCI.
```

## Sources
- [CSA CCM](https://cloudsecurityalliance.org/research/cloud-controls-matrix) · [CSA STAR registry](https://cloudsecurityalliance.org/star/) · related: [frameworks-overview](./frameworks-overview.md), [vendor-risk](../risk-management/vendor-risk.md)
