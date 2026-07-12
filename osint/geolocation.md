---
title: "Geolocation OSINT"
category: "osint"
tags: ["osint", "geolocation", "geoint"]
platform: "agnostic"
mitre: ["T1591.001"]
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Geolocation OSINT

## TL;DR
Determining where a photo/person/asset is located from open sources: image metadata, visual clues (chronolocation/geolocation), IP geodata, and mapping tools. Useful for physical recon in authorized engagements; a privacy risk to defend against.

## Image-based geolocation
```text
- EXIF GPS (if present) -> exact coordinates (exiftool; see osint/metadata-exif).
- Visual clues: signage/language, license plates, architecture, vegetation, sun position,
  business names, road markings, utility poles, mountains/skylines.
- Reverse image search: Google/Yandex/Bing Lens (Yandex often best for places/faces).
- Shadows + timestamp -> sun position -> approximate location/time (chronolocation).
```

## Tools
```bash
exiftool photo.jpg | grep -i gps          # embedded GPS
# Mapping/verification
# Google Earth, Google Street View, Mapillary, OpenStreetMap, SunCalc (sun position)
# GeoSpy / Picarta (AI location estimation), Overpass Turbo (query OSM features)
```

## IP & infrastructure geodata
```text
- IP geolocation (approximate; city-level at best; VPNs/proxies distort).
- WiFi BSSID lookups (WiGLE), cell tower databases.
- Shodan/Censys location data for exposed devices (see osint/shodan-dorks).
```

## Workflow (verify, don't guess)
```text
1. Extract hard data (EXIF GPS) if present.
2. Enumerate visual clues; form hypotheses (country -> region -> spot).
3. Reverse-image search + cross-reference on maps/Street View.
4. Confirm with multiple independent clues (never a single weak signal).
```

## Detection / defense (Blue Team)
- Strip GPS/EXIF before publishing; educate staff on background clues in photos (badges, screens, windows).

## Mitigation / Hardening
- Metadata scrubbing in publishing pipelines; policy on posting workplace photos.
- Awareness: uniforms, signage, and skylines can pinpoint facilities.
- Related: [metadata-exif](./metadata-exif.md), [social-media-osint](./social-media-osint.md).

## Sources
- [Bellingcat toolkit](https://www.bellingcat.com/) · [SunCalc](https://www.suncalc.org/)
