---
title: "GDPR / RODO – podstawy"
category: "compliance"
tags: ["compliance", "gdpr", "rodo", "privacy"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# GDPR / RODO

## TL;DR
Rozporządzenie UE o ochronie danych osobowych. Dotyczy każdego przetwarzającego dane osób w UE. Kary do 20 mln € lub 4% globalnego obrotu. Bezpieczeństwo to art. 32; zgłaszanie naruszeń w 72h.

## Kluczowe zasady (art. 5)
```text
- Zgodność z prawem, rzetelność, przejrzystość
- Ograniczenie celu               - Minimalizacja danych
- Prawidłowość                    - Ograniczenie przechowywania
- Integralność i poufność (security)  - Rozliczalność (accountability)
```

## Podstawy prawne przetwarzania (art. 6)
```text
zgoda · umowa · obowiązek prawny · żywotne interesy · zadanie publiczne · uzasadniony interes
```

## Prawa podmiotu danych
```text
dostęp · sprostowanie · usunięcie ("prawo do bycia zapomnianym") ·
ograniczenie · przenoszalność · sprzeciw · brak zautomatyzowanych decyzji
```

## Bezpieczeństwo (art. 32) – „odpowiednie środki"
```text
- Pseudonimizacja i szyfrowanie
- Poufność, integralność, dostępność, odporność systemów
- Zdolność szybkiego przywrócenia po incydencie
- Regularne testowanie skuteczności środków
```

## Naruszenia (art. 33/34)
```text
- Zgłoszenie do organu nadzorczego (UODO w PL) w ciągu 72h od wykrycia.
- Powiadomienie osób, jeśli wysokie ryzyko dla ich praw.
- Rejestr naruszeń (nawet niezgłaszanych).
```

## Praktyka dla zespołów tech
- Data mapping (RoPA – rejestr czynności), DPIA dla ryzykownego przetwarzania.
- Privacy by design/default, minimalizacja, retencja, DLP, szyfrowanie, kontrola dostępu.
- Umowy powierzenia (DPA) z procesorami, transfery poza EOG (SCC).

## Źródła
- [Tekst RODO (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [UODO](https://uodo.gov.pl/)
