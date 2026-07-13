---
title: "Dark web monitoring"
category: "osint"
tags: ["osint", "dark-web", "threat-intel"]
platform: "agnostic"
mitre: ["T1596"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Dark web monitoring

## TL;DR
Monitoring dark web / underground sources for mentions of your organization: leaked credentials, stolen data for sale, ransomware leak-site listings, and threat-actor chatter. Provides early warning of compromise and targeting. Do it lawfully and safely — observing, not participating in crime.

## What to monitor for
```text
- Leaked/for-sale credentials (combolists, stealer logs) tied to your domains.
- Company data for sale (databases, source code, documents).
- Ransomware leak sites listing your org (or partners/vendors).
- Initial-access-broker listings offering access to your environment.
- Threat-actor chatter naming your brand, executives, or products.
```

## Sources
```text
- Ransomware leak sites (Tor .onion) — track known groups' blogs.
- Underground forums/markets (credential/data trading).
- Telegram/Discord channels (increasingly where trading happens).
- Paste sites, breach aggregators, stealer-log channels.
- Commercial threat-intel platforms that safely index these (recommended over DIY).
```

## Safety & legality
```text
- Prefer vetted commercial services / your CTI provider — they handle access safely + legally.
- If DIY: isolated environment (dedicated VM, Tor), never authenticate with real identities,
  never purchase/download stolen data (legal + ethical + operational risk).
- Know your jurisdiction's rules; involve legal for handling of discovered data.
```

## Turning findings into action
```text
- Leaked creds -> force resets, check for use, enable/step-up MFA (see osint/breach-data).
- Data for sale -> IR + legal + notification obligations (GDPR/breach laws).
- Access broker listing -> hunt for the described access; assume breach; investigate.
- Actor targeting -> raise monitoring, brief execs (esp. for BEC/whaling).
```

## Detection / defense (Blue Team)
- Feed findings into IR + threat intel; correlate leaked creds with sign-in attempts.
- Monitor for stealer-log infections (they feed the credential trade).

## Sources
- [Have I Been Pwned](https://haveibeenpwned.com/) · related: [breach-data](./breach-data.md), [corporate-osint](./corporate-osint.md)
