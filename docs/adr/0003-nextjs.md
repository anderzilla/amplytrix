# ADR-0003: Next.js for web delivery

Status: accepted — 2026-08-01

Use Next.js 16 App Router/React 19 for accessible UI, server rendering, and UI-specific composition. A SPA adds hosting/API complexity; a full-stack Next-only system couples core API lifecycle to UI. Server Components are used only when they reduce client code or protect server data. Validate accessibility, caching, and standalone Cloud Run image.
