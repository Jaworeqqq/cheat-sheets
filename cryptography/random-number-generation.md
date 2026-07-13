---
title: "Random number generation"
category: "cryptography"
tags: ["cryptography", "randomness", "csprng", "fundamentals"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Random number generation

## TL;DR
Cryptography depends on unpredictable randomness. Using a non-cryptographic PRNG (like `rand()` / `Math.random()`) for security purposes — tokens, keys, IVs, nonces, salts — is a serious, common vulnerability: attackers can predict the output. Always use a CSPRNG for anything security-relevant.

## PRNG vs CSPRNG vs TRNG
```text
PRNG (non-crypto)  – fast, deterministic from a seed; PREDICTABLE. Fine for games/simulation,
                     NEVER for security (Math.random, rand(), Mersenne Twister).
CSPRNG             – cryptographically secure: unpredictable even given prior outputs; well-seeded
                     from OS entropy. Use this for all security purposes.
TRNG               – hardware/true randomness from physical noise; often feeds the OS entropy pool.
```

## Use the OS/crypto CSPRNG (by language)
```text
OS source   – /dev/urandom, getrandom() (Linux), CryptGenRandom/BCryptGenRandom (Windows).
Python      – secrets.token_bytes()/token_hex()  (NOT random.random for security)
Node.js     – crypto.randomBytes()               (NOT Math.random)
Java        – SecureRandom                        (NOT java.util.Random)
Go          – crypto/rand                          (NOT math/rand)
C/C++       – getrandom()/BCryptGenRandom          (NOT rand())
```

## What needs a CSPRNG
```text
Keys, IVs/nonces, salts, session IDs/tokens, password-reset tokens, API keys, OTP secrets,
CSRF tokens, ECDSA nonces — anything an attacker must not predict.
```

## Common failures
```text
- Using a fast PRNG for tokens/session IDs -> predictable -> account takeover.
- Poor/insufficient seeding (low entropy at boot, embedded devices) -> guessable keys.
- Reusing IVs/nonces (esp. AES-GCM, ECDSA) -> catastrophic (key/plaintext recovery).
- Truncating or biasing output; rolling your own RNG.
```

## Best practices
```text
- Always call the platform CSPRNG; never Math.random/rand for security.
- Ensure adequate entropy at startup (esp. VMs/containers/IoT); use getrandom (blocks until seeded).
- Unique nonces/IVs per operation; never reuse. Sufficient token length (>=128 bits).
```

## Sources
- [NIST SP 800-90A/B/C (RNG)](https://csrc.nist.gov/pubs/sp/800/90/a/r1/final) · [OWASP – Cryptographic Storage CS](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) · related: [key-management](./key-management.md)
