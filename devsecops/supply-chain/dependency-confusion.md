---
title: "Dependency confusion"
category: "devsecops"
tags: ["supply-chain", "dependencies", "npm", "pypi"]
platform: "agnostic"
mitre: ["T1195.001"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Dependency confusion

## TL;DR
If your build resolves an internal package name from a public registry, an attacker who publishes a same-named package (with a higher version) to the public registry gets their code executed in your build. A supply-chain attack that hit major companies.

## How the attack works
```text
1. Attacker learns an internal package name (e.g. from a leaked package.json).
2. Publishes "acme-internal-utils" to the PUBLIC registry with version 99.0.0.
3. Your build with mixed public+internal resolution picks the PUBLIC one
   (higher version wins) -> runs the attacker's install script.
```

## Vulnerable patterns
```text
- Internal packages without a reserved scope/namespace.
- Package managers configured with public + private in one resolution list where
  the highest version wins across both.
- Install-time scripts (npm postinstall, pip setup.py) = code exec on install.
```

## Defenses by ecosystem
```text
npm    – use a scope (@acme/*) and bind the scope to the private registry:
           @acme:registry=https://npm.internal
         Enable "install only from allowed registry"; reserve the public scope.
pip    – avoid implicit public fallback; use --index-url (not --extra-index-url)
         to a controlled proxy; hash-pinning (pip --require-hashes).
Maven  – lock repositories; use a repository manager (Nexus/Artifactory) with
         a single virtual repo and proper ordering; namespace groupIds.
General- pull-through proxy (Artifactory/Nexus) as the ONLY resolver; block
         mixed public/private resolution; verify integrity (lockfile hashes).
```

## Detection (Blue Team)
- Build logs: packages resolved from a public registry that should be internal.
- New/unexpected versions of internal package names on public registries (monitor).
- Outbound connections during install/build to unexpected hosts.

## Mitigation / Hardening
- **Reserve your namespaces/scopes** on public registries (defensive publishing).
- Single controlled resolver (proxy); no implicit public fallback; lockfiles + hashes.
- Disable/limit install scripts; verify provenance (see [sbom-cosign](./sbom-cosign.md)).

## Sources
- [Alex Birsan – Dependency Confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) · [MITRE T1195.001](https://attack.mitre.org/techniques/T1195/001/)
