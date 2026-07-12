---
title: "Service mesh security"
category: "devsecops"
tags: ["kubernetes", "service-mesh", "mtls", "zero-trust"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Service mesh security

## TL;DR
A service mesh (Istio, Linkerd, Cilium) adds a layer for service-to-service communication, giving you automatic mTLS, identity-based authorization, and observability — the building blocks of Zero Trust networking inside the cluster. It complements (not replaces) NetworkPolicies.

## What it provides for security
```text
mTLS (automatic)     – encrypt + mutually authenticate all service-to-service traffic.
Workload identity    – SPIFFE-style identities per service (not IP-based) for authz.
Authorization policy – "service A may call service B on /path with method X".
Observability        – traffic telemetry for anomaly detection and audit.
```

## mTLS
```text
- Sidecar proxies (Envoy) transparently encrypt traffic between pods.
- Enforce STRICT mode (reject plaintext) once rolled out — start PERMISSIVE to migrate.
- Certificates auto-rotated by the mesh CA (short-lived).
```
```yaml
# Istio: enforce strict mTLS in a namespace
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata: { name: default, namespace: app }
spec:
  mtls: { mode: STRICT }
```

## Authorization policy (identity-based)
```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata: { name: allow-web-to-api, namespace: app }
spec:
  selector: { matchLabels: { app: api } }
  action: ALLOW
  rules:
    - from: [{ source: { principals: ["cluster.local/ns/app/sa/web"] } }]
      to: [{ operation: { methods: ["GET"], paths: ["/v1/*"] } }]
```

## Mesh vs NetworkPolicy
```text
NetworkPolicy – L3/L4 (IP/port), enforced by the CNI. Coarse, no encryption/identity.
Service mesh  – L7 (HTTP methods/paths), identity-based, mTLS. Fine-grained + encrypted.
Use both: NetworkPolicy as the network floor, mesh for identity/L7/mTLS. Cilium can do both.
```

## Security considerations
```text
- The mesh control plane + CA are Tier-0 (compromise = impersonate any service). Protect them.
- Sidecars expand attack surface; keep proxies patched.
- Don't let mesh mTLS lull you — still enforce app-level authz and Pod Security.
```

## Detection (Blue Team)
- Mesh telemetry: unexpected service-to-service calls, denied authz, plaintext attempts (mTLS violations).

## Sources
- [Istio security](https://istio.io/latest/docs/concepts/security/) · [Linkerd](https://linkerd.io/) · related: [network-policies](./network-policies.md), [network-segmentation](../../networking/network-segmentation.md)
