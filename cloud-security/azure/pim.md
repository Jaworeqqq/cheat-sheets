---
title: "Azure PIM (Privileged Identity Management)"
category: "cloud-security"
tags: ["azure", "entra", "pim", "privileged-access"]
platform: "azure"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Azure PIM (Privileged Identity Management)

## TL;DR
PIM provides just-in-time (JIT), time-bound privileged access in Entra ID and Azure. Instead of standing admin rights, users are *eligible* for a role and must *activate* it (with justification, MFA, and optionally approval) for a limited window — drastically shrinking the attack surface of privileged accounts.

## Core concepts
```text
Eligible vs Active  – eligible = can activate when needed; active = currently holding the role.
Just-in-time (JIT)  – activate for a limited time (e.g. 1-8h), then it auto-expires.
Activation controls – require MFA, justification, ticket number, and/or approval.
Time-bound assignments – even "active" assignments can have start/end dates.
Access reviews      – periodic recertification of who should be eligible.
```

## What it protects
```text
- Entra ID roles (Global Admin, Privileged Role Admin, etc.).
- Azure resource roles (Owner, Contributor, User Access Administrator) at scope.
- PIM for Groups (JIT membership of privileged groups).
```

## Why it matters (attacker view)
```text
Standing Global Admins are prime targets — phish one and it's game over, anytime.
With PIM: the role is inactive most of the time; activation requires MFA + justification
(+ approval), is time-boxed, and is logged/alertable. A stolen credential alone isn't enough.
```

## Configuration best practices
```text
- Make privileged roles ELIGIBLE, not permanently active (zero standing admins ideally).
- Require MFA + justification (+ approval for the most sensitive: Global Admin, UAA).
- Short activation windows; limit max active time.
- Alert on activations; require approval for break-the-glass; keep 2 emergency accounts (excluded, monitored).
- Regular access reviews of eligible assignments.
```

## Detection (Blue Team)
- PIM audit logs: role activations (who/when/justification), assignment changes, approvals.
- Alert on Global Admin activation, out-of-hours activation, and eligibility grants.

## Mitigation / Hardening
- Combine PIM (JIT) with Conditional Access (require compliant device/phishing-resistant MFA on activation).
- Least privilege + access reviews; monitor activations feeding Sentinel.
- Related: [conditional-access](./conditional-access.md), [entra-enumeration](./entra-enumeration.md).

## Sources
- [Entra PIM docs](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/)
