---
title: "GCP IAM – basics and privesc"
category: "cloud-security"
tags: ["gcp", "iam", "privesc"]
platform: "gcp"
mitre: ["T1078.004"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# GCP IAM

## TL;DR
GCP: hierarchy Organization → Folder → Project → Resource; roles inherit downward. Privesc often via service accounts (impersonation, actAs, key creation).

## Enumeration
```bash
gcloud auth list
gcloud config list
gcloud projects list
gcloud projects get-iam-policy PROJECT_ID
# What can I do? (permission testing)
gcloud iam list-testable-permissions //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
# Automated
# GCPBucketBrute, ScoutSuite --provider gcp
```

## Common privesc vectors
```text
iam.serviceAccounts.getAccessToken / actAs -> impersonate stronger SAs
iam.serviceAccountKeys.create              -> create an SA key -> long-lived access
iam.serviceAccounts.implicitDelegation
deploymentmanager / cloudfunctions.create + actAs SA -> run code as an SA
compute.instances.create + actAs           -> VM with an SA -> token from metadata
setIamPolicy on the project                 -> grant yourself owner
```

```bash
# SA impersonation (if you have getAccessToken)
gcloud --impersonate-service-account=admin-sa@proj.iam.gserviceaccount.com <cmd>
# Token from metadata (on a VM)
curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
```

## Detection (Blue Team)
- Cloud Audit Logs: `SetIamPolicy`, `serviceAccountKeys.create`, `GenerateAccessToken`.
- SCC (Security Command Center): excessive roles, SA keys, public resources.

## Mitigation / Hardening
- Least privilege, no `Owner/Editor` for apps, org policy: block SA key creation.
- Workload Identity instead of SA keys, VPC Service Controls, restrict `actAs`.

## Sources
- [GCP IAM privesc – Rhino](https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/) · [ScoutSuite](https://github.com/nccgroup/ScoutSuite)
