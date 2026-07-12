---
title: "Browser forensics"
category: "blue-team"
tags: ["dfir", "forensics", "browser"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Browser forensics

## TL;DR
Browsers are a goldmine for DFIR: history, downloads, cookies/sessions, cache, autofill, and extensions reveal user activity, phishing clicks, data staging, and attacker tooling. Most data lives in SQLite databases in the user profile.

## Where the data lives
```text
Chrome/Edge (Chromium): <profile>/... (User Data\Default\)
  History, Cookies, Login Data, Web Data, Downloads (in History), Cache/, Extensions\
Firefox: <profile>.default-release\
  places.sqlite (history+bookmarks), cookies.sqlite, formhistory.sqlite, logins.json+key4.db
Safari (macOS): ~/Library/Safari/ (History.db, Downloads.plist)
```

## Key artifacts & value
```text
History        – URLs + visit timestamps -> phishing clicks, C2 panels, recon, exfil sites.
Downloads      – malware/tools downloaded, source URLs, target paths.
Cookies        – active sessions (session theft/impersonation), auth tokens.
Cache          – rendered pages/files even after "deletion" (evidence of visited content).
Autofill/Logins – saved credentials (also an attacker target — DPAPI-protected on Windows).
Extensions     – malicious add-ons (credential theft, injection).
Sessions/Tabs  – what was open at compromise time.
```

## Analysis
```bash
# Query the SQLite DBs directly (copy first — don't work on originals)
sqlite3 History "SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch'), url FROM urls ORDER BY last_visit_time DESC LIMIT 50;"
# Chromium timestamps = microseconds since 1601 (WebKit epoch) -> convert as above.
```
```text
Tools: Hindsight (Chromium), DB Browser for SQLite, KAPE (collection),
       Autopsy / browser plugins, Eric Zimmerman tools.
```

## Investigative uses
```text
- Confirm a user clicked a phishing link and when (history + timestamp).
- Identify downloaded malware/tooling and its origin.
- Detect data exfil to webmail/cloud storage/paste sites.
- Recover attacker activity if they browsed on a compromised host.
```

## Notes / pitfalls
- Incognito/private mode leaves little on disk (but memory + DNS cache may help).
- Timestamps: mind the epoch (WebKit vs Unix) and timezone; correlate across artifacts.
- Sync means activity may span multiple devices under one account.

## Sources
- [Hindsight](https://github.com/obsidianforensics/hindsight) · related: [dfir-triage](./dfir-triage.md), [ir-playbook-phishing](../incident-response/ir-playbook-phishing.md)
