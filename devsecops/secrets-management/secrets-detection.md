---
title: "Detekcja i zarządzanie sekretami"
category: "devsecops"
tags: ["secrets-management", "gitleaks", "vault"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Sekrety – detekcja i zarządzanie

## TL;DR
Nie trzymaj sekretów w kodzie. Zapobiegaj (pre-commit scan), wykrywaj (skan historii), zarządzaj (Vault/KMS/secret manager), rotuj po wycieku.

## Detekcja
```bash
# gitleaks – skan repo + historii
gitleaks detect --source . --redact -v
gitleaks protect --staged            # pre-commit (przed commitem)

# trufflehog – weryfikuje czy sekret żywy
trufflehog git file://. --only-verified
trufflehog github --repo=https://github.com/org/repo
```

## Pre-commit (zapobieganie)
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.x
    hooks: [{ id: gitleaks }]
```

## Zarządzanie
```text
HashiCorp Vault  – dynamiczne sekrety, leasing, rotacja, transit encryption
Cloud native     – AWS Secrets Manager / KMS, Azure Key Vault, GCP Secret Manager
K8s              – External Secrets Operator (sync z Vault/cloud), Sealed Secrets, SOPS
CI/CD            – OIDC zamiast long-lived, masked secrets, environment scoping
```

```bash
# SOPS – szyfrowanie plików sekretów w repo (KMS/age)
sops -e secrets.yaml > secrets.enc.yaml
sops -d secrets.enc.yaml
```

## Reakcja na wyciek (kolejność!)
```text
1. ROTUJ/unieważnij sekret (usunięcie z gita NIE wystarczy — jest w historii/forkach).
2. Zbadaj czy użyty (logi dostępu).
3. Dopiero potem czyść historię (git filter-repo) jeśli trzeba.
```

## Źródła
- [gitleaks](https://github.com/gitleaks/gitleaks) · [trufflehog](https://github.com/trufflesecurity/trufflehog) · [SOPS](https://github.com/getsops/sops)
