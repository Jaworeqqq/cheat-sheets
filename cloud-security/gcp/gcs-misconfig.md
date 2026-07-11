---
title: "GCP Cloud Storage (GCS) misconfig"
category: "cloud-security"
tags: ["gcp", "gcs", "storage"]
platform: "gcp"
mitre: ["T1530"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# GCP Cloud Storage (GCS) misconfigurations

## TL;DR
Public or over-permissive buckets leak data. Key risks: `allUsers`/`allAuthenticatedUsers` IAM bindings, legacy ACLs, and broad roles. Enumerate access, check IAM/ACL, verify uniform bucket-level access and encryption.

## Enumeration / access test
```bash
# List/anon access
gsutil ls gs://bucket-name                    # if you have access
curl -s https://storage.googleapis.com/bucket-name   # public listing?

# IAM policy + ACLs
gsutil iam get gs://bucket-name
gsutil acl get gs://bucket-name
gcloud storage buckets describe gs://bucket-name

# Name discovery / brute
# GCPBucketBrute (also checks privilege escalation via writable buckets)
python3 gcpbucketbrute.py -k company -u
```

## Common issues
```text
- IAM binding for allUsers / allAuthenticatedUsers (public)
- Legacy fine-grained ACLs instead of uniform bucket-level access
- Overly broad roles (roles/storage.admin) to wide groups
- No default encryption with CMEK where required; public via signed URLs (long TTL)
- Writable public bucket -> content/website tampering
```

## Detection (Blue Team)
- SCC (Security Command Center): "Public bucket" / "Public log bucket" findings.
- Cloud Audit Logs: SetIamPolicy adding allUsers; anomalous object access.

## Mitigation / Hardening
- **Uniform bucket-level access** (disable ACLs), no `allUsers`/`allAuthenticatedUsers`.
- Org policy: `storage.publicAccessPrevention = enforced`.
- Least-privilege IAM (roles/storage.objectViewer scoped), CMEK, VPC Service Controls.
- Access logging + monitoring; short-lived, scoped signed URLs.

## Sources
- [GCS security best practices](https://cloud.google.com/storage/docs/best-practices#security) · [Public access prevention](https://cloud.google.com/storage/docs/public-access-prevention)
