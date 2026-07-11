---
title: "Proces Incident Response (NIST)"
category: "blue-team"
tags: ["incident-response", "process", "nist"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Proces IR – NIST 800-61

## TL;DR
Cztery fazy: Preparation → Detection & Analysis → Containment/Eradication/Recovery → Post-Incident. SANS rozbija to na 6 (PICERL).

## Fazy
```text
1. Preparation      – narzędzia, runbooki, dostępy break-glass, kontakty, ćwiczenia
2. Detection&Analysis – triage alertów, scoping, klasyfikacja severity, timeline
3. Containment      – short-term (izolacja) + long-term (patch, tymczasowe kontrole)
   Eradication      – usuń malware/persystencję, załataj root cause
   Recovery         – przywróć usługi, monitoruj powrót atakującego
4. Post-Incident    – lessons learned, aktualizacja detekcji, raport
```

## Klasyfikacja severity (przykład)
| Sev | Kryterium | Reakcja |
|-----|-----------|---------|
| SEV1 | Krytyczne systemy / dane / aktywny atak | 24/7, escalacja natychmiast |
| SEV2 | Ograniczony zasięg, potencjał eskalacji | godziny |
| SEV3 | Pojedynczy host, niski wpływ | dzień roboczy |

## Zbieranie dowodów – kolejność ulotności (RFC 3227)
```text
1. Rejestry/cache CPU        2. RAM / tablice routingu / ARP
3. Procesy / połączenia sieciowe  4. Dysk       5. Logi zdalne / config    6. Nośniki archiwalne
```

## Dokumentacja (chain of custody)
- Kto, co, kiedy, skąd; hash każdego artefaktu; kolejne przekazania.

## Mitygacja / Hardening
- Regularne tabletop exercises, gotowe runbooki per scenariusz, przetestowane backupy.

## Źródła
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [SANS PICERL](https://www.sans.org/)
