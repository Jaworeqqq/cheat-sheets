---
title: "Post-quantum cryptography"
category: "cryptography"
tags: ["cryptography", "post-quantum", "pqc"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Post-quantum cryptography (PQC)

## TL;DR
A sufficiently large quantum computer would break today's asymmetric crypto (RSA, ECC) via Shor's algorithm. PQC are new algorithms believed resistant to quantum attacks. NIST has standardized the first set (2024). The urgent driver is **"harvest now, decrypt later"** — data stolen today can be decrypted once quantum arrives.

## What quantum breaks (and doesn't)
```text
Broken by Shor's algorithm (asymmetric):
  - RSA, Diffie-Hellman, ECC (ECDSA/ECDH) — key exchange & signatures.
Weakened by Grover's algorithm (symmetric/hash), but manageable:
  - AES / SHA — effectively halves strength -> use AES-256, SHA-384+ and you're fine.
So: the crisis is ASYMMETRIC crypto (key exchange + signatures), not symmetric.
```

## NIST standardized algorithms (2024)
```text
ML-KEM (FIPS 203, "Kyber")     – key encapsulation (key exchange). The main one.
ML-DSA (FIPS 204, "Dilithium") – digital signatures (general purpose).
SLH-DSA (FIPS 205, "SPHINCS+") – hash-based signatures (conservative fallback).
(FN-DSA / Falcon expected for compact signatures.)
```

## "Harvest now, decrypt later" (why act now)
```text
An adversary can record encrypted traffic today and decrypt it years later when quantum arrives.
-> Data with long confidentiality lifetimes (secrets, health, gov) is at risk NOW.
Priority: migrate key exchange for long-lived confidential data first.
```

## Migration approach
```text
1. Inventory where you use RSA/ECC (TLS, VPNs, code signing, PKI, tokens).
2. Adopt hybrid schemes first (classical + PQC together) — safe if one breaks.
   (e.g. X25519+ML-KEM hybrid key exchange, already appearing in TLS/SSH.)
3. Prioritize long-lived-secret systems and long-lived signatures (firmware, roots).
4. Ensure crypto-agility: abstract algorithms so you can swap them without rewrites.
```

## Practical status
```text
- TLS 1.3 hybrid KEX (X25519MLKEM768) rolling out in browsers/servers.
- OpenSSH added PQ hybrid key exchange. Cloud KMS/HSM adding PQC support.
- Start planning; don't wait for a "quantum day" announcement.
```

## Sources
- [NIST PQC](https://www.nist.gov/pqcrypto) · [FIPS 203/204/205](https://csrc.nist.gov/pubs/fips/203/final) · related: [symmetric-vs-asymmetric](./symmetric-vs-asymmetric.md)
