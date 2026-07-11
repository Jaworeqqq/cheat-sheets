---
title: "NIST CSF 2.0"
category: "compliance"
tags: ["compliance", "nist", "csf"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# NIST Cybersecurity Framework 2.0

## TL;DR
Dobrowolny, elastyczny framework zarządzania ryzykiem cyber. Wersja 2.0 (2024) dodała funkcję **GOVERN** i rozszerzyła zakres poza infrastrukturę krytyczną na wszystkie organizacje.

## 6 funkcji (Core)
```text
GOVERN (GV)   – strategia, role/odpowiedzialności, polityki, zarządzanie ryzykiem, nadzór łańcucha dostaw
IDENTIFY (ID) – zasoby, ryzyka, kontekst biznesowy
PROTECT (PR)  – kontrola dostępu, świadomość, bezpieczeństwo danych, konfiguracja, hardening
DETECT (DE)   – ciągłe monitorowanie, analiza zdarzeń
RESPOND (RS)  – zarządzanie incydentem, analiza, komunikacja, mitygacja
RECOVER (RC)  – plan odtworzenia, przywracanie, komunikacja
```

## Elementy
```text
Core        – funkcje > kategorie > podkategorie (konkretne wyniki)
Profiles    – Current vs Target (gap analysis -> plan)
Tiers (1-4) – dojrzałość: Partial -> Risk Informed -> Repeatable -> Adaptive
```

## Jak używać
```text
1. Ustal Target Profile (gdzie chcemy być, wg ryzyka biznesowego).
2. Oceń Current Profile (gdzie jesteśmy).
3. Gap analysis -> plan działań z priorytetami.
4. Mierz postęp, iteruj.
```

## Mapowania
- CSF mapuje się na 800-53, ISO 27001, CIS Controls — użyj Informative References do crosswalku.

## Źródła
- [NIST CSF 2.0](https://www.nist.gov/cyberframework) · [CSF 2.0 Reference Tool](https://csrc.nist.gov/projects/cybersecurity-framework/filters)
