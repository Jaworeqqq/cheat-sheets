---
title: "SAST / DAST / SCA – przegląd"
category: "devsecops"
tags: ["sast", "dast", "sca", "appsec"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# SAST / DAST / SCA

## TL;DR
Trzy komplementarne rodzaje testów: **SAST** analizuje kod (white-box, wcześnie), **DAST** testuje działającą aplikację (black-box), **SCA** sprawdza zależności/CVE. Wpinaj wszystkie w pipeline.

## Porównanie
| Typ | Co | Kiedy | Mocne / Słabe |
|-----|-----|-------|---------------|
| SAST | kod źródłowy | commit/PR | wcześnie, ale FP; nie widzi runtime |
| DAST | działająca app | staging | realne podatności; wolne, wymaga env |
| SCA | zależności/SBOM | commit + ciągle | znane CVE; nie łapie własnych bugów |
| IAST | instrumentacja w runtime | test | dokładne, ale złożone |

## SAST
```bash
semgrep --config auto .                # szybki, reguły community
semgrep --config p/owasp-top-ten .
# CodeQL (GitHub) – głęboka analiza dataflow
codeql database create db --language=javascript
codeql database analyze db --format=sarif-latest -o results.sarif
```

## DAST
```bash
# OWASP ZAP – baseline (pasywny) i full scan
zap-baseline.py -t https://staging.example.com -r report.html
# Nuclei – szablonowe podatności/misconfig
nuclei -u https://staging.example.com -t cves/ -t misconfiguration/
```

## SCA
```bash
trivy fs --scanners vuln,license .
grype dir:.
osv-scanner --lockfile package-lock.json
npm audit --production
```

## Integracja (fail policy)
```yaml
# CI: raportuj wszystko, blokuj tylko High/Critical + nowe (diff-aware)
- run: semgrep ci            # porównuje z baseline, tylko nowe findingi
```

## Dobre praktyki
- **Diff-aware** (blokuj nowe, nie zalej dewelopera długiem), triage FP, SARIF do jednego widoku.
- SBOM z SCA (patrz supply-chain), gate na severity + reachability.

## Źródła
- [Semgrep](https://semgrep.dev/) · [OWASP ZAP](https://www.zaproxy.org/) · [OSV-Scanner](https://github.com/google/osv-scanner)
