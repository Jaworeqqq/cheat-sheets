---
title: "HMAC & message authentication codes"
category: "cryptography"
tags: ["cryptography", "hmac", "mac", "integrity"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# HMAC & MACs

## TL;DR
A MAC (Message Authentication Code) proves a message's integrity and authenticity between two parties sharing a secret key. HMAC is the standard MAC construction built on a hash function. Unlike a digital signature, a MAC is symmetric (shared secret) so it gives no non-repudiation — but it's fast and ideal for API request signing, webhooks, and token integrity.

## MAC vs signature vs hash
```text
Hash        – integrity only; anyone can recompute (no secret) -> no authenticity.
MAC/HMAC    – integrity + authenticity via a SHARED secret; either party could produce it
              (no non-repudiation). Fast, symmetric.
Signature   – integrity + authenticity + non-repudiation via asymmetric keys; public verification
              (see cryptography/digital-signatures).
Pick MAC for two trusted parties; signature when third parties must verify / non-repudiation matters.
```

## HMAC
```text
HMAC(key, message) = H( (key ⊕ opad) || H( (key ⊕ ipad) || message ) )
- Built on a hash (HMAC-SHA256 recommended); resistant to length-extension attacks (unlike raw H(key||msg)).
- Security depends on a strong, secret key (>= the hash output size ideally).
```

## Common uses
```text
- API request signing (AWS SigV4, Stripe/GitHub webhooks) — see appsec/api-security/webhooks-security.
- Verifying integrity of tokens/cookies (JWT HS256 = HMAC-SHA256; see jwt-crypto).
- Message integrity in protocols; deriving keys (HKDF uses HMAC).
```

## Pitfalls
```text
- Timing attacks: compare MACs in CONSTANT TIME (hmac.compare_digest), not `==`.
- Don't roll your own MAC (H(key||msg) is length-extension vulnerable) — use HMAC or an AEAD.
- Key management: rotate; never hardcode; per-purpose keys (see key-management).
- Encrypt-then-MAC (or use an AEAD like AES-GCM/ChaCha20-Poly1305 that MACs internally).
```

## AEAD (the modern default for encryption + integrity)
```text
AES-GCM / ChaCha20-Poly1305 combine encryption + authentication in one primitive.
Prefer AEAD over hand-composing encrypt + separate MAC when you need confidentiality too.
```

## Sources
- [RFC 2104 (HMAC)](https://datatracker.ietf.org/doc/html/rfc2104) · related: [digital-signatures](./digital-signatures.md), [encoding-vs-encryption](./encoding-vs-encryption.md), [jwt-crypto](./jwt-crypto.md)
