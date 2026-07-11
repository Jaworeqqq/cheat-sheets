---
title: "AWS S3 – misconfiguracje"
category: "cloud-security"
tags: ["aws", "s3", "storage"]
platform: "aws"
mitre: ["T1530"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# AWS S3 Misconfigurations

## TL;DR
Publiczne buckety, zbyt luźne policy/ACL i podatne na przejęcie nazwy to klasyka wycieków danych. Enumeruj, sprawdź dostęp, zweryfikuj szyfrowanie/logi.

## Enumeracja / test dostępu
```bash
# Czy bucket istnieje / publiczny
aws s3 ls s3://bucket-name --no-sign-request
curl -s https://bucket-name.s3.amazonaws.com/     # listing jeśli publiczny

# Twoje uprawnienia
aws s3api get-bucket-acl --bucket bucket-name
aws s3api get-bucket-policy --bucket bucket-name
aws s3api get-public-access-block --bucket bucket-name

# Brute nazw / discovery
# cloud_enum, s3scanner
s3scanner scan --bucket-file names.txt
```

## Typowe problemy
```text
- Public-read / public-write ACL          - Policy z Principal:"*"
- Wyłączony Block Public Access           - Brak szyfrowania (SSE) at-rest
- Brak wersjonowania + brak MFA delete    - Brak access logging
- Presigned URL z długim TTL              - Dangling bucket (subdomain takeover)
```

## Wykrywanie (Blue Team)
- Config rule / Access Analyzer: publiczne buckety, policy z `*`.
- CloudTrail data events na wrażliwych bucketach, GuardDuty (anomalny dostęp/exfil).

## Mitygacja / Hardening
- **Block Public Access** na poziomie konta (domyślnie), SSE-KMS, wersjonowanie.
- Bucket policy least-privilege, VPC endpoint, `aws:SecureTransport` (wymuś TLS).
- Access logging + monitoring, brak wildcard Principal.

## Źródła
- [AWS S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
