---
name: aggregate-design
description: Design or review Amplytrix aggregates and roots around proven invariants, consistency boundaries, concurrency, and transaction ownership.
---

# Aggregate design

Start from command/scenario and invariant. Choose smallest consistency boundary/root; model value objects/entities only as needed; reference other aggregates by identity; specify valid transitions, concurrency strategy, events and aggregate-specific repository operations. Keep FastAPI/Pydantic/SQLAlchemy/provider types out. Test invariants without I/O. Complete with examples and explicit reasons for each abstraction.
