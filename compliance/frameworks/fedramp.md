---
title: "FedRAMP"
category: "compliance"
tags: ["compliance", "fedramp", "cloud", "government"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# FedRAMP

## TL;DR
FedRAMP (Federal Risk and Authorization Management Program) is the US government's standardized program for authorizing cloud services (CSPs) for federal use. It's built on NIST SP 800-53 controls with cloud-specific baselines, an assessment by a 3PAO, and an ongoing authorization (ATO) with continuous monitoring.

## Impact levels (baselines)
```text
Low       – limited impact if compromised (~150+ controls). LI-SaaS for low-risk SaaS.
Moderate  – most federal data; the common target (~300+ controls).
High      – sensitive data (law enforcement, health, financial) (~400+ controls).
Baselines derive from NIST 800-53 (see frameworks/nist-800-53) + FedRAMP additions.
```

## Authorization paths
```text
Agency ATO   – a federal agency sponsors and authorizes the CSP.
JAB P-ATO    – (historically) Joint Authorization Board provisional ATO; program has evolved.
Once authorized, listed in the FedRAMP Marketplace; other agencies can reuse the package.
```

## The process (high level)
```text
1. Readiness – (optional) RAR with a 3PAO; document the system (SSP).
2. Implement – controls per the baseline; write the System Security Plan (SSP).
3. Assess    – an accredited 3PAO independently tests controls (SAP/SAR).
4. Authorize – agency reviews the package -> issues an ATO (accepts residual risk in a POA&M).
5. Monitor   – continuous monitoring: monthly scans, annual assessment, POA&M management,
               significant-change requests.
```

## Key artifacts
```text
SSP    – System Security Plan (how each control is implemented).
SAP/SAR – Security Assessment Plan/Report (3PAO testing).
POA&M  – Plan of Action & Milestones (open findings + remediation timeline).
Continuous monitoring deliverables (monthly).
```

## Practical notes
```text
- Heavy lift: hundreds of controls + extensive documentation + independent assessment.
- Boundary definition is critical (what's in the authorization boundary).
- Overlaps with SOC 2 / ISO — but FedRAMP is prescriptive and government-specific.
- OSCAL increasingly used to machine-process the packages.
```

## Sources
- [FedRAMP](https://www.fedramp.gov/) · related: [nist-800-53](./nist-800-53.md), [frameworks-overview](./frameworks-overview.md)
