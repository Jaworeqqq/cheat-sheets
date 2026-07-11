---
title: "CSRF defense"
category: "appsec"
tags: ["secure-coding", "csrf", "sessions", "defense"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# CSRF defense

## TL;DR
Cross-Site Request Forgery tricks a logged-in victim's browser into sending a state-changing request the user didn't intend. It works because browsers auto-attach cookies. Defend with anti-CSRF tokens and/or `SameSite` cookies plus origin checks.

## How it works
```text
1. Victim is authenticated to bank.com (session cookie set).
2. Victim visits attacker.com, which auto-submits a form/request to bank.com.
3. Browser attaches the bank.com cookie -> the request is processed as the victim.
Precondition: the app relies solely on an ambient credential (cookie) for auth.
```

## Defenses (layer them)
```text
1. Synchronizer token (per-session/per-request) – server issues a secret token,
   embedded in forms; verified server-side. Not readable cross-origin. Gold standard.
2. SameSite cookies – Lax (default in modern browsers) blocks most cross-site POSTs;
   Strict is stronger but breaks some flows. Defense-in-depth, not a sole control.
3. Double-submit cookie – token in both a cookie and a request header/param; compare.
   Stateless; beware subdomain cookie-injection weaknesses.
4. Custom request header (APIs) – require e.g. X-Requested-With; browsers won't send
   custom headers cross-origin without a passing CORS preflight.
5. Origin/Referer validation – verify Origin (or Referer) matches an allow-list.
```

## Synchronizer token (pattern)
```html
<!-- server embeds a per-session token; validates it on POST -->
<form method="POST" action="/transfer">
  <input type="hidden" name="csrf_token" value="{{ server_generated_token }}">
  ...
</form>
```

## When SameSite is / isn't enough
```text
Enough-ish: Lax blocks cross-site POST/PUT/DELETE with cookies in modern browsers.
NOT enough:
 - Older/edge browsers without SameSite enforcement.
 - GET requests that change state (never do this) still allowed under Lax.
 - Same-site but cross-origin subdomains (an XSS/subdomain takeover bypasses it).
 - Non-cookie auth doesn't apply; token defenses still needed for robustness.
```

## SPA / API considerations
```text
- Token-based auth in a custom header (Authorization: Bearer ...) is NOT
  auto-attached cross-site -> largely immune to classic CSRF.
- Cookie-based sessions for SPAs still need CSRF protection (SameSite + token/header).
- For APIs: require a custom header + strict CORS; validate Origin.
```

## Detection (Blue Team)
- State-changing requests with missing/invalid CSRF tokens; Origin/Referer mismatches.
- Spikes of cross-site POSTs to sensitive endpoints.

## Mitigation / Hardening
- Anti-CSRF tokens on all state-changing requests + `SameSite` cookies + Origin checks.
- Never use GET for state changes; use framework CSRF middleware (don't hand-roll).
- Combine with XSS prevention — an XSS bypasses any CSRF defense. See [input-validation](./input-validation.md).

## Sources
- [OWASP – CSRF Prevention CS](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) · [PortSwigger – CSRF](https://portswigger.net/web-security/csrf)
