---
title: "Rootless builds & BuildKit"
category: "devsecops"
tags: ["containers", "buildkit", "rootless", "ci-cd"]
platform: "agnostic"
mitre: []
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Rootless builds & BuildKit

## TL;DR
Building container images in CI traditionally needs a privileged Docker daemon (`docker.sock` / DinD) — a big attack surface (root on the host). Rootless builders (BuildKit rootless, Kaniko, Buildah) build images without a privileged daemon, shrinking blast radius.

## The problem with classic builds
```text
- Mounting /var/run/docker.sock into CI = root on the host (container escape / takeover).
- Docker-in-Docker (DinD) usually runs --privileged = kernel-level access.
- A compromised build step can then pivot to other jobs / the runner host.
```

## Rootless / daemonless options
```text
BuildKit (rootless)  – Docker's modern builder; can run without root, better caching.
Kaniko               – builds in a container/K8s with NO daemon and no privileged mode.
Buildah              – daemonless OCI image builds (Podman ecosystem), rootless-capable.
img / makisu         – other daemonless builders.
```

## Examples
```bash
# Kaniko (in Kubernetes/CI, no privileged, no daemon)
/kaniko/executor --dockerfile=Dockerfile --context=. --destination=registry/app:tag

# BuildKit rootless
buildctl-daemonless.sh build --frontend dockerfile.v0 --local context=. --local dockerfile=.

# Buildah (daemonless)
buildah bud -t registry/app:tag .
```

## Build-time hardening
```text
- No secrets baked into layers; use BuildKit secret mounts (--secret) — not ARG/ENV.
    RUN --mount=type=secret,id=npmrc ...
- Pin base images by digest (see ci-cd/dependency-pinning).
- Multi-stage builds -> minimal final image (distroless). Scan the result.
- Reproducible builds where possible; generate SBOM + sign (supply-chain/sbom-cosign).
```

## Detection (Blue Team)
- CI runners mounting docker.sock or running --privileged (flag as risk).
- Secrets appearing in image layers (scan with trivy --scanners secret).

## Mitigation / Hardening
- Prefer rootless/daemonless builders in CI; isolate + ephemeral runners.
- Never mount docker.sock into untrusted jobs; BuildKit secret mounts for build secrets.
- Related: [docker-hardening](./docker-hardening.md), [image-scanning-deep](./image-scanning-deep.md).

## Sources
- [BuildKit](https://github.com/moby/buildkit) · [Kaniko](https://github.com/GoogleContainerTools/kaniko) · [Buildah](https://buildah.io/)
