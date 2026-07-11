---
title: "CIEM – cloud entitlement management"
category: "cloud-security"
tags: ["multi-cloud", "ciem", "iam", "least-privilege"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# CIEM – Cloud Infrastructure Entitlement Management

## TL;DR
CIEM focuses on the identity/permissions layer of cloud security: discovering who (users, roles, service accounts, workloads) can do what, finding excessive and unused entitlements, and right-sizing them toward least privilege. It's the "identity" pillar of a CNAPP (alongside CSPM for config and CWPP for workloads — see [cspm](./cspm.md)).

## The problem it solves
```text
- Cloud IAM is vast and additive: permissions accumulate, rarely get removed.
- Effective permissions are hard to compute (roles + policies + groups + resource
  policies + SCPs/boundaries + inheritance).
- Excessive/unused permissions = a huge blast radius when an identity is compromised.
- Non-human identities (roles, service accounts, workload identities) now outnumber humans.
```

## What CIEM analyzes
```text
- Effective (net) permissions per identity across accounts/projects/subscriptions
- Unused permissions/roles (granted but never used in N days)
- Privilege-escalation paths (e.g. iam:PassRole chains, actAs, role assumption)
- Cross-account/cross-project trust and external access
- Toxic combinations (e.g. write to IAM + read secrets)
```

## Right-sizing workflow
```text
1. Inventory all identities (human + workload) and their effective permissions.
2. Compare granted vs used (access analyzers / usage logs) over a window.
3. Generate least-privilege policies from actual usage.
4. Remove unused permissions; replace broad roles with scoped ones.
5. Continuously monitor for drift and new excessive grants.
```

## Tooling
```text
Native   – AWS IAM Access Analyzer (unused access, policy generation),
           GCP Policy Analyzer / Recommender, Azure Entra Permissions Management.
Open/3P  – CloudQuery + custom queries, PMapper (AWS privesc paths), Cloudsplaining,
           commercial CNAPP suites bundle CIEM.
```
```bash
# AWS: find unused access and generate least-privilege policy
aws accessanalyzer create-analyzer --type ACCOUNT_UNUSED_ACCESS --analyzer-name unused
# PMapper: visualize privilege-escalation paths
pmapper graph create ; pmapper query "preset privesc *"
```

## Detection (Blue Team)
- Alert on new excessive grants (wildcard actions, admin roles), unused-but-privileged identities.
- Monitor privilege-escalation-enabling permissions (PassRole/actAs/setIamPolicy) assignments.

## Mitigation / Hardening
- Least privilege by default; scope roles per workload (IRSA / Workload Identity / Managed Identity).
- Enforce permission boundaries / SCPs / org policies as guardrails.
- Periodic access reviews; automatically flag and remove unused entitlements.
- Separate human vs workload identities; prefer short-lived credentials over static keys.

## Sources
- [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) · [GCP Recommender](https://cloud.google.com/iam/docs/recommender-overview) · [PMapper](https://github.com/nccgroup/PMapper)
