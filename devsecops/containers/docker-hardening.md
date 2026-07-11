---
title: "Docker Hardening"
category: "devsecops"
tags: ["containers", "docker", "hardening"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Docker Hardening

## TL;DR
Minimalny obraz, non-root, read-only FS, brak zbędnych capabilities, skan obrazu. Kontener to nie granica bezpieczeństwa jak VM — traktuj defense-in-depth.

## Dockerfile – dobre praktyki
```dockerfile
# Multi-stage + minimalny/distroless obraz bazowy
FROM golang:1.22 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app ./cmd

FROM gcr.io/distroless/static:nonroot
COPY --from=build /app /app
USER nonroot:nonroot          # nie root!
ENTRYPOINT ["/app"]
```

## Runtime – ograniczenia
```bash
docker run \
  --read-only \                       # FS read-only (+ --tmpfs /tmp)
  --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
  --security-opt=no-new-privileges \
  --user 10001:10001 \
  --pids-limit=100 --memory=256m \
  --network=app-net \
  myimage
```

## Skanowanie
```bash
trivy image myimage:latest            # CVE + misconfig + sekrety
grype myimage:latest
docker scout cves myimage:latest
```

## Anti-patterny
```text
- Kontener jako root                  - Montowanie /var/run/docker.sock (=root na hoście)
- --privileged                        - Sekrety w ENV / warstwach obrazu
- latest jako tag (brak determinizmu) - Zbędne pakiety/narzędzia w obrazie
```

## Wykrywanie (Blue Team)
- Runtime security: Falco (reguły na spawn shell w kontenerze, mount docker.sock).
- Admission/skan w rejestrze; blokada obrazów z krytycznymi CVE.

## Źródła
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker) · [Trivy](https://github.com/aquasecurity/trivy) · [Distroless](https://github.com/GoogleContainerTools/distroless)
