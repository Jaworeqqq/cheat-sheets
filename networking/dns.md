---
title: "DNS – fundamentals for security"
category: "networking"
tags: ["networking", "dns", "protocols"]
platform: "agnostic"
mitre: ["T1071.004"]
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# DNS – fundamentals for security

## TL;DR
DNS resolves names to addresses and underpins nearly everything. Understanding record types, the resolution flow, and its security extensions is essential for both attacking (recon, tunneling) and defending (detection, filtering).

## Record types
```text
A / AAAA   – hostname -> IPv4 / IPv6
CNAME      – alias to another name (watch for dangling -> subdomain takeover)
MX         – mail servers
NS         – authoritative name servers
TXT        – arbitrary text (SPF/DKIM/DMARC, verifications)
SOA        – zone authority/serial
PTR        – reverse (IP -> name)
SRV        – service location (AD: _ldap._tcp, _kerberos._tcp)
CAA        – which CAs may issue certs for the domain
```

## Resolution flow
```text
Stub resolver (client) -> Recursive resolver (ISP/8.8.8.8) ->
  Root (.) -> TLD (.com) -> Authoritative (example.com) -> answer (cached with TTL)
```

## Encrypted DNS
```text
DoH (DNS over HTTPS, :443)  – blends with web traffic; bypasses network DNS filtering
DoT (DNS over TLS, :853)    – dedicated port, easier to allow/block explicitly
DNSSEC – signs records (integrity/authenticity), does NOT encrypt; prevents spoofing/cache poisoning
```

## Security-relevant angles
```text
Recon        – zone transfer (AXFR), brute/subdomain enum (see red-team/recon/dns-recon.md)
Tunneling    – data smuggled in subdomain labels / TXT (see red-team/exfiltration)
Cache poisoning – forged responses; mitigated by DNSSEC, source-port randomization
Fast flux / DGA – malware rotating domains/IPs to evade blocking
```

## Detection (Blue Team)
- Long/high-entropy subdomains, excessive TXT/NULL queries = tunneling/DGA.
- Clients bypassing internal resolvers (direct :53/DoH to external) — policy violation.
- Newly registered / rare domains resolved by endpoints.

## Mitigation / Hardening
- Force internal resolvers; block/deny external :53 and unsanctioned DoH endpoints.
- DNSSEC validation, response-policy zones (RPZ) / sinkholing of known-bad domains.
- Log and monitor DNS (Passive DNS), alert on tunneling/DGA patterns.

## Sources
- [Cloudflare – What is DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) · [DNSSEC](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)
