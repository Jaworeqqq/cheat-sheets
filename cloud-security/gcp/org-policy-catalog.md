---
title: "GCP Organization Policy catalog"
category: "cloud-security"
tags: ["gcp", "org-policy", "guardrails", "governance"]
platform: "gcp"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# GCP Organization Policy catalog

## TL;DR
Organization Policy Service enforces constraints on how GCP resources can be configured across the org/folder/project hierarchy — preventive guardrails that individual projects can't override. This is a catalog of the highest-value constraints to enforce. (General concept: [multi-cloud/terraform-cloud-guardrails](../multi-cloud/terraform-cloud-guardrails.md).)

## How it works
```text
- Constraints (predefined or custom) set what's allowed/denied for a resource type.
- Policies apply at org / folder / project; inherited down (with merge/override rules).
- Boolean constraints (on/off) or list constraints (allow/deny values).
- Custom constraints (CEL expressions) for org-specific rules.
```

## High-value constraints to enforce
```text
Identity/keys
 - iam.disableServiceAccountKeyCreation = true   (force WIF/attached SAs; kills static keys)
 - iam.allowedPolicyMemberDomains                (restrict to your domain — block external members)
 - iam.disableServiceAccountKeyUpload

Networking
 - compute.vmExternalIpAccess = deny all         (no public IPs on VMs)
 - compute.skipDefaultNetworkCreation
 - compute.restrictVpcPeering / restrictSharedVpc

Storage/data
 - storage.publicAccessPrevention = enforced     (no public buckets)
 - storage.uniformBucketLevelAccess = true        (disable ACLs)

Compute/other
 - compute.requireOsLogin = true                  (SSH via IAM, audited)
 - compute.requireShieldedVm = true
 - gcp.resourceLocations                          (data residency — restrict regions)
 - sql.restrictPublicIp                           (no public Cloud SQL)
```

## Rollout
```text
1. Apply at the ORG level for baseline guardrails; folders for team-specific.
2. Use dry-run mode where available; check for breakage before enforcing.
3. Document exceptions (a folder/project may need a narrower policy) — scoped, justified.
4. Manage as code (Terraform google_org_policy_*) with review.
```

## Guardrails vs detection
```text
Org Policy = PREVENT at config time. SCC/Event Threat Detection = DETECT after the fact.
Use both (see scc-deep, cloud-detection-strategy).
```

## Detection (Blue Team)
- Audit logs: org policy changes; attempts blocked by policy; new/loosened constraints.

## Sources
- [GCP Organization Policy constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) · related: [scc-deep](./scc-deep.md), [workload-identity-federation](./workload-identity-federation.md)
