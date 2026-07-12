---
title: "JWT – the cryptographic side"
category: "cryptography"
tags: ["cryptography", "jwt", "jws", "jwe"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# JWT – the cryptographic side

## TL;DR
The crypto foundations behind JWTs (attack/exploitation is in [appsec/api-security/jwt-attacks](../appsec/api-security/jwt-attacks.md)). A JWT is usually a **JWS** (signed, integrity-protected but readable) — not encrypted. **JWE** is the encrypted form. Choosing the right algorithm and key management is what makes it safe.

## JWS vs JWE
```text
JWS (signed)   – header.payload.signature; payload is base64url, NOT secret (anyone can read it).
                 Guarantees integrity + authenticity, not confidentiality.
JWE (encrypted) – header.encrypted_key.iv.ciphertext.tag; payload is confidential.
Rule: don't put secrets in a JWS payload; use JWE (or don't put them in the token at all).
```

## Algorithm families (the `alg` header)
```text
HS256/384/512  – HMAC with a shared secret (symmetric). Same key signs & verifies.
RS256/384/512  – RSA signature (asymmetric). Private key signs, public key verifies.
ES256/384/512  – ECDSA (asymmetric, smaller keys/signatures than RSA).
EdDSA (Ed25519) – modern, fast, safe defaults (recommended where supported).
none           – no signature. MUST be rejected by verifiers.
```

## Symmetric vs asymmetric — when to use
```text
HS* (shared secret) – simplest; fine when the SAME party signs and verifies (monolith).
                      Risk: the verifier needs the secret, so it can also FORGE tokens.
RS*/ES*/EdDSA       – use when many services verify but only one signs (issuer/IdP model):
                      distribute only the PUBLIC key; verifiers can't forge.
```

## Why "alg confusion" works (RS256 -> HS256)
```text
If a server fetches the algorithm from the token header and uses one verify() call,
an attacker can switch RS256 to HS256 and sign with the PUBLIC RSA key as the HMAC secret.
The server, expecting RSA, verifies HMAC using the public key it already trusts -> forged token.
Fix: pin the expected alg server-side; never let the token pick the algorithm/key type.
```

## Key management
```text
- Strong secrets for HS* (>= 256-bit random), rotate; never hardcode.
- Asymmetric keys via JWKS endpoint with a `kid`; rotate keys, cache with limits.
- Short token lifetimes (exp) + refresh; consider revocation for long-lived needs.
```

## Choosing algorithms (guidance)
```text
- Multi-service verification -> EdDSA or ES256 (asymmetric).
- Single trusted party -> HS256 with a strong secret is acceptable.
- Always reject `none` and enforce an allow-list of expected algs.
```

## Sources
- [RFC 7519 (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) · [RFC 7515 (JWS)](https://datatracker.ietf.org/doc/html/rfc7515) · [RFC 7516 (JWE)](https://datatracker.ietf.org/doc/html/rfc7516)
