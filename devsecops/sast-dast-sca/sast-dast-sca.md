---
title: "SAST / DAST / SCA – overview"
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
Three complementary kinds of testing: **SAST** analyzes code (white-box, early), **DAST** tests the running app (black-box), **SCA** checks dependencies/CVEs. Wire all three into the pipeline.

## Comparison
| Type | What | When | Strengths / Weaknesses |
|------|------|------|------------------------|
| SAST | source code | commit/PR | early, but FPs; blind to runtime |
| DAST | running app | staging | real vulns; slow, needs an env |
| SCA | dependencies/SBOM | commit + continuous | known CVEs; misses your own bugs |
| IAST | runtime instrumentation | test | accurate, but complex |

## SAST
```bash
semgrep --config auto .                # fast, community rules
semgrep --config p/owasp-top-ten .
# CodeQL (GitHub) – deep dataflow analysis
codeql database create db --language=javascript
codeql database analyze db --format=sarif-latest -o results.sarif
```

## DAST
```bash
# OWASP ZAP – baseline (passive) and full scan
zap-baseline.py -t https://staging.example.com -r report.html
# Nuclei – templated vulns/misconfig
nuclei -u https://staging.example.com -t cves/ -t misconfiguration/
```

## SCA
```bash
trivy fs --scanners vuln,license .
grype dir:.
osv-scanner --lockfile package-lock.json
npm audit --production
```

## Integration (fail policy)
```yaml
# CI: report everything, block only High/Critical + new (diff-aware)
- run: semgrep ci            # compares against baseline, only new findings
```

## Best practices
- **Diff-aware** (block new, don't drown the developer in debt), triage FPs, SARIF into one view.
- SBOM from SCA (see supply-chain), gate on severity + reachability.

## Sources
- [Semgrep](https://semgrep.dev/) · [OWASP ZAP](https://www.zaproxy.org/) · [OSV-Scanner](https://github.com/google/osv-scanner)
