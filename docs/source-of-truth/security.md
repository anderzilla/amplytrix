# Security

Deny by default; minimize and redact data; validate every external input; isolate tenants; scope tools; require approval for sensitive writes. Test SQL/command/template/header/log/LDAP injection, traversal, XSS, SSRF, unsafe deserialization, mass assignment, prompt/indirect/tool injection, context/memory/retrieval poisoning, exfiltration and excessive agency. BLOCKER/CRITICAL/HIGH findings block homologation. See ADR-0018, ADR-0020 and threat models.
