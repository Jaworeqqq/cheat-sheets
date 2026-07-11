---
title: "iOS – pentest basics"
category: "red-team"
tags: ["mobile", "ios"]
platform: "mobile"
mitre: ["T1626"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# iOS – pentest basics

## TL;DR
iOS testing usually needs a jailbroken device (or a re-signed app on a normal one). Static: inspect the IPA (Info.plist, binary, embedded secrets). Dynamic: intercept TLS + instrument with Frida/objection to bypass pinning/jailbreak detection.

## Static analysis
```bash
# IPA is a zip
unzip app.ipa -d app_extracted
# Binary info / encryption status
otool -l app_extracted/Payload/App.app/App | grep -A4 LC_ENCRYPTION_INFO
# Class dump (Objective-C) / Hopper/Ghidra for Swift
class-dump App
# Hunt for secrets/endpoints
grep -rniE "api_key|secret|https?://" app_extracted
```

## Dynamic (jailbroken)
```bash
# Decrypt app from memory (App Store apps are FairPlay-encrypted)
frida-ios-dump  # or bagbak
# Instrument – bypass SSL pinning / jailbreak detection
objection -g com.target.app explore
# ios sslpinning disable ; ios jailbreak disable
frida -U -f com.target.app -l frida-pinning-bypass.js
```

## Common issues
```text
- Secrets in Info.plist / binary / NSUserDefaults
- Sensitive data in Keychain with weak accessibility class
- Insecure local storage (plist, SQLite, cache), pasteboard leakage
- Missing ATS / cert pinning, custom URL scheme abuse
- Debuggable / weak jailbreak detection
```

## Mitigation / Hardening (defensive)
- Store secrets in the Keychain (`ThisDeviceOnly` classes), never in the binary/plist.
- Enforce ATS + certificate pinning; validate server certs.
- Jailbreak/tamper detection as defense-in-depth; disable debug in release.

## Sources
- [OWASP MASTG (iOS)](https://mas.owasp.org/) · [objection](https://github.com/sensepost/objection) · [Frida](https://frida.re/)
