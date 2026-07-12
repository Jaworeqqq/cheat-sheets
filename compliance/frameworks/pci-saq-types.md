---
title: "PCI DSS – SAQ types"
category: "compliance"
tags: ["compliance", "pci-dss", "saq"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# PCI DSS – SAQ types

## TL;DR
A Self-Assessment Questionnaire (SAQ) is how eligible merchants validate PCI DSS compliance without a full Report on Compliance (RoC). The right SAQ depends on **how you accept cards** and how much cardholder data touches your systems. Pick wrong and you under- or over-scope.

## SAQ types (choose by acceptance channel)
```text
SAQ A     – e-commerce/MOTO, ALL cardholder data functions fully outsourced
            (payment page from a PCI-compliant provider, e.g. hosted/redirect/iframe). Smallest.
SAQ A-EP  – e-commerce, your site influences the payment page but doesn't receive card data
            (e.g. direct-post / JS from your page). Much larger than A.
SAQ B     – imprint machines or standalone dial-out terminals, no electronic storage.
SAQ B-IP  – standalone, PTS-approved IP-connected terminals, no electronic storage.
SAQ C-VT  – virtual terminal, one device, no storage.
SAQ C     – payment application connected to the internet, no storage.
SAQ P2PE  – hardware PIN-entry with a validated P2PE solution. Very reduced scope.
SAQ D     – everyone else (merchants who store/process/transmit, or service providers). Largest.
```

## Choosing the right one
```text
Key question: does card data ever touch your systems?
 - Fully outsourced / hosted page -> SAQ A (minimize scope; best position).
 - Your page scripts the payment but data goes to the processor -> SAQ A-EP.
 - You handle card data directly -> SAQ D (full requirements).
Service providers almost always = SAQ D (SP) or a full RoC.
```

## Scope reduction (why it matters)
```text
- The less card data touches you, the smaller the SAQ and the fewer controls.
- Techniques: redirect/iframe hosted payment pages, tokenization, P2PE, network segmentation.
- Segmentation shrinks the CDE (Cardholder Data Environment) -> fewer in-scope systems.
```

## Validation & reporting
```text
- Complete the SAQ + Attestation of Compliance (AOC); ASV scans quarterly if applicable.
- Level (1-4) by transaction volume determines whether SAQ suffices or a QSA RoC is required.
```

## Sources
- [PCI SSC – SAQs](https://www.pcisecuritystandards.org/document_library/) · related: [pci-dss-v4](./pci-dss-v4.md)
