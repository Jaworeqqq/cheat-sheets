---
title: "Corporate OSINT"
category: "osint"
tags: ["osint", "corporate", "recon"]
platform: "agnostic"
mitre: ["T1591"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Corporate OSINT

## TL;DR
Profiling an organization from open sources: legal structure, subsidiaries, domains/IP ranges, technologies, suppliers, and financials. Maps the true attack surface (including forgotten assets and acquisitions) for scoping and social engineering.

## What to gather
```text
Structure   – legal entities, subsidiaries, acquisitions (each may hold in-scope assets/domains).
Domains/IP  – all domains, ASNs, IP ranges, cloud footprint (attack surface).
People      – employees, org chart, email format (-> phishing/spray; see people-osint).
Tech stack  – from job posts, BuiltWith/Wappalyzer, GitHub, error pages.
Suppliers   – vendors/partners (supply-chain + pretext material).
Financials  – filings, funding, news (context, timing, pretexts).
```

## Sources & tools
```text
Legal/registry – OpenCorporates, national company registries, SEC EDGAR (US filings).
Domains/ASN    – whois, amass, ASN lookups (bgp.he.net), crt.sh, DNS recon.
Tech           – BuiltWith, Wappalyzer, Shodan (org: filter), job postings.
Relationships  – Maltego, SpiderFoot (graph entities), LinkedIn (org + employees).
Brand/leaks    – GitHub org repos, paste sites, breach data (see breach-data).
```

## Attack-surface mapping workflow
```text
1. Seed: primary domain + company name.
2. Expand: subsidiaries/acquisitions -> their domains -> subdomains -> live hosts.
3. Map IP ranges/ASNs and cloud accounts; find forgotten/legacy assets.
4. Enumerate tech + exposed services (Shodan/httpx); note takeover-prone assets.
5. Correlate people + email format for the human layer.
```

## Detection / defense (Blue Team)
- Attack Surface Management (ASM): continuously discover your own external footprint before attackers do.
- Monitor for shadow IT, forgotten domains (dangling DNS -> takeover), and newly acquired assets.

## Mitigation / Hardening
- Maintain an accurate asset inventory across subsidiaries/acquisitions (CIS Control 1).
- Decommission dead assets/DNS; monitor brand + leaks; minimize public tech disclosure.
- Related: [recon-frameworks](./recon-frameworks.md), [people-osint](./people-osint.md), [subdomain-enum](../red-team/recon/subdomain-enum.md).

## Sources
- [OpenCorporates](https://opencorporates.com/) · [SpiderFoot](https://github.com/smicallef/spiderfoot)
