---
title: "Data retention & disposal"
category: "compliance"
tags: ["compliance", "policies", "data-retention", "privacy"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-12"
author: "core"
---

# Data retention & disposal

## TL;DR
Keep data only as long as you have a lawful/business reason, then dispose of it securely. Over-retention increases breach impact and violates privacy laws (GDPR storage limitation); under-retention breaks legal/audit obligations. A retention schedule balances the two.

## Why it matters
```text
- Privacy law: GDPR "storage limitation" — don't keep personal data longer than needed.
- Breach impact: data you don't hold can't be stolen (data minimization).
- Legal/regulatory: some records MUST be kept (tax, financial, healthcare) for set periods.
- Litigation holds override normal deletion for relevant data.
```

## Building a retention schedule
```text
1. Inventory data by category (PII, financial, logs, backups, HR, health).
2. For each: legal/regulatory requirement, business need, and privacy limit.
3. Set a retention period + trigger (from creation / last use / contract end).
4. Define disposal method and who is responsible.
5. Document exceptions (legal hold) and review annually.
```

## Example schedule (illustrative — verify against your jurisdiction)
```text
Category                Retention             Then
Security/audit logs     1-2 years (or more)   secure delete
Financial records       ~7 years (varies)     secure delete
Customer PII            duration of relationship + legal minimum   delete/anonymize
Backups                 defined cycle (e.g. 30-90 days)            rotate/overwrite
Employee records        per labor law          secure delete
```

## Secure disposal
```text
- Digital: crypto-shredding (destroy the key), secure wipe, or verified deletion across
  primary + backups + logs + third parties (processors).
- Physical: shredding, degaussing, certified destruction with certificates.
- Cloud: understand provider deletion timelines; delete across regions/replicas.
```

## Detection / governance (Blue Team)
- Monitor for data kept past retention (stale PII stores); alert on undeleted expired data.

## Best practices
- Automate deletion where possible; handle backups and third-party copies, not just primary.
- Honor data-subject erasure requests (GDPR) within the schedule + legal-hold exceptions.
- Tie to classification (see [policy-templates](./policy-templates.md)) and [gdpr](../frameworks/gdpr.md).

## Sources
- [GDPR Art. 5(1)(e) storage limitation](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIST SP 800-88 (media sanitization)](https://csrc.nist.gov/pubs/sp/800/88/r1/final)
