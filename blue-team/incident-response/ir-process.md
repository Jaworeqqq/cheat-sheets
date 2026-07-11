---
title: "Incident Response process (NIST)"
category: "blue-team"
tags: ["incident-response", "process", "nist"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# IR process – NIST 800-61

## TL;DR
Four phases: Preparation → Detection & Analysis → Containment/Eradication/Recovery → Post-Incident. SANS breaks it into 6 (PICERL).

## Phases
```text
1. Preparation      – tooling, runbooks, break-glass access, contacts, exercises
2. Detection&Analysis – alert triage, scoping, severity classification, timeline
3. Containment      – short-term (isolation) + long-term (patch, temporary controls)
   Eradication      – remove malware/persistence, fix root cause
   Recovery         – restore services, watch for the attacker's return
4. Post-Incident    – lessons learned, detection updates, report
```

## Severity classification (example)
| Sev | Criterion | Response |
|-----|-----------|----------|
| SEV1 | Critical systems / data / active attack | 24/7, escalate immediately |
| SEV2 | Limited scope, escalation potential | hours |
| SEV3 | Single host, low impact | business day |

## Evidence collection – order of volatility (RFC 3227)
```text
1. CPU registers/cache        2. RAM / routing tables / ARP
3. Processes / network connections  4. Disk       5. Remote logs / config    6. Archival media
```

## Documentation (chain of custody)
- Who, what, when, from where; hash of each artifact; each handoff.

## Mitigation / Hardening
- Regular tabletop exercises, ready runbooks per scenario, tested backups.

## Sources
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [SANS PICERL](https://www.sans.org/)
