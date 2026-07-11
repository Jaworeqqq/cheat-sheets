---
title: "Hardening GitHub Actions"
category: "devsecops"
tags: ["ci-cd", "github-actions", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Hardening GitHub Actions

## TL;DR
Pipeline to cel o wysokiej wartości (sekrety, deploy). Ryzyka: pwn request, wstrzyknięcie przez untrusted input, kradzież tokenu, złośliwe akcje. Zasady: least privilege, pin SHA, OIDC zamiast sekretów.

## Kluczowe zabezpieczenia
```yaml
# 1. Minimalne uprawnienia GITHUB_TOKEN (domyślnie read)
permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 2. Pinuj akcje do pełnego SHA (nie do taga!)
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
      # 3. OIDC do chmury zamiast long-lived secrets
      - uses: aws-actions/configure-aws-credentials@<sha>
        with:
          role-to-assume: arn:aws:iam::123:role/ci
          aws-region: eu-central-1
```

## Pułapki
```text
pull_request_target + checkout PR HEAD  -> wykonuje niezaufany kod z sekretami (RCE)
${{ github.event.issue.title }} w run:  -> script injection (używaj env: pośrednio)
self-hosted runner na public repo       -> obcy kod na Twojej infrze
zbyt szerokie permissions: write-all
```

## Injection-safe
```yaml
# ŹLE: run: echo "${{ github.event.pull_request.title }}"
# DOBRZE: przekaż przez env i cytuj
      - env:
          TITLE: ${{ github.event.pull_request.title }}
        run: echo "$TITLE"
```

## Wykrywanie / audyt
- Skanuj workflowy: `zizmor`, `octoscan`, StepSecurity Harden-Runner (monitoruje egress).
- Alert na zmiany w `.github/workflows` (CODEOWNERS + review).

## Mitygacja / Hardening
- OIDC, pin SHA + Dependabot na akcje, `permissions` least-privilege, environment protection rules.
- Harden-Runner (network egress policy), branch protection, brak `pull_request_target` z checkoutem PR.

## Źródła
- [GitHub – Security hardening for Actions](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions) · [zizmor](https://github.com/woodruffw/zizmor)
