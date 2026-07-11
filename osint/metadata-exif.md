---
title: "Metadata & EXIF analysis"
category: "osint"
tags: ["osint", "metadata", "exif"]
platform: "agnostic"
mitre: ["T1592"]
difficulty: "basic"
updated: "2026-07-11"
author: "core"
---

# Metadata & EXIF

## TL;DR
Files leak metadata: photos (GPS, device, timestamps), documents (author, software, usernames, paths, revision history). Great for OSINT recon; a real data-leak risk for organizations.

## Extract metadata
```bash
# Images / general
exiftool photo.jpg                    # all metadata
exiftool -gpslatitude -gpslongitude photo.jpg
exiftool -r -ext jpg ./              # recurse a directory

# Documents (Office/PDF)
exiftool report.pdf                   # author, producer, dates
# PDF specifics
pdfinfo report.pdf
```

## What it reveals (recon value)
```text
Photos    – GPS coordinates, camera/phone model, capture time
Office    – author names (-> usernames/email format), template paths, company
PDF       – producing software (versions -> CVEs), creation tools
All       – internal paths (\\server\share\user\...), software versions
```

## Bulk org recon
```text
- Harvest public docs (site:example.com filetype:pdf|docx) -> exiftool -> usernames.
- FOCA / metagoofil automate download + metadata extraction across a domain.
```

## Detection / defense (Blue Team)
- Monitor published files for embedded metadata leaks (author, paths, versions).

## Mitigation / Hardening
- **Strip metadata before publishing** (exiftool -all=, Office "Inspect Document",
  server-side sanitization on upload/download).
- Policy + tooling in the publishing pipeline; scrub GPS from public images.

## Sources
- [ExifTool](https://exiftool.org/) · [metagoofil](https://github.com/laramies/metagoofil)
