---
title: "JWT – attacks and defense"
category: "appsec"
tags: ["api-security", "jwt", "authentication"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# JWT – attacks and defense

## TL;DR
JSON Web Token = `header.payload.signature` (base64url). Attacks target weak signature verification: `alg:none`, RS256→HS256 confusion, weak secret, missing claim validation.

## Anatomy
```text
header:    {"alg":"HS256","typ":"JWT"}
payload:   {"sub":"user","role":"user","exp":1710000000}
signature: HMACSHA256(base64(header)+"."+base64(payload), secret)
```

## Attacks
```text
1. alg:none         – set "alg":"none", drop the signature (if the server accepts it)
2. alg confusion    – RS256 -> HS256, use the PUBLIC key as the HMAC secret
3. weak secret      – bruteforce the HMAC (hashcat -m 16500)
4. kid injection    – path traversal / SQLi in the kid header
5. jwk/jku spoofing – supply your own public key
6. no validation    – exp/aud/iss ignored -> replay/forwarding
```

```bash
# Bruteforce an HS256 secret
hashcat -m 16500 jwt.txt rockyou.txt
# Manipulation (Burp JWT Editor / jwt_tool)
jwt_tool eyJ... -T           # tamper
jwt_tool eyJ... -X a         # alg:none exploit
jwt_tool eyJ... -C -d wordlist.txt   # crack
```

## Detection (Blue Team)
- Tokens with `alg:none`, an alg inconsistent with the expected one, failed signature verifications.
- Token reuse from different IPs/devices (replay).

## Mitigation / Hardening
- Enforce the expected `alg` server-side (allow-list; don't trust the header).
- Strong secret (256-bit random) for HMAC / correct RS256 verification.
- Validate `exp`, `nbf`, `aud`, `iss`; short TTL + refresh; key rotation (kid from a secure store).
- Consider reference tokens + revocation instead of long-lived JWTs.

## Sources
- [PortSwigger – JWT](https://portswigger.net/web-security/jwt) · [jwt_tool](https://github.com/ticarpi/jwt_tool)
