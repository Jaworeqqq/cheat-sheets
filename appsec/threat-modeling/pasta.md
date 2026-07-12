---
title: "Threat modeling – PASTA"
category: "appsec"
tags: ["threat-modeling", "pasta", "risk"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Threat modeling – PASTA

## TL;DR
PASTA (Process for Attack Simulation and Threat Analysis) is a 7-stage, risk-centric threat modeling methodology. Unlike STRIDE (technique-centric), PASTA ties threats to business impact and simulates real attacks — heavier, but strong for high-value systems and executive buy-in.

## The 7 stages
```text
1. Define Objectives      – business objectives, compliance, risk appetite.
2. Define Technical Scope – architecture, components, dependencies, trust boundaries.
3. Application Decomposition – data flows, entry points, assets, actors (DFDs).
4. Threat Analysis        – threat intel, likely attackers, TTPs relevant to this app.
5. Vulnerability Analysis – map weaknesses (findings, CVEs, design flaws) to threats.
6. Attack Modeling        – build attack trees / simulate how threats exploit weaknesses.
7. Risk & Impact Analysis – quantify business risk; prioritize countermeasures.
```

## PASTA vs STRIDE vs attack trees
```text
STRIDE   – fast, technique-centric enumeration per element (breadth). Good default.
Attack trees – depth toward a single goal (see threat-modeling/attack-trees).
PASTA    – risk- and attacker-centric, links threats to business impact end-to-end.
           Heavier; best for critical apps and when you need business-aligned prioritization.
```

## When to use PASTA
```text
- High-value / high-risk systems where business impact justifies the effort.
- When you need to align security with business risk for leadership decisions.
- Mature programs with threat intel to feed stages 4-6.
Combine: STRIDE for quick per-feature coverage; PASTA for the crown-jewel systems.
```

## Outputs
```text
- Threat model doc: scope, DFDs, threat/vuln mapping, attack scenarios.
- Prioritized, risk-ranked countermeasures tied to business impact.
- Feeds the risk register (see compliance/risk-management/risk-assessment).
```

## Sources
- [PASTA (VerSprite)](https://versprite.com/blog/what-is-pasta-threat-modeling/) · related: [stride](./stride.md), [attack-trees](./attack-trees.md)
