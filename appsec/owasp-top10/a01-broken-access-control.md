---
title: "A01 – Broken Access Control"
category: "appsec"
tags: ["owasp", "access-control", "idor"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A01 – Broken Access Control

## TL;DR
Najczęstsze ryzyko OWASP. Użytkownik robi to, na co nie powinien mieć uprawnień: dostęp do cudzych danych (IDOR), funkcji admina, obejście autoryzacji. Autoryzacja **musi** być egzekwowana po stronie serwera.

## Typowe warianty
```text
IDOR                 – /api/orders/123 -> zmień na 124 (cudze zamówienie)
Missing function-level authz – ukryty przycisk admina, ale endpoint /admin/* działa
Vertical privesc     – zwykły user -> funkcje admina
Horizontal privesc   – user A -> dane usera B
Metadata manipulation – rola/uprawnienia w JWT/cookie edytowane przez klienta
CORS misconfig       – Access-Control-Allow-Origin: * + credentials
Path traversal       – ../../etc/passwd
Force browsing       – bezpośredni URL do chronionego zasobu
```

## Testowanie
```text
- Powtórz żądania z sesją innego usera (Burp Autorize) -> te same dane?
- Zmieniaj ID/UUID w parametrach, ciałach JSON, ukrytych polach.
- Usuń/zmień nagłówki autoryzacji, testuj metody (GET->POST/PUT/DELETE).
- Testuj IDOR na eksportach, załącznikach, presigned URL.
```

## Wykrywanie (Blue Team)
- Logi: dostęp do wielu ID zasobów przez jednego usera, 403 followed by success (bypass).
- Anomalie: user pobierający zakresy ID sekwencyjnie.

## Mitygacja / Hardening
- **Deny by default**; autoryzacja per żądanie po stronie serwera (nie ukrywanie w UI).
- Sprawdzaj właściciela zasobu (`resource.owner == currentUser`), nie ufaj ID z klienta.
- Nieodgadywalne identyfikatory (UUID) to defense-in-depth, nie autoryzacja.
- Centralny mechanizm authz (policy engine), testy autoryzacji w CI.

## Źródła
- [OWASP A01:2021](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) · [PortSwigger – Access control](https://portswigger.net/web-security/access-control)
