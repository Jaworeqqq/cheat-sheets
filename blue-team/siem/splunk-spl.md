---
title: "Splunk SPL – ściągawka"
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
Search Processing Language: `search → transform → visualize`. Potok `|` łączy komendy. Kluczowe: `stats`, `eval`, `where`, `rex`, `lookup`, `tstats`.

## Podstawy
```sql
index=windows EventCode=4625 host=DC01
| stats count by user, src_ip
| where count > 5
| sort -count
```

## Częste komendy
```sql
-- Agregacja
... | stats count, dc(user) AS unique_users by src_ip
-- Timechart
... | timechart span=1h count by EventCode
-- Ekstrakcja pola regexem
... | rex field=_raw "user=(?<username>\w+)"
-- Warunki / nowe pola
... | eval is_admin=if(match(user,"adm_"),"yes","no")
-- Wzbogacenie z lookup
... | lookup asset_owner host OUTPUT owner
-- Wykluczanie
... | search NOT user IN ("svc_backup","healthcheck")
```

## Detekcje – przykłady
```sql
-- Password spray (wiele kont, jedno IP)
index=win EventCode=4625
| stats dc(user) AS accts by src_ip, bin(_time, 1h)
| where accts > 10

-- Rzadkie procesy potomne (stack counting)
index=sysmon EventCode=1
| stats count by ParentImage, Image | sort count asc

-- Czyszczenie logów
index=win EventCode=1102
```

## Wydajność
- `tstats` na indeksowanych polach = dużo szybsze niż `stats` na surowych.
- Zawężaj czas i `index=` na starcie; filtruj wcześnie w potoku.

## Źródła
- [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference)
