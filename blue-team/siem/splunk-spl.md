---
title: "Splunk SPL – cheat sheet"
category: "blue-team"
tags: ["siem", "splunk", "spl"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Splunk SPL

## TL;DR
Search Processing Language: `search → transform → visualize`. The `|` pipe chains commands. Key ones: `stats`, `eval`, `where`, `rex`, `lookup`, `tstats`.

## Basics
```sql
index=windows EventCode=4625 host=DC01
| stats count by user, src_ip
| where count > 5
| sort -count
```

## Common commands
```sql
-- Aggregation
... | stats count, dc(user) AS unique_users by src_ip
-- Timechart
... | timechart span=1h count by EventCode
-- Field extraction with regex
... | rex field=_raw "user=(?<username>\w+)"
-- Conditions / new fields
... | eval is_admin=if(match(user,"adm_"),"yes","no")
-- Enrichment with a lookup
... | lookup asset_owner host OUTPUT owner
-- Exclusion
... | search NOT user IN ("svc_backup","healthcheck")
```

## Detections – examples
```sql
-- Password spray (many accounts, one IP)
index=win EventCode=4625
| stats dc(user) AS accts by src_ip, bin(_time, 1h)
| where accts > 10

-- Rare child processes (stack counting)
index=sysmon EventCode=1
| stats count by ParentImage, Image | sort count asc

-- Log clearing
index=win EventCode=1102
```

## Performance
- `tstats` on indexed fields = much faster than `stats` on raw events.
- Narrow the time range and `index=` up front; filter early in the pipeline.

## Sources
- [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference)
