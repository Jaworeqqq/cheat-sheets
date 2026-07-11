---
title: "Audyt – checklista dowodów"
category: "compliance"
tags: ["compliance", "audit", "evidence"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Audyt – gromadzenie dowodów

## TL;DR
Audytor weryfikuje, że kontrola jest **zaprojektowana** i **działa**. Dobry dowód: aktualny, kompletny, powtarzalny, powiązany z okresem audytu. Zbieraj ciągle, nie w noc przed audytem.

## Rodzaje dowodów
```text
- Polityki i procedury (zatwierdzone, wersjonowane, z datą przeglądu)
- Zrzuty konfiguracji (MFA on, szyfrowanie, retencja logów)
- Logi/zapisy (dostępy, zmiany, przeglądy) za cały okres audytu
- Tickety (change management, incydenty, dostęp) z akceptacjami
- Wyniki testów (skany podatności, pentesty, DR test, backup restore)
- Rejestry (ryzyk, aktywów, szkoleń, dostawców)
```

## Checklista wg obszaru
```text
Kontrola dostępu   – przegląd uprawnień (kwartalny), lista offboardingu, MFA enforcement
Change management  – tickety z approvalem, CI/CD logi, brak zmian bez zatwierdzenia
Logowanie/monitoring – retencja, alerty, próbki reakcji na alert
Kopie zapasowe     – harmonogram, log udanych backupów, dowód testu odtworzenia
Vuln management    – skany, SLA remediacji, dowód załatania krytycznych
Reakcja na incydent – runbooki, zapisy incydentów, post-mortem
Dostawcy           – DPA/umowy, przeglądy ryzyka, SOC 2 dostawców
HR/świadomość      – logi szkoleń, screening, NDA
```

## Dobre praktyki
- **Automatyzuj** zbieranie (Drata/Vanta/Secureframe lub własne skrypty + evidence store).
- Próbkowanie: audytor wybierze losowe przypadki — dowód musi obejmować cały okres.
- Powiąż każdy dowód z konkretną kontrolą (mapowanie kontrola → dowód).

## Źródła
- [AICPA SOC 2](https://www.aicpa-cima.com/) · [ISO 27001 Annex A](../frameworks/iso27001-annex-a.md)
