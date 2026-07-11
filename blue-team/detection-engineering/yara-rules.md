---
title: "YARA – rules for malware"
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
YARA classifies files by patterns (strings, bytes, conditions). Used to detect malware on disk/in memory and for threat hunting.

## Structure
```yara
rule SuspiciousWebshell_PHP
{
    meta:
        author = "core"
        description = "Simple PHP webshell"
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

## Running
```bash
yara -r rules.yar /var/www/          # recursively over a directory
yara -s rule.yar sample.bin          # show matched strings
yara rule.yar -p 4 --scan-list files.txt
# scan process memory
yara rule.yar --scan-list <(ls /proc/<pid>/)
```

## Best practices
```text
- Combine strings + conditions (filesize, magic) to reduce FPs.
- Use the pe/elf/math (entropy) module for packed samples.
- Don't rely on a single string — easy to bypass.
```

## Sources
- [YARA docs](https://yara.readthedocs.io/) · [YARA-Rules repo](https://github.com/Yara-Rules/rules)
