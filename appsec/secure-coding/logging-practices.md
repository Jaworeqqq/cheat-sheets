---
title: "Secure logging practices"
category: "appsec"
tags: ["secure-coding", "logging", "detection"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-13"
author: "core"
---

# Secure logging practices

## TL;DR
Good application logging enables detection and investigation (OWASP A09); bad logging leaks secrets, enables injection, or provides nothing useful during an incident. Log security-relevant events with enough context — but never sensitive data — and protect the logs themselves.

## What to log (security events)
```text
- Authentication: login success/failure, logout, MFA events, password/credential changes.
- Authorization: access-control failures, privilege changes.
- Input validation failures, high-value transactions, admin actions.
- Include: timestamp (UTC), who (user/session), what (action + outcome), where (source IP),
  and a correlation/request ID. Enough to reconstruct an incident.
```

## What NOT to log (a real risk)
```text
- Passwords, tokens, session IDs, API keys, secrets.
- Full PII/PAN, health data (privacy + PCI/GDPR violations).
- Full request bodies with sensitive fields.
-> Redact/mask before logging; treat logs as potentially exposed.
```

## Log injection (don't let logs become an attack)
```text
- Untrusted input in logs can forge entries or exploit log viewers (CRLF injection, fake lines).
- Worse: log libraries that evaluate input (Log4Shell — JNDI lookup in logged strings = RCE).
- Defenses: neutralize newlines/control chars; use structured logging (JSON) so input is data,
  not interpreted; keep logging libraries patched.
```

## Protecting logs
```text
- Centralize (ship off-host) so attackers can't easily erase local evidence.
- Tamper-evidence/immutability; access controls; sufficient retention (months for IR).
- Time sync (NTP) + consistent UTC timestamps for correlation.
```

## Structured logging (recommended)
```text
- Log as JSON with fields (event, user, ip, outcome, request_id) — parseable, injection-resistant.
- Consistent schema (e.g. ECS) across services -> easy SIEM correlation.
```

## Detection (Blue Team)
- These logs ARE the detection substrate — ensure coverage of ATT&CK-relevant events and ship to SIEM.
- Related: [a09-logging-monitoring-failures](../owasp-top10/a09-logging-monitoring-failures.md), blue-team [log-sources-priority](../../blue-team/siem/log-sources-priority.md).

## Sources
- [OWASP – Logging CS](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
