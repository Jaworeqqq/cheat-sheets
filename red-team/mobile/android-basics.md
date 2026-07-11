---
title: "Android – podstawy pentestu"
category: "red-team"
tags: ["mobile", "android"]
platform: "mobile"
mitre: ["T1626"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Android – podstawy pentestu

## TL;DR
Statycznie: dekompilacja APK (manifest, sekrety, endpointy). Dynamicznie: przechwycenie ruchu (Burp + cert), instrumentacja (Frida) do obejścia SSL pinning/root detection.

## Statyczna analiza
```bash
# Rozpakuj + dekompiluj
apktool d app.apk -o app_src
jadx-gui app.apk                 # czytelny kod źródłowy
# Szukaj sekretów/endpointów
grep -rniE "api_key|secret|http://|https://|firebaseio" app_src
```

## Dynamiczna
```bash
adb install app.apk
adb shell pm list packages | grep target
# Proxy ruchu przez Burp (ustaw proxy + zainstaluj cert jako system CA)
# SSL pinning / root bypass
frida -U -f com.target.app -l frida-ssl-bypass.js
objection -g com.target.app explore   # android sslpinning disable
```

## Typowe problemy
```text
- Sekrety w kodzie/strings.xml         - Insecure storage (SharedPrefs, SQLite plaintext)
- Eksportowane komponenty (activity/provider) - Debuggable=true
- Słaba walidacja certów / brak pinningu    - WebView JS bridge
```

## Mitygacja / Hardening (dla defensywy)
- Nie trzymaj sekretów w APK; SSL pinning + walidacja; szyfruj lokalne dane.
- `android:debuggable=false`, minimalizuj eksportowane komponenty, ProGuard/R8.
- Root/tamper detection jako defense-in-depth (nie jedyna warstwa).

## Źródła
- [OWASP MASTG](https://mas.owasp.org/) · [Frida](https://frida.re/)
