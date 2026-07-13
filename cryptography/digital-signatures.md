---
title: "Digital signatures"
category: "cryptography"
tags: ["cryptography", "signatures", "integrity", "authenticity"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Digital signatures

## TL;DR
A digital signature proves a message's **integrity** (not altered) and **authenticity** (who signed it), and provides **non-repudiation** (the signer can't credibly deny it). The signer uses a private key; anyone verifies with the public key. Underpins TLS certs, code signing, JWTs, and software supply-chain integrity.

## How it works
```text
Sign:   hash the message -> encrypt/sign the hash with the SIGNER'S PRIVATE key -> signature.
Verify: hash the message -> check the signature with the signer's PUBLIC key -> match = valid.
Because only the private key holder can produce a signature the public key verifies,
it proves authenticity + integrity (any change breaks the hash match).
```

## Signature vs MAC vs encryption
```text
Signature (asymmetric) – integrity + authenticity + non-repudiation; public verification.
MAC/HMAC (symmetric)   – integrity + authenticity, but NO non-repudiation (shared secret;
                         either party could have produced it). Faster; for two trusted parties.
Encryption             – confidentiality (different goal). Sign-then-encrypt / AEAD as needed.
```

## Algorithms
```text
RSA (RSA-PSS)  – widely supported; larger keys/signatures.
ECDSA          – smaller keys, efficient; needs good randomness (nonce reuse = key leak!).
EdDSA (Ed25519) – modern, fast, deterministic (avoids the ECDSA nonce pitfall). Recommended.
Post-quantum   – ML-DSA/SLH-DSA emerging (see cryptography/post-quantum).
```

## Where they're used
```text
- TLS certificates (CA signs the cert; see pki-x509).
- Code/artifact signing (cosign/Sigstore — supply-chain integrity).
- JWTs (JWS — see jwt-crypto), documents, email (S/MIME, PGP), software updates.
```

## Security considerations
```text
- Protect the private key (HSM/KMS) — compromise = forge signatures until revoked.
- ECDSA needs unique, unpredictable nonces (reuse/bias leaks the private key — famous failures).
- Verify the WHOLE chain + validity + revocation, not just "a signature exists".
- Bind signatures to context (what/when/who) to prevent replay/substitution.
```

## Sources
- [NIST FIPS 186-5 (DSS)](https://csrc.nist.gov/pubs/fips/186-5/final) · related: [symmetric-vs-asymmetric](./symmetric-vs-asymmetric.md), [pki-x509](./pki-x509.md), [jwt-crypto](./jwt-crypto.md)
