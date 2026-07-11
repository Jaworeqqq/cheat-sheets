---
title: "Kubernetes NetworkPolicies"
category: "devsecops"
tags: ["kubernetes", "networkpolicy", "segmentation"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Kubernetes NetworkPolicies

## TL;DR
By default, all pods can talk to all pods (flat network). NetworkPolicies add micro-segmentation: deny by default, then explicitly allow. Requires a CNI that enforces them (Calico, Cilium; not plain flannel).

## Default-deny (start here)
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: app
spec:
  podSelector: {}                 # all pods in the namespace
  policyTypes: [Ingress, Egress]  # nothing allowed until you add allows
```

## Allow specific traffic
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web-to-api
  namespace: app
spec:
  podSelector:
    matchLabels: { app: api }
  policyTypes: [Ingress]
  ingress:
    - from:
        - podSelector:
            matchLabels: { app: web }
      ports:
        - protocol: TCP
          port: 8080
```

## Common patterns
```text
- Allow DNS egress (kube-dns) — otherwise everything breaks:
    egress to kube-system on UDP/TCP 53
- Namespace isolation: allow only from same namespace (namespaceSelector)
- Restrict egress to the internet (allow only required external CIDRs)
- Deny pod -> cloud metadata (169.254.169.254) to blunt SSRF -> IMDS
```

## Testing / verification
```bash
# Confirm the CNI enforces policies (test connectivity)
kubectl exec -n app web -- curl -m3 http://api:8080   # allowed?
kubectl exec -n app web -- curl -m3 http://db:5432    # should be denied
# Calico/Cilium provide policy visualization & flow logs (Hubble)
```

## Best practices
- Default-deny per namespace, then least-privilege allows; always allow DNS.
- Label pods consistently (policies key off labels); block egress to metadata.
- For richer policy (L7, FQDN, identity): Cilium NetworkPolicy / Calico GlobalNetworkPolicy.

## Sources
- [K8s – Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) · [Cilium](https://cilium.io/) · [Calico](https://docs.tigera.io/)
