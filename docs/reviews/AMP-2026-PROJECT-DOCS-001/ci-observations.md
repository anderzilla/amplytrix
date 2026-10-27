# Observações de CI da entrega documental

Consulta em 27/10/2026, America/Sao_Paulo. Task AMP-2026-PROJECT-DOCS-001.
Head observado: `96c4f2b`. Estes resultados pertencem a esse head; um commit posterior terá
seus próprios checks. Não tratar a aprovação documental como aprovação de runtime ou de merge.

## Resultados confirmados

Checks docs, validate, secrets e terraform passaram. Os jobs de backend e dependency-review
falharam em auditoria de dependências:

- [Backend / run 40599449782](https://github.com/anderzilla/amplytrix/actions/runs/40599449782/job/122523618089):
  o pip-audit reportou 9 vulnerabilidades em 4 pacotes: certifi 2026.7.22, filelock 3.32.2,
  msgpack 1.2.1 e urllib3 2.7.0. O log lista versões de correção; precisam de análise e
  validação próprias antes de atualizar o lockfile.
- [Dependency review / mesmo run](https://github.com/anderzilla/amplytrix/actions/runs/40599449782/job/122523617642):
  a auditoria reportou 37 ocorrências: 4 baixas, 16 moderadas, 12 altas e 5 críticas.

Manifests e lockfiles de Node e backend estão idênticos aos de origin/develop no commit-base
da documentação. Assim, esta entrega não introduziu mudança de versões. Os relatórios são
sinais de auditoria; não houve avaliação de explorabilidade, alcance produtivo ou validação
independente de cada advisory nesta tarefa. Não instalar atualizações cegamente nem desativar
os checks para liberar a documentação.

## Pendência para o MVP

Engenharia e segurança precisam abrir um escopo técnico de triagem, identificar dependências
diretas/transitivas e caminhos afetados, selecionar atualizações compatíveis, executar testes
e auditorias e registrar riscos residuais. Só então os gates pertinentes podem ser considerados
para promoção. Revisão humana mantém autoridade sobre risco, orçamento e implantação.

Os demais jobs devem ser consultados no PR #188; resultados pendentes ou posteriores não são
inferidos deste registro. Reverter um documento não corrige as dependências herdadas.
