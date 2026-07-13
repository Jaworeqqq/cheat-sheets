---
title: "WebSocket security"
category: "appsec"
tags: ["api-security", "websocket", "web"]
platform: "web"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# WebSocket security

## TL;DR
WebSockets (ws://, wss://) provide persistent, bidirectional connections — and bypass many HTTP protections developers assume are present. Key issues: no same-origin enforcement by default (CSWSH), auth done only at handshake, and message-level injection. Treat every message as untrusted.

## Key risks
```text
CSWSH (Cross-Site WebSocket Hijacking)
  - WebSocket handshakes are NOT subject to the Same-Origin Policy; if auth relies only on
    cookies and the Origin isn't validated, an attacker page can open an authenticated socket
    to your server and read/act as the victim (CSRF for WebSockets).
Auth only at handshake
  - Many apps authenticate the upgrade request but then trust the whole session; no per-message
    authz. Combine with weak tokens -> hijack.
Message injection / validation
  - Messages feed backends (SQLi/XSS/command injection) if unvalidated; XSS if a message is
    rendered into the DOM.
Other
  - No/weak rate limiting (DoS, brute force over a socket), missing TLS (ws:// = cleartext),
    tunneling/SSRF via server-side WebSocket clients.
```

## Testing
```text
- Check Origin validation on the handshake (replay with a different Origin).
- Auth model: is it just a cookie? Can another origin open an authenticated socket? (CSWSH)
- Fuzz messages for injection; check authz per action, not just at connect.
- Burp supports WebSocket interception/repeat.
```

## Detection (Blue Team)
- Handshakes with unexpected Origins; message floods; injection patterns in message payloads.

## Mitigation / Hardening
```text
- Validate the Origin header on the handshake (allow-list); don't rely on cookies alone —
  use a CSRF-style token / bearer token for the WebSocket auth.
- Use wss:// (TLS) always.
- Authorize per message/action (not just at connect); validate + encode every message
  (same injection/output-encoding rules as HTTP — see input-validation).
- Rate limit + size-limit messages; timeouts; authenticate reconnections.
```

## Sources
- [PortSwigger – WebSockets](https://portswigger.net/web-security/websockets) · [OWASP – HTML5/WebSocket](https://cheatsheetseries.owasp.org/) · related: [csrf-defense](../secure-coding/csrf-defense.md), [rate-limiting](./rate-limiting.md)
