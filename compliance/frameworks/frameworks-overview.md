---
title: "Frameworki bezpieczeństwa – przegląd"
category: "compliance"
tags: ["compliance", "frameworks", "grc"]
platform: "agnostic"
mitre: []
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Frameworki bezpieczeństwa – przegląd

## TL;DR
Ściąga porównawcza najważniejszych standardów: cel, obowiązkowość, komu potrzebny. Wiele kontroli się pokrywa — mapuj raz, spełniaj wiele (crosswalk).

## Porównanie
| Framework | Typ | Kogo dotyczy | Certyfikacja |
|-----------|-----|--------------|--------------|
| ISO/IEC 27001 | ISMS (system zarządzania) | dowolna org | tak, audyt zewnętrzny |
| SOC 2 | atestacja (Trust Services) | SaaS/usługodawcy (USA) | raport audytora (Type I/II) |
| NIST CSF 2.0 | dobrowolny framework | dowolna org | nie (samoocena) |
| NIST 800-53 | katalog kontroli | agencje federalne US + kontraktorzy | via FedRAMP/RMF |
| PCI DSS v4.0 | wymóg branżowy | przetwarzający karty płatnicze | tak (QSA/SAQ) |
| GDPR / RODO | prawo (UE) | przetwarzający dane osobowe UE | nie (zgodność prawna) |
| HIPAA | prawo (USA) | ochrona zdrowia (PHI) | nie (zgodność prawna) |
| CIS Controls v8 | zestaw kontroli (priorytetyzowany) | dowolna org | nie |

## NIST CSF 2.0 – funkcje
```text
GOVERN (nowe w 2.0) – nadzór, role, ryzyko, polityki
IDENTIFY – aktywa, ryzyka
PROTECT  – kontrole zapobiegawcze
DETECT   – wykrywanie zdarzeń
RESPOND  – reakcja na incydenty
RECOVER  – przywracanie
```

## Praktyka
- **Mapuj kontrole między standardami** (np. Secure Controls Framework, CIS crosswalk) — jedno wdrożenie, wiele zgodności.
- Zacznij od CIS Controls (praktyczne, priorytetyzowane), formalizuj przez ISO 27001.

## Powiązane
- [ISO 27001 Annex A](./iso27001-annex-a.md) · [NIST CSF](./nist-csf.md) · [PCI DSS](./pci-dss-v4.md)

## Źródła
- [NIST CSF](https://www.nist.gov/cyberframework) · [CIS Controls](https://www.cisecurity.org/controls) · [ISO 27001](https://www.iso.org/standard/27001)
