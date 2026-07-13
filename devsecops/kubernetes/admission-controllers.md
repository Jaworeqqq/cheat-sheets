---
title: "Kubernetes admission controllers"
category: "devsecops"
tags: ["kubernetes", "admission-control", "policy", "kyverno"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# Kubernetes admission controllers

## TL;DR
Admission controllers intercept requests to the Kubernetes API after authn/authz but before persistence — the enforcement point for "what may run in the cluster". They can validate (allow/deny) or mutate (modify) objects. Policy engines (Kyverno, OPA/Gatekeeper) let you write custom admission rules as code.

## Where they sit
```text
API request -> Authentication -> Authorization -> Admission (mutating -> validating) -> etcd.
Mutating admission: modify objects (inject sidecars, defaults, labels).
Validating admission: allow/deny based on policy (the security gate).
```

## Built-in vs policy engines
```text
Built-in       – PodSecurity (PSS enforcement), ResourceQuota, etc. (see pod-security-standards).
Kyverno        – policies as YAML (no new language); validate/mutate/generate; popular + simple.
OPA/Gatekeeper – Rego-based ConstraintTemplates + Constraints; powerful, steeper curve.
Validating/Mutating Webhooks – custom webhook servers for bespoke logic.
```

## What to enforce
```text
- Block privileged / hostPath / hostNetwork / hostPID pods.
- Require runAsNonRoot, drop capabilities, readOnlyRootFilesystem (or enforce PSS restricted).
- Only allow images from approved registries; require signed images + valid provenance (see slsa-levels).
- Disallow :latest tags; require resource limits, required labels, and NetworkPolicies.
- Restrict RBAC-dangerous objects; deny default-namespace workloads.
```

## Kyverno example (deny :latest)
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata: { name: disallow-latest-tag }
spec:
  validationFailureAction: Enforce      # Audit first, then Enforce
  rules:
    - name: require-image-tag
      match: { any: [{ resources: { kinds: [Pod] } }] }
      validate:
        message: "Using ':latest' or no tag is not allowed."
        pattern:
          spec: { containers: [{ image: "!*:latest" }] }
```

## Rollout & pitfalls
```text
- Start in Audit/dry-run; review violations; then Enforce (avoid breaking existing workloads).
- The webhook is in the critical path — HA + failurePolicy tuning (Fail vs Ignore) matters:
  Fail = secure but can block the cluster if the webhook is down; Ignore = available but bypassable.
- Exempt system namespaces explicitly; verify image-signing policies with test workloads.
```

## Detection (Blue Team)
- API audit log: admission denials, policy changes, webhook config changes (bypass attempts).

## Sources
- [K8s Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) · [Kyverno](https://kyverno.io/) · [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) · related: [pod-security-standards](./pod-security-standards.md), [k8s-security](./k8s-security.md)
