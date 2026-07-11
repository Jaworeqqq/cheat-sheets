---
title: "IR Playbook – Ransomware"
category: "blue-team"
tags: ["incident-response", "ransomware", "playbook"]
platform: "agnostic"
mitre: ["T1486"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# IR Playbook – Ransomware

## TL;DR
Phases per NIST 800-61: Preparation → Detection/Analysis → Containment/Eradication/Recovery → Lessons Learned. For ransomware: **isolate fast, don't pay hastily, preserve evidence**.

## 1. Detection and triage
```text
Signals: mass file changes (.locked), ransom note, EDR alert, backup/AV disabled,
         unusual logons, CPU spike (encryption).
First questions: patient zero? entry vector? scope? is encryption still active?
```

## 2. Containment
```text
- Isolate infected hosts (disconnect the network, do NOT power off — preserve RAM for forensics).
- Disable compromised accounts, reset passwords (including krbtgt x2 if AD).
- Cut C2 channels (firewall/DNS sinkhole), disable remote access.
- Protect backups (offline/immutable) from deletion.
```

## 3. Eradication and recovery
```text
- Identify and remove persistence mechanisms, patch the entry vector.
- Restore from clean, verified backups (check they aren't infected).
- Rebuild from trusted images; don't trust "cleaned" hosts on deep compromise.
```

## 4. Post-incident
```text
- Timeline, root cause, lessons learned, detection updates (Sigma/EDR).
- Regulatory reporting (GDPR 72h if personal data), communications.
```

## Evidence collection (before cleaning)
```bash
# Memory + disk before you modify the host
# (winpmem/DumpIt for RAM; disk image dd/FTK)
# Preserve: logs, samples, ransom note, IOCs
```

## Don't / Do
- ❌ Don't reflexively power off the host (RAM loss), don't pay without legal/business analysis.
- ✅ Isolate, collect evidence, engage legal/insurer/authorities per policy.

## Sources
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [CISA #StopRansomware](https://www.cisa.gov/stopransomware)
