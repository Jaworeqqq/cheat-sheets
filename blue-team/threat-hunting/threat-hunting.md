---
title: "Threat Hunting – methodology"
category: "blue-team"
tags: ["threat-hunting", "detection"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Threat Hunting

## TL;DR
Proactively searching for threats that alerts didn't catch. Driven by hypotheses based on TTPs (ATT&CK), not IOCs. Goal: find + turn into a durable detection.

## Cycle (hypothesis-driven)
```text
1. Hypothesis    – "The attacker uses WMI for lateral movement"
2. Data          – which logs will show it? (Sysmon 1/3, WMI-Activity 5857)
3. Hunt          – queries, baselining, deviations from the norm
4. Result        – confirm/reject; if found -> IR
5. Operationalize – turn into a Sigma rule/alert
```

## Example hypotheses → signals
```text
LOLBins            -> certutil/mshta/regsvr32 from unusual parents
Lateral (WMI)      -> wmiprvse.exe -> child process (cmd/powershell)
C2 beaconing       -> regular connection intervals, JA3, young domains
Persistence        -> new Run keys / tasks / services outside baseline
Cred dumping       -> lsass access, NTDS/SAM copies
```

## Example (Splunk – rare child processes)
```sql
index=sysmon EventCode=1
| stats count by ParentImage, Image
| sort count asc          // rare combinations = worth attention
```

## Analytical techniques
- **Stack counting** (frequency analysis) — rare = suspicious.
- **Baselining** — what is normal in the environment?
- **Grouping / clustering** by host, user, time.

## Sources
- [MITRE ATT&CK](https://attack.mitre.org/) · [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) · [ThreatHunting Project](https://www.threathunting.net/)
