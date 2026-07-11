---
title: "Subdomain enumeration"
category: "red-team"
tags: ["recon", "osint", "subdomains"]
platform: "web"
mitre: ["T1595", "T1590"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Subdomain enumeration

## TL;DR
Map a domain's attack surface: passively (without touching the target) → actively (bruteforce/permutations) → verify live hosts.

## Commands
```bash
# Passive – from public sources (CT logs, APIs)
subfinder -d example.com -all -silent -o subs.txt
amass enum -passive -d example.com -o amass.txt

# Certificate Transparency
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sort -u

# Active – DNS bruteforce
puredns bruteforce wordlist.txt example.com -r resolvers.txt

# Permutations of existing subdomains
gotator -sub subs.txt -perm words.txt | puredns resolve -r resolvers.txt

# Verify live + title/status
cat subs.txt | httpx -silent -title -status-code -tech-detect
```

## Detection (Blue Team)
- Monitor **your own CT logs** (crt.sh, Cert Spotter) — new certs = new subdomains to inventory.
- DNS log anomalies: bursts of NXDOMAIN from one resolver = bruteforce.

## Mitigation / Hardening
- Wildcard DNS with care (frustrates bruteforce but masks real state).
- Regular asset inventory (ASM), remove dead records (dangling → subdomain takeover).

## Notes / Pitfalls
- Check for **subdomain takeover**: `nuclei -t takeovers/` on CNAMEs pointing to non-existent services (S3, Azure, GitHub Pages).

## Sources
- [OWASP Amass](https://github.com/owasp-amass/amass)
- [ProjectDiscovery](https://docs.projectdiscovery.io/)
