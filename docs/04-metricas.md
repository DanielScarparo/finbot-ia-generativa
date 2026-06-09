# Avaliação e Métricas do Agente

Para garantir a qualidade, segurança e evolução contínua do FinBot, estabelecemos três pilares de avaliação focados na experiência do usuário e na mitigação de riscos:

## 1. Taxa de Respostas Seguras (Anti-Alucinação)
* **Objetivo:** Garantir que 100% das respostas sobre produtos e dados financeiros sejam baseadas exclusivamente na base de conhecimento (Arquivos CSV e JSON).
* **Métrica:** Número de respostas contendo "Não tenho essa informação" em cenários fora de escopo, dividido pelo total de perguntas fora de escopo (Edge Cases).

## 2. Precisão e Assertividade (RAG Accuracy)
* **Objetivo:** Medir a capacidade do agente em recuperar e calcular os dados corretos (ex: somar os gastos totais de uma categoria específica).
* **Métrica:** Validação cruzada amostral. Comparação entre o valor calculado internamente pelo Pandas e o valor textual gerado na resposta do LLM.

## 3. Engajamento e Coerência de Perfil
* **Objetivo:** Avaliar se o agente está utilizando o perfil do cliente para personalizar as interações, e não apenas entregando relatórios frios.
* **Métrica:** Porcentagem de interações em que o agente menciona proativamente uma "Meta" ou "Objetivo Financeiro" do usuário durante a análise de uma despesa.
