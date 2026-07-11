---
title: "Google GKE security"
category: "cloud-security"
tags: ["gcp", "gke", "kubernetes", "hardening"]
platform: "gcp"
mitre: ["T1078.004", "T1552.005"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Google GKE security

## TL;DR
Like EKS, GKE security bridges GCP IAM and Kubernetes RBAC. The critical control is **Workload Identity** — bind K8s ServiceAccounts to GCP service accounts so pods get scoped, short-lived credentials instead of inheriting the node's service account. Autopilot enforces many hardening defaults for you.

## Pod → GCP credentials
```text
Node service account   – default: pods reach metadata -> node SA token (over-privileged!)
Workload Identity      – KSA -> GSA mapping; pods get scoped, short-lived tokens (preferred)
```
```bash
# Enable Workload Identity on the cluster, then bind KSA <-> GSA
gcloud container clusters update c1 --workload-pool=PROJECT.svc.id.goog
gcloud iam service-accounts add-iam-policy-binding GSA@PROJECT.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:PROJECT.svc.id.goog[NS/KSA]"
kubectl annotate sa KSA iam.gke.io/gcp-service-account=GSA@PROJECT.iam.gserviceaccount.com
```

## Autopilot vs Standard
```text
Autopilot – Google manages/hardens nodes: no SSH/node access, Shielded + Workload Identity
            on by default, restricted privileged pods, hostPath limits. Less to misconfigure.
Standard  – you manage node pools; you must enable the hardening controls yourself.
```

## Node & cluster hardening
```text
- Shielded GKE nodes (secure boot, integrity monitoring), Confidential Nodes (encrypted RAM)
- Private cluster (no public node IPs), authorized networks for the control plane
- Metadata concealment / Workload Identity so pods can't read node SA token
- Least-privilege node service account (NOT default Compute Engine SA / Editor)
```

## Admission & network
```text
Binary Authorization – only deploy signed/attested images (block untrusted images)
Network Policy        – Calico/Dataplane V2; default-deny then allow (network-policies.md)
Pod Security          – enforce restricted standard; disable legacy PSP
```
```bash
# Binary Authorization enforcement
gcloud container clusters update c1 --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
```

## Detection (Blue Team)
```text
Security Command Center (SCC): GKE misconfig findings (public cluster, default SA, legacy auth).
Cloud Audit Logs: control-plane API activity, RBAC changes, exec into pods.
GKE audit logging -> Cloud Logging: anomalous verbs, secret access, privileged pods.
```

## Mitigation / Hardening
- Prefer **Autopilot**; on Standard enable Workload Identity, Shielded Nodes, private cluster.
- Never use the default/Editor node SA — scope it minimally.
- Binary Authorization + image signing, restricted Pod Security, default-deny NetworkPolicy.
- Application-layer secrets via Secret Manager + Workload Identity; enable SCC + audit logs.
- See also: [gcp-iam-basics](./gcp-iam-basics.md), [k8s-security](../../devsecops/kubernetes/k8s-security.md).

## Sources
- [GKE hardening guide](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) · [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)
