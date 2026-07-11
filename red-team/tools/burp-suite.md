---
title: "Burp Suite – quick workshop"
category: "red-team"
tags: ["tools", "web", "proxy"]
platform: "web"
mitre: ["T1190"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Burp Suite

## TL;DR
An intercepting HTTP(S) proxy. Flow: Proxy (intercept) → Repeater (manual tampering) → Intruder (fuzzing) → Scanner (Pro).

## Setup
```text
1. Proxy > Options: listener 127.0.0.1:8080
2. Browser: proxy to 8080 (or the built-in Burp Browser)
3. Install the Burp CA cert (http://burp -> CA Certificate) to see HTTPS
```

## Modules
```text
Proxy     – intercept/modify requests on the fly (Intercept)
Repeater  – send a request, edit, repeat (Ctrl+R from Proxy)
Intruder  – fuzzing: Sniper/Battering ram/Pitchfork/Cluster bomb
Decoder   – encode/decode (base64, URL, hex)
Comparer  – diff responses (blind SQLi/boolean)
Extender  – BApp Store (Autorize, Turbo Intruder, JWT Editor, Param Miner)
```

## Useful extensions
```text
Autorize     – authorization/IDOR testing (compares responses with/without a session)
Turbo Intruder – fast fuzzing (race conditions)
JWT Editor   – JWT manipulation and signing
Param Miner  – hidden parameters, cache poisoning
```

## Notes / Pitfalls
- Set scope at the start (Target > Scope) — otherwise you catch noise from the whole internet.
- Match & Replace to auto-inject headers/tokens.

## Mitigation / Hardening (blue perspective)
- HSTS + cert pinning makes MITM harder; certificate transparency monitoring.

## Sources
- [PortSwigger – Burp docs](https://portswigger.net/burp/documentation)
