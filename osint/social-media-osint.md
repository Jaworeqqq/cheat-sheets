---
title: "Social media OSINT"
category: "osint"
tags: ["osint", "social-media", "recon"]
platform: "agnostic"
mitre: ["T1593.001"]
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Social media OSINT

## TL;DR
Public social profiles leak org structure, tech stack, physical locations, and pretext material for social engineering. Used in authorized red-team recon; defended by awareness and minimizing oversharing.

## Sources & value
```text
LinkedIn   – employees, roles, tech stack (from job posts), org chart, email format.
X/Twitter  – tech discussions, conference talks, real-time location/activity.
GitHub     – repos, commit emails, leaked secrets, internal tooling names.
Instagram/Facebook – physical locations, badges/screens in photos, personal details.
Job boards – exact technologies, security tools, cloud providers in use.
```

## Techniques
```text
- Build an employee list (LinkedIn) -> derive email format -> target list for phishing/spray.
- Extract tech stack from job postings ("must know Splunk, CrowdStrike, Okta").
- Photo analysis: badges, screens, whiteboards, building interiors (physical recon).
- Correlate usernames across platforms (Sherlock/Maigret) -> more data points.
- Commit emails on GitHub -> real names + internal usernames.
```

## Tools
```text
- Sherlock / Maigret (username correlation), theHarvester (emails/hosts)
- SpiderFoot / Maltego (graph relationships)
- Manual review + advanced search operators
```

## Detection / defense (Blue Team)
- Monitor brand/employee mentions; watch for impersonation accounts.
- Detect targeted phishing that references social-media-sourced pretexts.

## Mitigation / Hardening
- Employee awareness: limit oversharing (badges, screens, internal tool names).
- Minimize what job posts reveal about the security stack.
- Scrub metadata from published photos (see [metadata-exif](./metadata-exif.md)).
- Phishing-resistant MFA blunts the payoff of harvested target lists.

## Sources
- [OSINT Framework](https://osintframework.com/) · related: [people-osint](./people-osint.md), [recon-frameworks](./recon-frameworks.md)
