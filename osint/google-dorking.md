---
title: "Google dorking"
category: "osint"
tags: ["osint", "recon", "google"]
platform: "web"
mitre: ["T1593.002"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Google dorking

## TL;DR
Advanced search-engine operators reveal exposed files, panels, errors and sensitive data. Part of passive reconnaissance.

## Operators
```text
site:example.com                 – domain only
filetype:pdf (or ext:)           – file type
intitle:"index of"               – directory listing
inurl:admin                      – URL fragment
intext:"password"                – in the body
cache:example.com                – cached version
"-" excludes, "|" OR, "*" wildcard
```

## Useful combinations (recon of your own surface)
```text
site:example.com filetype:pdf | filetype:xlsx | filetype:docx
site:example.com intitle:"index of"
site:example.com inurl:(login | admin | portal | dashboard)
site:example.com intext:"api_key" | "secret" | "BEGIN RSA PRIVATE KEY"
site:*.example.com                 – indexed subdomains
site:pastebin.com "example.com"    – leaks
```

## Related
- Google Hacking Database (GHDB) — ready-made dorks on Exploit-DB.
- Similarly: Shodan (`org:`, `ssl:`, `port:`), GitHub search (secrets in code).

## Detection / defense (Blue Team)
- Monitor indexing of sensitive paths; `robots.txt` does **not** protect (it only suggests).
- Alert when company files/domains appear in results/pastebins.

## Mitigation / Hardening
- Authorization on panels/files (not "security by obscurity"), `X-Robots-Tag: noindex`.
- Remove exposed directories (`index of`), regularly dork your own domain.

## Sources
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
