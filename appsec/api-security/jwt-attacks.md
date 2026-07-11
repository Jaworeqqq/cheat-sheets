---
title: "JWT – ataki i obrona"
category: "appsec"
tags: ["api-security", "jwt", "authentication"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# JWT – ataki i obrona

## TL;DR
JSON Web Token = `header.payload.signature` (base64url). Ataki celują w słabą weryfikację podpisu: `alg:none`, confusion RS256→HS256, słaby sekret, brak walidacji claims.

## Anatomia
```text
header:    {"alg":"HS256","typ":"JWT"}
payload:   {"sub":"user","role":"user","exp":1710000000}
signature: HMACSHA256(base64(header)+"."+base64(payload), secret)
```

## Ataki
```text
1. alg:none         – ustaw "alg":"none", usuń podpis (jeśli serwer akceptuje)
2. alg confusion    – RS256 -> HS256, użyj klucza PUBLICZNEGO jako sekretu HMAC
3. weak secret      – bruteforce HMAC (hashcat -m 16500)
4. kid injection    – path traversal / SQLi w nagłówku kid
5. jwk/jku spoofing – podstaw własny klucz publiczny
6. brak walidacji   – exp/aud/iss ignorowane -> replay/forwarding
```

```bash
# Bruteforce sekretu HS256
hashcat -m 16500 jwt.txt rockyou.txt
# Manipulacja (Burp JWT Editor / jwt_tool)
jwt_tool eyJ... -T           # tamper
jwt_tool eyJ... -X a         # alg:none exploit
jwt_tool eyJ... -C -d wordlist.txt   # crack
```

## Wykrywanie (Blue Team)
- Tokeny z `alg:none`, niespójny alg vs oczekiwany, nieudane weryfikacje podpisu.
- Reużycie tokenów z różnych IP/urządzeń (replay).

## Mitygacja / Hardening
- Wymuś oczekiwany `alg` po stronie serwera (allow-list; nie ufaj nagłówkowi).
- Silny sekret (256-bit losowy) dla HMAC / poprawna weryfikacja RS256.
- Waliduj `exp`, `nbf`, `aud`, `iss`; krótki TTL + refresh; rotacja kluczy (kid z bezpiecznego store).
- Rozważ tokeny referencyjne + revocation zamiast długożyjących JWT.

## Źródła
- [PortSwigger – JWT](https://portswigger.net/web-security/jwt) · [jwt_tool](https://github.com/ticarpi/jwt_tool)
