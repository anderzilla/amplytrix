# C4 context

```mermaid
flowchart LR
  client["Client decision owner"] --> amp["Amplytrix project platform"]
  operator["CodeMatrix project operator"] --> amp
  reviewer["Independent reviewer"] --> amp
  amp --> identity["Identity provider (proposed)"]
  amp --> model["AI model providers (future)"]
  amp --> scm["Client source/artifact systems (future)"]
  amp --> gcp["Google Cloud managed services"]
  agency["CodeMatrix Agency (preferred prepared intake)"] -. "versioned API/events only" .-> amp
  clientdocs["Client / third-party documents"] --> amp
  public["CodeMatrix public site"] --> amp
```

CodeMatrix Agency owns corporate/commercial management. Amplytrix owns project delivery data and
execution. No direct database, filesystem, or implicit identity trust crosses that boundary.
