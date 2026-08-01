# ADR-0058: Cloud Storage for execution artifacts

Status: accepted — 2026-08-01

## Context and decision

Large/binary artifacts live in Cloud Storage; PostgreSQL stores tenant-scoped metadata, checksum, class, retention and object reference. PostgreSQL blobs and public object URLs were rejected.

## Consequences and validation

Adds lifecycle/access coordination. Verify signed/scoped access, deletion, integrity, malware/content controls and orphan reconciliation.
