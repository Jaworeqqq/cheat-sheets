---
title: "Exposed & vulnerable services"
category: "red-team"
tags: ["initial-access", "recon", "exploitation"]
platform: "agnostic"
mitre: ["T1190", "T1133", "T1078"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Exposed & vulnerable services

## TL;DR
The most common real-world entry point: a service exposed to the internet (or an untrusted segment) that has default credentials, no auth, or a known CVE. Triage what's listening, then pick the cheapest path in.

## Triage exposure
```bash
# Port/service discovery (see recon/nmap.md, recon/nmap-nse.md)
nmap -p- -sV --min-rate 2000 target
nmap -sV -sC -p <open> target
# Internet-wide view (passive)
shodan host <ip>
# Web panels / tech
httpx -u target -title -status-code -tech-detect
```

## Common exposed-service wins
```text
RDP (3389)      – brute/spray, BlueKeep (CVE-2019-0708), no-NLA; -> lateral-movement
SMB (445)       – null sessions, EternalBlue (MS17-010); see recon/smb-enum.md
Admin panels    – Tomcat /manager, Jenkins, Jupyter, phpMyAdmin, GitLab (default/weak creds)
VPN / edge dev  – Citrix, Fortinet, Ivanti, Exchange -> frequent critical CVEs
Databases       – see below (often no auth)
CI/CD & registries – Jenkins RCE, exposed Docker API (2375), Kubelet (10250)
```

## Exposed databases (frequently unauthenticated)
```bash
redis-cli -h target ping                 # Redis: no auth -> RCE via module/webshell/SSH key
mongo --host target --eval 'db.adminCommand("listDatabases")'   # Mongo: open by default (older)
curl http://target:9200/_cat/indices     # Elasticsearch: data exposure
# Also: Memcached (11211), CouchDB (5984), Kibana, RethinkDB
```

## Known-CVE workflow
```bash
searchsploit <product> <version>
nmap --script vuln -p <port> target       # intrusive – authorization required
nuclei -u https://target -t cves/ -t default-logins/ -t exposures/
```

## Detection (Blue Team)
- External scanning + first-time inbound to management ports; exploit signatures (IDS/WAF).
- Default-credential logins, anonymous DB access, spikes from edge appliances.

## Mitigation / Hardening
- **Reduce exposure**: management/DBs behind VPN, default-deny firewall, no internet-facing admin.
- Change/disable default credentials, enforce MFA, patch edge/appliances fast (they're prime targets).
- External attack surface management (ASM) to find exposures before attackers do — see [cloud-security/multi-cloud/cspm](../../cloud-security/multi-cloud/cspm.md).

## Sources
- [Shodan](https://www.shodan.io/) · [HackTricks – Pentesting services](https://book.hacktricks.xyz/) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
