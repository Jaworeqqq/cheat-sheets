---
title: "HTTP request smuggling"
category: "red-team"
tags: ["web", "request-smuggling", "http"]
platform: "web"
mitre: ["T1190"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# HTTP request smuggling

## TL;DR
When a front-end (proxy/CDN/LB) and back-end server disagree on where one HTTP request ends and the next begins, an attacker can "smuggle" a partial request that prepends to the next user's request — enabling request hijacking, cache poisoning, bypassing front-end controls, and credential theft. Rooted in `Content-Length` vs `Transfer-Encoding` ambiguity.

## Variants
```text
CL.TE  – front-end uses Content-Length, back-end uses Transfer-Encoding.
TE.CL  – front-end uses Transfer-Encoding, back-end uses Content-Length.
TE.TE  – both support TE but one can be induced to ignore it (obfuscated header).
CL.0 / H2.CL / H2.TE – HTTP/2 downgrade + header desync (modern, increasingly common).
```

## Classic CL.TE probe
```http
POST / HTTP/1.1
Host: target
Content-Length: 6
Transfer-Encoding: chunked

0

G
```
```text
Front-end (CL) forwards the whole body; back-end (TE) sees the chunked terminator "0\r\n\r\n"
and treats "G" as the start of the NEXT request -> desync.
```

## Impact
```text
- Hijack other users' requests (steal cookies/CSRF tokens, capture credentials).
- Bypass front-end security controls (WAF, auth) by smuggling to the back-end.
- Web cache poisoning (serve attacker content to other users).
- Turn reflected issues into stored/mass exploitation.
```

## Tooling
```text
- Burp Suite "HTTP Request Smuggler" extension (detect + exploit, incl. HTTP/2 desync).
- Manual: send timing/differential probes; watch for delayed responses / desync effects.
```

## Detection (Blue Team)
- Malformed/duplicate `Content-Length` + `Transfer-Encoding`; unusual chunked encodings.
- Anomalous request boundaries, responses to the wrong client; front-end/back-end log mismatches.

## Mitigation / Hardening
- Normalize/reject ambiguous requests at the front-end (both CL and TE present -> reject).
- Use HTTP/2 end-to-end (don't downgrade to HTTP/1.1 at the back-end); consistent parsing.
- Keep proxies/servers patched; disable connection reuse to the back-end where feasible.

## Sources
- [PortSwigger – Request smuggling](https://portswigger.net/web-security/request-smuggling)
