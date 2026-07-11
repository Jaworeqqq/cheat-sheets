---
title: "macOS hardening"
category: "blue-team"
tags: ["hardening", "macos", "endpoint"]
platform: "macos"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# macOS hardening

## TL;DR
macOS ships with layered protections (SIP, Gatekeeper, XProtect, TCC, FileVault). Hardening = keep them enabled, enforce via MDM against a CIS baseline, minimize services, and centralize logging. Never disable SIP/Gatekeeper in production.

## Built-in protections (keep on)
```bash
# System Integrity Protection (protects system files/processes)
csrutil status                       # should be "enabled"
# Gatekeeper (only allow signed/notarized apps)
spctl --status                       # should be "assessments enabled"
# XProtect / notarization are automatic (Apple's built-in AV + signing checks)
```

## Disk & network
```bash
# FileVault full-disk encryption
fdesetup status                      # enable; escrow recovery key via MDM
sudo fdesetup enable
# Application firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on
```

## Privacy & permissions (TCC)
```text
TCC (Transparency, Consent, Control) gates access to camera, mic, files,
Full Disk Access, Screen Recording, Accessibility.
- Manage via MDM (PPPCP profiles) — least privilege for apps/agents.
- Watch for apps requesting Accessibility/Full Disk Access (malware abuses these).
```

## Reduce attack surface
```bash
# Disable risky/unneeded services
sudo systemsetup -setremotelogin off       # SSH off unless needed
sudo systemsetup -setremoteappleevents off
# Disable automatic login; require password immediately after sleep
# Remove/limit Remote Management (ARD) unless required
```

## Logging & monitoring (unified log)
```bash
# Query the unified log (auth, process exec, network)
log show --predicate 'eventMessage contains "authenticat"' --last 1h
log stream --predicate 'process == "sudo"'
# Endpoint Security framework feeds EDR tools (process/file/network events)
```

## Detection (Blue Team)
- Unexpected TCC grants (Full Disk Access/Accessibility), unsigned/quarantine-stripped binaries.
- LaunchAgents/LaunchDaemons persistence (`~/Library/LaunchAgents`, `/Library/Launch*`).
- Gatekeeper/SIP disabled, new admin accounts, ARD/SSH enabled.

## Mitigation / Hardening
- Enforce a **CIS macOS Benchmark** baseline via MDM (Jamf/Intune); FileVault + escrow.
- Keep SIP, Gatekeeper, FileVault, firewall + stealth on; auto-update enabled.
- Least-privilege TCC via MDM profiles; ship Endpoint Security telemetry + unified log to SIEM.
- Standard (non-admin) daily accounts; strong password + screen-lock policy.

## Sources
- [CIS Apple macOS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [Apple Platform Security](https://support.apple.com/guide/security/) · [macOS Security Compliance Project](https://github.com/usnistgov/macos_security)
