---
title: "AWS S3 – misconfigurations"
category: "cloud-security"
tags: ["aws", "s3", "storage"]
platform: "aws"
mitre: ["T1530"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# AWS S3 misconfigurations

## TL;DR
Public buckets, overly loose policy/ACL, and takeover-prone names are the classic sources of data leaks. Enumerate, check access, verify encryption/logging.

## Enumeration / access test
```bash
# Does the bucket exist / is it public
aws s3 ls s3://bucket-name --no-sign-request
curl -s https://bucket-name.s3.amazonaws.com/     # listing if public

# Your permissions
aws s3api get-bucket-acl --bucket bucket-name
aws s3api get-bucket-policy --bucket bucket-name
aws s3api get-public-access-block --bucket bucket-name

# Name bruteforce / discovery
# cloud_enum, s3scanner
s3scanner scan --bucket-file names.txt
```

## Common issues
```text
- Public-read / public-write ACL          - Policy with Principal:"*"
- Block Public Access disabled            - No at-rest encryption (SSE)
- No versioning + no MFA delete           - No access logging
- Presigned URL with a long TTL           - Dangling bucket (subdomain takeover)
```

## Detection (Blue Team)
- Config rule / Access Analyzer: public buckets, policy with `*`.
- CloudTrail data events on sensitive buckets, GuardDuty (anomalous access/exfil).

## Mitigation / Hardening
- **Block Public Access** at the account level (default), SSE-KMS, versioning.
- Least-privilege bucket policy, VPC endpoint, `aws:SecureTransport` (enforce TLS).
- Access logging + monitoring, no wildcard Principal.

## Sources
- [AWS S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
