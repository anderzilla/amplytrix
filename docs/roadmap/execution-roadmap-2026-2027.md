# Roadmap de Execução 2026–2027

Este documento é a referência viva do programa: sprints, gates de saída e o
critério que decide se uma entrega pode avançar. Um gate só abre com
evidência anexada ao commit correspondente — data de calendário, isoladamente,
nunca é suficiente.

## Como usar este documento

- Cada sprint tem sua própria seção, com escopo, owners e um **gate de saída**.
- Um gate é uma checklist binária: ou toda evidência exigida existe e está
  vinculada ao commit, ou o gate permanece fechado e a entrega não avança de
  fase.
- Itens de backlog/decisão referenciados como `OQ-NN` ("Open Question") são
  rastreados aqui até serem resolvidos e substituídos por uma decisão
  registrada.

---

## Sprint 2026-09-14 → 2026-09-18 — Programa e Gates

### Objetivo

Fechar o baseline operacional do programa (orçamento, classificação de
dados, riscos e backlog) com o rigor de um gate: **o gate depende de
evidência, não apenas da data agendada de término da sprint.** Se a
evidência não estiver pronta e vinculada em 18/09, o gate permanece aberto
até que esteja — a sprint seguinte não herda um gate incompleto sem que
isso seja explicitamente registrado como risco.

### Entregas e Owners

| ID    | Entrega                    | Owner | Status |
|-------|-----------------------------|-------|--------|
| OQ-01 | Orçamento                   | TBD   | Não iniciado |
| OQ-04 | Classificação de dados      | TBD   | Não iniciado |
| OQ-14 | Baseline de riscos          | TBD   | Não iniciado |
| OQ-16 | Backlog                     | TBD   | Não iniciado |

> Preencher a coluna `Owner` com a pessoa responsável antes do kickoff da
> sprint. Um item sem owner nomeado não pode entrar em "Em andamento".

### Gate de Saída — Qualidade e Documentação

Nenhuma entrega acima é considerada concluída até que **todos** os itens
abaixo estejam satisfeitos e a evidência esteja vinculada ao commit final
da entrega:

- [ ] **Critérios de aceite definidos antes da implementação** — critérios
      positivos (o que deve acontecer) e negativos (o que não pode
      acontecer) documentados e aprovados antes do trabalho começar.
- [ ] **Testes aplicáveis executados** — resultados registrados (log, link
      de CI, ou evidência equivalente), não apenas "passou localmente".
- [ ] **Documentação, contratos, riscos e rollback sincronizados** — nenhum
      desses artefatos pode ficar desatualizado em relação ao que foi
      entregue; inclui plano de rollback testável.
- [ ] **Owner primário e revisor independente vinculados ao mesmo commit** —
      revisor não pode ser a mesma pessoa que implementou.
- [ ] **Nenhum BLOCKER/CRITICAL/HIGH aberto** — risco residual, se houver,
      está formalmente registrado (owner, mitigação, prazo de reavaliação).
- [ ] **Demonstração e retrospectiva concluídas** — demo da entrega
      apresentada e retrospectiva da sprint realizada e registrada.

### Regra do gate

> O gate depende de evidência, não apenas da data. Chegar a 18/09/2026 sem
> os itens acima marcados **não fecha o gate**. Nesse caso: (1) registrar o
> item em aberto como risco na baseline de riscos (OQ-14), com owner e nova
> data; (2) comunicar o bloqueio antes do início da sprint seguinte; (3) não
> iniciar trabalho que dependa desta entrega até o gate abrir.

---

## Sprints futuras

_A detalhar conforme o programa avança. Cada nova sprint deve seguir o
mesmo formato: Objetivo → Entregas e Owners → Gate de Saída._
