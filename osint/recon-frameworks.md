---
title: "OSINT – tools and frameworks"
category: "osint"
tags: ["osint", "recon"]
platform: "agnostic"
mitre: ["T1591", "T1593"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# OSINT – tools and frameworks

## TL;DR
Reconnaissance from open sources: infrastructure, people, breaches, media. Passive (without touching the target) minimizes detection.

## Infrastructure
```bash
whois example.com
amass enum -passive -d example.com          # subdomains, ASN
# Shodan – exposed services
shodan search "org:\"Example Corp\""
shodan host 93.184.216.34
# Censys / FOFA – similarly
# theHarvester – emails, hosts, from many sources
theHarvester -d example.com -b all
```

## People / accounts
```text
- Sherlock / Maigret – username across many services
- hunter.io / phonebook.cz – corporate emails
- LinkedIn -> employee list -> email format -> list for spray/phishing
- EXIF in published photos (exiftool) – location, device
```

## Data breaches
```text
- HaveIBeenPwned (API) – is an email in a breach
- Dehashed / IntelX – breach data (authorized use)
- GitHub/GitLab search + gitleaks/trufflehog on the company's public repos
```

## Frameworks
```text
- Maltego – relationship graph (transforms)
- SpiderFoot – OSINT automation (200+ modules)
- recon-ng – modular, like metasploit for OSINT
- OSINT Framework (osintframework.com) – tool catalog
```

## Defense (Blue Team)
- Monitor your own surface (ASM), leaks (HIBP domain), company mentions.
- Minimize metadata in publications, employee awareness (LinkedIn oversharing).

## Sources
- [OSINT Framework](https://osintframework.com/) · [SpiderFoot](https://github.com/smicallef/spiderfoot)
