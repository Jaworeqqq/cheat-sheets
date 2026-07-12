---
title: "Firewall fundamentals"
category: "networking"
tags: ["networking", "firewall", "segmentation"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Firewall fundamentals

## TL;DR
Firewalls enforce network access policy — which traffic is allowed between zones. Types range from simple stateless packet filters to next-gen firewalls doing app/identity inspection. Core principle: default-deny, allow only what's needed, in both directions.

## Types (evolution)
```text
Packet filter (stateless) – allow/deny by IP/port/protocol; no connection state. Fast, coarse.
Stateful firewall         – tracks connections (return traffic auto-allowed). The baseline.
Next-Gen Firewall (NGFW)  – app-aware (L7), identity-aware, IPS, TLS inspection, threat intel.
WAF                       – application-layer, HTTP-specific (SQLi/XSS) — different tool (see appsec).
Host firewall             – on the endpoint (iptables/nftables, Windows Firewall).
Cloud                     – security groups (stateful), NACLs (stateless) — see cloud-security.
```

## Core concepts
```text
Default-deny        – deny everything, explicitly allow required flows (allow-list).
Stateful inspection – track connection state; allow established/related return traffic.
Zones/segmentation  – DMZ, internal, management; control traffic BETWEEN zones.
Ingress vs egress   – filter BOTH; egress filtering blunts C2/exfil (often neglected).
Rule order          – most firewalls evaluate top-down, first match wins.
```

## Egress filtering (commonly missed, high value)
```text
- Restrict outbound to only required destinations/ports.
- Blocks/limits reverse shells, C2 beaconing, and data exfiltration.
- Force outbound through proxies/DNS you control and log.
```

## Example (nftables, default-deny)
```bash
nft add table inet filter
nft add chain inet filter input '{ type filter hook input priority 0; policy drop; }'
nft add rule inet filter input ct state established,related accept
nft add rule inet filter input tcp dport 22 accept
```

## Detection (Blue Team)
- Firewall logs: denied outbound (recon/C2 attempts), port scans, policy violations.
- Feed logs to SIEM; alert on new/unexpected allowed flows and rule changes.

## Mitigation / Hardening
- Default-deny both directions; least-privilege rules; segment zones (management isolated).
- Egress filtering + logging; regular rule review (remove stale/any-any rules).
- Related: [network-segmentation](./network-segmentation.md), [common-protocols](./common-protocols.md), [aws/vpc-network-security](../cloud-security/aws/vpc-network-security.md).

## Sources
- [NIST SP 800-41 (firewalls)](https://csrc.nist.gov/pubs/sp/800/41/r1/final)
