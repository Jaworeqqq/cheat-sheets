---
title: "Network segmentation"
category: "networking"
tags: ["networking", "segmentation", "zero-trust"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Network segmentation

## TL;DR
Segmentation divides the network into zones with controlled traffic between them, so a compromise in one area can't freely spread. It's the single biggest limiter of lateral movement and blast radius. Micro-segmentation takes it down to the workload level.

## Why it matters
```text
- Flat networks let one compromised host reach everything (lateral movement heaven).
- Segmentation contains breaches, shrinks the CDE (PCI scope), and enforces least privilege.
- Limits blast radius: ransomware/worms can't spread across segment boundaries.
```

## Levels of segmentation
```text
Perimeter/zones   – DMZ, internal, management, guest (classic 3-tier).
VLAN segmentation – separate broadcast domains; enforce with ACLs/firewall between VLANs.
Micro-segmentation – per-workload policy (identity-based), e.g. only web->app:8080, app->db:5432.
Cloud             – VPCs/subnets + security groups; K8s NetworkPolicies (default-deny).
```

## Design principles
```text
- Group by trust level + function (data tier separate from web tier).
- Isolate management planes (jump/bastion only), OT/ICS, IoT, guest, and Tier 0 (AD).
- Default-deny between segments; allow only required flows (least privilege).
- Don't trust "internal" — combine with Zero Trust (authenticate every access).
```

## Key isolation targets
```text
- Tier 0 (domain controllers, PKI, secrets) — admin only from PAWs.
- Databases / crown-jewel data — reachable only from their app tier.
- OT/ICS and IoT — separate from IT, tightly controlled.
- Management interfaces — out-of-band / bastion only.
- Backups — isolated (ransomware can't reach them).
```

## Detection (Blue Team)
- Cross-segment traffic that violates policy (east-west monitoring, NDR).
- First-time host-to-host flows across boundaries; management access from wrong zones.

## Mitigation / Hardening
- Default-deny inter-segment; micro-segment crown jewels; isolate Tier 0 and backups.
- Enforce with firewalls/SGs/NetworkPolicies; monitor east-west, not just north-south.
- Related: [firewall-fundamentals](./firewall-fundamentals.md), [k8s network-policies](../devsecops/kubernetes/network-policies.md), blue-team [lateral-movement-hunt](../blue-team/threat-hunting/lateral-movement-hunt.md).

## Sources
- [NIST SP 800-207 (Zero Trust)](https://csrc.nist.gov/pubs/sp/800/207/final) · [CIS Control 12](https://www.cisecurity.org/controls)
