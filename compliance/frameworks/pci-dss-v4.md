---
title: "PCI DSS v4.0"
category: "compliance"
tags: ["compliance", "pci-dss", "payments"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# PCI DSS v4.0

## TL;DR
Standard ochrony danych kart płatniczych (obowiązkowy dla przetwarzających/przechowujących/przesyłających dane kart). 12 wymagań w 6 celach. v4.0 obowiązuje w pełni od 31 marca 2025.

## 12 wymagań
```text
Buduj i utrzymuj bezpieczną sieć
 1. Zapory / kontrola ruchu sieciowego
 2. Brak domyślnych haseł / bezpieczne konfiguracje
Chroń dane posiadaczy kart
 3. Ochrona przechowywanych danych (minimalizacja, szyfrowanie; NIGDY nie przechowuj CVV)
 4. Szyfrowanie transmisji przez sieci publiczne (TLS)
Zarządzaj podatnościami
 5. Ochrona przed malware (AV/EDR)
 6. Bezpieczne tworzenie i utrzymanie systemów (secure SDLC, patching)
Silna kontrola dostępu
 7. Least privilege (need-to-know)
 8. Identyfikacja i uwierzytelnianie (MFA!)
 9. Ograniczenie dostępu fizycznego
Monitoruj i testuj
 10. Logowanie i monitorowanie dostępu do danych/sieci
 11. Regularne testy bezpieczeństwa (skany ASV, pentesty)
Polityka
 12. Polityka bezpieczeństwa informacji
```

## Nowości v4.0
```text
- MFA dla WSZYSTKICH dostępów do CDE (nie tylko zdalnych/admin).
- Customized Approach – alternatywne spełnienie celu (obok Defined Approach).
- Więcej wymagań "as-a-BAU" (ciągłe, nie tylko roczne).
- Ochrona przed phishingiem, zarządzanie skryptami w przeglądarce (płatności), TLS wymogi.
```

## Zakres i walidacja
```text
Scope    – CDE (Cardholder Data Environment) + systemy połączone; segmentacja zmniejsza zakres.
Walidacja: SAQ (self-assessment) lub RoC przez QSA; skany ASV kwartalnie; pentest rocznie.
Poziomy 1-4 wg wolumenu transakcji.
```

## Praktyka
- **Zmniejsz zakres** (tokenizacja, segmentacja, outsourcing do PCI-compliant providera) — mniej CDE = mniej wymagań.
- Nigdy nie przechowuj pełnych danych uwierzytelniających (CVV, PIN, track).

## Źródła
- [PCI SSC – DSS v4.0](https://www.pcisecuritystandards.org/)
