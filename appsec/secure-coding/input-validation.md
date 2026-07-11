---
title: "Secure Coding – walidacja i output encoding"
category: "appsec"
tags: ["secure-coding", "input-validation", "injection"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Walidacja wejścia i output encoding

## TL;DR
Większość injection (SQLi/XSS/cmd) wynika z mieszania danych z kodem. Zasady: waliduj wejście (allow-list), separuj dane od poleceń (parametryzacja), koduj wyjście kontekstowo.

## Walidacja wejścia
```text
- Allow-list > deny-list (definiuj co dozwolone, nie co zakazane).
- Waliduj: typ, długość, zakres, format (regex), kanoniczna forma.
- Waliduj na granicy zaufania (serwer), NIE tylko w kliencie.
- Odrzucaj, nie „naprawiaj" po cichu (sanityzacja bywa obchodzona).
```

## Separacja danych od poleceń (per kontekst)
```java
// SQL – prepared statement (NIE konkatenacja)
PreparedStatement ps = conn.prepareStatement("SELECT * FROM u WHERE id = ?");
ps.setInt(1, userId);
```
```python
# Command – argv, NIE shell=True z interpolacją
subprocess.run(["ping", "-c", "1", host])   # nie f"ping {host}" w shell
```
```javascript
// Output encoding – kontekstowy
res.send(escapeHtml(userInput));   // HTML context
// framework z auto-escape (React {var}, Jinja autoescape) zamiast innerHTML
```

## Mapowanie kontekst → obrona
| Kontekst | Ryzyko | Obrona |
|----------|--------|--------|
| SQL | SQLi | prepared statements / ORM binding |
| HTML | XSS | HTML entity encoding, auto-escape |
| OS command | command inj. | argv array, brak shell, allow-list |
| LDAP | LDAP inj. | escaping DN/filter |
| Path | traversal | kanonikalizacja + allow-list, brak `..` |
| Deserializacja | RCE | nie deserializuj niezaufanego; formaty bez kodu (JSON) |

## Weryfikacja
- SAST (Semgrep/CodeQL) na wzorce injection, code review, testy z payloadami.

## Źródła
- [OWASP Input Validation CS](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) · [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
