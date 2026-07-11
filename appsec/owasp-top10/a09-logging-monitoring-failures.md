---
title: "A09 – Security Logging and Monitoring Failures"
category: "appsec"
tags: ["owasp", "logging", "monitoring", "detection"]
platform: "web"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# A09 – Security Logging and Monitoring Failures

## TL;DR
Without adequate logging, detection and response, breaches go unnoticed. This is what lets attackers dwell for months. The bridge between AppSec and the Blue Team.

## Common failures
```text
- Auth events (login, failure, privilege change) not logged
- No alerting on suspicious activity (thresholds, anomalies)
- Logs stored only locally / not tamper-resistant / short retention
- Logs contain sensitive data (passwords, tokens, PII) — a new risk
- No incident response plan tied to alerts
```

## What to log
```text
- Authentication: success, failure, logout, MFA events
- Authorization: access-control failures, privilege changes
- Input validation failures, high-value transactions
- Include: who, what, when, where (source IP), outcome — NOT secrets
```

## Detection (Blue Team)
- This category *is* detection — ensure coverage of ATT&CK-relevant events.
- Test detections against Atomic Red Team; measure MTTD.

## Mitigation / Hardening
- Centralized, tamper-evident logging (SIEM), sufficient retention.
- Alerting with tuned thresholds; runbooks tied to alerts (see blue-team/incident-response).
- Redact/avoid secrets in logs; monitor log integrity and gaps.
- Regularly exercise detection + response (purple teaming).

## Sources
- [OWASP A09:2021](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) · [blue-team/logging-monitoring](../../blue-team/logging-monitoring/windows-event-ids.md)
