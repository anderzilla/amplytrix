---
name: internationalization-review
description: Review pt-BR/en-US readiness, translation keys and locale-safe formatting.
---

# Internationalization review

Read `docs/source-of-truth/internationalization.md`. Search affected code/resources for hardcoded user text, missing/unused keys, manual date/number/currency formatting, unsafe fallbacks and technical leakage. Exercise `pt-BR` and `en-US` plus expansion. Report evidence/severity/fix; block locale-caused critical errors. Do not invent approved translations.
