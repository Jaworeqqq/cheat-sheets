---
title: "Risk assessment and management"
category: "compliance"
tags: ["risk-management", "grc"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Risk management

## TL;DR
Risk = likelihood × impact. Process: identify → analyze → evaluate → treat → monitor. Basis of ISO 27005 / NIST 800-30. It drives the choice of controls (not the other way around).

## Process (ISO 27005)
```text
1. Establish context      – scope, risk acceptance criteria
2. Identification         – assets, threats, vulnerabilities, impacts
3. Analysis               – likelihood × impact (qualitative/quantitative)
4. Evaluation             – compare against risk appetite
5. Treatment              – reduce / transfer / avoid / accept
6. Monitoring and review  – risk register, KRIs, reassessment
```

## Risk matrix (5×5)
```text
Impact →       Low   Med   High   Critical
Likelihood ↓
Very high        M    H     C        C
High             L    M     H        C
Medium           L    M     M        H
Low              L    L     M        H
(L=low, M=medium, H=high, C=critical -> action priority)
```

## Treatment options
```text
Reduce (mitigate) – implement a control (most common)
Transfer          – insurance, outsourcing
Avoid             – drop the risky activity
Accept            – deliberately, with the risk owner's sign-off (residual risk)
```

## Risk register (fields)
```text
ID · description · asset · threat/vulnerability · likelihood · impact ·
inherent risk · control · residual risk · owner · status · due date
```

## Quantitative (optional)
- **ALE = SLE × ARO** (Annual Loss Expectancy = Single Loss Expectancy × Annual Rate of Occurrence). Justifies control budget (control cost < ALE reduction).

## Sources
- [NIST SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [ISO 27005](https://www.iso.org/standard/80585.html) · [FAIR](https://www.fairinstitute.org/)
