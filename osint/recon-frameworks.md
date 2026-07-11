---
title: "OSINT – narzędzia i frameworki"
category: "osint"
tags: ["osint", "recon"]
platform: "agnostic"
mitre: ["T1591", "T1593"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# OSINT – narzędzia i frameworki

## TL;DR
Rozpoznanie z jawnych źródeł: infrastruktura, ludzie, wycieki, media. Pasywne (bez dotykania celu) minimalizuje wykrycie.

## Infrastruktura
```bash
whois example.com
amass enum -passive -d example.com          # subdomeny, ASN
# Shodan – wystawione usługi
shodan search "org:\"Example Corp\""
shodan host 93.184.216.34
# Censys / FOFA – analogicznie
# theHarvester – e-maile, hosty, z wielu źródeł
theHarvester -d example.com -b all
```

## Ludzie / konta
```text
- Sherlock / Maigret – nazwa użytkownika po wielu serwisach
- hunter.io / phonebook.cz – e-maile firmowe
- LinkedIn -> lista pracowników -> format e-mail -> lista do spray/phishing
- EXIF w publikowanych zdjęciach (exiftool) – lokalizacja, sprzęt
```

## Wycieki danych
```text
- HaveIBeenPwned (API) – czy e-mail w wycieku
- Dehashed / IntelX – dane z breachy (autoryzowane użycie)
- GitHub/GitLab search + gitleaks/trufflehog na publicznych repo firmy
```

## Frameworki
```text
- Maltego – graf powiązań (transforms)
- SpiderFoot – automat OSINT (200+ modułów)
- recon-ng – modułowy, jak metasploit dla OSINT
- OSINT Framework (osintframework.com) – katalog narzędzi
```

## Obrona (Blue Team)
- Monitoruj własną powierzchnię (ASM), wycieki (HIBP domain), wzmianki firmy.
- Minimalizuj metadane w publikacjach, świadomość pracowników (LinkedIn oversharing).

## Źródła
- [OSINT Framework](https://osintframework.com/) · [SpiderFoot](https://github.com/smicallef/spiderfoot)
