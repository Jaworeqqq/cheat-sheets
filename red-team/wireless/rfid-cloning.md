---
title: "RFID / NFC badge cloning"
category: "red-team"
tags: ["wireless", "rfid", "nfc", "physical"]
platform: "agnostic"
mitre: ["T1200"]
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# RFID / NFC badge cloning

## TL;DR
Many physical access badges use weak or cloneable RFID/NFC tech. In authorized physical/red-team engagements, an attacker reads a badge (often from a short distance) and clones it to gain building access. Low-frequency 125 kHz proximity cards are especially trivial to clone.

## Card technologies (weak -> strong)
```text
125 kHz LF (HID Prox, EM4100, Indala) – no crypto; trivially cloneable. Very common (legacy).
13.56 MHz HF (MIFARE Classic)         – broken crypto (Crypto-1); keys crackable.
13.56 MHz (MIFARE DESFire EV2/EV3, iCLASS SE, SEOS) – strong crypto; the secure choice.
```

## Tools
```text
Proxmark3        – the standard RFID research/attack tool (read/clone/emulate LF+HF).
Flipper Zero     – convenient LF/HF/NFC read/emulate (great for demos/awareness).
Long-range reader – covert readers can capture LF cards from a distance (weaponized readers).
```

## Cloning workflow (LF prox, lab/authorized)
```bash
# Proxmark3
lf search                 # identify the card type
lf hid read               # read a HID Prox card (get the ID)
lf hid clone -r <ID>      # write to a T5577 blank -> a working clone
# HF MIFARE Classic
hf mf autopwn             # crack keys + dump, then clone to a magic card
```

## Engagement context
```text
- Tailgating + a covert reader to capture a badge in a queue/elevator.
- Clone to a blank/magic card or emulate with Proxmark/Flipper at the door.
- Pair with physical recon (badge design/OSINT) and social engineering.
```

## Detection (Blue Team / physical security)
- Access-control logs: same badge used at improbable times/places (impossible travel, physical).
- Anti-passback violations; tailgating on cameras; unexpected door reads.

## Mitigation / Hardening
- Migrate off 125 kHz prox and MIFARE Classic to **DESFire EV3 / SEOS / iCLASS SE** (strong crypto).
- Mutual authentication + rotating keys; consider mobile credentials (phone + biometric).
- Anti-passback, tailgating detection, mantraps, camera coverage; badge + PIN/biometric for sensitive areas.
- Security awareness (don't let people tailgate; shield badges).

## Sources
- [Proxmark3](https://github.com/RfidResearchGroup/proxmark3) · [MITRE T1200](https://attack.mitre.org/techniques/T1200/)
