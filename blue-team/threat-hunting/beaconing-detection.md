---
title: "Detecting C2 beaconing"
category: "blue-team"
tags: ["threat-hunting", "c2", "beaconing", "network"]
platform: "agnostic"
mitre: ["T1071", "T1573"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Detecting C2 beaconing

## TL;DR
Implants "beacon" home on a schedule to receive commands. Even when the payload is encrypted, the *timing and shape* of the traffic betray it: regular intervals, consistent sizes, and connections to young/rare destinations. Hunt the pattern, not the content.

## Beacon signatures
```text
Timing     – regular check-in intervals (even with jitter, a periodicity remains).
Volume     – many small, similar-sized requests over time to one destination.
Duration   – long-lived, low-and-slow sessions; activity outside business hours.
Destination – young/low-prevalence domains, rare for your org, cloud/CDN abuse, direct IPs.
TLS/JA3    – client TLS fingerprint (JA3) matching known C2 tooling; self-signed/odd certs.
DNS        – high-entropy/long subdomains (DNS C2 — see dns-anomaly-hunt).
```

## Analytical techniques
```text
- Interval analysis: compute time deltas between connections per src/dst pair;
  low variance (accounting for jitter) = suspicious periodicity.
- Frequency/stack counting of destinations by prevalence (rare = investigate).
- Data-size consistency: repeated near-identical request/response sizes.
- Enrich destinations: domain age, reputation, ASN, category; flag the anomalous.
- JA3/JA3S fingerprint matching against known-bad.
```

## Queries / tooling
```sql
-- Splunk sketch: periodic connections to one dest (low interval variance)
index=proxy OR index=netflow
| streamstats current=f last(_time) as prev by src_ip, dest
| eval delta=_time-prev
| stats count avg(delta) as mean stdev(delta) as sd by src_ip, dest
| where count>20 AND sd < (mean*0.15)      // very regular
```
```text
Tools: RITA (Real Intelligence Threat Analytics) for beacon scoring on Zeek data;
       Zeek/Suricata logs; JA3 via Zeek/Suricata; commercial NDR.
```

## Watch for evasion
```text
- High jitter + long sleep smears the interval (still detectable statistically over time).
- Domain fronting / CDN + legit-looking TLS -> lean on prevalence + JA3 + behavior.
- Malleable profiles mimic real apps -> combine multiple weak signals.
```

## Turn into detection
- Score and alert on periodicity + rare-destination combos; feed to IR (see cloud-ir/ir-process).
- Related: [dns-anomaly-hunt](./dns-anomaly-hunt.md), [c2-matrix](../../red-team/command-and-control/c2-matrix.md), [sliver](../../red-team/tools/sliver.md).

## Sources
- [Active Countermeasures – RITA](https://www.activecountermeasures.com/free-tools/rita/) · [MITRE T1071](https://attack.mitre.org/techniques/T1071/)
