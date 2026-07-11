---
title: "A03 – Injection"
category: "appsec"
tags: ["owasp", "injection", "sqli", "xss"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# A03 – Injection

## TL;DR
Untrusted input interpreted as a command/query. Includes SQLi, NoSQLi, command injection, LDAP, XPath, and XSS (now folded into this category). Root cause: mixing data with code.

## Variants
```text
SQL injection      – see red-team/web/sqli.md
NoSQL injection    – {"$gt":""} / {"$ne":null} in Mongo filters
Command injection  – ; | ` $() in shelled-out input
LDAP injection     – *)(uid=* in filters
XPath / XXE         – malicious XML / external entities
SSTI               – {{7*7}} in template engines -> often RCE
XSS                – JS in the browser (see red-team/web/xss.md)
```

## Quick tests
```text
'  "  `  ;  |  --  {{7*7}}  ${7*7}  <img src=x onerror=alert(1)>
NoSQL: username[$ne]=x&password[$ne]=x
XXE:   <!DOCTYPE r [<!ENTITY x SYSTEM "file:///etc/passwd">]><r>&x;</r>
```

## Detection (Blue Team)
- WAF/log patterns for query keywords, template markers, shell metacharacters.
- Spikes in DB/app errors; SSRF/DNS callbacks from SSTI/XXE.

## Mitigation / Hardening
- **Parameterization / prepared statements** (SQL), safe query builders (NoSQL).
- No shelling out with interpolation — use argv arrays / language APIs.
- Context-aware output encoding (XSS), disable XML external entities (XXE).
- Sandbox / logic-less templates (SSTI), input allow-listing, least-privilege backends.

## Sources
- [OWASP A03:2021](https://owasp.org/Top10/A03_2021-Injection/) · [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
