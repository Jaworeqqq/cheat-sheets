---
title: "Risk rating – DREAD"
category: "appsec"
tags: ["threat-modeling", "dread", "risk"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-13"
author: "core"
---

# Risk rating – DREAD

## TL;DR
DREAD is a simple model for rating and prioritizing the threats you find (e.g. via STRIDE). Score each threat across 5 factors, sum/average them, and rank. It's subjective — its value is a consistent, comparable ordering, not scientific precision.

## The 5 factors
```text
D – Damage:          how bad is the impact if exploited?
R – Reproducibility: how reliably can it be reproduced?
E – Exploitability:  how much effort/skill to exploit?
A – Affected users:  how many users/systems are impacted?
D – Discoverability: how easy is it to find? (often controversial — see below)
```

## Scoring
```text
Rate each factor (e.g. 0-10, or Low/Med/High = 1/2/3). Sum or average -> a risk score.
Rank threats by score to prioritize remediation.
Example (1-3 scale): Damage 3, Repro 3, Exploit 2, Affected 3, Discover 2 = 13/15 -> High.
```

## How it fits
```text
STRIDE (find threats)  ->  DREAD (rate/prioritize them)  ->  fix highest first.
Alternative ratings: CVSS (vuln scoring), likelihood x impact matrix (see risk-assessment),
                     or OWASP Risk Rating Methodology.
```

## Caveats (why teams adjust it)
```text
- Subjective: scores vary by rater — agree on rubric definitions for consistency.
- "Discoverability" is debated (assuming attackers won't find it = security by obscurity).
  Many teams DROP Discoverability or fix its score high, using DREA / likelihood-impact instead.
- Use it for relative prioritization within a project, not as an absolute risk number.
```

## Practical tips
```text
- Define concrete anchors for each score (what "Damage=3" means for YOUR app).
- Have 2+ people rate and reconcile; document the rationale.
- Combine with business context (crown-jewel data raises Damage/Affected).
```

## Sources
- [OWASP – Threat Modeling / Risk Rating](https://owasp.org/www-community/Threat_Modeling) · related: [stride](./stride.md), [attack-trees](./attack-trees.md), [risk-assessment](../../compliance/risk-management/risk-assessment.md)
