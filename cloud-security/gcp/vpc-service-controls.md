---
title: "GCP VPC Service Controls"
category: "cloud-security"
tags: ["gcp", "vpc-service-controls", "data-exfiltration"]
platform: "gcp"
mitre: ["T1530"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# GCP VPC Service Controls (VPC-SC)

## TL;DR
VPC Service Controls create a "service perimeter" around GCP resources (GCS, BigQuery, etc.) so that even a valid, authorized identity cannot move data outside the perimeter. It's an anti-exfiltration control that complements IAM — IAM says *who can*, VPC-SC says *from where / to where*.

## The problem it solves
```text
IAM alone: a leaked/over-privileged credential can read a bucket from anywhere on the internet.
VPC-SC: wraps the project/resources in a perimeter — API calls to protected services are
        only honored from inside the perimeter (defined VPCs/IPs/identities). Stolen creds
        used from outside are denied, even if IAM would allow them.
```

## Core concepts
```text
Service perimeter – boundary around projects + restricted services (storage, bigquery, ...).
Access levels     – conditions to enter (source IP/CIDR, device, identity) via Access Context Manager.
Ingress/Egress rules – fine-grained allowed flows across the perimeter boundary.
Dry-run mode      – log violations without enforcing (test before enforcing).
```

## Typical setup
```text
1. Define which services to protect (e.g. storage.googleapis.com, bigquery.googleapis.com).
2. Create a perimeter around the project(s).
3. Define access levels (corp IP ranges, trusted identities).
4. Add ingress/egress rules for legitimate cross-perimeter flows (partners, CI).
5. Run in dry-run, review violation logs, then enforce.
```

## What it stops
```text
- Data exfil via stolen service account keys used from the internet.
- SSRF-to-metadata -> token -> reading a bucket from outside the perimeter.
- Accidental public/cross-project data movement.
```

## Detection (Blue Team)
- VPC-SC violation logs (dry-run and enforced) — attempts to access protected services from outside.
- Correlate denied access with identity/source for exfil attempts.

## Mitigation / Hardening
- Enforce VPC-SC on sensitive data services; combine with least-privilege IAM and org policies.
- Use dry-run first to avoid breaking legitimate flows; tightly scope ingress/egress rules.
- Related: [gcp-iam-basics](./gcp-iam-basics.md), [gcs-misconfig](./gcs-misconfig.md).

## Sources
- [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview) · [Access Context Manager](https://cloud.google.com/access-context-manager/docs)
