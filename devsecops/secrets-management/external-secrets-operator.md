---
title: "External Secrets Operator (Kubernetes)"
category: "devsecops"
tags: ["secrets-management", "kubernetes", "eso"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# External Secrets Operator (ESO)

## TL;DR
ESO syncs secrets from an external store (Vault, AWS/GCP/Azure secret managers) into native Kubernetes Secrets, so apps consume secrets normally while the source of truth stays in a proper secrets manager. Avoids committing secrets to manifests/git.

## Why (the problem it solves)
```text
- Kubernetes Secrets are only base64-encoded (NOT encrypted) at rest by default.
- Hardcoding secrets in manifests/Helm values -> ends up in git.
- ESO keeps the real secret in Vault/cloud KMS; K8s gets a synced, rotatable copy.
```

## Core objects
```text
SecretStore / ClusterSecretStore – connection to the backend (auth + provider config).
ExternalSecret                   – "pull key X from the store into K8s Secret Y".
PushSecret (optional)            – push a K8s secret up to the store.
```

## Example
```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata: { name: aws-sm, namespace: app }
spec:
  provider:
    aws:
      service: SecretsManager
      region: eu-central-1
      auth:                       # use IRSA/pod identity, not static keys
        jwt: { serviceAccountRef: { name: eso-sa } }
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata: { name: db-creds, namespace: app }
spec:
  refreshInterval: 1h
  secretStoreRef: { name: aws-sm, kind: SecretStore }
  target: { name: db-creds }      # created/updated K8s Secret
  data:
    - secretKey: password
      remoteRef: { key: prod/db, property: password }
```

## Best practices
```text
- Authenticate to the backend with workload identity (IRSA / GKE Workload Identity / K8s auth
  for Vault) — NOT static credentials. See devsecops/secrets-management/vault-patterns.md.
- Enable K8s Secret encryption at rest (KMS provider) even with ESO.
- Least-privilege on the store (read only the paths needed); scope per namespace.
- Set sensible refreshInterval for rotation; monitor sync failures.
```

## Detection (Blue Team)
- Backend audit logs (Vault/cloud) for anomalous secret reads by the ESO identity.
- Alert on ESO sync errors and unexpected new ExternalSecrets.

## Sources
- [External Secrets Operator](https://external-secrets.io/) · related: [vault-patterns](./vault-patterns.md), [secrets-detection](./secrets-detection.md)
