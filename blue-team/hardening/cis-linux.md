---
title: "Linux hardening (CIS)"
category: "blue-team"
tags: ["hardening", "linux", "cis"]
platform: "linux"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Linux hardening (CIS baseline)

## TL;DR
Reduce the attack surface per the CIS Benchmark: minimize services, permissions, auditing, SSH, kernel params. Automate (Ansible/lynis) and verify.

## Quick audit
```bash
lynis audit system            # assessment + recommendations
# or the official CIS-CAT
```

## Key areas
```bash
# Accounts and passwords
awk -F: '($3==0){print}' /etc/passwd     # only root has uid 0?
chage --list <user>                       # expiration policy

# SSH (/etc/ssh/sshd_config)
PermitRootLogin no
PasswordAuthentication no        # keys only
Protocol 2
MaxAuthTries 4
AllowUsers ...                   # allow-list

# Firewall
ufw default deny incoming; ufw enable
# or nftables/firewalld – deny by default

# Kernel (sysctl)
net.ipv4.conf.all.rp_filter=1
net.ipv4.tcp_syncookies=1
kernel.randomize_va_space=2      # ASLR
fs.suid_dumpable=0

# Mounts
/tmp, /var/tmp  -> nodev,nosuid,noexec
```

## Auditing and logs
```bash
# auditd – log changes to sensitive files
auditctl -w /etc/passwd -p wa -k identity
auditctl -w /etc/sudoers -p wa -k scope
systemctl enable --now auditd
```

## Verification / maintenance
- Baseline (AIDE) on key files, regular `lynis`, patch management.
- IaC (Ansible role: dev-sec.linux-baseline) instead of manual work.

## Sources
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [Lynis](https://cisofy.com/lynis/) · [dev-sec hardening](https://github.com/dev-sec)
