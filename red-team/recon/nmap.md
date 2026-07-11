---
title: "Nmap – scanning and enumeration"
category: "red-team"
tags: ["recon", "scanning", "nmap"]
platform: "agnostic"
mitre: ["T1046", "T1595"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Nmap – scanning and enumeration

## TL;DR
Map hosts, ports and services. Start broad (host discovery), then targeted service scan + NSE scripts.

## Commands
```bash
# Host discovery (ping sweep, no port scan)
nmap -sn 10.10.10.0/24

# Fast top-1000 TCP scan
nmap -sV -T4 10.10.10.5

# Full scan of all TCP ports + versions + OS + default scripts
nmap -p- -sV -sC -O -T4 -oA scans/full 10.10.10.5

# UDP top-100 (slow – limit ports)
nmap -sU --top-ports 100 10.10.10.5

# Specific NSE scripts (e.g. SMB)
nmap -p445 --script "smb-vuln-*" 10.10.10.5
```

## Detection (Blue Team)
Bursts of SYN to many ports in a short time from one source.
```sql
-- Splunk: potential port scan
index=firewall action=blocked
| stats dc(dest_port) AS ports by src_ip
| where ports > 100
```
IDS: Suricata/Snort `stream5`/`sfPortscan` rules.

## Mitigation / Hardening
- Rate-limiting and IPS at the network edge.
- Minimize port exposure (least exposure), segmentation.
- Firewall drop instead of reject (makes enumeration harder).

## Notes / Pitfalls
- `-T5` can be unfriendly / drop results on filtered networks — stick with `-T4`.
- `-oA` saves 3 formats (nmap/gnmap/xml) — handy for later parsing.

## Sources
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [MITRE T1046](https://attack.mitre.org/techniques/T1046/)
