---
title: "Google Dorking"
category: "osint"
tags: ["osint", "recon", "google"]
platform: "web"
mitre: ["T1593.002"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Google Dorking

## TL;DR
Zaawansowane operatory wyszukiwarki ujawniają wystawione pliki, panele, błędy i wrażliwe dane. Element rekonesansu pasywnego.

## Operatory
```text
site:example.com                 – tylko domena
filetype:pdf (lub ext:)          – typ pliku
intitle:"index of"               – listing katalogów
inurl:admin                      – fragment URL
intext:"password"                – w treści
cache:example.com                – wersja z cache
"-" wyklucza, "|" OR, "*" wildcard
```

## Przydatne kombinacje (recon własnej powierzchni)
```text
site:example.com filetype:pdf | filetype:xlsx | filetype:docx
site:example.com intitle:"index of"
site:example.com inurl:(login | admin | portal | dashboard)
site:example.com intext:"api_key" | "secret" | "BEGIN RSA PRIVATE KEY"
site:*.example.com                 – subdomeny w indeksie
site:pastebin.com "example.com"    – wycieki
```

## Powiązane
- Google Hacking Database (GHDB) — gotowe dorki na Exploit-DB.
- Analogicznie: Shodan (`org:`, `ssl:`, `port:`), GitHub search (sekrety w kodzie).

## Wykrywanie / obrona (Blue Team)
- Monitoruj indeksację wrażliwych ścieżek; `robots.txt` **nie** chroni (tylko sugeruje).
- Alert na pojawienie się firmowych plików/domen w wynikach/pastebinach.

## Mitygacja / Hardening
- Autoryzacja na panelach/plikach (nie „security by obscurity"), `X-Robots-Tag: noindex`.
- Usuń wystawione katalogi (`index of`), skanuj własną domenę dorkami regularnie.

## Źródła
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
