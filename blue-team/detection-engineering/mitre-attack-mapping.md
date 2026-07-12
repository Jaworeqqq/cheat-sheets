---
title: "MITRE ATT&CK mapping & coverage"
category: "blue-team"
tags: ["detection-engineering", "mitre-attack", "coverage"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# MITRE ATT&CK mapping & coverage

## TL;DR
ATT&CK is a knowledge base of adversary tactics (the "why") and techniques (the "how"). Mapping your detections and data sources to ATT&CK turns "we have 500 rules" into "we can detect these techniques and are blind to those" — a measurable coverage picture.

## Structure
```text
Tactics      – the adversary's goal (e.g. TA0006 Credential Access) — the columns.
Techniques   – how they achieve it (T1558 Kerberoasting) — the cells.
Sub-techniques – specific variants (T1558.003).
Procedures   – real-world implementations by specific actors/malware.
```

## Why map
```text
- Coverage gaps: which techniques have NO detection/telemetry.
- Prioritization: focus on techniques relevant to YOUR threat model / seen in the wild.
- Communication: a common language across red, blue, threat intel, and leadership.
- Measure improvement over time (heatmap trending).
```

## Building a coverage heatmap
```text
1. Inventory detections (Sigma rules, EDR/SIEM alerts) — tag each with technique IDs.
2. Inventory data sources (do you even collect what a technique needs? e.g. 4769 for Kerberoast).
3. Score each technique: None / Telemetry-only / Detection / High-confidence.
4. Visualize in ATT&CK Navigator (color-coded layers).
5. Prioritize gaps by relevance (threat intel, red-team findings) + feasibility.
```

## Tools
```text
- ATT&CK Navigator – layered heatmaps (JSON layers).
- DeTT&CT – map data sources & detection quality to ATT&CK.
- Atomic Red Team – execute techniques to TEST your detections (validate, don't assume).
- MITRE CAR / Sigma – detection analytics mapped to techniques.
```

## Best practices
```text
- Coverage != count of rules; measure detection QUALITY and data-source availability.
- Validate with adversary emulation (Atomic Red Team / purple teaming), don't trust paper coverage.
- Drive detection-as-code backlog from the biggest relevant gaps.
- Related: detection-as-code.md, threat-hunting.md.
```

## Sources
- [MITRE ATT&CK](https://attack.mitre.org/) · [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) · [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT)
