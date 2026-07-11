---
title: "A04 – Insecure Design"
category: "appsec"
tags: ["owasp", "design", "threat-modeling"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A04 – Insecure Design

## TL;DR
Flaws in the design itself, not the implementation — missing or ineffective security controls by design. You can't patch your way out of a bad design; it must be addressed upfront.

## Examples
```text
- No rate limiting on sensitive flows (password reset, OTP, purchase)
- Trusting client-side controls (price in the request body)
- Missing business-logic limits (negative quantity, coupon stacking)
- No segregation of tenants / trust zones
- Recoverable secrets (security questions, plaintext reset)
- No defense against credential stuffing / enumeration
```

## Design-level practices
```text
- Threat modeling (STRIDE) early and on changes -> see appsec/threat-modeling/stride.md
- Secure design patterns & reference architectures
- Define security requirements (abuse cases) alongside functional ones
- Establish trust boundaries; never trust the client
- Plausibility/limit checks on business logic, resource quotas
```

## Detection (Blue Team)
- Business-logic anomaly monitoring (velocity, out-of-range values).
- Abuse-case alerting (mass resets, impossible carts).

## Mitigation / Hardening
- Threat model per feature; encode security requirements as tests.
- Rate limiting + anti-automation on sensitive flows.
- Server-side enforcement of all business rules and prices.
- Secure defaults, fail closed, least privilege by design.

## Sources
- [OWASP A04:2021](https://owasp.org/Top10/A04_2021-Insecure_Design/) · [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
