# Agent catalog

Portable definitions live in `.codex/agents/`: Product Architect, Software Architect, Domain Modeler, Python Backend Engineer, Python Architecture Reviewer, Frontend Engineer, AI Agent Engineer, Documentation Architect, QA and Test Engineer, Security Engineer, DevSecOps and Cloud Engineer, Code Reviewer, FinOps Reviewer, Release Manager, and the legacy generic Backend Engineer role for cross-stack coordination. All inherit repository safety policy, require evidence, escalate sensitive/external actions, record structural decisions in ADRs and use the common handoff prompt.

Managed-project roles add Project Conductor and Evidence Supervisor. The conductor owns method
progress but cannot approve scope, contracts, finance, or its own output. The supervisor is read-only
and independent for the reviewed artifact. Project registry admission pins role/version and never
grants more authority than the project baseline.

Homologation specialists are UI/UX Architecture, Accessibility, Internationalization, Visual Quality, Usability Flow, User Communication, Injection Security, Bot and Abuse Detection, Monetization Strategy, Ethical Persuasion, Commercial Integrity, and Gamification and Loyalty. Their exact contracts live beside the original roles and share severity/report rules in `.codex/agents/README.md`. CI verifies contracts but does not pretend Markdown roles executed; manual evidence is tracked in `docs/testing/develop-to-homolog-checklist.md`.
