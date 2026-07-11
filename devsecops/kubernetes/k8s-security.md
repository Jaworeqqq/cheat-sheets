---
title: "Kubernetes security"
category: "devsecops"
tags: ["kubernetes", "k8s", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Kubernetes security

## TL;DR
Layers: RBAC (who can do what), Pod Security (how pods run), NetworkPolicy (traffic), admission control (what to admit), secrets. Default clusters are too permissive.

## Cluster audit
```bash
kube-bench run              # CIS Benchmark
kubectl-who-can create pods --all-namespaces   # who has dangerous permissions
kubescape scan             # posture + NSA/CISA hardening
```

## RBAC – least privilege
```yaml
kind: Role
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get","list"]        # NOT "*" and NOT cluster-admin for apps
```
```bash
# Dangerous permissions to catch:
# create pods (+ hostPath/privileged), secrets get/list, exec, impersonate,
# bind/escalate on roles, nodes/proxy
```

## Pod Security Standards
```yaml
# Namespace label -> enforce baseline/restricted
metadata:
  labels:
    pod-security.kubernetes.io/enforce: restricted
```
```yaml
# pod securityContext
securityContext:
  runAsNonRoot: true
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities: { drop: ["ALL"] }
  seccompProfile: { type: RuntimeDefault }
```

## NetworkPolicy (default-deny)
```yaml
kind: NetworkPolicy
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]   # nothing without an explicit allow
```

## Admission control
- OPA/Gatekeeper or Kyverno: block `privileged`, `hostPath`, `:latest`, enforce image scanning/signing.

## Detection (Blue Team)
- Falco (spawning a shell in a pod, `kubectl exec`, mounting sensitive paths).
- API server audit log: anomalous `create pods`, secrets access, impersonate.

## Sources
- [kube-bench](https://github.com/aquasecurity/kube-bench) · [NSA/CISA k8s Hardening](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF) · [Kyverno](https://kyverno.io/)
