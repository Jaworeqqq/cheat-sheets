---
title: "Secure file upload (defensive)"
category: "appsec"
tags: ["secure-coding", "file-upload", "defense"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Secure file upload (defensive)

## TL;DR
The defensive counterpart to the file-upload attack sheet. Uploads are dangerous because they combine untrusted content, storage, and often execution. Defend in depth: validate, store safely, isolate execution, and scan. (Attack side: [red-team/web/file-upload](../../red-team/web/file-upload.md).)

## Validation (all server-side)
```text
- Allow-list extensions AND verify content (magic bytes) — don't trust the filename or Content-Type.
- Enforce max size + dimensions; reject archives/polyglots where not needed.
- Re-generate a random filename; strip the original name and path (no traversal).
- For images: re-encode/transcode server-side (destroys embedded payloads/polyglots).
```

## Safe storage
```text
- Store OUTSIDE the web root, or in object storage (S3/GCS/Blob) that never executes code.
- Serve via a separate domain/subdomain (isolate cookies/origin); set:
    Content-Disposition: attachment (for downloads)
    X-Content-Type-Options: nosniff
    a restrictive Content-Type (not attacker-controlled)
- Never let the upload dir have an interpreter handler (no PHP/CGI execution there).
```

## Execution isolation & scanning
```text
- Disable script execution in the upload path (server config / storage that can't execute).
- Antivirus/malware scanning (ClamAV, cloud scanning) on ingest.
- Process untrusted files in a sandbox (image/PDF conversion in an isolated worker).
- Rate limit + authenticate uploads; log them.
```

## Common bypasses to defend against
```text
- Double extensions (shell.jpg.php), case tricks (.pHp), null bytes, alternate exts (.phtml, .php5).
- MIME spoofing; magic-byte polyglots (GIF89a + PHP).
- .htaccess/web.config upload to change handler mappings.
- Path traversal in filename (../../).
-> Random rename + no-execute storage + content re-encode neutralizes most of these.
```

## Detection (Blue Team)
- Executable/script files in upload dirs; access to freshly uploaded files; AV hits; WAF web-shell signatures; FIM on upload storage.

## Sources
- [OWASP – File Upload CS](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) · related: [input-validation](./input-validation.md), [secure-headers](./secure-headers.md)
