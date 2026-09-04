# ADR-0045: Mercado Pago as first Brazilian billing adapter

Status: proposed — 2026-08-01

## Context and decision

Use Mercado Pago first for Brazil behind the neutral port, conditional on merchant, tax, webhook-mode, certification and contract review. Stripe-first and building payments were alternatives.

## Consequences and validation

Local methods/retries are beneficial; provider semantics and signature modes add risk. Sandbox contract tests and finance/legal/security approval are mandatory before credentials or production.
