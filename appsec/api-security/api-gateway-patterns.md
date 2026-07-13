---
title: "API gateway security patterns"
category: "appsec"
tags: ["api-security", "api-gateway", "architecture"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# API gateway security patterns

## TL;DR
An API gateway is the single entry point in front of your APIs — the right place to centralize cross-cutting security controls: authentication, rate limiting, input limits, TLS termination, and routing. It reduces per-service duplication, but is not a substitute for per-service authorization.

## Security controls to centralize at the gateway
```text
- Authentication: validate JWT/OAuth tokens, API keys, mTLS at the edge.
- Rate limiting & quotas (see api-security/rate-limiting) + request/payload size limits.
- TLS termination + enforce HTTPS/HSTS; optional mTLS to backends.
- Routing + versioning; hide internal topology; strip internal headers.
- WAF integration (SQLi/XSS/bot), IP allow/deny, geo-blocking.
- Centralized logging/metrics for detection.
```

## What the gateway should NOT own alone
```text
- Object/function-level authorization (BOLA/BFLA) — enforce PER SERVICE too. The gateway
  authenticates and coarse-authorizes; fine-grained authz belongs at the service (defense-in-depth).
- Don't assume "behind the gateway" = trusted (Zero Trust; services still authenticate callers).
```

## Common patterns
```text
BFF (Backend-for-Frontend) – a gateway/edge per client type; handles auth + shaping.
Token exchange             – swap an external token for an internal, narrowly-scoped one.
Gateway offload            – TLS, authn, rate limit, caching at the edge; services stay lean.
Zero-trust internal        – mTLS + per-service authz even east-west (see service-mesh-security).
```

## Pitfalls
```text
- Single point of failure/compromise -> HA + hardening + strict admin access to the gateway config.
- Over-trusting gateway-injected identity headers if services are reachable directly (bypass).
  -> Make services reject traffic not from the gateway (network policy / mTLS).
- Inconsistent auth between gateway and services.
```

## Detection (Blue Team)
- Gateway logs: auth failures, rate-limit hits, anomalous routes/versions, direct-to-service bypass attempts.

## Mitigation / Hardening
- Centralize authn + rate limits + input limits at the edge; enforce authz per service.
- Lock down direct service access (only the gateway/mesh can reach them); harden gateway admin plane.
- Related: [owasp-api-top10](./owasp-api-top10.md), [rate-limiting](./rate-limiting.md), [service-mesh-security](../../devsecops/kubernetes/service-mesh-security.md).

## Sources
- [OWASP API Security](https://owasp.org/API-Security/) · [Microsoft – Gateway patterns](https://learn.microsoft.com/azure/architecture/microservices/design/gateway)
