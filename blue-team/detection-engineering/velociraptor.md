---
title: "Velociraptor – endpoint DFIR & hunting"
category: "blue-team"
tags: ["detection-engineering", "dfir", "velociraptor", "threat-hunting"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Velociraptor

## TL;DR
Velociraptor is an open-source endpoint visibility, DFIR, and hunting platform. Agents run on endpoints; you query them at scale with VQL (Velociraptor Query Language) to collect artifacts, hunt across the fleet, and monitor continuously. A go-to for incident response and proactive hunting.

## Architecture
```text
Server   – GUI + hunt orchestration + artifact storage.
Clients  – agents on endpoints (Windows/Linux/macOS).
VQL      – SQL-like query language to collect/analyze data live on endpoints.
Artifacts – reusable VQL "recipes" (collect Prefetch, browser history, run YARA, etc.).
```

## Core use cases
```text
Hunting        – run a query/artifact across ALL endpoints (e.g. find hosts with a given IOC).
IR collection  – pull triage artifacts from a specific host fast (KAPE-like at scale).
Continuous monitoring – client event queries (process/file/network) as detections.
Remote forensics – live analysis without pulling a full disk image.
```

## VQL examples
```sql
-- Processes with a suspicious command line, fleet-wide
SELECT Name, CommandLine, Pid FROM pslist()
WHERE CommandLine =~ "-enc|FromBase64String|IEX"

-- Run YARA over a directory on the endpoint
SELECT * FROM yara(rules=MyRules, files="C:/Windows/Temp/*")
```

## Hunting workflow
```text
1. Hypothesis / IOC (e.g. a filename, hash, registry key, C2 domain).
2. Pick or write an artifact (VQL) that would surface it.
3. Launch a hunt across the fleet; collect results centrally.
4. Triage hits; pivot (collect more from affected hosts); scope the incident.
5. Promote repeatable hunts to continuous client monitoring.
```

## Strengths
```text
- Agentless-feeling scale: query thousands of endpoints in minutes.
- Rich artifact library (community + custom); YARA integration.
- Cross-platform; free/open-source. Great for IR retainers and labs.
```

## Best practices
- Version custom artifacts (detection-as-code); test before fleet-wide hunts.
- Scope hunts to avoid performance impact; secure the server (it has fleet-wide reach — Tier 0).
- Feed findings to your SIEM/IR process. Related: [dfir-triage](../digital-forensics/dfir-triage.md), [persistence-hunt](../threat-hunting/persistence-hunt.md).

## Sources
- [Velociraptor](https://docs.velociraptor.app/) · [Artifact Exchange](https://docs.velociraptor.app/exchange/)
