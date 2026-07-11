---
title: "Password cracking (hashcat / john)"
category: "cryptography"
tags: ["cryptography", "password-cracking", "hashcat"]
platform: "agnostic"
mitre: ["T1110.002"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Password cracking

## TL;DR
Offline cracking of hashes obtained legally during an engagement. Identify the type → pick an attack (dictionary + rules → mask → brute) → hashcat (GPU) or john.

## Hash identification
```bash
hashid '$2y$10$...'          # bcrypt
nth --text '<hash>'          # name-that-hash
# hashcat --identify hash.txt
```

## Common hashcat modes (-m)
```text
0     MD5              100   SHA1           1400  SHA256
1000  NTLM             3200  bcrypt         1800  sha512crypt
5600  NetNTLMv2        13100 Kerberoast (TGS-REP RC4)   18200 AS-REP
16500 JWT (HS256)      22000 WPA-PBKDF2     500   md5crypt
```

## Attacks
```bash
# Dictionary + rules (most effective on human passwords)
hashcat -m 1000 hashes.txt rockyou.txt -r rules/best64.rule

# Mask (brute with a known pattern) – ?l lower ?u upper ?d digit ?s special
hashcat -m 1000 hashes.txt -a 3 '?u?l?l?l?l?l?d?d'

# Combinator / hybrid
hashcat -m 1000 hashes.txt -a 6 wordlist.txt '?d?d?d'

# John
john --wordlist=rockyou.txt --rules hashes.txt
john --show hashes.txt
```

## Optimization
- `--opt-kernel` (-O), sort wordlists, good rules (OneRuleToRuleThemAll).
- Start with dictionary+rules, then masks based on found patterns.

## Defense (Blue Team / hardening)
- Strong KDFs: **bcrypt/scrypt/argon2** with a salt (not raw MD5/SHA).
- Enforce long passwords/passphrases, banned password list, MFA (reduces the value of a cracked password).
- Slow hashes + per-user salt make mass cracking impractical.

## Sources
- [hashcat wiki](https://hashcat.net/wiki/) · [John the Ripper](https://www.openwall.com/john/)
