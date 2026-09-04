---
name: python-type-safety
description: Enforce or review strict Pyright type safety in Amplytrix Python, including Protocols, generics, unknowns, Optional, overrides, and justified exceptions.
---

# Python type safety

Run Pyright strict and trace unknown/Any to the boundary. Add concrete annotations, Protocols and generic variance that express real contracts; narrow external untyped data with validation/cast at adapters. Do not silence globally or use Any to appease the checker. Any suppression is diagnostic-specific, local, explained and tracked if temporary. Re-run tests because types do not prove runtime validation.
