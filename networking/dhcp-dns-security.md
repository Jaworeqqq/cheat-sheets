---
title: "DHCP & DNS security"
category: "networking"
tags: ["networking", "dhcp", "dns", "hardening"]
platform: "agnostic"
mitre: ["T1557"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# DHCP & DNS security

## TL;DR
DHCP and DNS are foundational and frequently abused: rogue DHCP servers and DNS spoofing let attackers become a man-in-the-middle, redirect traffic, and harvest credentials. Both need active protection — the protocols themselves are trust-by-default.

## DHCP attacks
```text
Rogue DHCP server – attacker answers DHCP requests, hands out a malicious gateway/DNS -> MITM.
DHCP starvation   – exhaust the pool (spoofed MACs) -> DoS, then rogue server takes over.
DHCP spoofing     – combined: starve + rogue -> control clients' gateway/DNS.
```

## DHCP defenses
```text
- DHCP snooping (switch feature): only trusted ports may send DHCP OFFER/ACK (block rogue servers).
- Dynamic ARP Inspection (DAI) + IP Source Guard: use snooping bindings to stop ARP/IP spoofing.
- Port security (limit MACs) to blunt starvation.
- 802.1X/NAC so only authenticated devices get on the network (see networking/802.1x-nac).
```

## DNS attacks
```text
Spoofing/cache poisoning – forged responses redirect victims (mitigated by DNSSEC + randomization).
Rogue/hijacked DNS       – via rogue DHCP or resolver compromise -> redirect everything.
DNS tunneling/exfil      – covert channel (detect: see blue-team/threat-hunting/dns-anomaly-hunt).
Local hosts/resolver tampering, NXDOMAIN hijacking.
```

## DNS defenses
```text
- DNSSEC validation (integrity/authenticity of responses).
- Force internal resolvers; block/deny external :53 and unsanctioned DoH; source-port randomization.
- Response Policy Zones (RPZ) / DNS filtering to sinkhole known-bad domains.
- Protect the resolver + zone data; monitor + log DNS (Passive DNS) — see networking/dns.
- DoT/DoH for client-resolver privacy (but control which endpoints are allowed).
```

## Detection (Blue Team)
- Multiple DHCP servers on a segment; DHCP from untrusted ports (snooping violations).
- Clients using unexpected DNS servers; DNS answers inconsistent with authoritative; tunneling patterns.

## Mitigation / Hardening (summary)
- DHCP snooping + DAI + IP Source Guard + port security + 802.1X on the access layer.
- DNSSEC + internal resolvers + egress DNS control + RPZ + logging.

## Sources
- [Cisco – DHCP Snooping/DAI](https://www.cisco.com/) · related: [dns](./dns.md), [dns-anomaly-hunt](../blue-team/threat-hunting/dns-anomaly-hunt.md), [802.1x-nac](./802.1x-nac.md)
