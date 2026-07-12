---
title: "Symmetric vs Asymmetric cryptography"
category: "cryptography"
tags: ["cryptography", "fundamentals", "encryption"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Symmetric vs Asymmetric cryptography

## TL;DR
Symmetric = one shared key, fast, for bulk data. Asymmetric = a public/private key pair, slower, solves key distribution and enables signatures. Real systems use both: asymmetric to exchange a symmetric key, symmetric for the data (hybrid encryption).

## Side by side
| | Symmetric | Asymmetric |
|---|-----------|------------|
| Keys | one shared secret | public + private pair |
| Speed | fast (bulk data) | slow (small data only) |
| Solves | confidentiality | key distribution, signatures, identity |
| Examples | AES, ChaCha20 | RSA, ECC (ECDSA/ECDH), EdDSA |
| Challenge | sharing the key securely | slower, bigger keys/ops |

## Symmetric
```text
Use: encrypting data at rest / in transit (bulk).
Algorithms: AES-256-GCM, ChaCha20-Poly1305 (AEAD = encryption + integrity).
Key sizes: AES-128/256. Requires: secure key exchange + nonce/IV management.
```

## Asymmetric
```text
Use: key exchange, digital signatures, identity/certificates.
Encryption: RSA-OAEP (small payloads only, e.g. a symmetric key).
Key exchange: ECDH / X25519 (derive a shared secret over an insecure channel).
Signatures: RSA-PSS, ECDSA, Ed25519.
Key sizes: RSA >= 2048/3072; ECC P-256 ~ RSA 3072 strength (smaller & faster).
```

## Hybrid encryption (how TLS actually works)
```text
1. Asymmetric key exchange (ECDHE) establishes a shared secret + authenticates the server (cert).
2. That secret derives symmetric keys.
3. Bulk application data is encrypted symmetrically (AES-GCM/ChaCha20).
-> Best of both: secure key distribution + fast bulk encryption + forward secrecy.
```

## Choosing (quick guidance)
```text
- Encrypt lots of data -> symmetric (AES-GCM / ChaCha20).
- Exchange a key over an insecure channel / verify identity -> asymmetric.
- Signatures / tokens across services -> Ed25519 or ECDSA (see jwt-crypto).
- Prefer modern curves (X25519/Ed25519); avoid textbook RSA and weak params.
```

## Sources
- [Cloudflare – asymmetric vs symmetric](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/) · related: [tls-config](./tls-config.md), [key-management](./key-management.md)
