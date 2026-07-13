---
title: "AWS Organizations & SCP patterns"
category: "cloud-security"
tags: ["aws", "organizations", "scp", "guardrails"]
platform: "aws"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# AWS Organizations & SCP patterns

## TL;DR
AWS Organizations lets you manage many accounts centrally; Service Control Policies (SCPs) are org-level guardrails that cap the maximum permissions in member accounts — even root/admins can't exceed them. The multi-account structure itself is a core security control (blast-radius isolation).

## Multi-account structure
```text
- Separate accounts per environment/workload (prod, dev, security, logging, sandbox).
- Organizational Units (OUs) group accounts to apply SCPs by function.
- Central accounts: log-archive (immutable logs), security-tooling (GuardDuty/SecHub admin).
- Isolation limits blast radius: a compromised dev account can't reach prod.
```

## SCPs — how they work
```text
- SCPs set a PERMISSION BOUNDARY on member accounts; effective perms = SCP ∩ IAM.
- They DENY or allow-list actions; they never GRANT (IAM still grants).
- Root user in a member account is also constrained by SCPs.
- Applied at OU or account level; inherited down the tree.
```

## Common SCP guardrails
```text
- Deny disabling CloudTrail/Config/GuardDuty (protect detective controls).
- Restrict regions (deny actions outside approved regions).
- Deny leaving the org, deleting log buckets, or tampering with the security tooling.
- Deny creating IAM users / access keys (force SSO/roles/OIDC).
- Require encryption; deny public S3; restrict root usage.
- Deny modifying specific IAM roles (e.g. the security/audit roles).
```

## Example (deny disabling CloudTrail)
```json
{ "Effect": "Deny",
  "Action": ["cloudtrail:StopLogging","cloudtrail:DeleteTrail"],
  "Resource": "*" }
```

## Best practices
```text
- Start with AWS-provided guardrails (Control Tower) + a few high-value denies.
- Test SCPs in a non-prod OU first (they can break workloads silently).
- Layer: SCP (prevent) + Config/GuardDuty (detect) + IAM least privilege.
- Don't rely on SCPs alone for data-plane access control (they gate API actions).
```

## Detection (Blue Team)
- CloudTrail: SCP/Org changes, attempts blocked by SCP (AccessDenied with org-policy context).

## Sources
- [AWS Organizations SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) · related: [terraform-cloud-guardrails](../multi-cloud/terraform-cloud-guardrails.md), [cloudtrail-detection](./cloudtrail-detection.md)
