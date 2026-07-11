---
title: "People OSINT"
category: "osint"
tags: ["osint", "recon", "people", "sock-puppet"]
platform: "agnostic"
mitre: ["T1589", "T1591"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# People OSINT

## TL;DR
Building a profile of a person from open sources: usernames, emails, social media, and breach correlation. Used for social-engineering pretexts and target mapping in authorized engagements; used defensively to reduce employee exposure.

## Username enumeration
```bash
# Check a username across hundreds of sites
sherlock johndoe
maigret johndoe --html            # richer, more sites + report
# Pivot: a reused handle links accounts across platforms
```

## Email discovery & format
```bash
# Corporate email format + known addresses
theHarvester -d example.com -b all
# hunter.io / phonebook.cz -> pattern (first.last@, flast@, first@)
# Verify without sending mail
# holehe user@example.com   -> which sites an email is registered on
```

## Social media & identity
```text
- LinkedIn  – employees, roles, tech stack, org chart (spray/phish targeting)
- X/Instagram/Facebook – interests, location, connections, photos (EXIF -> metadata-exif.md)
- GitHub    – commits reveal emails (git log), projects, other handles
- Public records / people-search aggregators (jurisdiction-dependent)
```

## Breach correlation
```text
- Cross-reference emails/usernames with breach data (see breach-data.md).
- Reused passwords/usernames link personas and enable credential attacks (authorized).
- Stealer logs increasingly tie an identity to live sessions + creds.
```

## OPSEC (investigator side)
- Use sock-puppet accounts and a clean/isolated browser; avoid logging in with real accounts.
- Passive first — viewing a LinkedIn profile can notify the target.

## Defensive notes (Blue Team)
- Employee awareness: minimize oversharing (roles, tech, travel) on public profiles.
- Monitor executive exposure; scrub metadata from published photos/docs.
- Enforce MFA + breached-password checks so leaked personal creds don't cross into corporate.

## Sources
- [Sherlock](https://github.com/sherlock-project/sherlock) · [Maigret](https://github.com/soxoj/maigret) · [OSINT Framework](https://osintframework.com/)
