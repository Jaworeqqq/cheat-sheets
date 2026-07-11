---
title: "OWASP API Security Top 10 (2023)"
category: "appsec"
tags: ["api-security", "owasp", "api"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# OWASP API Security Top 10 (2023)

## TL;DR
APIs have a distinct risk profile from web UIs — authorization at the object/property level dominates. This list complements the main Top 10 for API-first apps.

## The list
| # | Category | Essence | Key mitigation |
|---|----------|---------|----------------|
| API1 | Broken Object Level Authorization (BOLA) | access other users' objects by ID | per-object ownership checks server-side |
| API2 | Broken Authentication | weak/again broken auth flows, tokens | strong auth, token validation, MFA |
| API3 | Broken Object Property Level Authorization | mass assignment / excessive data exposure | explicit allow-list of fields in/out |
| API4 | Unrestricted Resource Consumption | no rate/size limits -> DoS/cost | rate limiting, quotas, pagination caps |
| API5 | Broken Function Level Authorization (BFLA) | call admin functions as a user | role checks per function/route |
| API6 | Unrestricted Access to Sensitive Business Flows | automate a business flow (scalping) | anti-automation, business-flow limits |
| API7 | Server-Side Request Forgery (SSRF) | fetch attacker URLs | allow-list, block internal/metadata |
| API8 | Security Misconfiguration | defaults, verbose errors, CORS | hardening baseline, headers |
| API9 | Improper Inventory Management | shadow/old API versions (v1, staging) | API inventory, retire old versions |
| API10 | Unsafe Consumption of APIs | trusting third-party API data blindly | validate/sanitize upstream responses |

## The dominant theme: authorization
```text
BOLA (API1) + BFLA (API5) + BOPLA (API3) are all authorization failures at
different granularities (object / function / property). Test each endpoint:
 - Can user A access user B's object by changing an ID? (BOLA)
 - Can a normal user hit admin routes/methods? (BFLA)
 - Can I set/read fields I shouldn't (role, isAdmin, price)? (BOPLA/mass assignment)
```

## Testing
```text
- Burp Autorize: replay every request with a low-priv session -> same data?
- Fuzz object IDs (sequential/UUID), HTTP methods, hidden/extra JSON fields.
- Enumerate API versions/hosts (v1, v2, /internal, staging) — inventory gaps.
```

## Mitigation / Hardening
- Enforce authorization per object/function/property server-side (deny by default).
- Explicit input/output schemas (allow-list fields), no mass assignment.
- Rate limiting + quotas, API gateway, inventory & retire old versions, validate upstream data.

## Sources
- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
