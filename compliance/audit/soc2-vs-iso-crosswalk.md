---
title: "SOC 2 ↔ ISO 27001 crosswalk"
category: "compliance"
tags: ["compliance", "soc2", "iso27001", "crosswalk"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SOC 2 ↔ ISO 27001 crosswalk

## TL;DR
SOC 2 and ISO 27001 overlap heavily — the same underlying controls satisfy both. Doing them together (map once, evidence once) is far cheaper than running two separate programs. This is the mental model, not a certified mapping.

## Fundamental differences
```text
                SOC 2                        ISO 27001
Type            Attestation (auditor report)  Certification (accredited body)
Framework       Trust Services Criteria       ISMS + Annex A controls
Geography       Primarily US/B2B              Global
Output          Report (Type I/II)            Certificate (3-year cycle)
Core idea       "controls meet criteria"      "a managed system + controls"
```

## Concept mapping
```text
SOC 2 Common Criteria (CC)          ~ ISO 27001 clause / Annex A
CC1 Control environment             ~ Clause 5 (leadership), A.5 (org policies)
CC2 Communication & information     ~ A.5, Clause 7.4
CC3 Risk assessment                 ~ Clause 6 (planning/risk), A.5
CC4 Monitoring                      ~ Clause 9 (evaluation), A.8 logging
CC5 Control activities              ~ Annex A controls broadly
CC6 Logical & physical access       ~ A.5/A.7/A.8 (access, physical, technical)
CC7 System operations               ~ A.8 (vuln, incident, monitoring)
CC8 Change management               ~ A.8 change management
CC9 Risk mitigation (vendors)       ~ A.5 supplier relationships
```

## Shared control examples (evidence once)
```text
- Access reviews, MFA, least privilege        (CC6  ~ A.8.2/A.8.3)
- Change management with approvals            (CC8  ~ A.8.32)
- Vulnerability & patch management            (CC7  ~ A.8.8)
- Incident response process                   (CC7  ~ A.5.24-A.5.28)
- Vendor risk / DPAs                          (CC9  ~ A.5.19-A.5.23)
- Logging & monitoring                        (CC7  ~ A.8.15/A.8.16)
```

## Running both efficiently
```text
- Build one control set; tag each control with SOC 2 CC + ISO Annex A refs.
- Collect evidence once, reuse for both audits.
- ISO adds: formal ISMS (scope, SoA, internal audit, management review).
- SOC 2 adds: auditor testing over a period (Type II), TSC selection.
```

## Sources
- [ISO 27001 Annex A](../frameworks/iso27001-annex-a.md) · [SOC 2](../frameworks/soc2.md) · [Secure Controls Framework](https://securecontrolsframework.com/)
