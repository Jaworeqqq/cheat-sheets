---
title: "GitLab CI hardening"
category: "devsecops"
tags: ["ci-cd", "gitlab", "supply-chain"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# GitLab CI hardening

## TL;DR
Same threat model as any pipeline: protect secrets, restrict runners, prevent injection, use short-lived cloud creds via OIDC. GitLab specifics: protected branches/variables, runner tags, `CI_JOB_TOKEN` scope.

## Key protections
```yaml
# Least-privilege job token + explicit stages
stages: [build, test]

build:
  stage: build
  # Pin the image by digest, not a floating tag
  image: alpine@sha256:...
  script:
    - ./build.sh
```

## Secrets & variables
```text
- Mark variables Protected (only protected branches/tags) + Masked.
- Prefer OIDC to cloud (id_tokens:) over long-lived CI variables:
```
```yaml
deploy:
  id_tokens:
    AWS_TOKEN:
      aud: https://gitlab.example.com
  script:
    - # exchange the OIDC token for short-lived AWS creds
```

## Runners
```text
- Don't run untrusted MRs on privileged/shared runners.
- Avoid privileged Docker-in-Docker; use rootless/BuildKit where possible.
- Tag runners; isolate production deploy runners from build runners.
- Restrict who can run pipelines on protected branches.
```

## Injection-safe
```text
- Never interpolate untrusted input (MR title/branch) directly into script:.
  Pass via variables and quote: echo "$CI_MERGE_REQUEST_TITLE"
- Beware CI_JOB_TOKEN over-scoping (limit project access in the allowlist).
```

## Detection / audit
- Review `.gitlab-ci.yml` changes (CODEOWNERS), audit runner registration, secret scanning.

## Mitigation / Hardening
- Protected + masked variables, OIDC, pinned image digests, isolated/tagged runners.
- Enable GitLab secret detection, SAST, dependency scanning templates.

## Sources
- [GitLab – Pipeline security](https://docs.gitlab.com/ee/ci/pipelines/pipeline_security.html) · [GitLab OIDC](https://docs.gitlab.com/ee/ci/cloud_services/)
