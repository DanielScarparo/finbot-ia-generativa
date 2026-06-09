# Base de Conhecimento do Agente

A inteligência do agente é alimentada por uma base de conhecimento estática e estruturada, simulando o banco de dados de uma instituição financeira. Os arquivos estão localizados na pasta `data/`.

## Estrutura de Dados

| Arquivo | Formato | Descrição e Uso |
| :--- | :--- | :--- |
| `transacoes.csv` | CSV | Contém o registro diário de receitas e despesas. Usado para calcular totais por categoria, médias de gastos e identificar padrões de consumo. |
| `perfil_investidor.json` | JSON | Define a idade, renda, tolerância ao risco e as metas financeiras do cliente. Usado para personalizar conselhos e direcionar esforços de economia. |
| `produtos_financeiros.json` | JSON | Catálogo de soluções financeiras disponíveis (ex: CDB, Cartão de Crédito com trava). Usado para sugestões ativas quando o agente identifica oportunidades. |
| `historico_atendimento.csv` | CSV | Logs de interações passadas do usuário com o suporte. Usado para manter o contexto de reclamações ou dúvidas anteriores e não ser repetitivo. |

## Limitações e Escalabilidade
Atualmente, os dados são arquivos locais para facilitar o protótipo e garantir a segurança do ambiente de teste. Em uma arquitetura de produção, essa camada seria substituída por conexões diretas a bancos de dados relacionais (SQL) e APIs de *Open Finance*.