---
title: "Kubernetes Security"
category: "devsecops"
tags: ["kubernetes", "k8s", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Kubernetes Security

## TL;DR
Warstwy: RBAC (kto może co), Pod Security (jak działają pody), NetworkPolicy (ruch), admission control (co wpuścić), secrets. Domyślne klastry są zbyt liberalne.

## Audyt klastra
```bash
kube-bench run              # CIS Benchmark
kubectl-who-can create pods --all-namespaces   # kto ma groźne uprawnienia
kubescape scan             # postura + NSA/CISA hardening
```

## RBAC – least privilege
```yaml
kind: Role
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get","list"]        # NIE "*" i NIE cluster-admin dla appek
```
```bash
# Groźne uprawnienia do wychwycenia:
# create pods (+ hostPath/privileged), secrets get/list, exec, impersonate,
# bind/escalate na rolach, nodes/proxy
```

## Pod Security Standards
```yaml
# Namespace label -> enforce baseline/restricted
metadata:
  labels:
    pod-security.kubernetes.io/enforce: restricted
```
```yaml
# securityContext podu
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
  policyTypes: [Ingress, Egress]   # nic bez jawnego allow
```

## Admission control
- OPA/Gatekeeper lub Kyverno: blokuj `privileged`, `hostPath`, `:latest`, wymuszaj skan/podpis obrazu.

## Wykrywanie (Blue Team)
- Falco (spawn shell w podzie, `kubectl exec`, mount wrażliwych ścieżek).
- Audit log API servera: anomalne `create pods`, dostęp do secrets, impersonate.

## Źródła
- [kube-bench](https://github.com/aquasecurity/kube-bench) · [NSA/CISA k8s Hardening](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF) · [Kyverno](https://kyverno.io/)
