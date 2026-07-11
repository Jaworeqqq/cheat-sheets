---
title: "PCI DSS v4.0"
category: "compliance"
tags: ["compliance", "pci-dss", "payments"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# PCI DSS v4.0

## TL;DR
The standard for protecting payment card data (mandatory for anyone processing/storing/transmitting card data). 12 requirements across 6 goals. v4.0 is fully in force as of 31 March 2025.

## The 12 requirements
```text
Build and maintain a secure network
 1. Firewalls / network traffic control
 2. No default passwords / secure configurations
Protect cardholder data
 3. Protect stored data (minimization, encryption; NEVER store CVV)
 4. Encrypt transmission over public networks (TLS)
Manage vulnerabilities
 5. Malware protection (AV/EDR)
 6. Secure development and maintenance (secure SDLC, patching)
Strong access control
 7. Least privilege (need-to-know)
 8. Identification and authentication (MFA!)
 9. Restrict physical access
Monitor and test
 10. Log and monitor access to data/network
 11. Regular security testing (ASV scans, pentests)
Policy
 12. Information security policy
```

## New in v4.0
```text
- MFA for ALL access to the CDE (not just remote/admin).
- Customized Approach – alternative way to meet an objective (alongside Defined Approach).
- More "as-a-BAU" requirements (continuous, not just annual).
- Anti-phishing requirements, browser script management (payments), TLS requirements.
```

## Scope and validation
```text
Scope    – CDE (Cardholder Data Environment) + connected systems; segmentation shrinks scope.
Validation: SAQ (self-assessment) or RoC by a QSA; ASV scans quarterly; pentest annually.
Levels 1-4 by transaction volume.
```

## In practice
- **Reduce scope** (tokenization, segmentation, outsourcing to a PCI-compliant provider) — less CDE = fewer requirements.
- Never store full authentication data (CVV, PIN, track).

## Sources
- [PCI SSC – DSS v4.0](https://www.pcisecuritystandards.org/)
