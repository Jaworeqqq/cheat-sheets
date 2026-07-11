---
title: "proxychains & SOCKS pivoting"
category: "networking"
tags: ["networking", "pivoting", "proxychains", "socks"]
platform: "agnostic"
mitre: ["T1090"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# proxychains & SOCKS pivoting

## TL;DR
proxychains forces arbitrary TCP tools through a SOCKS/HTTP proxy — typically a SOCKS server you opened via a pivot (SSH `-D`, chisel, ligolo-ng). This lets you reach an internal network with tools that don't natively support proxies. Complements [ssh-tunneling](./ssh-tunneling.md).

## Config
```text
# /etc/proxychains4.conf (or ~/.proxychains/proxychains.conf)
# Chain behavior:
strict_chain      # use proxies in order; all must be up
# dynamic_chain   # skip dead proxies in the list
# random_chain    # random order (with chain_len)

proxy_dns          # resolve DNS through the proxy (critical – avoids leaks)

[ProxyList]
socks5 127.0.0.1 1080
```

## Basic use
```bash
# Open a SOCKS proxy first (pick one):
ssh -D 1080 user@jump                 # SSH dynamic
chisel client 10.10.14.1:8000 R:socks # chisel reverse SOCKS
# ligolo-ng: use its tun interface instead of proxychains (often nicer)

# Then run tools through it:
proxychains nmap -sT -Pn -p 445,3389 10.0.0.5   # TCP connect scan only
proxychains crackmapexec smb 10.0.0.0/24
proxychains curl http://10.0.0.5
proxychains evil-winrm -i 10.0.0.5 -u user -p 'Pass'
```

## Chaining multiple hops
```text
[ProxyList]
socks5 127.0.0.1 1080     # first pivot
socks5 127.0.0.1 1081     # second pivot (reached through the first)
# strict_chain routes traffic through both in order (double pivot).
```

## Tool compatibility & pitfalls
```text
- SOCKS carries TCP only. No ICMP -> nmap ping scan fails; use -Pn.
- Use TCP connect scan (-sT), not SYN (-sS) — raw packets won't traverse SOCKS.
- Enable proxy_dns or DNS leaks (and breaks name resolution to internal hosts).
- UDP generally unsupported (SOCKS5 UDP associate is rarely usable here).
- ligolo-ng's tun interface avoids most of these limits (full IP stack).
```

## Detection (Blue Team)
- Long-lived outbound SOCKS/reverse tunnels; an internal host proxying scans/connections.
- Sudden host-to-host fan-out sourced from one pivot machine.

## Mitigation / Hardening
- Egress filtering, network segmentation, disable `AllowTcpForwarding` where unneeded.
- Monitor for tunneling tools (chisel/ligolo signatures) and anomalous internal scanning.

## Sources
- [proxychains-ng](https://github.com/rofl0r/proxychains-ng) · related: [ssh-tunneling](./ssh-tunneling.md)
