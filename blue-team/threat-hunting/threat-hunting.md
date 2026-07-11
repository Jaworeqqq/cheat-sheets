---
title: "Threat Hunting – metodyka"
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
Proaktywne szukanie zagrożeń, których nie złapały alerty. Napędzane hipotezami opartymi o TTP (ATT&CK), nie o IOC. Cel: znaleźć + zamienić w trwałą detekcję.

## Cykl (hypothesis-driven)
```text
1. Hipoteza      – "Atakujący używa WMI do lateral movement"
2. Dane          – jakie logi to pokażą? (Sysmon 1/3, WMI-Activity 5857)
3. Hunt          – zapytania, baselining, odchylenia od normy
4. Wynik         – potwierdź/odrzuć; jeśli znaleziono -> IR
5. Operacjonalizacja – zamień w regułę Sigma/alert
```

## Przykładowe hipotezy → sygnały
```text
LOLBins            -> certutil/mshta/regsvr32 z nietypowych rodziców
Lateral (WMI)      -> wmiprvse.exe -> proces potomny (cmd/powershell)
C2 beaconing       -> regularne odstępy połączeń, JA3, młode domeny
Persistence        -> nowe Run keys / tasks / usługi poza baseline
Cred dumping       -> dostęp do lsass, kopie NTDS/SAM
```

## Przykład (Splunk – rzadkie procesy potomne)
```sql
index=sysmon EventCode=1
| stats count by ParentImage, Image
| sort count asc          // rzadkie kombinacje = warte uwagi
```

## Techniki analityczne
- **Stack counting** (frequency analysis) — rzadkie = podejrzane.
- **Baselining** — co jest normą w środowisku?
- **Grouping / clustering** po hostach, użytkownikach, czasie.

## Źródła
- [MITRE ATT&CK](https://attack.mitre.org/) · [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) · [ThreatHunting Project](https://www.threathunting.net/)
