---
title: "Linux auditd"
category: "blue-team"
tags: ["logging", "linux", "auditd", "detection"]
platform: "linux"
mitre: []
difficulty: "intermediate"
updated: "2026-07-12"
author: "core"
---

# Linux auditd

## TL;DR
The Linux Audit daemon records security-relevant events at the kernel level: syscalls, file access, command execution, auth. The Linux equivalent of rich Windows/Sysmon telemetry — essential for detection and DFIR. Rules make or break its value.

## Basics
```bash
systemctl enable --now auditd
auditctl -l                     # list active rules
ausearch -k <key> -ts today     # search by rule key
aureport --summary              # summary report
auditctl -s                     # status (backlog, lost events)
```

## Rule types
```text
Watch rules  – file/dir access:   -w <path> -p <rwxa> -k <key>
Syscall rules – syscalls:         -a always,exit -F arch=b64 -S <syscall> -k <key>
```

## High-value rules (/etc/audit/rules.d/*.rules)
```bash
# Identity & privilege files
-w /etc/passwd -p wa -k identity
-w /etc/sudoers -p wa -k priv_esc
-w /etc/ssh/sshd_config -p wa -k sshd

# Command execution (execve) — powerful, high volume; tune carefully
-a always,exit -F arch=b64 -S execve -k exec

# Suspicious: changing file capabilities / mounts / loading kernel modules
-a always,exit -F arch=b64 -S init_module -S finit_module -k modules
-w /sbin/insmod -p x -k modules

# Access to sensitive dirs / credential theft
-w /root/.ssh -p rwa -k root_ssh
-w /etc/shadow -p rwa -k shadow
```

## Detection use cases
```text
- Privilege escalation: writes to /etc/sudoers, use of setuid, capability changes.
- Persistence: cron/systemd/rc modifications, new SSH keys.
- Credential access: reads of /etc/shadow, ssh keys.
- Defense evasion: audit config tampering, log deletion.
- Map rules to ATT&CK; ship logs to a SIEM (auditd -> syslog/journald -> collector).
```

## Best practices
```text
- Start from a maintained ruleset (Neo23x0/auditd, or CIS-aligned) then tune.
- execve rules are high-volume — filter noise, watch the backlog (lost events = gaps).
- Make rules immutable in prod: end rules with `-e 2` (requires reboot to change).
- Centralize logs; correlate with Sysmon-for-Linux where deployed.
```

## Sources
- [Neo23x0 auditd ruleset](https://github.com/Neo23x0/auditd) · [RHEL Audit docs](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/) · related: [cis-linux](../hardening/cis-linux.md)
