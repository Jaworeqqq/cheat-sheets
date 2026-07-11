---
title: "IR Playbook – Ransomware"
category: "blue-team"
tags: ["incident-response", "ransomware", "playbook"]
platform: "agnostic"
mitre: ["T1486"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# IR Playbook – Ransomware

## TL;DR
Faza wg NIST 800-61: Przygotowanie → Wykrycie/Analiza → Zawężenie/Eradykacja/Odtworzenie → Wnioski. Przy ransomware: **izoluj szybko, nie płać pochopnie, zabezpiecz dowody**.

## 1. Wykrycie i triage
```text
Sygnały: masowe zmiany plików (.locked), note ransomowy, alert EDR, wyłączony backup/AV,
         nietypowe logowania, spike CPU (szyfrowanie).
Pierwsze pytania: pacjent zero? wektor wejścia? zasięg? czy trwa aktywne szyfrowanie?
```

## 2. Containment (zawężenie)
```text
- Izoluj zainfekowane hosty (odłącz sieć, NIE wyłączaj — zachowaj RAM na forensics).
- Zablokuj konta skompromitowane, zresetuj hasła (w tym krbtgt x2 jeśli AD).
- Odetnij kanały C2 (firewall/DNS sinkhole), wyłącz zdalny dostęp.
- Chroń kopie zapasowe (offline/immutable) przed skasowaniem.
```

## 3. Eradykacja i odtworzenie
```text
- Ustal i usuń mechanizmy persystencji, załataj wektor wejścia.
- Odtwarzaj z czystych, zweryfikowanych backupów (sprawdź czy nie zainfekowane).
- Odbuduj z zaufanych obrazów; nie ufaj „wyczyszczonym" hostom przy głębokim compromise.
```

## 4. Po incydencie
```text
- Timeline, root cause, lessons learned, aktualizacja detekcji (Sigma/EDR).
- Zgłoszenia regulacyjne (GDPR 72h jeśli dane osobowe), komunikacja.
```

## Zbieranie dowodów (przed czyszczeniem)
```bash
# Pamięć + dysk zanim zmodyfikujesz hosta
# (winpmem/DumpIt dla RAM; obraz dysku dd/FTK)
# Zachowaj: logi, próbki, notę ransomową, IOC
```

## Nie / Tak
- ❌ Nie wyłączaj hosta odruchowo (utrata RAM), nie płać bez analizy prawnej/biznesowej.
- ✅ Izoluj, zbierz dowody, angażuj prawników/ubezpieczyciela/organy wg polityki.

## Źródła
- [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) · [CISA #StopRansomware](https://www.cisa.gov/stopransomware)
