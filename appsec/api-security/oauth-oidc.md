---
title: "OAuth 2.0 / OIDC – security"
category: "appsec"
tags: ["api-security", "oauth", "oidc", "authentication"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# OAuth 2.0 / OIDC security

## TL;DR
OAuth 2.0 = authorization (access tokens); OIDC adds authentication (ID token) on top. Use the Authorization Code flow with PKCE. Most bugs come from redirect_uri handling, state/PKCE, and token validation.

## Flows (use the right one)
```text
Authorization Code + PKCE  – web & mobile & SPA (recommended default)
Client Credentials         – machine-to-machine (no user)
Device Code                – input-constrained devices (TVs)
Implicit                   – DEPRECATED (token in URL fragment)
ROPC (password)            – DEPRECATED (app sees the password)
```

## Common attacks
```text
- redirect_uri manipulation -> open redirect / token theft (must be exact-match allow-list)
- Missing state -> CSRF on the callback
- Missing/replayed PKCE -> authorization code interception
- Token leakage via Referer / logs / browser history
- Accepting tokens without validating aud / iss / exp / signature
- Mix-up attacks (multiple IdPs), scope creep, consent phishing
```

## Token validation checklist (resource server)
```text
- Verify signature (JWKS), iss, aud, exp/nbf
- Check scopes/permissions for the requested action
- For ID tokens: nonce matches, azp/aud correct
- Short-lived access tokens + refresh token rotation
```

## Detection (Blue Team)
- Anomalous redirect_uri values, tokens used from unexpected clients, consent-grant spikes.

## Mitigation / Hardening
- Authorization Code + PKCE everywhere; exact redirect_uri allow-list.
- Enforce state + PKCE; validate all token claims server-side.
- Short TTL + refresh rotation; restrict/monitor OAuth app consent (see cloud entra sheet).
- Use a vetted library / IdP; don't hand-roll token handling.

## Sources
- [OAuth 2.0 Security BCP (RFC 9700)](https://datatracker.ietf.org/doc/rfc9700/) · [OWASP – OAuth](https://cheatsheetseries.owasp.org/)
