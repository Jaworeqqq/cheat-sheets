---
title: "Security headers"
category: "appsec"
tags: ["secure-coding", "headers", "web"]
platform: "web"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Security headers

## TL;DR
HTTP response headers that instruct the browser to enforce protections: mitigate XSS, clickjacking, protocol downgrade, and information leakage. Cheap, high-value defense-in-depth — but not a substitute for fixing the underlying issue.

## The important headers
```text
Content-Security-Policy (CSP)      – controls allowed script/style/resource origins (anti-XSS)
Strict-Transport-Security (HSTS)   – force HTTPS: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff    – stop MIME sniffing
X-Frame-Options: DENY              – anti-clickjacking (legacy; prefer CSP frame-ancestors)
Referrer-Policy: strict-origin-when-cross-origin  – limit referrer leakage
Permissions-Policy                 – disable unused browser features (camera, geolocation)
Cross-Origin-Opener-Policy / -Embedder-Policy / -Resource-Policy – isolation (Spectre, leaks)
Cache-Control: no-store            – on sensitive responses
```

## CSP — the high-value one
```http
Content-Security-Policy: default-src 'self';
  script-src 'self' 'nonce-{random}';
  object-src 'none'; base-uri 'none'; frame-ancestors 'none'
```
```text
- Prefer nonces/hashes over 'unsafe-inline'; avoid 'unsafe-eval'.
- frame-ancestors replaces X-Frame-Options (clickjacking).
- Start in report-only (Content-Security-Policy-Report-Only) to tune, then enforce.
```

## What NOT to rely on / avoid leaking
```text
- Remove/So generic: Server, X-Powered-By (version disclosure).
- X-XSS-Protection is deprecated (can introduce bugs) — omit; use CSP instead.
```

## Testing
```bash
curl -sI https://example.com | grep -iE 'content-security|strict-transport|x-frame|x-content|referrer|permissions-policy'
# securityheaders.com / Mozilla Observatory for a graded report
```

## Detection (Blue Team)
- CSP `report-uri`/`report-to` endpoint collects violation reports (signals XSS attempts/misconfig).

## Mitigation / Hardening
- Ship all headers via the framework/reverse proxy centrally; enforce in CI (fail if missing).
- Build a strict CSP (nonce-based); treat headers as defense-in-depth atop input/output handling.
- Related: [a05-security-misconfiguration](../owasp-top10/a05-security-misconfiguration.md), [xss](../../red-team/web/xss.md).

## Sources
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) · [MDN – CSP](https://developer.mozilla.org/docs/Web/HTTP/CSP)
