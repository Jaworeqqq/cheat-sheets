---
title: "CI/CD environment protection"
category: "devsecops"
tags: ["ci-cd", "deployment", "governance"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# CI/CD environment protection

## TL;DR
Environments (staging, production) are trust boundaries with their own secrets and deploy access. Protect them with required reviewers, restricted branches, scoped secrets, and wait timers — so a compromised PR or developer can't ship straight to prod.

## Core controls
```text
- Required reviewers/approvals before deploying to protected environments (esp. prod).
- Restrict which branches/tags can deploy (e.g. only `main`/release tags -> prod).
- Environment-scoped secrets (prod secrets only available in prod deploy jobs).
- Wait timer / manual gate before prod deploy (time to abort).
- Separate identities for build vs deploy; least-privilege deploy credentials.
```

## GitHub Actions environments
```yaml
jobs:
  deploy-prod:
    environment:
      name: production          # protection rules apply: reviewers, branch policy, wait timer
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<sha>
      # prod secrets are only exposed to jobs targeting this environment
```
```text
Configure in repo settings: required reviewers, deployment branches allow-list, wait timer,
and environment secrets (not repo-wide). See github-actions-hardening.md.
```

## GitLab equivalents
```text
- Protected environments (who can deploy), protected branches/tags.
- Manual jobs / approval rules for deployments; environment-scoped variables.
```

## Deployment safety
```text
- Progressive delivery (canary/blue-green) + automated rollback on health checks.
- Immutable, signed artifacts (see supply-chain/sbom-cosign); verify at deploy (admission).
- Separate plan vs apply (IaC); human review of the plan for prod.
- Audit every deploy: who, what version, when, approved by whom.
```

## Detection (Blue Team)
- Deploys bypassing approvals; deploys from unexpected branches/identities; secret access anomalies.
- Alert on protection-rule changes and self-approval.

## Mitigation / Hardening
- Required reviewers + branch restrictions + scoped secrets + wait timers on prod.
- OIDC deploy creds (short-lived), least privilege, separate build/deploy roles.
- Related: [github-actions-hardening](./github-actions-hardening.md), [dependency-pinning](./dependency-pinning.md).

## Sources
- [GitHub – Deployment environments](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment) · [GitLab protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)
