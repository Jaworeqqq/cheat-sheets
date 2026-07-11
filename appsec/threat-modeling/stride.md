---
title: "Threat modeling – STRIDE"
category: "appsec"
tags: ["threat-modeling", "stride", "design"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Threat modeling – STRIDE

## TL;DR
A structured way to find threats at design time. STRIDE = 6 threat categories, each opposing a security property. Answers 4 questions: what are we building, what can go wrong, what do we do about it, did we do a good job.

## STRIDE
| Threat | Violates | Example | Control |
|--------|----------|---------|---------|
| **S**poofing | Authentication | impersonating a user/service | MFA, mutual TLS, strong identities |
| **T**ampering | Integrity | modifying data/code | signing, HMAC, validation, WORM |
| **R**epudiation | Non-repudiation | denying an action | audit logs, timestamping |
| **I**nformation Disclosure | Confidentiality | data leak | encryption, least privilege |
| **D**enial of Service | Availability | resource exhaustion | rate limit, quotas, autoscaling |
| **E**levation of Privilege | Authorization | privesc | authz, sandboxing, least priv |

## Process
```text
1. Diagram (DFD)  – processes, data stores, external entities, data flows, trust boundaries
2. Enumeration    – walk STRIDE for each element/flow
3. Risk rating    – likelihood x impact (or DREAD)
4. Mitigations    – a control per threat; accept/transfer/reduce
5. Verification   – tests confirming the controls
```

## Tips
- Focus attention on **trust boundaries** (that's where threats live).
- Do it early (design) and update on architecture changes.
- Tools: Microsoft Threat Modeling Tool, OWASP Threat Dragon, "elevation of privilege" question cards.

## Sources
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) · [Threat Dragon](https://owasp.org/www-project-threat-dragon/) · *Threat Modeling* (Shostack)
