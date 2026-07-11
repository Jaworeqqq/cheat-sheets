---
title: "Elastic – KQL & EQL"
category: "blue-team"
tags: ["siem", "elastic", "eql", "kql"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Elastic – KQL & EQL

## TL;DR
Elastic Security uses two query languages: **KQL** (Kibana Query Language) for filtering, and **EQL** (Event Query Language) for sequence/behavioral detection (event ordering — great for attack chains). ES|QL is the newer piped language.

## KQL (filtering)
```text
event.category:process and process.name:"powershell.exe"
process.command_line:*-enc* and not user.name:"svc_backup"
source.ip:10.0.0.0/24 and destination.port:(445 or 3389)
network.protocol:dns and dns.question.name:*.suspicious.com
```

## EQL (sequences / behavior)
```eql
// Single event with conditions
process where process.name == "certutil.exe" and process.args : "*urlcache*"

// Sequence: encoded PowerShell then an outbound connection, same host, within 1m
sequence by host.name with maxspan=1m
  [ process where process.name == "powershell.exe" and process.args : "*-enc*" ]
  [ network where true ]

// Parent/child: Office spawning a shell
process where process.parent.name in ("winword.exe","excel.exe")
  and process.name in ("cmd.exe","powershell.exe")
```

## ES|QL (piped, newer)
```sql
FROM logs-* | WHERE process.name == "powershell.exe"
| STATS count = COUNT(*) BY host.name | SORT count DESC
```

## When to use which
```text
KQL   – quick filtering, dashboards, alert conditions.
EQL   – behavioral detections needing event ordering/correlation (attack chains).
ES|QL – aggregation/transformation, ad-hoc analysis (SQL-like piped).
```

## Best practices
- Use ECS (Elastic Common Schema) field names for portable rules.
- Leverage the Elastic prebuilt detection rules (open-source repo) as a baseline.
- Version detections (see [detection-as-code](../detection-engineering/detection-as-code.md)).

## Sources
- [EQL syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/eql-syntax.html) · [Elastic detection-rules](https://github.com/elastic/detection-rules) · [ECS](https://www.elastic.co/guide/en/ecs/current/index.html)
