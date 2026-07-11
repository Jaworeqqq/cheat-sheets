---
title: "Phishing – dostęp początkowy"
category: "red-team"
tags: ["initial-access", "phishing", "social-engineering"]
platform: "agnostic"
mitre: ["T1566"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Phishing – dostęp początkowy

## TL;DR
Wektory: link do fałszywego logowania (credential harvest), złośliwy załącznik (makro/HTA/LNK), lub OAuth consent (device code). Zawsze w ramach autoryzowanego zaangażowania i uzgodnionego zakresu.

## Wymagania / Kontekst
- Zaufana domena (postarzona), poprawny SPF/DKIM/DMARC na infrastrukturze wysyłkowej.
- Pretekst dopasowany do celu (OSINT).

## Techniki
```text
1. Credential harvesting  – Evilginx2 (reverse proxy, kradnie też sesję/MFA), GoPhish (landing)
2. Payload w załączniku    – makra VBA, .lnk → LOLBin, .iso/.img (omija MOTW), HTML smuggling
3. OAuth Device Code       – ofiara wkleja kod, atakujący dostaje token (omija hasło)
```

```bash
# GoPhish – framework kampanii (landing + tracking)
./gophish   # panel na :3333

# Evilginx2 – phishlet dla adversary-in-the-middle (kradnie sesyjne cookie + MFA)
evilginx2 -p ./phishlets
```

## Wykrywanie (Blue Team)
- Nowo zarejestrowane / podobne domeny (typosquatting) — monitoring.
- Email gateway: anomalie SPF/DKIM/DMARC, linki do świeżych domen, HTML z JS blob.
- **Sign-in z nietypowej geolokalizacji tuż po kliknięciu** (AiTM → skradziona sesja).

## Mitygacja / Hardening
- MFA odporne na phishing: **FIDO2 / passkeys** (Evilginx tego nie obejdzie).
- Blokada legacy auth, ograniczenie OAuth consent, MOTW enforcement.
- Szkolenia + łatwy przycisk „zgłoś phishing".

## Uwagi / Pułapki
- FIDO2 pokonuje AiTM; zwykłe TOTP/SMS — nie.

## Źródła
- [Evilginx](https://github.com/kgretzky/evilginx2) · [GoPhish](https://getgophish.com/)
