---
title: "SSTI defense (secure templating)"
category: "appsec"
tags: ["owasp", "ssti", "injection", "defense"]
platform: "web"
mitre: []
difficulty: "intermediate"
updated: "2026-07-13"
author: "core"
---

# SSTI defense (secure templating)

## TL;DR
Server-Side Template Injection leads to RCE when user input is treated as template code. The defense is architectural: never let untrusted input become part of the template — pass it as data to a pre-defined template, and sandbox the engine. (Attack side: [red-team/web/ssti](../../red-team/web/ssti.md).)

## Root cause
```text
Vulnerable: render_template_string("Hello " + user_input)   # input becomes template CODE
Safe:       render_template("hello.html", name=user_input)  # input is DATA passed to a fixed template
The bug is concatenating/using user input as the template itself, not as a variable within it.
```

## Defenses (in order of strength)
```text
1. Don't build templates from user input. Use static templates + pass data as context variables.
2. If users MUST supply templates (rare), use a logic-less / sandboxed engine:
   - Logic-less: Mustache (no code execution by design).
   - Sandboxed: Jinja2 SandboxedEnvironment, etc. — but sandboxes have escapes; defense-in-depth only.
3. Input validation/allow-listing where a limited templating subset is truly needed.
4. Run the renderer with least privilege / in an isolated process (limit blast radius of a bypass).
```

## Framework guidance
```text
Jinja2 (Python) – use render_template with context; if user templates unavoidable, SandboxedEnvironment.
Twig (PHP)      – sandbox mode with an allow-list of tags/filters/functions.
Freemarker/Velocity (Java) – restrict/deny dangerous built-ins (e.g. Execute); newer secure configs.
General         – disable dangerous features; keep the engine updated.
```

## Detection (Blue Team)
- WAF/logs: template markers in input reaching render paths; sandbox-escape indicators;
  unexpected process spawns from the app. (See the attack sheet for signatures.)

## Testing your defense
- Attempt the standard SSTI probes ({{7*7}}, ${7*7}) against inputs — they must render literally, not evaluate.

## Sources
- [OWASP – SSTI / Injection](https://owasp.org/Top10/A03_2021-Injection/) · [PortSwigger – SSTI](https://portswigger.net/web-security/server-side-template-injection) · related: [ssti (attack)](../../red-team/web/ssti.md), [input-validation](../secure-coding/input-validation.md)
