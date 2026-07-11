---
title: "Ocena i zarządzanie ryzykiem"
category: "compliance"
tags: ["risk-management", "grc"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Zarządzanie ryzykiem

## TL;DR
Ryzyko = prawdopodobieństwo × wpływ. Proces: identyfikuj → analizuj → oceń → potraktuj → monitoruj. Podstawa ISO 27005 / NIST 800-30. Napędza wybór kontroli (nie odwrotnie).

## Proces (ISO 27005)
```text
1. Ustalenie kontekstu     – zakres, kryteria akceptacji ryzyka
2. Identyfikacja           – aktywa, zagrożenia, podatności, skutki
3. Analiza                 – prawdopodobieństwo × wpływ (jakościowo/ilościowo)
4. Ewaluacja               – porównaj z apetytem na ryzyko
5. Postępowanie (treatment) – redukuj / przenieś / unikaj / akceptuj
6. Monitorowanie i przegląd – rejestr ryzyk, KRI, reasesment
```

## Macierz ryzyka (5×5)
```text
Wpływ →        Niski  Śr   Wysoki  Krytyczny
Prawd. ↓
Bardzo wysokie   M    W     K        K
Wysokie          N    M     W        K
Średnie          N    M     M        W
Niskie           N    N     M        W
(N=niskie, M=średnie, W=wysokie, K=krytyczne -> priorytet działań)
```

## Opcje postępowania
```text
Redukuj (mitigate) – wdróż kontrolę (najczęstsze)
Przenieś (transfer) – ubezpieczenie, outsourcing
Unikaj (avoid)      – zrezygnuj z ryzykownej działalności
Akceptuj (accept)   – świadomie, z podpisem właściciela ryzyka (residual risk)
```

## Rejestr ryzyk (pola)
```text
ID · opis · aktywo · zagrożenie/podatność · prawdopodobieństwo · wpływ ·
ryzyko inherentne · kontrola · ryzyko rezydualne · właściciel · status · termin
```

## Ilościowo (opcjonalnie)
- **ALE = SLE × ARO** (Annual Loss Expectancy = Single Loss Expectancy × Annual Rate of Occurrence). Uzasadnia budżet kontroli (koszt kontroli < redukcja ALE).

## Źródła
- [NIST SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [ISO 27005](https://www.iso.org/standard/80585.html) · [FAIR](https://www.fairinstitute.org/)
