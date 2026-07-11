---
title: "DNS Recon"
category: "red-team"
tags: ["recon", "dns"]
platform: "agnostic"
mitre: ["T1590.002"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# DNS Recon

## TL;DR
Rekordy DNS ujawniają infrastrukturę: mail (MX), serwery (A/AAAA), usługi (SRV), polityki (SPF/DMARC), a czasem transfer strefy oddaje wszystko.

## Komendy
```bash
# Podstawowe rekordy
dig example.com ANY +noall +answer
dig example.com MX +short
dig TXT example.com +short          # SPF/DMARC/weryfikacje

# Reverse lookup
dig -x 93.184.216.34 +short

# Próba transferu strefy (AXFR) – częsty misconfig
dig AXFR example.com @ns1.example.com

# Automat
dnsrecon -d example.com -t std,axfr
fierce --domain example.com
```

## Wykrywanie (Blue Team)
- Żądania AXFR z niedozwolonych IP w logach serwera DNS.
- Nietypowo wysoka liczba zapytań PTR/TXT z jednego źródła.

## Mitygacja / Hardening
- Ogranicz AXFR do autoryzowanych slave'ów (`allow-transfer`).
- Minimalizuj informacje w rekordach TXT (nie zostawiaj starych weryfikacji).
- Wdróż DMARC `p=reject`, poprawny SPF (`-all`).

## Źródła
- [dnsrecon](https://github.com/darkoperator/dnsrecon)
