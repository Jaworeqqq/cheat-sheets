---
title: "BloodHound – analiza ścieżek ataku w AD"
category: "red-team"
tags: ["active-directory", "enumeration", "bloodhound"]
platform: "windows"
mitre: ["T1069", "T1482"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# BloodHound

## TL;DR
Zbiera relacje w AD (członkostwa, ACL, sesje, delegacje) do grafu i pokazuje najkrótszą ścieżkę do Domain Admin. Zbieranie = SharpHound (collector), analiza = BloodHound GUI.

## Zbieranie (SharpHound)
```powershell
# Windows, z hosta w domenie
SharpHound.exe -c All --zipfilename loot.zip
```
```bash
# Z Linuksa, zdalnie (bez implantu) – bloodhound-python / netexec
bloodhound-python -u user -p 'Pass' -d corp.local -ns 10.10.10.10 -c All
nxc ldap 10.10.10.10 -u user -p 'Pass' --bloodhound -c All --dns-server 10.10.10.10
```

## Analiza (typowe zapytania)
```text
Pre-built:
 - "Find Shortest Paths to Domain Admins"
 - "Find Principals with DCSync Rights"
 - "Shortest Path from Owned Principals"  (oznacz swoje konta jako Owned!)

Przydatne kanty (edges):
 GenericAll / GenericWrite / WriteDacl / WriteOwner  -> przejęcie obiektu
 AddMember  -> dodaj się do grupy
 ForceChangePassword -> reset hasła użytkownika
 AllowedToDelegate / Constrained/Unconstrained delegation
```

## Wykrywanie (Blue Team)
- Masowe zapytania LDAP/SAMR z jednego hosta (enumeracja).
- Nietypowe sesje SharpHound (`--stealth` je ogranicza, ale LDAP i tak widać).
- Honeytoken: konto-przynęta z „ciekawymi" ACL.

## Mitygacja / Hardening
- Ograniczaj nadmiarowe ACL (GenericAll/WriteDacl), tiering (Tier 0/1/2).
- Usuwaj unconstrained delegation, czyść zagnieżdżone członkostwa grup.
- Monitoruj i redukuj ścieżki do DA (regularne przeglądy grafu przez blue team).

## Źródła
- [BloodHound CE](https://github.com/SpecterOps/BloodHound) · [The Hacker Recipes – AD](https://www.thehacker.recipes/ad/)
