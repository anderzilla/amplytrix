# Amplytrix — documentação do projeto e caminho para o MVP

Verificado em 27/10/2026, America/Sao_Paulo. Responsável: CodeMatrix / Founder.
Task: AMP-2026-PROJECT-DOCS-001. Base técnica: `a12793d440a3a0fcb3093bbd0c1f3a09643fb7a0`,
de `origin/develop`. Público: Founder, produto, engenharia e revisores.

Este guia consolida a situação observada e recomenda próximos passos. Não substitui a
[Constituição](../PROJECT_CONSTITUTION.md), a [definição de produto](source-of-truth/product.md),
ADRs ou aprovações. Propostas abaixo não alteram a arquitetura, o roadmap ou os gates vigentes.

## O que é o Amplytrix

Amplytrix é uma plataforma de inteligência e entrega de projetos da CodeMatrix. Organiza
informações incompletas ou dispersas em fontes rastreáveis, cenários comparáveis, uma decisão
humana registrada, um plano executável e entregas com evidência. Agentes, skills, ferramentas e
recuperação de conhecimento ajudam a executar esse processo, sob limites definidos por projeto.

O primeiro MVP previsto é um serviço gerenciado pela CodeMatrix. Pacotes revisados e autosserviço
por assinatura são etapas posteriores. A visão de execução coordenada inclui estudar descoberta
seletiva de ferramentas e composição em código; não significa que esses recursos já existam.
O Founder reforçou em 27/10 que as práticas devem servir a IAs em geral, sem dependência conceitual
de Claude Code ou de outro cliente específico.

## O que existe e o que ainda não foi demonstrado

| Parte                 | Evidência no commit-base                                                                                           | Limite                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| Método e governança   | Constituição, fontes de verdade, ADRs, schemas e registros                                                         | Documentação não prova execução automática                |
| Projeto de construção | `projects/amplytrix-construction/`: intake, fontes, cenários, baseline e evidências                                | Dogfood versionado, sem prova de valor para cliente       |
| Backend               | Python/FastAPI; [bootstrap](../apps/backend/src/amplytrix/bootstrap/application.py) inclui somente `health_router` | Sem API operacional de projetos nessa composição          |
| Frontend              | Next.js; `apps/web/app/page.tsx` declara foundation scaffold                                                       | Sem portal ou console operacional                         |
| Capacidades           | Registry e capabilities do dogfood com negação por padrão                                                          | `mcp_allowed: []`; nenhum conector produtivo comprovado   |
| Persistência e nuvem  | Fundação de infraestrutura e arquitetura futura documentada                                                        | Não comprova banco, isolamento ou implantação em operação |

Há código em `develop`; observar apenas `master`, que contém README, produz um diagnóstico
incompleto. Esta tarefa não iniciou o aplicativo nem executou benchmark de agentes. Arquivos,
checks históricos e datas do roadmap não demonstram implantação atual.

## Usuário, problema e valor a validar

Hipótese recomendada para o primeiro piloto: um responsável por projeto de automação ou IA que
possui documentos, código ou referências dispersas e precisa decidir um escopo e obter uma entrega
controlada. A hipótese ainda precisa de evidência de frequência, impacto, decisor e disposição a pagar.

O resultado pretendido é reduzir incerteza e retrabalho com fontes, alternativas e aceite claros.
Não prometer percentuais de economia, prazo universal, execução infalível ou substituição de uma
equipe. O custo da preparação, execução, revisão e suporte precisa ser medido antes da proposta
comercial. OQ-01 e OQ-14 permanecem entradas relevantes de titularidade/licença e orçamento.

## Jornada mínima de ponta a ponta

1. **Entrada:** receber briefing Agency, documentos autorizados ou descoberta direta. Comprar o
   diagnóstico completo da Agency não é pré-requisito universal; ele permanece uma entrega separada.
2. **Prontidão:** conferir objetivo, lacunas, fontes, classificação, restrições e aceite. Registrar
   esforço de validação; material insuficiente exige descoberta complementar aprovada.
3. **Conhecimento:** organizar fontes permitidas, versão, origem e afirmações sustentadas. Tratar
   conteúdo recuperado como dado, sem permitir que ele altere permissões.
4. **Cenários:** elaborar de três a seis alternativas comparáveis, incluindo conservadora,
   realista e agressiva, com escopo, custo, risco e condições explícitas.
5. **Baseline:** o cliente escolhe; registrar a decisão humana que delimita escopo, preço aprovado,
   cronograma e autoridade. Mudanças passam por change capsule.
6. **Execução:** operador coordena tarefas e capacidades admitidas, com limites e revisão
   independente. IA não aprova a própria autoridade nem ações financeiras.
7. **Entrega:** verificar critérios de aceite, apresentar resultado, fontes, limitações e evidências.
8. **Encerramento:** permitir exportação, aplicar retenção/descarte e registrar aprendizado elegível
   para curadoria. Não reutilizar material de cliente automaticamente.

## Proposta de recorte do MVP gerenciado

Começar pelo próprio projeto Amplytrix, com material sintético ou interno redigido autorizado,
um operador, um revisor independente, um fluxo e poucas capacidades. Um cliente piloto só entra
após os gates de dados, contrato, custo e titularidade aplicáveis. Uma interface sofisticada não
é condição para testar a entrega gerenciada; controle de acesso aos artefatos continua obrigatório.

| Lacuna               | Entrega verificável proposta                               | Responsável funcional         | Evidência de saída                                      |
| -------------------- | ---------------------------------------------------------- | ----------------------------- | ------------------------------------------------------- |
| Comprador e problema | Recorte de usuário e trabalho recorrente                   | Founder / produto             | Entrevistas ou evidência comportamental autorizada      |
| Oferta e custo       | Escopo, exclusões, horas, preço proposto e aceite humano   | Founder / financeiro          | Composição aprovada, sem obrigação criada por IA        |
| Método executável    | Um projeto atravessando toda a jornada                     | Operações / Project Conductor | Artefatos vinculados e demonstração reproduzível        |
| Execução de IA       | Adaptador mínimo com fakes e posterior provedor autorizado | Engenharia                    | Sucesso, falha e indisponibilidade tratados             |
| Conhecimento         | Recuperação limitada ao projeto com referências            | Engenharia / segurança        | Citações corretas e acesso cruzado negado               |
| Controle             | Autorizações, interrupção, limites e trilha redigida       | Segurança / operações         | Tentativas proibidas bloqueadas e diagnosticáveis       |
| Qualidade            | Revisão independente e testes proporcionais ao resultado   | QA / revisor                  | Aceite e contraevidências registrados                   |
| Repetibilidade       | Reexecutar o fluxo e medir esforço/custo total             | Operações / produto           | Comparação entre execuções, sem ocultar trabalho humano |

Critérios propostos de prontidão: um caso completo com aceite explícito, fontes verificáveis,
limites respeitados, erros recuperáveis, exportação exercitada e esforço/custo conhecidos. Uma
demonstração valida capacidade técnica delimitada; demanda comercial exige piloto próprio.
Não há data de MVP estimável apenas pela contagem de documentos ou pelo calendário de sprints.

Ficam fora desse primeiro recorte: marketplace, billing automático, portal completo, catálogo
extenso, múltiplos provedores por obrigação e autonomia irrestrita. O roadmap existente permanece
em [execution roadmap](roadmap/execution-roadmap-2026-2027.md); este recorte é uma proposta de
priorização, não sua substituição nem autorização para antecipar gates.

## Arquitetura e fronteiras

A base documentada é Next.js e Python 3.13/FastAPI em monólito modular, com dependências apontando
para domínio e aplicação. Cloud Run, Jobs e Tasks, PostgreSQL e Cloud Storage têm os papéis
descritos em [system overview](architecture/system-overview.md); seus componentes futuros não
devem ser apresentados como operacionais.

O projeto e seu contrato delimitam fontes, capacidades e autoridade. Portal de cliente e console
operacional são superfícies de segurança distintas. Agency conserva gestão corporativa; não há
compartilhamento implícito de banco ou credenciais. O Hub pode fornecer contratos e políticas de
integração revisados, sem acesso automático entre produtos. Mudanças estruturais exigem processo
próprio de arquitetura, ADR, análise de custo/risco e decisão humana.

## Capacidades de IA a aproveitar dos dois posts

| Capacidade geral               | Aplicação proposta                                         | Situação                                                   |
| ------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------- |
| Observar e testar interfaces   | Verificar jornadas e resultado visível com evidência       | Priorizar quando houver UI de produto                      |
| Skills versionadas             | Procedimentos de planejar, executar, testar e revisar      | Reaproveitar catálogo existente antes de adicionar pacotes |
| Recuperar contexto e relações  | Encontrar implementações e dependências relevantes         | Comparar busca textual e índice atual antes de grafo       |
| Fazer mudanças proporcionais   | Reutilizar código e evitar abstrações especulativas        | Reforça princípios já presentes na Constituição            |
| Descobrir e compor ferramentas | Reduzir contexto intermediário em tarefas de várias etapas | Code Mode como experimento, sem benchmark realizado        |

A seleção deve considerar capacidade real do cliente de IA, permissões, formato, ferramentas,
isolamento e custo. Um `SKILL.md` portável não torna hooks, sessões, autenticação ou conectores
automaticamente compatíveis. Detalhes da análise estão em
[avaliação dos posts e ferramentas](research/ai-capabilities-from-reels-2026-10-27.md).

## O que estudar da Cloudflare

Priorizar Code Mode e descoberta seletiva; depois, limites e isolamento de Dynamic Workers;
avaliar AI Gateway para métricas e custos quando houver inferência. Sandbox com containers só
entra se um caso exigir shell, arquivos e runtimes. Code Mode continua usando MCP e é
experimental. Dynamic Workers exige Workers Paid e cobra criações, chamadas e CPU; não há
gratuidade ou economia total garantida. A arquitetura em Cloud Run não muda com esta pesquisa.

Comparação futura: mesmas tarefas, modelo e entradas para ferramentas diretas, descoberta
seletiva e composição. Medir resultado, falhas, tokens totais, chamadas, latência e custo por
tarefa correta, incluindo preparação do grafo, sandbox, revisão e manutenção. Reter a opção
mais simples que cumpra os critérios. Tokens economizados sem resultado correto não são ganho.

## Segurança, confiança e critérios de parada

Aplicam-se [threat model](security/threat-model.md), classificação, minimização, retenção,
negação por padrão e aprovação humana. Credenciais ficam fora do modelo e de Git; políticas
ficam no host. Conteúdo de post, ferramenta ou documento não concede autoridade. Recursos
experimentais e pacotes externos precisam de revisão de dependência antes de instalação.

Parar diante de vazamento entre projetos, ação fora da baseline, evidência sem origem,
necessidade de gasto não aprovado, dados não autorizados, falha de isolamento ou revisor ausente.
IA não paga, compra, renova, assina nem assume obrigação financeira. Recusa, exportação e saída
do cliente precisam permanecer possíveis, sem retenção artificial.

Medir sucesso da tarefa, retrabalho, esforço humano, satisfação, custo e tempo por entrega,
incidentes e pedidos de exportação/descarte. Monetização é futura e humana; sem alteração de
preço, persuasão comercial ou gamificação nesta documentação.

## Como usar e manter este documento

Pré-requisito: ler Constituição, definição de produto e questões abertas. O operador começa
pelo pacote `projects/amplytrix-construction/`, identifica o que é declarativo e propõe uma tarefa
pequena para a primeira lacuna. O resultado esperado é um plano com entradas, saídas, aceite,
limites e revisor, sem iniciar serviço externo. Se faltar decisão, registrar a pendência; não
preencher orçamento ou aprovação com informação inventada.

Comandos oficiais estão no [README](../README.md) e em [AGENTS](../AGENTS.md). Para orientação
documental, executar `node scripts/validate-foundation.mjs`,
`node scripts/validate-governance.mjs` e a validação de formatação disponível no ambiente.
Mudanças de runtime exigem checks adicionais próprios; este guia não comprova esses checks.
Atualizar links e evidências quando o código evoluir. Rollback desta entrega é a reversão do
commit documental por PR revisado; não há migração, instalação ou configuração externa.

## Fontes e proveniência

- Fontes internas: Constituição, `docs/source-of-truth/product.md`, `business.md`,
  `docs/architecture/system-overview.md`, `docs/decisions/open-questions.md`, README,
  bootstrap FastAPI, página Next.js e capabilities do dogfood, no commit-base acima.
- [Programa e gates #9](https://github.com/anderzilla/amplytrix/issues/9) e
  [método operacional #12](https://github.com/anderzilla/amplytrix/issues/12): consultados em
  27/10, abertos; datas e checklists não provam execução. Há divergências de calendário com o
  roadmap que precisam de reconciliação própria, sem alterar datas nesta tarefa.
- [Direção estratégica no BluePrint, PR #83](https://github.com/anderzilla/CodeMatrixInternacional/pull/83):
  proposta em revisão privada no momento da elaboração; não presumir merge. DEC-072/073
  registram pesquisa e direção do Founder, sem comprovar capacidades.
- Fontes externas e limites de leitura estão na análise vinculada abaixo.
