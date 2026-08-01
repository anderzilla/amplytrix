# ADR-0004: Modular monolith before microservices

Status: accepted — 2026-08-01

Keep bounded contexts in one API deployment with enforced module ownership. Microservices add network, consistency, observability, and cost burdens without team/load evidence. Extract only for independent ownership/release, isolation, or measured scaling, with ADR and contract/outbox plan.
