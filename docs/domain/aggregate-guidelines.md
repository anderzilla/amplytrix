# Aggregate guidelines

Start from an invariant and consistency boundary, not a table. Keep aggregates small; one root controls mutation; reference other aggregates by typed identity; enforce invariants synchronously; publish past-tense domain events after state change; use an aggregate-specific repository; avoid cross-aggregate transactions unless the invariant proves necessity. Pydantic, SQLAlchemy and provider SDK types cannot enter an aggregate. Concurrency strategy and transaction owner are part of design review.
