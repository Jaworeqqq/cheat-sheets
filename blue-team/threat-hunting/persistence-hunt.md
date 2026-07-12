---
title: "Hunting persistence"
category: "blue-team"
tags: ["threat-hunting", "persistence", "detection"]
platform: "windows"
mitre: ["T1547", "T1053", "T1543"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Hunting persistence

## TL;DR
After access, attackers plant persistence to survive reboots and re-entry. Hunt the known autostart locations for anomalies — new, rare, or unsigned entries outside your baseline. Autoruns/OSQuery/Sysmon are your friends.

## Windows persistence locations to hunt
```text
Registry Run keys   – HKLM/HKCU ...\CurrentVersion\Run, RunOnce (Sysmon 13)
Scheduled tasks     – Event 4698; \Windows\System32\Tasks; unusual triggers/authors
Services            – Event 7045; auto-start, odd binPath, unsigned
WMI event subs      – __EventFilter/__EventConsumer/Binding (Sysmon 19-21)
Startup folders     – per-user + all-users Startup
DLL/COM hijacks     – Sysmon 7 image loads from user-writable paths; COM CLSID hijacks
Winlogon/LSA        – Userinit/Shell/Notify, security packages
Office/add-ins, BITS jobs, AppInit_DLLs, screensavers
```

## Hunt approach
```text
1. Baseline: what autostarts are normal in your environment (golden image).
2. Collect: Autoruns (autorunsc -a * -h), OSQuery (startup_items, scheduled_tasks), Sysmon.
3. Stack-count entries across hosts — RARE = suspicious.
4. Enrich: signature status, path (user-writable?), file age, parent, hash reputation.
5. Investigate outliers; confirm; turn into a detection.
```

## Queries
```sql
-- Splunk: new services outside baseline
index=win EventCode=7045
| stats count values(Service_File_Name) by host, Service_Name
| lookup service_baseline Service_Name OUTPUT known | where isnull(known)
```
```bash
# OSQuery: unsigned autostart items
SELECT name, path, source FROM startup_items;
SELECT name, path, arguments FROM scheduled_tasks WHERE hidden=1;
```

## Signals of malicious persistence
```text
- Unsigned/rare binary in a user-writable path set to autostart.
- Scheduled task with a suspicious author, hidden, or launching LOLBins/encoded PowerShell.
- WMI event subscription (rare in normal environments) — high-signal.
- Run key added right after a suspicious process chain.
```

## Turn into detection
- Alert on new services/tasks/WMI subs deviating from baseline; feed detection-as-code.
- Related: [windows-event-ids](../logging-monitoring/windows-event-ids.md), [sysmon-config](../logging-monitoring/sysmon-config.md), red-team [windows-persistence](../../red-team/persistence/windows-persistence.md).

## Sources
- [MITRE Persistence (TA0003)](https://attack.mitre.org/tactics/TA0003/) · [Sysinternals Autoruns](https://learn.microsoft.com/sysinternals/downloads/autoruns)
