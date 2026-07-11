---
title: "Łamanie haseł (hashcat / john)"
category: "cryptography"
tags: ["cryptography", "password-cracking", "hashcat"]
platform: "agnostic"
mitre: ["T1110.002"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Łamanie haseł

## TL;DR
Offline cracking hashy zdobytych legalnie w zaangażowaniu. Zidentyfikuj typ → wybierz atak (słownik + reguły → maska → brute) → hashcat (GPU) lub john.

## Identyfikacja hasha
```bash
hashid '$2y$10$...'          # bcrypt
nth --text '<hash>'          # name-that-hash
# hashcat --identify hash.txt
```

## Częste tryby hashcat (-m)
```text
0     MD5              100   SHA1           1400  SHA256
1000  NTLM             3200  bcrypt         1800  sha512crypt
5600  NetNTLMv2        13100 Kerberoast (TGS-REP RC4)   18200 AS-REP
16500 JWT (HS256)      22000 WPA-PBKDF2     500   md5crypt
```

## Ataki
```bash
# Słownik + reguły (najskuteczniejsze na ludzkie hasła)
hashcat -m 1000 hashes.txt rockyou.txt -r rules/best64.rule

# Maska (brute o znanym wzorcu) – ?l lower ?u upper ?d digit ?s special
hashcat -m 1000 hashes.txt -a 3 '?u?l?l?l?l?l?d?d'

# Combinator / hybrid
hashcat -m 1000 hashes.txt -a 6 wordlist.txt '?d?d?d'

# John
john --wordlist=rockyou.txt --rules hashes.txt
john --show hashes.txt
```

## Optymalizacja
- `--opt-kernel` (-O), sortuj słowniki, dobre reguły (OneRuleToRuleThemAll).
- Zacznij od słownik+reguły, potem maski na podstawie znalezionych wzorców.

## Obrona (Blue Team / hardening)
- Silne KDF: **bcrypt/scrypt/argon2** z solą (nie MD5/SHA-raw).
- Wymuś długie hasła/passphrase, banned password list, MFA (redukuje wartość złamanego hasła).
- Wolne hashe + per-user salt czynią masowy crack niepraktycznym.

## Źródła
- [hashcat wiki](https://hashcat.net/wiki/) · [John the Ripper](https://www.openwall.com/john/)
