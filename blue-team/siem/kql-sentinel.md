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
Język zapytań Microsoft Sentinel / Defender XDR / Log Analytics. Potok `|`, deklaratywny. Kluczowe: `where`, `summarize`, `join`, `extend`, `project`.

## Podstawy
```kql
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != 0
| summarize FailedCount = count() by UserPrincipalName, IPAddress
| where FailedCount > 10
| sort by FailedCount desc
```

## Częste operatory
```kql
// Filtrowanie i projekcja
DeviceProcessEvents
| where FileName in~ ("powershell.exe","cmd.exe")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine

// Nowe pola
| extend IsEncoded = ProcessCommandLine has "-enc"

// Agregacja czasowa
| summarize count() by bin(Timestamp, 1h), DeviceName

// Join
DeviceLogonEvents
| join kind=inner (DeviceNetworkEvents) on DeviceId
```

## Detekcje – przykłady (Defender)
```kql
// Kodowany PowerShell
DeviceProcessEvents
| where FileName == "powershell.exe" and ProcessCommandLine has_any ("-enc","-e ","FromBase64String")

// Impossible travel (uproszczone)
SigninLogs
| summarize Countries = dcount(Location) by UserPrincipalName, bin(TimeGenerated, 1h)
| where Countries > 1

// LOLBin – certutil pobiera plik
DeviceProcessEvents
| where FileName == "certutil.exe" and ProcessCommandLine has "urlcache"
```

## Wskazówki
- `has` (word-match, szybkie) vs `contains` (substring, wolniejsze).
- Zawężaj czas na starcie; `project` ogranicza kolumny → szybciej.

## Źródła
- [KQL – Microsoft Learn](https://learn.microsoft.com/kusto/query/) · [Sentinel GitHub](https://github.com/Azure/Azure-Sentinel)
