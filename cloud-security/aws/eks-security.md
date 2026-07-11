---
title: "Amazon EKS security"
category: "cloud-security"
tags: ["aws", "eks", "kubernetes", "hardening"]
platform: "aws"
mitre: ["T1078.004", "T1552.005"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Amazon EKS security

## TL;DR
EKS security sits at the intersection of AWS IAM and Kubernetes RBAC. The two biggest levers: how pods get AWS credentials (IRSA / Pod Identity vs the node role) and how AWS identities map to K8s RBAC (access entries / aws-auth). Misconfigure either and a pod becomes an account-wide foothold.

## Pod → AWS credentials
```text
Node instance role   – ALL pods inherit it via IMDS (worst; over-privileged blast radius)
IRSA                 – ServiceAccount -> OIDC -> scoped IAM role (per-workload least privilege)
EKS Pod Identity     – newer, association-based, no OIDC trust juggling (preferred going forward)
```
```bash
# IRSA: annotate the ServiceAccount with the role ARN
kubectl annotate sa app-sa eks.amazonaws.com/role-arn=arn:aws:iam::123:role/app-role
# Pod Identity association
aws eks create-pod-identity-association --cluster-name c1 \
  --namespace app --service-account app-sa --role-arn arn:aws:iam::123:role/app-role
```

## AWS identity → Kubernetes RBAC
```text
Access entries (current)  – native API mapping IAM principal -> K8s groups/access policies
aws-auth ConfigMap (legacy) – maps IAM roles/users to K8s users/groups
Risk: overly broad mappings (system:masters) = cluster-admin to an IAM principal.
```
```bash
aws eks create-access-entry --cluster-name c1 --principal-arn arn:aws:iam::123:role/dev
aws eks associate-access-policy --cluster-name c1 --principal-arn ... \
  --access-scope type=namespace,namespaces=dev \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSEditPolicy
```

## Common misconfigurations
```text
- Pods reach IMDS -> steal the node role creds (block with hop limit / IMDSv2 / network policy)
- Public API server endpoint with wide CIDR (should be private or restricted)
- system:masters granted to broad IAM roles via aws-auth
- Secrets stored unencrypted in etcd (enable KMS envelope encryption)
- No NetworkPolicy (flat pod network) — see devsecops/kubernetes/network-policies.md
- Node role with excessive IAM (ECR + SSM + more than needed)
```

## Detection (Blue Team)
```text
CloudTrail: EKS API calls (CreateAccessEntry, UpdateClusterConfig), AssumeRoleWithWebIdentity
            from unexpected service accounts, aws-auth ConfigMap edits.
GuardDuty (EKS Protection): audit-log anomalies — exec into pods, privileged pods,
            anonymous access, sensitive mounts.
K8s audit log -> CloudWatch: verb/user anomalies, secret access, RBAC changes.
```

## Mitigation / Hardening
- Least-privilege pod credentials via **IRSA or Pod Identity**; never rely on the node role.
- Restrict/private API endpoint; scope access entries by namespace (no blanket system:masters).
- Enable **KMS envelope encryption** for secrets; block pod access to IMDS (hop limit=1, IMDSv2).
- Enforce Pod Security (restricted), NetworkPolicies, GuardDuty EKS, and ship audit logs.
- See also: [k8s-security](../../devsecops/kubernetes/k8s-security.md), [iam-privesc](./iam-privesc.md).

## Sources
- [EKS Best Practices Guide](https://aws.github.io/aws-eks-best-practices/security/docs/) · [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
