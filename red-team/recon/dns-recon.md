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
DNS records reveal infrastructure: mail (MX), servers (A/AAAA), services (SRV), policies (SPF/DMARC), and sometimes a zone transfer hands over everything.

## Commands
```bash
# Basic records
dig example.com ANY +noall +answer
dig example.com MX +short
dig TXT example.com +short          # SPF/DMARC/verifications

# Reverse lookup
dig -x 93.184.216.34 +short

# Zone transfer (AXFR) attempt – common misconfig
dig AXFR example.com @ns1.example.com

# Automated
dnsrecon -d example.com -t std,axfr
fierce --domain example.com
```

## Detection (Blue Team)
- AXFR requests from unauthorized IPs in the DNS server logs.
- Unusually high volume of PTR/TXT queries from one source.

## Mitigation / Hardening
- Restrict AXFR to authorized slaves (`allow-transfer`).
- Minimize information in TXT records (don't leave stale verifications).
- Deploy DMARC `p=reject`, a correct SPF (`-all`).

## Sources
- [dnsrecon](https://github.com/darkoperator/dnsrecon)
