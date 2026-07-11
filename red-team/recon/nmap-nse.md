---
title: "Nmap NSE – scripting engine"
category: "red-team"
tags: ["recon", "scanning", "nmap", "nse"]
platform: "agnostic"
mitre: ["T1046", "T1595"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Nmap NSE (Scripting Engine)

## TL;DR
NSE extends Nmap with Lua scripts for deeper enumeration, vuln checks and light exploitation. Scripts live in categories; `-sC` runs the `default` set.

## Categories & usage
```bash
# Default scripts (safe-ish, run with -sC)
nmap -sC -sV target
# Category selection
nmap --script "default,safe" target
nmap --script vuln target                 # vulnerability checks
nmap --script "discovery,safe" target
# Specific scripts / wildcards
nmap -p445 --script "smb-enum-*,smb-vuln-*" target
# Pass script arguments
nmap --script http-title --script-args http.useragent="Mozilla" target
```

## High-value scripts by service
```text
SMB   – smb-enum-shares, smb-enum-users, smb-os-discovery, smb-vuln-ms17-010
HTTP  – http-enum, http-title, http-headers, http-methods, http-wordpress-enum
DNS   – dns-zone-transfer, dns-brute
SSL   – ssl-enum-ciphers, ssl-cert, ssl-heartbleed
SSH   – ssh-auth-methods, ssh2-enum-algos
LDAP  – ldap-rootdse, ldap-search
SMTP  – smtp-enum-users, smtp-open-relay
```

## Finding & updating scripts
```bash
ls /usr/share/nmap/scripts/ | grep smb
nmap --script-help "smb-vuln-ms17-010"
sudo nmap --script-updatedb
```

## Detection (Blue Team)
- NSE probes look like targeted service interaction (SMB enum, HTTP fuzz paths).
- `vuln`/exploit-category scripts can trip IDS; `smb-vuln-*` touches known CVE paths.

## Mitigation / Hardening
- Restrict service exposure, IPS on known probe signatures, disable info-leaking responses.

## Notes / Pitfalls
- `vuln` and `exploit`/`intrusive` categories are not safe — get authorization; they can crash services.

## Sources
- [Nmap NSE docs](https://nmap.org/book/nse.html) · [Script list](https://nmap.org/nsedoc/)
