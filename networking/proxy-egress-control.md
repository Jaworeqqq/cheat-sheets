---
title: "Proxy & egress control"
category: "networking"
tags: ["networking", "egress", "proxy", "exfiltration"]
platform: "agnostic"
mitre: ["T1071", "T1048"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Proxy & egress control

## TL;DR
Most networks tightly control inbound traffic but let outbound (egress) flow freely — a gap attackers exploit for C2, tunneling, and data exfiltration. Egress control (default-deny outbound via a forward proxy + firewall) is one of the highest-impact, most-neglected defenses.

## Why egress control matters
```text
- Reverse shells / C2 rely on the compromised host connecting OUT. Block that and you break them.
- Data exfiltration leaves via egress — DLP + proxy inspection catch/stop it.
- DNS/HTTP(S) tunneling needs an egress path; controlling it removes covert channels.
```

## Controls
```text
Default-deny egress firewall – allow only required destinations/ports (allow-list).
Forward proxy (explicit)     – all web traffic through a logging/inspecting proxy; block direct outbound.
TLS inspection               – decrypt+inspect where policy/law allows (privacy trade-off);
                               otherwise rely on SNI/JA3/domain category + endpoint telemetry.
DNS control                  – internal resolvers only; block external :53 + unsanctioned DoH.
URL/category filtering       – block uncategorized/newly-registered/known-bad domains.
Cloud egress                 – NAT + egress firewall / private endpoints; restrict SG egress.
```

## Allow-listing approach
```text
- Servers: usually a SMALL, known set of outbound needs (updates, APIs) -> strict allow-list.
- Workstations: broader, but still block direct outbound (force through proxy), filter categories.
- Block egress to cloud metadata (169.254.169.254) to blunt SSRF->credential theft.
```

## What good egress control catches
```text
- Reverse shells / C2 beaconing to non-allowed destinations.
- DNS/ICMP/HTTP tunneling; large uploads to fresh/unusual domains.
- Malware calling home; LOLBins downloading second stages.
```

## Detection (Blue Team)
- Proxy/firewall logs: denied outbound (recon/C2 attempts), beaconing patterns, exfil volume anomalies.
- Direct-to-internet attempts bypassing the proxy; connections to young/rare domains.

## Mitigation / Hardening
- Default-deny egress + forward proxy + DNS control + metadata blocking + logging to SIEM.
- Tight allow-lists for servers; category/reputation filtering for users; DLP on the proxy.
- Related: [firewall-fundamentals](./firewall-fundamentals.md), [beaconing-detection](../blue-team/threat-hunting/beaconing-detection.md), [exfil-channels](../red-team/exfiltration/exfil-channels.md).

## Sources
- [SANS – Egress Filtering](https://www.sans.org/) · [MITRE T1048](https://attack.mitre.org/techniques/T1048/)
