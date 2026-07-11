---
title: "GitHub Actions hardening"
category: "devsecops"
tags: ["ci-cd", "github-actions", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# GitHub Actions hardening

## TL;DR
The pipeline is a high-value target (secrets, deploy). Risks: pwn request, injection via untrusted input, token theft, malicious actions. Rules: least privilege, pin SHA, OIDC instead of secrets.

## Key protections
```yaml
# 1. Minimal GITHUB_TOKEN permissions (default is read)
permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 2. Pin actions to a full SHA (not a tag!)
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
      # 3. OIDC to the cloud instead of long-lived secrets
      - uses: aws-actions/configure-aws-credentials@<sha>
        with:
          role-to-assume: arn:aws:iam::123:role/ci
          aws-region: eu-central-1
```

## Pitfalls
```text
pull_request_target + checkout PR HEAD  -> runs untrusted code with secrets (RCE)
${{ github.event.issue.title }} in run:  -> script injection (use env: indirectly)
self-hosted runner on a public repo       -> foreign code on your infra
permissions: write-all too broad
```

## Injection-safe
```yaml
# BAD: run: echo "${{ github.event.pull_request.title }}"
# GOOD: pass via env and quote
      - env:
          TITLE: ${{ github.event.pull_request.title }}
        run: echo "$TITLE"
```

## Detection / audit
- Scan workflows: `zizmor`, `octoscan`, StepSecurity Harden-Runner (monitors egress).
- Alert on changes to `.github/workflows` (CODEOWNERS + review).

## Mitigation / Hardening
- OIDC, pin SHA + Dependabot for actions, least-privilege `permissions`, environment protection rules.
- Harden-Runner (network egress policy), branch protection, no `pull_request_target` with PR checkout.

## Sources
- [GitHub – Security hardening for Actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) · [zizmor](https://github.com/woodruffw/zizmor)
