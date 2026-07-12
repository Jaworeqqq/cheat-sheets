---
title: "Race conditions (TOCTOU)"
category: "appsec"
tags: ["secure-coding", "race-conditions", "concurrency"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Race conditions (TOCTOU)

## TL;DR
A race condition happens when the outcome depends on timing of concurrent operations. In security, the classic is TOCTOU (Time-Of-Check to Time-Of-Use): a value is checked, then used, and an attacker changes it in between. In web apps this enables limit bypasses (redeem a coupon N times, overdraw a balance) by firing parallel requests.

## Web/business-logic races (most common today)
```text
Pattern: check-then-act without atomicity.
 - Apply a gift card / coupon: parallel requests each pass the "is it unused?" check.
 - Withdraw/transfer: parallel requests each see the old balance -> overdraw.
 - "One vote / one signup / one redemption": fire many at once -> multiple succeed.
 - MFA/OTP or rate-limit windows: parallelism slips extra attempts through.
```

## Exploitation
```text
- Send many identical requests as simultaneously as possible.
- Burp "Turbo Intruder" or the single-packet attack (send in one TCP packet / HTTP/2)
  to minimize timing jitter and maximize the race window.
- Look for state changes that should be "once" but happen multiple times.
```

## Classic filesystem TOCTOU
```text
if access(path) == OK:      # check
    open(path)              # use  <- attacker swaps path -> symlink to /etc/shadow
Fix: operate on file descriptors/handles, not paths; use atomic open with the right flags.
```

## Detection (Blue Team)
- Bursts of near-simultaneous identical requests; state that changed more times than allowed
  (e.g. a coupon used twice, balance below zero).

## Mitigation / Hardening
```text
- Make the operation ATOMIC:
    * DB constraints (unique index, CHECK), atomic UPDATE ... WHERE balance >= amount.
    * Row/record locking (SELECT ... FOR UPDATE) or optimistic concurrency (version column).
    * Idempotency keys for "once" operations.
    * Distributed locks (Redis/etcd) where DB atomicity isn't enough.
- Don't rely on check-then-act across separate statements/requests.
- Rate limiting helps but does NOT fix a true race — enforce atomicity at the data layer.
```

## Sources
- [PortSwigger – Race conditions](https://portswigger.net/web-security/race-conditions) · [OWASP – TOCTOU](https://owasp.org/www-community/vulnerabilities/)
