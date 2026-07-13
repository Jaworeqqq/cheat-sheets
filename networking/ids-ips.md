---
title: "IDS / IPS"
category: "networking"
tags: ["networking", "ids", "ips", "detection"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# IDS / IPS

## TL;DR
An IDS (Intrusion Detection System) monitors traffic and alerts on suspicious activity; an IPS (Intrusion Prevention System) sits inline and can block it. They detect via signatures (known bad) and anomalies (deviation from normal). A core network detection control that feeds the SOC.

## IDS vs IPS
```text
IDS – out-of-band (span/tap); detects + alerts; no traffic impact if it fails.
IPS – inline; can DROP/RESET malicious traffic; a failure/false-positive can block legit traffic.
NIDS/NIPS – network-based; HIDS/HIPS – host-based (endpoint).
```

## Detection methods
```text
Signature-based – match known attack patterns (fast, low FP, but misses novel/zero-day).
Anomaly-based   – baseline "normal", flag deviations (catches unknowns, more false positives).
Protocol analysis – detect protocol violations/abuse.
Reputation/IOC  – known-bad IPs/domains/hashes.
```

## Tools
```text
Suricata – high-performance IDS/IPS, multi-threaded, rich protocol logging (EVE JSON), file extraction.
Snort    – classic signature IDS/IPS.
Zeek     – network security MONITOR (not signatures) — rich logs/metadata for hunting (great with a SIEM).
Rules    – Emerging Threats / Talos rulesets; write custom rules for your environment.
```

## Placement & tuning
```text
- Placement: perimeter (north-south) AND internal (east-west) for lateral movement.
- Encrypted traffic: IDS sees little inside TLS -> pair with TLS inspection or rely on
  metadata/JA3 + endpoint telemetry. Decryption has privacy/perf trade-offs.
- Tune aggressively: disable irrelevant rules, suppress known-good, prioritize by severity.
- IPS: start in IDS/alert mode, validate, then enable blocking on high-confidence rules.
```

## Where it fits (defense-in-depth)
```text
- Complements EDR (endpoint) + firewall (access) + NDR/SIEM (analytics).
- Zeek logs feed threat hunting (beaconing, DNS anomalies — see blue-team hunts).
- Not a silver bullet: encrypted C2, novel attacks, and insider misuse need more than signatures.
```

## Detection (Blue Team)
- Feed IDS/IPS alerts + Zeek logs to the SIEM; correlate with endpoint/identity for context.

## Sources
- [Suricata](https://suricata.io/) · [Zeek](https://zeek.org/) · related: [beaconing-detection](../blue-team/threat-hunting/beaconing-detection.md), [firewall-fundamentals](./firewall-fundamentals.md)
