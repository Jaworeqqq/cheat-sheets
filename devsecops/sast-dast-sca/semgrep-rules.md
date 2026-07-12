---
title: "Semgrep – writing custom rules"
category: "devsecops"
tags: ["sast", "semgrep", "rules"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Semgrep – writing custom rules

## TL;DR
Semgrep matches code patterns that look like the source (not regex). Great for custom org rules: banned functions, insecure patterns, taint from source to sink. Rules are YAML; fast, CI-friendly, low false positives when scoped well.

## Run
```bash
semgrep --config auto .                 # community + language rules
semgrep --config p/owasp-top-ten .
semgrep --config ./rules/ .             # your custom rules
semgrep ci                              # diff-aware (only new findings) for CI
```

## Basic rule (pattern match)
```yaml
rules:
  - id: dangerous-exec
    languages: [python]
    severity: ERROR
    message: "os.system with a variable can lead to command injection"
    patterns:
      - pattern: os.system($X)
      - pattern-not: os.system("...")     # allow string literals
```

## Taint mode (source -> sink)
```yaml
rules:
  - id: sql-injection-taint
    languages: [python]
    severity: ERROR
    message: "User input flows into a raw SQL query"
    mode: taint
    pattern-sources:
      - pattern: request.$ANY
    pattern-sinks:
      - pattern: cursor.execute($QUERY)
    pattern-sanitizers:
      - pattern: sanitize(...)
```

## Useful pattern operators
```text
pattern / patterns        – match / AND of conditions
pattern-either            – OR
pattern-not               – exclude
pattern-inside            – only within a context (e.g. inside a function)
metavariables ($X, $ANY)  – capture and correlate across the rule
mode: taint               – dataflow from sources to sinks with sanitizers
```

## Best practices
```text
- Scope tightly (pattern-inside/pattern-not) to keep false positives low.
- Test rules with `semgrep --test` (pass/fail annotated fixtures).
- Use `semgrep ci` for diff-aware gating (block new issues, don't drown in backlog).
- Version rules in git; share via Semgrep Registry; map to CWE/OWASP in metadata.
```

## Detection (Blue Team / AppSec)
- Enforce in PR checks; surface findings as SARIF into one dashboard with DAST/SCA.

## Sources
- [Semgrep docs](https://semgrep.dev/docs/) · [Rule syntax](https://semgrep.dev/docs/writing-rules/rule-syntax/) · related: [sast-dast-sca](./sast-dast-sca.md)
