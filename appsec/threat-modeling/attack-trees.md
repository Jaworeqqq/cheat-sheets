---
title: "Attack trees"
category: "appsec"
tags: ["threat-modeling", "attack-trees", "design"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Attack trees

## TL;DR
An attack tree models how an attacker could reach a goal: the goal is the root, sub-goals branch down, leaves are concrete attacks. AND/OR nodes express combinations. Complements STRIDE by focusing on an adversary's paths to one objective.

## Structure
```text
Goal: Steal customer PII            (root)
├─ OR: Compromise the database
│   ├─ AND: SQL injection + no WAF
│   └─ Leaked DB credentials (secret in repo)
├─ OR: Compromise an admin account
│   ├─ Phishing (no phishing-resistant MFA)
│   └─ Credential stuffing (no rate limit + reused password)
└─ OR: Exploit an exposed backup
    └─ Public S3 bucket with a DB dump
```
- **OR** node: any child achieves the parent. **AND** node: all children required.

## Building one
```text
1. Define the goal (what the attacker wants — one per tree).
2. Brainstorm ways to achieve it (sub-goals) — OR branches.
3. Decompose each until leaves are concrete, testable attacks.
4. Annotate leaves: cost, skill, detectability, existing control (yes/no).
5. Find the cheapest/most likely path -> prioritize mitigations there.
```

## Using it
```text
- Prioritize by the weakest branch (attacker takes the easy path).
- Map existing controls to leaves; gaps = where a control is missing.
- Great for a specific high-value asset/flow (payment, auth, data export).
- Pairs with STRIDE (breadth) — attack trees give depth toward one goal.
```

## Example annotation
```text
Leaf: Credential stuffing
  Cost: low  Skill: low  Detected?: no (no rate limit)  Control: MISSING
  -> Mitigation: rate limiting + breached-password check + MFA
```

## Sources
- [Schneier – Attack Trees](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) · [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
