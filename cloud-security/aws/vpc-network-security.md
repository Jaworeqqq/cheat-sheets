---
title: "AWS VPC network security"
category: "cloud-security"
tags: ["aws", "vpc", "network", "segmentation"]
platform: "aws"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# AWS VPC network security

## TL;DR
The VPC is your cloud network perimeter and segmentation boundary. Key controls: security groups (stateful, instance-level), NACLs (stateless, subnet-level), route tables, and endpoints. Design for least exposure and defense-in-depth.

## Core controls
```text
Security Group (SG)  – stateful, allow-only, attached to ENIs/instances. Primary control.
Network ACL (NACL)   – stateless, allow+deny, subnet-level. Coarse guardrail (e.g. block IP ranges).
Route tables         – control reachability (public vs private subnets, egress paths).
IGW / NAT GW         – internet ingress / egress; private subnets egress via NAT.
VPC Endpoints        – reach AWS services (S3, etc.) without traversing the internet.
```

## Segmentation pattern
```text
- Public subnet: only load balancers / NAT — never databases.
- Private subnets: app + data tiers; no direct internet.
- Reference SGs by SG-ID (not CIDR) for tier-to-tier rules (web-SG -> app-SG:8080).
- Separate VPCs/accounts per environment; connect via TGW/PrivateLink, not broad peering.
```

## Common misconfigs
```text
- SG allowing 0.0.0.0/0 on 22/3389/3306/etc (management/DB exposed to the internet).
- Databases in public subnets or with public IPs.
- Overly broad VPC peering (full CIDR access between environments).
- No VPC Flow Logs -> no network visibility for IR.
- Missing egress restrictions (data exfil / C2 paths).
```

## Detection (Blue Team)
```text
- VPC Flow Logs -> detect port scans, exfil, connections to unexpected IPs.
- Config rules: SGs open to 0.0.0.0/0 on sensitive ports; public DB instances.
- GuardDuty: recon, unusual traffic, connections to known-bad IPs.
```

## Mitigation / Hardening
- Least-exposure SGs (no 0.0.0.0/0 on management/DB); reference SG-IDs for tiering.
- Private subnets for app/data; access management via SSM Session Manager / bastion, not open SSH.
- VPC endpoints for AWS services; restrict egress; enable Flow Logs everywhere.
- Segment by account/VPC; PrivateLink over broad peering. See [cloudtrail-detection](./cloudtrail-detection.md).

## Sources
- [AWS VPC security best practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
