---
title: "Rate limiting & anti-automation"
category: "appsec"
tags: ["api-security", "rate-limiting", "dos", "anti-automation"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Rate limiting & anti-automation

## TL;DR
Rate limiting caps how often a client can call an endpoint — the primary defense against brute force, credential stuffing, scraping, enumeration, and resource-exhaustion DoS (OWASP API4). Must be enforced server-side, keyed on something the attacker can't trivially rotate.

## Algorithms
```text
Fixed window     – N requests per time window. Simple; burst at window edges.
Sliding window   – smooths the edge problem; more accurate.
Token bucket     – tokens refill at a rate; allows controlled bursts. Common default.
Leaky bucket     – constant outflow; smooths bursts.
Concurrency limit – cap simultaneous in-flight requests (protects backends).
```

## What to key on (and the pitfalls)
```text
- API key / authenticated user ID (best for authed endpoints).
- IP address — but attackers rotate IPs (botnets, proxies); combine signals.
- Per-endpoint + per-account for sensitive flows (login, OTP, password reset, checkout).
Pitfall: keying only on IP is bypassable; keying only on username enables account lockout DoS.
```

## Where sensitive flows need extra
```text
Login / MFA / password reset -> strict per-account + per-IP limits + backoff + CAPTCHA on abuse.
Signup / coupon / purchase   -> business-flow limits (OWASP API6 unrestricted business flows).
Search / export / GraphQL    -> cost/complexity limits, pagination caps.
```

## Response & headers
```text
- Return 429 Too Many Requests with Retry-After.
- Expose limits: RateLimit-Limit / RateLimit-Remaining / RateLimit-Reset.
- Exponential backoff on repeated auth failures; progressive CAPTCHA.
```

## Enforcement points
```text
- API gateway / reverse proxy (nginx, Kong, cloud API GW) — centralized, before the app.
- WAF for volumetric/bot patterns; app-level for business-logic limits.
- Distributed store (Redis) so limits hold across instances.
```

## Detection (Blue Team)
- Spikes in 429s, credential-stuffing patterns (many accounts/one source or distributed), scraping.

## Mitigation / Hardening
- Layer gateway + app limits; key on user+IP+endpoint; strict on auth/business flows.
- Bot management / CAPTCHA on anomalies; monitor and tune thresholds.
- Related: [owasp-api-top10](./owasp-api-top10.md), [a07-auth-failures](../owasp-top10/a07-auth-failures.md).

## Sources
- [OWASP API4:2023](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) · [IETF RateLimit headers](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/)
