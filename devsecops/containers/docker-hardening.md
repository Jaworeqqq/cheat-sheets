---
title: "Docker hardening"
category: "devsecops"
tags: ["containers", "docker", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Docker hardening

## TL;DR
Minimal image, non-root, read-only FS, no unnecessary capabilities, image scanning. A container is not a security boundary like a VM — treat it as defense-in-depth.

## Dockerfile – best practices
```dockerfile
# Multi-stage + minimal/distroless base image
FROM golang:1.22 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app ./cmd

FROM gcr.io/distroless/static:nonroot
COPY --from=build /app /app
USER nonroot:nonroot          # not root!
ENTRYPOINT ["/app"]
```

## Runtime – restrictions
```bash
docker run \
  --read-only \                       # read-only FS (+ --tmpfs /tmp)
  --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
  --security-opt=no-new-privileges \
  --user 10001:10001 \
  --pids-limit=100 --memory=256m \
  --network=app-net \
  myimage
```

## Scanning
```bash
trivy image myimage:latest            # CVEs + misconfig + secrets
grype myimage:latest
docker scout cves myimage:latest
```

## Anti-patterns
```text
- Container as root                  - Mounting /var/run/docker.sock (=root on the host)
- --privileged                       - Secrets in ENV / image layers
- latest as a tag (non-deterministic) - Unnecessary packages/tools in the image
```

## Detection (Blue Team)
- Runtime security: Falco (rules on spawning a shell in a container, mounting docker.sock).
- Admission/scan in the registry; block images with critical CVEs.

## Sources
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) · [Trivy](https://github.com/aquasecurity/trivy) · [Distroless](https://github.com/GoogleContainerTools/distroless)
