---
title: "ISO 27001:2022 – Annex A"
category: "compliance"
tags: ["compliance", "iso27001", "isms"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# ISO/IEC 27001:2022 – Annex A

## TL;DR
ISO 27001 to standard systemu zarządzania bezpieczeństwem informacji (ISMS). Annex A (z ISO 27002) to katalog **93 kontroli** w 4 tematach. Zgodność = ISMS + Statement of Applicability + ciągłe doskonalenie (PDCA).

## Struktura klauzul (4-10 = wymagania ISMS)
```text
4  Kontekst organizacji        5  Przywództwo
6  Planowanie (ryzyko!)        7  Wsparcie (zasoby, świadomość)
8  Działania operacyjne        9  Ocena wyników (audyt, przegląd)
10 Doskonalenie (CAPA)
```

## Annex A – 4 tematy (93 kontrole, wersja 2022)
| Temat | # kontroli | Przykłady |
|-------|-----------|-----------|
| A.5 Organizacyjne | 37 | polityki, role, dostawcy, threat intel*, incydenty |
| A.6 Ludzie | 8 | screening, świadomość, praca zdalna, NDA |
| A.7 Fizyczne | 14 | strefy, dostęp fizyczny, sprzęt, nośniki |
| A.8 Technologiczne | 34 | kontrola dostępu, krypto, logowanie, kopie, secure dev |

\* Nowości 2022: threat intelligence, ICT readiness for BC, physical monitoring, config management, information deletion, data masking, DLP, web filtering, secure coding, cloud services.

## Ścieżka do certyfikacji
```text
1. Zakres ISMS + kontekst
2. Ocena ryzyka + plan postępowania (risk treatment)
3. Statement of Applicability (SoA) – które kontrole i dlaczego
4. Wdrożenie kontroli + dowody
5. Audyt wewnętrzny + przegląd zarządzania
6. Audyt certyfikacyjny (Stage 1 dokumenty, Stage 2 wdrożenie)
7. Nadzór (surveillance) rocznie, recertyfikacja co 3 lata
```

## Praktyka
- SoA to serce — uzasadnij włączenie/wyłączenie każdej kontroli względem ryzyka.
- Dowody: polityki, logi, zapisy przeglądów, wyniki testów. Zobacz [evidence-checklist](../audit/evidence-checklist.md).

## Źródła
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) · [ISO 27002:2022 (kontrole)](https://www.iso.org/standard/75652.html)
