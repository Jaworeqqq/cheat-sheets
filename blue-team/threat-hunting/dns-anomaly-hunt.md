---
title: "Hunting DNS anomalies"
category: "blue-team"
tags: ["threat-hunting", "dns", "detection", "c2"]
platform: "agnostic"
mitre: ["T1071.004", "T1568"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Hunting DNS anomalies

## TL;DR
DNS is a favorite covert channel: C2 beaconing, tunneling (exfil), and DGA malware all leave DNS fingerprints. Hunt for entropy, volume, and timing anomalies in DNS telemetry. Requires DNS query logging (resolver logs, Sysmon 22, Zeek/Suricata).

## What to hunt
```text
Tunneling   – long/high-entropy subdomain labels, many TXT/NULL/CNAME, high query volume to one domain.
DGA         – bursts of NXDOMAIN, random-looking domains, many unique domains per host.
Beaconing   – regular-interval lookups to the same domain (low jitter).
Fast flux   – one domain resolving to many rapidly-changing IPs.
Rare domains – young/low-prevalence domains resolved by few hosts.
```

## Hunt queries
```kql
// Sentinel/Defender: high volume of subdomains under one parent (tunneling)
DnsEvents
| extend parent = strcat(tostring(split(Name, ".")[-2]), ".", tostring(split(Name, ".")[-1]))
| summarize q = count(), uniqLabels = dcount(Name) by parent, bin(TimeGenerated, 1h)
| where uniqLabels > 100
```
```sql
-- Splunk: NXDOMAIN bursts per host (DGA signal)
index=dns rcode=NXDOMAIN
| stats count dc(query) AS unique_domains by src_ip, bin(_time, 1h)
| where unique_domains > 50
```

## Techniques
```text
- Entropy scoring on subdomain labels (high entropy = encoded data).
- Query length distribution (tunneling uses long names).
- Stack counting of domains by prevalence (rare = suspicious).
- Timing analysis for beacon intervals (regular gaps, low jitter).
- Ratio of TXT/NULL/unusual record types per host.
```

## Turn into detection
- Promote confirmed patterns to Sigma rules; feed threat intel (known DGA families, C2 domains).
- See [detection-as-code](../detection-engineering/detection-as-code.md), [networking/dns](../../networking/dns.md).

## Mitigation / Hardening
- Force internal resolvers, block external :53 / unsanctioned DoH; RPZ sinkholing.
- Passive DNS + logging retention; rate-limit and alert on tunneling signatures.

## Sources
- [SANS – DNS Threat Hunting](https://www.sans.org/) · [Zeek DNS logs](https://docs.zeek.org/)
