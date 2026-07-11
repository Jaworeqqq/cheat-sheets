---
title: "Android – pentest basics"
category: "red-team"
tags: ["mobile", "android"]
platform: "mobile"
mitre: ["T1626"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Android – pentest basics

## TL;DR
Statically: decompile the APK (manifest, secrets, endpoints). Dynamically: intercept traffic (Burp + cert), instrument (Frida) to bypass SSL pinning/root detection.

## Static analysis
```bash
# Unpack + decompile
apktool d app.apk -o app_src
jadx-gui app.apk                 # readable source
# Hunt for secrets/endpoints
grep -rniE "api_key|secret|http://|https://|firebaseio" app_src
```

## Dynamic
```bash
adb install app.apk
adb shell pm list packages | grep target
# Proxy traffic through Burp (set proxy + install cert as system CA)
# SSL pinning / root bypass
frida -U -f com.target.app -l frida-ssl-bypass.js
objection -g com.target.app explore   # android sslpinning disable
```

## Common issues
```text
- Secrets in code/strings.xml           - Insecure storage (SharedPrefs, SQLite plaintext)
- Exported components (activity/provider) - Debuggable=true
- Weak cert validation / no pinning       - WebView JS bridge
```

## Mitigation / Hardening (defensive)
- Don't ship secrets in the APK; SSL pinning + validation; encrypt local data.
- `android:debuggable=false`, minimize exported components, ProGuard/R8.
- Root/tamper detection as defense-in-depth (not the only layer).

## Sources
- [OWASP MASTG](https://mas.owasp.org/) · [Frida](https://frida.re/)
