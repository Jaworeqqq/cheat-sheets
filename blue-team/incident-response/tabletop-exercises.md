---
title: "Tabletop exercises"
category: "blue-team"
tags: ["incident-response", "tabletop", "preparation"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Tabletop exercises (TTX)

## TL;DR
A tabletop is a discussion-based drill where the IR team walks through a realistic incident scenario to test the plan, roles, and decisions — before a real incident does it for you. Low-cost, high-value preparation; required/expected by ISO 27001, SOC 2, DORA, NIS2.

## Why run them
```text
- Validate the IR plan and runbooks actually work in practice.
- Clarify roles/decision authority (who can isolate systems, call the CEO, notify regulators).
- Surface gaps: missing contacts, unclear escalation, tooling assumptions, legal steps.
- Build muscle memory so real incidents run calmer and faster.
```

## Types (increasing realism/cost)
```text
Tabletop (discussion) – talk through a scenario around a table. Cheapest, start here.
Functional drill      – actually perform some actions (failover, restore a backup).
Full simulation / red-team-driven – live technical exercise (purple team).
```

## Running a tabletop
```text
1. Objectives + scope (test the ransomware runbook / regulatory reporting / comms).
2. Participants: IR team, IT, legal, comms/PR, exec sponsor, relevant business owners.
3. A facilitator drives; a scribe records decisions, gaps, and action items.
4. Inject the scenario in stages ("EDR alerts on 3 hosts" -> "backups encrypted" -> "press calls").
5. At each inject, ask: what do we do, who decides, what do we need, who do we notify?
6. Debrief: what worked, what didn't, concrete action items with owners + dates.
```

## Scenario ideas
```text
- Ransomware across file servers (test containment + BCP/DR + comms).
- BEC / executive fraud (test money-movement + identity response).
- Cloud key compromise / data exfil (test cloud IR).
- Insider threat; third-party/supply-chain breach; regulatory 72h clock.
```

## Getting value
```text
- Realistic, relevant scenarios (your threat model), not generic.
- Include decision-makers, not just technical staff.
- Track action items to closure; re-test the fixed gaps next time.
- Run at least annually + after major changes.
```

## Sources
- [CISA Tabletop Exercise Packages (CTEP)](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) · related: [ir-process](./ir-process.md), [incident-response-policy](../../compliance/policies/incident-response-policy.md)
