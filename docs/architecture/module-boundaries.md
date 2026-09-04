# Module boundaries

Candidate contexts and classifications live in `docs/domain/bounded-contexts.md`. An accepted Python module owns `domain`, `application`, `infrastructure`, and `presentation`; it exposes published application/contracts only and cannot query another context's tables or import internals. Cross-context transactions are avoided; initial in-process events may later map to an outbox. FastAPI and web never bypass application use cases.
