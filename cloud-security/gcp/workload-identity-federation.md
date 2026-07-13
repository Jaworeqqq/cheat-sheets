---
title: "GCP Workload Identity Federation"
category: "cloud-security"
tags: ["gcp", "workload-identity", "oidc", "keyless"]
platform: "gcp"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# GCP Workload Identity Federation (WIF)

## TL;DR
WIF lets external workloads (GitHub Actions, AWS, on-prem, other clouds) authenticate to GCP using their own identity tokens (OIDC/SAML) to get short-lived GCP credentials — **without service account keys**. Killing long-lived SA keys removes one of the biggest cloud credential-leak risks.

## The problem it solves
```text
Service account KEYS are long-lived static secrets:
 - Leak in a repo/CI/config = persistent access until manually revoked.
 - Frequently over-privileged and rarely rotated.
WIF replaces them: external identity -> short-lived GCP token, no key to leak.
```

## How it works
```text
1. Create a Workload Identity Pool + Provider (trusts an external OIDC/SAML issuer).
2. Map external claims (e.g. GitHub repo/branch) to conditions.
3. External workload presents its OIDC token -> STS exchanges it for a short-lived GCP token
   (optionally impersonating a service account with the needed roles).
4. No SA key anywhere; access is time-bound and attributable.
```

## GitHub Actions example (concept)
```yaml
# The runner's OIDC token is exchanged for GCP creds via WIF
- uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: projects/123/locations/global/workloadIdentityPools/gh/providers/gh-oidc
    service_account: ci@project.iam.gserviceaccount.com
```

## Security best practices
```text
- Scope the provider tightly: attribute conditions (specific repo + branch/tag/environment),
  not "any token from GitHub" — otherwise ANY repo could impersonate you.
- Least-privilege on the impersonated service account.
- Prefer WIF (or attached service accounts on GCP compute) over SA keys everywhere.
- If SA keys are unavoidable: org policy to restrict key creation; short rotation; monitor.
```

## Detection (Blue Team)
- Audit logs: token exchanges (GenerateAccessToken via WIF), provider config changes.
- Alert on new/loosely-scoped providers; any remaining SA key creation/usage.

## Sources
- [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation) · related: [gcp-iam-basics](./gcp-iam-basics.md), [dynamic-secrets](../../devsecops/secrets-management/dynamic-secrets.md)
