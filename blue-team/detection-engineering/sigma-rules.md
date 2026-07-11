---
title: "Sigma – detection as code"
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
Sigma is a universal, portable detection rule format (YAML). Write once, convert (`sigma`/`pySigma`) to SPL/KQL/EQL/Elastic. A common language for the blue team.

## Rule structure
```yaml
title: Potential Kerberoasting (RC4 TGS)
id: 0e1a2b3c-...
status: experimental
description: Detects TGS requests with RC4 encryption
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
    ServiceName|endswith: '$'      # skip machine accounts
  condition: selection and not filter
falsepositives:
  - Legacy services still on RC4
level: medium
tags:
  - attack.credential_access
  - attack.t1558.003
```

## Convert to a SIEM
```bash
# pySigma / sigma-cli
sigma convert -t splunk rule.yml
sigma convert -t 'microsoft365defender' rule.yml
sigma convert -t elasticsearch -f dsl rule.yml
```

## Best practices
```text
- Start from TTPs (ATT&CK), not IOCs (more durable detections).
- Always define falsepositives + level.
- Test against Atomic Red Team before production.
- Version rules in git (detection-as-code), review in PRs.
```

## Sources
- [SigmaHQ](https://github.com/SigmaHQ/sigma) · [pySigma](https://github.com/SigmaHQ/pySigma)
