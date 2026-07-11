---
title: "Sigma – detekcja jako kod"
category: "blue-team"
tags: ["detection-engineering", "sigma", "siem"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Sigma Rules

## TL;DR
Sigma to uniwersalny, przenośny format reguł detekcji (YAML). Piszesz raz, konwertujesz (`sigma`/`pySigma`) do SPL/KQL/EQL/Elastic. Wspólny język blue teamu.

## Struktura reguły
```yaml
title: Potencjalny Kerberoasting (RC4 TGS)
id: 0e1a2b3c-...
status: experimental
description: Wykrywa żądania TGS z szyfrowaniem RC4
references:
  - https://attack.mitre.org/techniques/T1558/003/
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4769
    TicketEncryptionType: '0x17'
  filter:
    ServiceName|endswith: '$'      # pomiń konta maszynowe
  condition: selection and not filter
falsepositives:
  - Legacy usługi wciąż na RC4
level: medium
tags:
  - attack.credential_access
  - attack.t1558.003
```

## Konwersja do SIEM
```bash
# pySigma / sigma-cli
sigma convert -t splunk rule.yml
sigma convert -t 'microsoft365defender' rule.yml
sigma convert -t elasticsearch -f dsl rule.yml
```

## Dobre praktyki
```text
- Zaczynaj od TTP (ATT&CK), nie od IOC (trwalsze detekcje).
- Zawsze definiuj falsepositives + level.
- Testuj na Atomic Red Team przed produkcją.
- Wersjonuj reguły w gicie (detection-as-code), review w PR.
```

## Źródła
- [SigmaHQ](https://github.com/SigmaHQ/sigma) · [pySigma](https://github.com/SigmaHQ/pySigma)
