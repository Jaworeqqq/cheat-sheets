---
title: "CI/CD pipeline threat model"
category: "devsecops"
tags: ["ci-cd", "threat-modeling", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-13"
author: "core"
---

# CI/CD pipeline threat model

## TL;DR
The pipeline is a high-value target: it holds secrets, has deploy access to production, and processes untrusted inputs (PRs, dependencies). Compromise it and you compromise everything it ships. Threat-model it like any critical system — OWASP has a "Top 10 CI/CD Security Risks" as a guide.

## Trust boundaries & assets
```text
Assets: source, secrets/credentials, build artifacts, deploy access to prod, the runners themselves.
Boundaries: untrusted PRs/forks, third-party dependencies, third-party actions/plugins,
            the SCM <-> CI <-> registry <-> cloud handoffs.
```

## Key risks (OWASP CI/CD Top 10, condensed)
```text
1. Insufficient flow control – push straight to prod without review/approval.
2. Inadequate IAM – over-privileged pipeline identities, long-lived cloud keys.
3. Dependency chain abuse – confusion/typosquatting/malicious packages (see dependency-confusion).
4. Poisoned pipeline execution (PPE) – untrusted PR modifies the build to run attacker code.
5. Insufficient PBAC – runners/jobs with excessive permissions; shared runners for untrusted code.
6. Insufficient credential hygiene – secrets in logs/env/layers; not scoped/rotated.
7. Insecure system config – unhardened runners, exposed dashboards.
8. Ungoverned third-party services – over-permissioned integrations/apps.
9. Improper artifact integrity – unsigned artifacts, no provenance (see slsa-levels).
10. Insufficient logging/visibility – can't detect or investigate pipeline abuse.
```

## Poisoned Pipeline Execution (PPE) — the sharpest edge
```text
- Untrusted PR triggers a workflow that runs repo-controlled build scripts WITH secrets
  (e.g. pull_request_target + checkout of the PR head). Attacker code exfiltrates secrets / deploys.
- Defense: don't run untrusted PRs with secrets/privileged runners; separate trusted/untrusted flows.
```

## Mitigations (mapped)
```text
- Flow control: required reviews + environment protection (see environment-protection).
- IAM: OIDC short-lived creds, least privilege, no long-lived keys.
- Dependencies: pin + verify + SCA; single controlled resolver.
- Runners: ephemeral, isolated; never run untrusted code on privileged/shared runners.
- Secrets: scoped + masked + OIDC; scan for leaks (gitleaks); never in logs.
- Integrity: sign artifacts + SLSA provenance; verify at deploy.
- Visibility: audit logs on pipeline actions + config changes.
```

## Sources
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) · related: [github-actions-hardening](./github-actions-hardening.md), [environment-protection](./environment-protection.md), [slsa-levels](../supply-chain/slsa-levels.md)
