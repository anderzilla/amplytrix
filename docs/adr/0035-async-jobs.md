# ADR-0035: Asynchronous jobs strategy

Status: proposed — 2026-08-01

Prefer Cloud Tasks for bounded HTTP work and Cloud Run Jobs for finite administrative/batch work. Use Pub/Sub for fan-out events only when needed. Do not adopt Celery/Dramatiq/ARQ until retries, scheduling or local portability outweigh managed-service operations. Every job needs idempotency, timeout, DLQ/failure handling, audit and cost bounds.
