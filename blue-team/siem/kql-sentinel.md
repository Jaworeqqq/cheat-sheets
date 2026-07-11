---
title: "KQL – Sentinel / Defender"
category: "blue-team"
tags: ["siem", "kql", "sentinel", "defender"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# KQL (Kusto Query Language)

## TL;DR
The query language for Microsoft Sentinel / Defender XDR / Log Analytics. The `|` pipe, declarative. Key ones: `where`, `summarize`, `join`, `extend`, `project`.

## Basics
```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != 0
| summarize FailedCount = count() by UserPrincipalName, IPAddress
| where FailedCount > 10
| sort by FailedCount desc
```

## Common operators
```kql
// Filtering and projection
DeviceProcessEvents
| where FileName in~ ("powershell.exe","cmd.exe")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine

// New fields
| extend IsEncoded = ProcessCommandLine has "-enc"

// Time aggregation
| summarize count() by bin(Timestamp, 1h), DeviceName

// Join
DeviceLogonEvents
| join kind=inner (DeviceNetworkEvents) on DeviceId
```

## Detections – examples (Defender)
```kql
// Encoded PowerShell
DeviceProcessEvents
| where FileName == "powershell.exe" and ProcessCommandLine has_any ("-enc","-e ","FromBase64String")

// Impossible travel (simplified)
SigninLogs
| summarize Countries = dcount(Location) by UserPrincipalName, bin(TimeGenerated, 1h)
| where Countries > 1

// LOLBin – certutil downloads a file
DeviceProcessEvents
| where FileName == "certutil.exe" and ProcessCommandLine has "urlcache"
```

## Tips
- `has` (word-match, fast) vs `contains` (substring, slower).
- Narrow time up front; `project` limits columns → faster.

## Sources
- [KQL – Microsoft Learn](https://learn.microsoft.com/kusto/query/) · [Sentinel GitHub](https://github.com/Azure/Azure-Sentinel)
