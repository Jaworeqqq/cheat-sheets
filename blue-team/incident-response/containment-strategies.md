---
title: "Containment strategies"
category: "blue-team"
tags: ["incident-response", "containment"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# Containment strategies

## TL;DR
Containment stops the incident from spreading while preserving evidence and business function. The hard part is timing and trade-offs: contain too early and you tip off the attacker / lose intel; too late and damage spreads. Balance short-term (immediate stop) vs long-term (stable control while eradicating).

## Short-term vs long-term
```text
Short-term  – immediate actions to halt spread (isolate host, disable account, block C2).
Long-term   – stable measures while you eradicate + recover (temporary rules, rebuilt segments).
```

## Containment options (by asset)
```text
Endpoint  – network isolation via EDR (keeps it up for forensics) > pull cable > power off (last;
            loses RAM). Snapshot memory/disk before drastic action.
Identity  – disable/reset account, REVOKE SESSIONS/TOKENS (critical for cloud/SaaS/AiTM),
            reset krbtgt x2 (AD), remove attacker MFA/app grants.
Network   – block C2 (firewall/DNS sinkhole), segment/quarantine VLAN, egress cutoff.
Cloud     – restrict SG/policy, deactivate keys, quarantine instance (preserve for forensics).
Account/app – revoke OAuth grants, remove malicious inbox rules, rotate secrets.
```

## The evidence-vs-speed trade-off
```text
- Powering off destroys volatile memory (RAM = malware, keys, network state). Isolate instead
  when you can, to keep the host live for forensics.
- Snapshot/image BEFORE eradication where feasible (see dfir-triage).
- For ransomware actively encrypting, speed usually wins — isolate fast.
```

## Watch-and-learn vs immediate containment
```text
- Sometimes monitoring an attacker (in a controlled way) yields scope/attribution before you act.
- Risk: they may detect monitoring or cause damage. Decision belongs to IR lead + leadership
  (documented in the IR policy). Default to containment when impact is high or uncertain.
```

## Avoid tipping off the attacker (when watching)
```text
- Don't clean one host and leave others (they'll notice and burn persistence / escalate).
- Coordinate a SIMULTANEOUS containment across all known footholds ("big bang" eviction)
  once scoping is complete — piecemeal cleanup lets them adapt.
```

## Sources
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · related: [ir-process](./ir-process.md), [dfir-triage](../digital-forensics/dfir-triage.md), [cloud-ir-aws](./cloud-ir-aws.md)
