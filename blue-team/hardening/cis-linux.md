---
title: "Hardening Linux (CIS)"
category: "blue-team"
tags: ["hardening", "linux", "cis"]
platform: "linux"
mitre: []
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# Hardening Linux (CIS baseline)

## TL;DR
Redukcja powierzchni ataku wg CIS Benchmark: minimalizacja usług, uprawnienia, audyt, SSH, kernel params. Automatyzuj (Ansible/lynis) i weryfikuj.

## Szybki audyt
```bash
lynis audit system            # ocena + rekomendacje
# lub oficjalny CIS-CAT
```

## Kluczowe obszary
```bash
# Konta i hasła
awk -F: '($3==0){print}' /etc/passwd     # tylko root ma uid 0?
chage --list <user>                       # polityka wygasania

# SSH (/etc/ssh/sshd_config)
PermitRootLogin no
PasswordAuthentication no        # tylko klucze
Protocol 2
MaxAuthTries 4
AllowUsers ...                   # allow-list

# Firewall
ufw default deny incoming; ufw enable
# lub nftables/firewalld – domyślnie deny

# Kernel (sysctl)
net.ipv4.conf.all.rp_filter=1
net.ipv4.tcp_syncookies=1
kernel.randomize_va_space=2      # ASLR
fs.suid_dumpable=0

# Montowania
/tmp, /var/tmp  -> nodev,nosuid,noexec
```

## Audyt i logi
```bash
# auditd – rejestruj zmiany wrażliwych plików
auditctl -w /etc/passwd -p wa -k identity
auditctl -w /etc/sudoers -p wa -k scope
systemctl enable --now auditd
```

## Weryfikacja / utrzymanie
- Baseline (AIDE) na kluczowe pliki, regularne `lynis`, patch management.
- IaC (Ansible role: dev-sec.linux-baseline) zamiast ręcznie.

## Źródła
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [Lynis](https://cisofy.com/lynis/) · [dev-sec hardening](https://github.com/dev-sec)
