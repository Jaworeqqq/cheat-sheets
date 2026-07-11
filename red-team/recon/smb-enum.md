---
title: "SMB enumeration"
category: "red-team"
tags: ["recon", "smb", "active-directory"]
platform: "windows"
mitre: ["T1135", "T1087"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# SMB enumeration

## TL;DR
SMB (445) is a rich enumeration surface: shares, users, groups, password policy, OS info — often via null/guest sessions. First thing to hit on a Windows/AD network.

## Quick discovery
```bash
# Alive + SMB signing (relay potential) + OS
nxc smb 10.10.10.0/24
# Nmap scripts
nmap -p445 --script "smb-os-discovery,smb-security-mode,smb2-security-mode" 10.10.10.10
```

## Null / guest session enumeration
```bash
# Shares
smbclient -L //10.10.10.10 -N              # null session
smbmap -H 10.10.10.10 -u '' -p ''
nxc smb 10.10.10.10 -u '' -p '' --shares

# Users / groups / policy (RID cycling, RPC)
enum4linux-ng -A 10.10.10.10
nxc smb 10.10.10.10 -u guest -p '' --users --rid-brute
rpcclient -U '' -N 10.10.10.10             # then: enumdomusers, querydominfo
```

## Access & spider shares
```bash
smbclient //10.10.10.10/Share -N           # connect
nxc smb 10.10.10.10 -u user -p 'Pass' --shares -M spider_plus   # crawl for interesting files
smbmap -H 10.10.10.10 -u user -p 'Pass' -R Share --depth 5
```

## What to look for
```text
- Readable/writable shares (SYSVOL, NETLOGON -> GPP passwords: Groups.xml cpassword)
- Config files, scripts, credentials in shares
- Password policy (for safe spraying), user list (for spray/roast)
- SMB signing disabled -> NTLM relay opportunity
```

## Detection (Blue Team)
- Null/guest session attempts, RID cycling (many 4625/4624 anonymous), mass share access (5140/5145).
- enum4linux/rpcclient patterns; access to SYSVOL Groups.xml.

## Mitigation / Hardening
- Disable SMBv1, require SMB signing, restrict anonymous/null sessions (RestrictAnonymous).
- Remove GPP cpassword files; least-privilege share ACLs; monitor share access.

## Sources
- [enum4linux-ng](https://github.com/cddmp/enum4linux-ng) · [HackTricks – SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)
