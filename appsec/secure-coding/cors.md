---
title: "CORS security"
category: "appsec"
tags: ["secure-coding", "cors", "web"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# CORS security

## TL;DR
CORS (Cross-Origin Resource Sharing) relaxes the browser's same-origin policy to allow controlled cross-origin requests. Misconfiguration — reflecting arbitrary origins, or allowing credentials with a wildcard — lets attacker sites read authenticated responses. CORS is an allow mechanism, not a defense.

## How it works
```text
Browser sends Origin: https://site.com
Server responds:
  Access-Control-Allow-Origin: <origin>   (which origins may read the response)
  Access-Control-Allow-Credentials: true  (may cookies/creds be sent?)
Preflight (OPTIONS) for non-simple requests checks allowed methods/headers.
```

## Dangerous misconfigurations
```text
1. Reflecting the Origin header without validation:
   ACAO: <reflected origin> + ACAC: true  -> ANY site reads authed responses.
2. ACAO: * with credentials — browsers block this combo, but apps sometimes hack around it.
3. Trusting null origin (ACAO: null) — sandboxed iframes/redirects can send Origin: null.
4. Weak allow-list regex: `https://site.com` matching `https://site.com.evil.com` or `evilsite.com`.
5. Trusting all subdomains when one is attacker-controlled (subdomain takeover -> CORS bypass).
```

## Testing
```bash
# Does the server reflect an arbitrary origin with credentials?
curl -s -I https://api.target.com/data -H "Origin: https://evil.com" | grep -i access-control
# Look for: Access-Control-Allow-Origin: https://evil.com  +  Allow-Credentials: true
```

## Impact
```text
If ACAO reflects attacker origin AND ACAC:true, an attacker page can make the victim's browser
fetch authenticated endpoints (with cookies) and READ the response -> data theft (like CSRF but readable).
```

## Detection (Blue Team)
- Responses reflecting arbitrary Origins with credentials; `null` origin allowed on sensitive APIs.

## Mitigation / Hardening
- **Strict allow-list** of exact origins (no reflection, no loose regex); validate the full origin.
- Never combine `Allow-Credentials: true` with a wildcard or reflected origin.
- Don't allow `null` origin for authenticated endpoints.
- Keep sensitive APIs same-origin where possible; CORS is not a substitute for authz/CSRF defense.
- Related: [csrf-defense](./csrf-defense.md), [secure-headers](./secure-headers.md).

## Sources
- [PortSwigger – CORS](https://portswigger.net/web-security/cors) · [MDN – CORS](https://developer.mozilla.org/docs/Web/HTTP/CORS)
