---
title: "Security metrics & KRIs"
category: "compliance"
tags: ["risk-management", "metrics", "kri", "kpi"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Security metrics & KRIs

## TL;DR
You can't manage what you don't measure. Security metrics turn activity into evidence of effectiveness and risk. KPIs measure performance ("are we doing the work?"); KRIs (Key Risk Indicators) are early-warning signals that risk is rising. Good metrics are actionable, trended, and tied to decisions.

## KPI vs KRI
```text
KPI (performance) – how well a control/process operates (e.g. % systems patched within SLA).
KRI (risk)        – a leading indicator that risk exposure is increasing (e.g. count of
                    internet-exposed systems with critical CVEs). Set thresholds -> alert/escalate.
```

## Useful metrics by area
```text
Vulnerability mgmt – MTTR to remediate (by severity), % criticals patched within SLA, open-vuln aging.
Detection & response – MTTD / MTTR for incidents, alert volume + false-positive rate, dwell time.
Access             – # standing privileged accounts, orphaned/stale accounts, MFA coverage %.
Attack surface     – # internet-exposed services, expiring certs, shadow IT discovered.
Awareness          – phishing-simulation click/report rate, training completion %.
Third party        – # vendors overdue for review, high-risk vendors.
Compliance         – control test pass rate, overdue POA&M/CAPA items.
```

## Example KRIs (with thresholds)
```text
- Critical vulns open >30 days: green <5, amber 5-15, red >15.
- Privileged accounts without MFA: red if >0.
- Mean time to detect > target -> investigate detection gaps.
- Failed backup restores / untested DR beyond cadence.
```

## Making metrics useful
```text
- Actionable: each metric maps to a decision/owner (not vanity numbers).
- Trended: track over time; direction matters more than a single value.
- Contextual: normalize (per asset/user), tie to risk appetite thresholds.
- Audience-fit: technical detail for teams; risk-in-business-terms for leadership/board.
- Automate collection (SIEM/GRC/vuln tools) — manual metrics rot.
```

## Sources
- [NIST SP 800-55 (measurement)](https://csrc.nist.gov/pubs/sp/800/55/r2/final) · [FAIR (risk quantification)](https://www.fairinstitute.org/) · related: [risk-assessment](./risk-assessment.md)
