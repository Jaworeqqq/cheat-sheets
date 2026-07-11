---
title: "Shodan / Censys dorks"
category: "osint"
tags: ["osint", "recon", "shodan", "censys", "attack-surface"]
platform: "agnostic"
mitre: ["T1596", "T1595"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Shodan / Censys dorks

## TL;DR
Internet-wide scan engines (Shodan, Censys, FOFA, ZoomEye) index exposed services with rich metadata. Passive attack-surface discovery: find your org's exposed hosts, forgotten services, and misconfigurations before an attacker does.

## Shodan filters
```text
org:"Example Corp"            # organization
net:203.0.113.0/24           # CIDR
port:3389                    # open port
product:"MySQL"              # service/product
http.title:"Dashboard"       # page title
http.html:"login"            # body content
ssl.cert.subject.cn:example.com   # certificate CN
hostname:example.com         # hostname
country:PL  city:"Warsaw"    # geo
vuln:CVE-2021-44228          # tagged vulnerable (paid)
```

## Useful combinations
```text
org:"Example Corp" port:3389                 # exposed RDP
org:"Example Corp" "230 login successful"    # anonymous FTP
product:"MongoDB" -authentication            # unauthenticated Mongo
http.title:"index of /"                      # open directory listings
ssl.cert.subject.cn:example.com 200          # your certs across the internet
"default password" org:"Example Corp"
```

## Censys (search syntax)
```text
services.service_name: HTTP and services.port: 8080
services.tls.certificates.leaf_data.subject.common_name: example.com
autonomous_system.name: "Example Corp"
```

## What people find (know your own exposure)
```text
- Exposed databases (Mongo/Elastic/Redis) with no auth
- ICS/SCADA (Modbus/BACnet), printers, webcams, IPMI/BMC
- Forgotten dev/staging panels, admin interfaces, VPN/RDP
- Expired/misissued certs, default-credential devices
```

## Tooling
```bash
shodan search 'org:"Example Corp" port:3389'
shodan host 203.0.113.10
# CLI for scoped monitoring / alerts (Shodan Monitor)
```

## Defensive monitoring (Blue Team)
- Run these queries against **your own** org/ASN/CIDR regularly (attack-surface management).
- Set Shodan Monitor / Censys alerts for new exposed ports/services on your ranges.
- Feed findings into asset inventory; close or authenticate anything unexpected.

## Sources
- [Shodan search filters](https://www.shodan.io/search/filters) · [Censys](https://search.censys.io/) · related: [recon-frameworks](./recon-frameworks.md)
