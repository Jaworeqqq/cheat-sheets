---
title: "Cloud guardrails (SCP / Azure Policy / Org Policy)"
category: "cloud-security"
tags: ["multi-cloud", "guardrails", "governance", "policy"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Cloud guardrails

## TL;DR
Guardrails are preventive controls that stop bad configurations at the platform level — before a resource is even created. Each cloud has one: AWS SCPs, Azure Policy, GCP Organization Policy. They enforce org-wide rules that individual accounts/projects cannot override.

## The three (equivalent concept)
```text
AWS Service Control Policies (SCPs) – org/OU-level permission boundaries (deny even for admins).
Azure Policy                        – audit or DENY resource configs; deployIfNotExists remediation.
GCP Organization Policy             – constraints on resource config across the org/folder/project.
```

## What to enforce (preventive)
```text
- Restrict regions (data residency, blast radius).
- Deny public storage (S3/Blob/GCS public access), require encryption.
- Deny disabling logging (CloudTrail/Activity Log/Audit Logs).
- Require tags/labels (ownership, cost, data classification).
- Restrict which services/instance types can be used.
- Deny creating IAM users / long-lived keys (force SSO/OIDC/roles).
- Enforce private networking, no public IPs on databases.
```

## Examples
```text
AWS SCP (deny disabling CloudTrail):
  Effect: Deny  Action: cloudtrail:StopLogging, cloudtrail:DeleteTrail  Resource: *

Azure Policy (deny public blob):
  policyRule: if storageAccount allowBlobPublicAccess == true -> deny

GCP Org Policy:
  constraints/storage.publicAccessPrevention = enforced
  constraints/compute.vmExternalIpAccess = deny all
```

## Guardrails vs detective controls
```text
Guardrails (SCP/Policy/Org Policy) = PREVENT (block at creation).
CSPM (Defender/Prowler/SCC) = DETECT drift/misconfig after the fact.
Use both: guardrails stop the common mistakes; CSPM catches what slips through.
```

## Best practices
```text
- Start in audit/dry-run, measure impact, then enforce (avoid breaking legitimate workloads).
- Layer at org/OU/folder level so accounts can't opt out.
- Version policies as code (IaC); review changes; least-privilege on who can edit them.
```

## Sources
- [AWS SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) · [Azure Policy](https://learn.microsoft.com/azure/governance/policy/) · [GCP Org Policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview) · related: [cspm](./cspm.md)
