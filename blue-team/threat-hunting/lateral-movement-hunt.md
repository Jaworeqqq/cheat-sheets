---
title: "Hunting lateral movement"
category: "blue-team"
tags: ["threat-hunting", "lateral-movement", "detection"]
platform: "windows"
mitre: ["T1021", "T1550", "T1570"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Hunting lateral movement

## TL;DR
Lateral movement is where an intrusion becomes a breach. Hunt the artifacts of remote execution (PsExec/WMI/WinRM), credential reuse (PtH/PtT), and admin-share access across hosts.

## Hypotheses → signals
```text
Remote exec (PsExec)  -> Event 7045 PSEXESVC, 5145 ADMIN$/IPC$, file in C:\Windows
Remote exec (WMI)     -> wmiprvse.exe spawning cmd/powershell (Sysmon 1); WMI-Activity 5857/5860
Remote exec (WinRM)   -> wsmprovhost.exe as parent; 4624 logon type 3
Pass-the-Hash         -> 4624/4776 NTLM network logons from a workstation to many hosts
Pass-the-Ticket       -> Kerberos tickets used from a different host than issued
Scheduled task (atexec)-> 4698 task creation on remote hosts
Admin share access    -> 5140/5145 to ADMIN$/C$ from non-admin workstations
```

## Hunt queries
```sql
-- Splunk: one source authenticating to many destinations (fan-out)
index=win EventCode=4624 Logon_Type=3
| stats dc(dest_host) AS hosts values(dest_host) by src_ip, user
| where hosts > 5
```
```kql
// Defender: WMI/WinRM remote exec parents
DeviceProcessEvents
| where InitiatingProcessFileName in~ ("wmiprvse.exe","wsmprovhost.exe")
| where FileName in~ ("cmd.exe","powershell.exe")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine
```

## Techniques
```text
- Fan-out analysis: a single account/host reaching an unusual number of systems.
- New admin-share access outside baseline; first-time host-to-host connections.
- Correlate logon (4624) + service/task creation + process spawn into a chain.
- Timeline across hosts to reconstruct the movement path.
```

## Turn into detection
- Promote confirmed patterns to Sigma rules (see [detection-as-code](../detection-engineering/detection-as-code.md)).

## Sources
- [MITRE ATT&CK – Lateral Movement](https://attack.mitre.org/tactics/TA0008/) · [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
