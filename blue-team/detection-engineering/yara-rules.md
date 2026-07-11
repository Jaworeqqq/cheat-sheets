---
title: "YARA – reguły dla malware"
category: "blue-team"
tags: ["detection-engineering", "yara", "malware"]
platform: "agnostic"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# YARA

## TL;DR
YARA klasyfikuje pliki wg wzorców (stringi, bajty, warunki). Używane do wykrywania malware na dysku/w pamięci i threat huntingu.

## Struktura
```yara
rule SuspiciousWebshell_PHP
{
    meta:
        author = "core"
        description = "Prosty PHP webshell"
        reference = "internal"
        severity = "high"
    strings:
        $a = "system($_GET" nocase
        $b = "eval(base64_decode(" nocase
        $c = /passthru\s*\(\$_(GET|POST|REQUEST)/ nocase
    condition:
        filesize < 50KB and any of them
}
```

## Uruchamianie
```bash
yara -r rules.yar /var/www/          # rekurencyjnie po katalogu
yara -s rule.yar sample.bin          # pokaż dopasowane stringi
yara rule.yar -p 4 --scan-list files.txt
# skan pamięci procesu
yara rule.yar --scan-list <(ls /proc/<pid>/)
```

## Dobre praktyki
```text
- Łącz stringi + warunki (filesize, magic) by ograniczyć FP.
- Używaj modułu pe/elf/math (entropia) dla pakowanych próbek.
- Nie opieraj się na 1 stringu — łatwo obejść.
```

## Źródła
- [YARA docs](https://yara.readthedocs.io/) · [YARA-Rules repo](https://github.com/Yara-Rules/rules)
