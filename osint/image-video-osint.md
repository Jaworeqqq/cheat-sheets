---
title: "Image & video OSINT"
category: "osint"
tags: ["osint", "image", "video", "verification"]
platform: "agnostic"
mitre: ["T1592"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# Image & video OSINT

## TL;DR
Extracting intelligence from images and videos: reverse search to find the source/other copies, metadata for device/location/time, and visual analysis to geolocate or verify authenticity. Core skill for investigations, verification, and physical recon.

## Reverse image search
```text
- Google Images, Yandex (often best for faces/places), Bing Visual Search, TinEye.
- Find: original source, other appearances, date first seen, manipulated versions.
- Crop/zoom to search specific elements (a sign, a face, a landmark).
```

## Metadata
```text
- EXIF: camera/phone model, timestamp, sometimes GPS (see osint/metadata-exif).
- Note: most social platforms STRIP EXIF on upload — absence isn't proof of anything.
- Video containers carry metadata too (creation time, device, software).
```

## Visual analysis / geolocation
```text
- Geolocate via landmarks, signage/language, architecture, vegetation, sun position
  (chronolocation) — see osint/geolocation.
- Reflections, screens, badges, license plates reveal context.
- Frame-by-frame video analysis; extract keyframes for reverse search.
```

## Verification (is it real / when / where)
```text
- Corroborate with multiple independent clues; beware recycled/old media reposted as new.
- Cross-reference weather/shadows with claimed date/time.
- Check for manipulation: inconsistencies, error-level analysis, and — increasingly —
  AI-generated/deepfake indicators (artifacts, provenance tools like C2PA/Content Credentials).
```

## Tools
```text
- InVID/WeVerify (video verification, keyframes, reverse search), Forensically (image analysis),
  ExifTool, Google Earth/Street View, Yandex, C2PA verifiers for provenance.
```

## Detection / defense (Blue Team)
- Strip metadata before publishing; be aware background details leak locations/identities.
- For orgs: monitor for leaked internal photos (screens, whiteboards, facilities).

## Sources
- [Bellingcat](https://www.bellingcat.com/) · [InVID/WeVerify](https://www.invid-project.eu/) · related: [geolocation](./geolocation.md), [metadata-exif](./metadata-exif.md)
