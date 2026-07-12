---
title: "Dependency pinning"
category: "devsecops"
tags: ["ci-cd", "supply-chain", "dependencies"]
platform: "agnostic"
mitre: ["T1195"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Dependency pinning

## TL;DR
Pin dependencies (and CI actions, base images) to exact, verified versions/digests so builds are reproducible and can't silently pull a malicious or breaking update. Floating tags (`latest`, `^1.2`, `@v4`) are a supply-chain risk.

## What to pin (and how)
```text
Packages   – lockfiles with hashes (package-lock.json, poetry.lock, Cargo.lock, go.sum).
             pip: --require-hashes. Commit lockfiles.
CI actions – GitHub Actions to a full commit SHA, not a tag:
             uses: actions/checkout@<40-char-sha>   # not @v4
Base images – by digest, not tag:
             FROM alpine@sha256:...                 # not alpine:latest
Tools       – pin CLI tool versions in CI (installers with checksums).
```

## Why floating refs are dangerous
```text
- `@v4` / `latest` are mutable — a compromised maintainer or hijacked tag ships you new code.
- Transitive deps update silently -> new CVE or backdoor enters your build.
- Reproducibility breaks: "works on my machine / yesterday's build".
```

## Balancing pinning with patching
```text
Pinning freezes versions — so you MUST actively update, or you rot with known CVEs.
Solution: pin + automated update PRs:
 - Dependabot / Renovate open PRs to bump pins; CI (SCA + tests) gates the merge.
 - You get reproducibility AND timely patching, with a human/automated review in between.
```

## Verification
```text
- Enforce lockfile presence + hash verification in CI (fail if missing/changed unexpectedly).
- Verify base image digests; scan images (see containers/image-scanning-deep).
- Combine with provenance/signing (see supply-chain/sbom-cosign) for end-to-end integrity.
```

## Detection (Blue Team)
- CI alerts on unpinned actions/images; lockfile drift; unexpected registry sources.

## Sources
- [OpenSSF – Scorecard (Pinned-Dependencies)](https://github.com/ossf/scorecard) · related: [dependency-confusion](../supply-chain/dependency-confusion.md), [github-actions-hardening](./github-actions-hardening.md)
