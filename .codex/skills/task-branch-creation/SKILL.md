---
name: task-branch-creation
description: Safely create an Amplytrix task branch from develop after mandatory scope confirmation.
---

# Task branch creation

For a prompt beginning `NOVA TAREFA`, first ask exactly: `Esta tarefa pertence a qual escopo: frontend, backend, infraestrutura ou transversal?` Do not plan or edit before the answer. Check status and fetch `develop` without destructive reset; preserve local changes. Create `task/<scope>/<short-kebab-name>` only from `develop`. If the name is unclear, ask only for a short name. Record base SHA and branch.
