---
title: "AWS IAM Privilege Escalation"
category: "cloud-security"
tags: ["aws", "iam", "privesc"]
platform: "aws"
mitre: ["T1078.004"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# AWS IAM Privilege Escalation

## TL;DR
Nadmiarowe uprawnienia IAM pozwalają eskalować z low-priv do admina. Klasyka: `iam:CreatePolicyVersion`, `iam:PassRole` + uruchomienie usługi, `sts:AssumeRole`. Enumeruj `enumerate-iam` / Pacu / ScoutSuite.

## Enumeracja
```bash
aws sts get-caller-identity
aws iam get-account-authorization-details        # pełny obraz (jeśli wolno)
# Automat
pacu   # moduł iam__enum_permissions, iam__privesc_scan
enumerate-iam --access-key ... --secret-key ...
```

## Typowe wektory privesc
```text
iam:CreatePolicyVersion            -> nadpisz politykę, daj sobie *:*
iam:AttachUserPolicy / PutUserPolicy -> podepnij AdministratorAccess
iam:PassRole + ec2:RunInstances     -> odpal EC2 z rolą admina, weź jej creds z metadata
iam:PassRole + lambda:CreateFunction -> Lambda z rolą admina
sts:AssumeRole (zbyt luźny trust)   -> przejmij mocniejszą rolę
iam:CreateAccessKey (na innego usera) -> klucze admina
iam:UpdateAssumeRolePolicy          -> dopisz siebie do trust policy roli
```

```bash
# Przykład: CreatePolicyVersion -> admin
aws iam create-policy-version --policy-arn <arn> \
  --policy-document file://admin.json --set-as-default
```

## Wykrywanie (Blue Team)
```text
CloudTrail: CreatePolicyVersion, AttachUserPolicy, CreateAccessKey, UpdateAssumeRolePolicy,
            PassRole do wrażliwych ról, AssumeRole z nietypowych źródeł.
GuardDuty: anomalie IAM, credential exfiltration.
```

## Mitygacja / Hardening
- Least privilege, **permission boundaries**, SCP na poziomie org.
- Ogranicz `iam:PassRole` (warunek `iam:PassedToService`), brak `*` na Action.
- Access Analyzer (nieużywane uprawnienia/publiczny dostęp), MFA, rotacja kluczy → IAM Roles zamiast userów.

## Źródła
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) · [Rhino – AWS privesc methods](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
