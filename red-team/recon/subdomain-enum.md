---
title: "Enumeracja subdomen"
category: "red-team"
tags: ["recon", "osint", "subdomains"]
platform: "web"
mitre: ["T1595", "T1590"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Enumeracja subdomen

## TL;DR
Mapowanie powierzchni ataku domeny: pasywnie (bez dotykania celu) → aktywnie (bruteforce/permutacje) → weryfikacja żywych hostów.

## Komendy
```bash
# Pasywnie – z publicznych źródeł (CT logs, API)
subfinder -d example.com -all -silent -o subs.txt
amass enum -passive -d example.com -o amass.txt

# Certificate Transparency
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sort -u

# Aktywnie – bruteforce DNS
puredns bruteforce wordlist.txt example.com -r resolvers.txt

# Permutacje istniejących subdomen
gotator -sub subs.txt -perm words.txt | puredns resolve -r resolvers.txt

# Weryfikacja żywych + tytuł/status
cat subs.txt | httpx -silent -title -status-code -tech-detect
```

## Wykrywanie (Blue Team)
- Monitoruj **własne CT logi** (crt.sh, Cert Spotter) — nowe certy = nowe subdomeny do inwentaryzacji.
- Anomalie w logach DNS: masowe NXDOMAIN z jednego resolvera = bruteforce.

## Mitygacja / Hardening
- Wildcard DNS z ostrożnością (utrudnia bruteforce, ale maskuje realny stan).
- Regularna inwentaryzacja assetów (ASM), usuwanie martwych rekordów (dangling → subdomain takeover).

## Uwagi / Pułapki
- Sprawdź **subdomain takeover**: `nuclei -t takeovers/` na CNAME-ach wskazujących nieistniejące usługi (S3, Azure, GitHub Pages).

## Źródła
- [OWASP Amass](https://github.com/owasp-amass/amass)
- [ProjectDiscovery](https://docs.projectdiscovery.io/)
