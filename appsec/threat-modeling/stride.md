---
title: "Threat Modeling – STRIDE"
category: "appsec"
tags: ["threat-modeling", "stride", "design"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Threat Modeling – STRIDE

## TL;DR
Strukturalne szukanie zagrożeń na etapie projektu. STRIDE = 6 kategorii zagrożeń, każda z przeciwstawną własnością bezpieczeństwa. Odpowiada na 4 pytania: co budujemy, co może pójść źle, co z tym zrobimy, czy dobrze zrobiliśmy.

## STRIDE
| Zagrożenie | Narusza | Przykład | Kontrola |
|-----------|---------|----------|----------|
| **S**poofing | Authentication | podszycie pod usera/usługę | MFA, mutual TLS, silne tożsamości |
| **T**ampering | Integrity | modyfikacja danych/kodu | podpisy, HMAC, walidacja, WORM |
| **R**epudiation | Non-repudiation | zaprzeczenie akcji | logi audytowe, timestamping |
| **I**nformation Disclosure | Confidentiality | wyciek danych | szyfrowanie, least privilege |
| **D**enial of Service | Availability | wyczerpanie zasobów | rate limit, quotas, autoscaling |
| **E**levation of Privilege | Authorization | privesc | authz, sandboxing, least priv |

## Proces
```text
1. Diagram (DFD)  – procesy, data stores, external entities, data flows, trust boundaries
2. Enumeracja     – dla każdego elementu/przepływu przejdź STRIDE
3. Ocena ryzyka   – prawdopodobieństwo x wpływ (lub DREAD)
4. Mitygacje      – kontrola per zagrożenie; zaakceptuj/przenieś/zredukuj
5. Weryfikacja    – testy potwierdzające kontrole
```

## Wskazówki
- Skup uwagę na **trust boundaries** (tam żyją zagrożenia).
- Rób wcześnie (design) i aktualizuj przy zmianach architektury.
- Narzędzia: Microsoft Threat Modeling Tool, OWASP Threat Dragon, pytania „elevation of privilege" (karty).

## Źródła
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) · [Threat Dragon](https://owasp.org/www-project-threat-dragon/) · książka *Threat Modeling* (Shostack)
