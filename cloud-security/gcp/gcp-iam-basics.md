---
title: "GCP IAM – podstawy i privesc"
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
GCP: hierarchia Organization → Folder → Project → Resource; role dziedziczą w dół. Privesc często przez service accounts (impersonacja, actAs, tworzenie kluczy).

## Enumeracja
```bash
gcloud auth list
gcloud config list
gcloud projects list
gcloud projects get-iam-policy PROJECT_ID
# Co mogę? (testowanie uprawnień)
gcloud iam list-testable-permissions //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
# Automat
# GCPBucketBrute, ScoutSuite --provider gcp
```

## Typowe wektory privesc
```text
iam.serviceAccounts.getAccessToken / actAs -> impersonuj mocniejsze SA
iam.serviceAccountKeys.create              -> stwórz klucz SA -> długotrwały dostęp
iam.serviceAccounts.implicitDelegation
deploymentmanager / cloudfunctions.create + actAs SA -> uruchom kod jako SA
compute.instances.create + actAs           -> VM z SA -> token z metadata
setIamPolicy na projekcie                   -> nadaj sobie owner
```

```bash
# Impersonacja SA (jeśli masz getAccessToken)
gcloud --impersonate-service-account=admin-sa@proj.iam.gserviceaccount.com <cmd>
# Token z metadata (na VM)
curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
```

## Wykrywanie (Blue Team)
- Cloud Audit Logs: `SetIamPolicy`, `serviceAccountKeys.create`, `GenerateAccessToken`.
- SCC (Security Command Center): nadmiarowe role, klucze SA, publiczne zasoby.

## Mitygacja / Hardening
- Least privilege, zakaz `Owner/Editor` dla appek, org policy: blokada tworzenia kluczy SA.
- Workload Identity zamiast kluczy SA, VPC Service Controls, ograniczenie `actAs`.

## Źródła
- [GCP IAM privesc – Rhino](https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/) · [ScoutSuite](https://github.com/nccgroup/ScoutSuite)
