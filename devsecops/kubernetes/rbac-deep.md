---
title: "Kubernetes RBAC – deep dive"
category: "devsecops"
tags: ["kubernetes", "rbac", "authorization", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Kubernetes RBAC – deep dive

## TL;DR
RBAC decides who can do what on which resources. Four objects: Role/ClusterRole (permissions) + RoleBinding/ClusterRoleBinding (grant to subjects). The danger isn't obvious `admin` grants — it's subtle verbs (escalate, bind, impersonate) and resources (secrets, pods/exec) that enable full-cluster takeover.

## Object model
```text
Role            – namespaced permissions (verbs on resources)
ClusterRole     – cluster-wide permissions (or reusable in namespaces)
RoleBinding     – grants a Role/ClusterRole within a namespace to subjects
ClusterRoleBinding – grants a ClusterRole cluster-wide (powerful — audit these)
Subjects        – User, Group, ServiceAccount
```

## Rule anatomy
```yaml
kind: Role
metadata: { namespace: app, name: pod-reader }
rules:
  - apiGroups: [""]           # "" = core group
    resources: ["pods"]
    verbs: ["get","list","watch"]   # least privilege — NOT ["*"]
```

## Dangerous permissions (privesc paths)
```text
escalate (on roles)  – grant yourself MORE than you have -> bypass least privilege
bind (on roles)      – bind an existing powerful role to yourself
impersonate          – act as another user/group/SA (become cluster-admin)
create pods          – schedule a pod with hostPath/privileged -> node/secret access
secrets get/list     – read every secret in scope (creds, tokens, TLS keys)
pods/exec, pods/attach – shell into running pods
create serviceaccounts/tokens – mint tokens for privileged SAs
nodes/proxy, */* wildcards, csr approval, mutatingwebhookconfigurations
```

## Auditing who-can-do-what
```bash
# Who can perform a dangerous action?
kubectl who-can create pods --all-namespaces
kubectl who-can get secrets -n kube-system
kubectl who-can impersonate users

# Analyze/visualize RBAC
rbac-tool analysis            # flags risky rules
rbac-tool who-can escalate roles
kubectl auth can-i --list --as system:serviceaccount:app:default

# Find wildcards / cluster-admin bindings
kubectl get clusterrolebindings -o json | jq '.items[] | select(.roleRef.name=="cluster-admin")'
```

## ServiceAccount tokens
```text
- Every pod gets its SA token mounted by default -> a compromised pod inherits its RBAC.
- Set automountServiceAccountToken: false unless the pod needs the API.
- Prefer short-lived bound tokens (TokenRequest API) over legacy non-expiring secrets.
- A default SA with broad RBAC = a cluster-wide risk.
```

## Least-privilege patterns
```text
- One SA per workload, scoped Role in its own namespace (no ClusterRole unless required).
- Avoid ClusterRoleBindings; never grant cluster-admin to apps/CI.
- No wildcards in verbs/resources; enumerate exactly what's needed.
- Separate human (OIDC groups) from workload (SA) identities.
- Review bindings in CI (policy-as-code) — see [iac/opa-conftest](../iac/opa-conftest.md).
```

## Detection (Blue Team)
- API server audit log: use of impersonate/escalate/bind, secret enumeration, exec into pods.
- Alert on new ClusterRoleBindings and changes to privileged roles.

## Mitigation / Hardening
- Least-privilege SAs, disable token automount, short-lived tokens, no wildcards.
- Audit with `kubectl who-can`/`rbac-tool`; enforce via admission ([k8s-security](./k8s-security.md)).

## Sources
- [K8s RBAC docs](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) · [rbac-tool](https://github.com/alcideio/rbac-tool) · [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can)
