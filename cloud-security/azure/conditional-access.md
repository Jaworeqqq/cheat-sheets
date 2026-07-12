---
title: "Azure Conditional Access"
category: "cloud-security"
tags: ["azure", "entra", "conditional-access", "identity"]
platform: "azure"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Azure Conditional Access (CA)

## TL;DR
Conditional Access is Entra ID's policy engine: "if these signals, then require these controls (or block)". It's the core of Zero Trust for Microsoft identity — enforcing MFA, device compliance, and blocking risky/legacy access.

## Policy model
```text
IF (signals / conditions):
  - Users/groups, roles, guests
  - Apps (target resources)
  - Conditions: location/IP, device platform, client app, sign-in risk, user risk
THEN (access controls):
  - Grant: require MFA, compliant device, hybrid-joined, approved app, ToU
  - Session: sign-in frequency, persistent browser, app-enforced restrictions
  - Or BLOCK access
```

## Baseline policies (recommended)
```text
- Require MFA for all users (phishing-resistant where possible).
- Block legacy authentication (kills most password spray / basic-auth attacks).
- Require compliant or hybrid-joined device for sensitive apps.
- Require MFA for Azure management + admin roles; higher bar for privileged roles.
- Risk-based (P2): block/step-up on high sign-in or user risk (Identity Protection).
- Block or restrict access from unexpected countries; secure guest access.
```

## Common gaps / attacker angles
```text
- Legacy auth still enabled -> bypasses MFA (basic auth protocols).
- Excessive named-location trust / IP allow-lists that attackers can source from.
- Report-only policies never enforced; exclusions (break-glass) too broad or unmonitored.
- Device-code/OAuth consent flows not covered.
```

## Detection (Blue Team)
- Sign-in logs: CA result per sign-in; legacy-auth attempts; policy exclusions used.
- Alert on CA policy changes, disabled policies, break-glass account usage.

## Mitigation / Hardening
- Enforce MFA + block legacy auth as the foundation; move to phishing-resistant MFA.
- Use report-only mode to test, then enforce; keep 2 excluded break-glass accounts (monitored).
- Pair with PIM (just-in-time roles), Identity Protection (risk), and device compliance.
- Related: [entra-enumeration](./entra-enumeration.md), [managed-identity-abuse](./managed-identity-abuse.md).

## Sources
- [Conditional Access docs](https://learn.microsoft.com/entra/identity/conditional-access/) · [CA best practices](https://learn.microsoft.com/entra/identity/conditional-access/plan-conditional-access)
