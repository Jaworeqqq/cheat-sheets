---
title: "Pod Security Standards"
category: "devsecops"
tags: ["kubernetes", "pod-security", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Pod Security Standards (PSS)

## TL;DR
PSS defines three security profiles (Privileged, Baseline, Restricted). The Pod Security Admission (PSA) controller enforces them per namespace via labels. Replaced the deprecated PodSecurityPolicy (removed in 1.25).

## The three profiles
```text
Privileged  – no restrictions (system/infra workloads only).
Baseline    – prevents known privilege escalations; minimal restrictions for common apps.
              (no hostNetwork/hostPID, no privileged, limited hostPath, etc.)
Restricted  – hardened best practice: runAsNonRoot, drop ALL caps, seccomp RuntimeDefault,
              readOnly where possible, no privilege escalation. Use for app workloads.
```

## Enforcement (namespace labels)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: app
  labels:
    # modes: enforce (block), audit (log), warn (user warning)
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
```

## What "Restricted" requires (pod spec)
```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile: { type: RuntimeDefault }
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities: { drop: ["ALL"] }
```

## Rollout strategy
```text
1. Label namespaces with `warn` + `audit` first (observe violations, no blocking).
2. Fix workloads that violate Restricted (or set to Baseline where justified).
3. Switch to `enforce`. Pin `enforce-version` for stability.
4. Exempt system namespaces (kube-system) explicitly, not globally.
```

## PSA vs policy engines
```text
PSA covers the built-in profiles only. For custom rules (registries, labels, resource limits),
use Kyverno/Gatekeeper alongside PSA. See devsecops/kubernetes/k8s-security.md and rbac-deep.md.
```

## Detection (Blue Team)
- PSA audit annotations in the API audit log; alert on `enforce` denials and privileged pods.

## Mitigation / Hardening
- Enforce `restricted` for app namespaces; least-privilege securityContext by default.
- Combine with NetworkPolicies (default-deny) and admission policy for full coverage.

## Sources
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) · [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
