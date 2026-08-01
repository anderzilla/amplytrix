# ADR-0015: Risk-based test portfolio

Status: accepted — 2026-08-01

Use Vitest/unit and architecture tests now; add Testing Library, Playwright, Testcontainers, accessibility and security tests with relevant surfaces. Pact waits for independent consumers; k6 waits for real flows. Coverage thresholds grow per critical module, not a blanket 100%.
