---
title: "Burp Suite – szybki warsztat"
category: "red-team"
tags: ["tools", "web", "proxy"]
platform: "web"
mitre: ["T1190"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Burp Suite

## TL;DR
Proxy przechwytujący ruch HTTP(S). Przepływ: Proxy (przechwyć) → Repeater (ręczne manipulacje) → Intruder (fuzzing) → Scanner (Pro).

## Setup
```text
1. Proxy > Options: listener 127.0.0.1:8080
2. Przeglądarka: proxy na 8080 (lub wbudowany Burp Browser)
3. Zainstaluj cert CA Burpa (http://burp -> CA Certificate) by widzieć HTTPS
```

## Moduły
```text
Proxy     – przechwytuj/modyfikuj żądania w locie (Intercept)
Repeater  – wyślij żądanie, edytuj, powtarzaj (Ctrl+R z Proxy)
Intruder  – fuzzing: Sniper/Battering ram/Pitchfork/Cluster bomb
Decoder   – encode/decode (base64, URL, hex)
Comparer  – diff odpowiedzi (blind SQLi/boolean)
Extender  – BApp Store (Autorize, Turbo Intruder, JWT Editor, Param Miner)
```

## Przydatne rozszerzenia
```text
Autorize     – testy autoryzacji/IDOR (porównuje odpowiedzi z/bez sesji)
Turbo Intruder – szybki fuzzing (race conditions)
JWT Editor   – manipulacja i podpisywanie JWT
Param Miner  – ukryte parametry, cache poisoning
```

## Uwagi / Pułapki
- Scope ustaw na start (Target > Scope) — inaczej łapiesz szum z całego internetu.
- Match & Replace do automatycznego wstrzykiwania nagłówków/tokenów.

## Mitygacja / Hardening (perspektywa blue)
- HSTS + cert pinning utrudnia MITM; certificate transparency monitoring.

## Źródła
- [PortSwigger – Burp docs](https://portswigger.net/burp/documentation)
