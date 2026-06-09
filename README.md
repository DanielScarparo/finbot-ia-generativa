# 🤖 FinBot - Agente Financeiro Inteligente com IA Generativa

Este projeto foi desenvolvido como desafio final para a formação em IA Generativa da DIO. O FinBot é um assistente financeiro proativo que utiliza arquitetura RAG (Retrieval-Augmented Generation) para analisar transações reais, entender o perfil do investidor e fornecer conselhos personalizados de controle de gastos.

## 🎯 O Problema que Resolvemos
Aplicativos financeiros tradicionais fornecem gráficos estáticos. O FinBot atua como um consultor de bolso interativo. Em vez de apenas mostrar que você gastou R$ 400 em alimentação, ele cruza esse dado com o seu objetivo de "Reduzir gastos com delivery" e sugere limites semanais de forma encorajadora e humanizada.

## 🚀 Tecnologias Utilizadas
* **Python 3.12+**: Linguagem base da aplicação.
* **Pandas**: Processamento e estruturação dos dados locais (arquivos CSV e JSON).
* **Streamlit**: Criação da interface web interativa (Chat e Dashboards).
* **Groq API (Llama 3.1)**: Modelo de Linguagem Grande (LLM) responsável pela inteligência do agente, processando os prompts com altíssima velocidade.

## 🧠 Arquitetura e Segurança (Anti-Alucinação)
O sistema foi desenhado com foco estrito em segurança, um requisito básico para o setor financeiro:
1. **Isolamento de Dados**: A IA não tem acesso direto à internet para buscar cotações ou notícias. Todo o conhecimento provém de bases de dados locais e validadas (`data/`).
2. **Engenharia de Prompt**: O *System Prompt* restringe o agente a responder **apenas** com base no contexto injetado pelo script em Python.
3. **Bloqueio de Recomendações de Risco**: O agente é instruído a negar pedidos de sugestões de investimentos de alto risco ou ações fora do seu escopo de consultoria de gastos.

## 📁 Estrutura do Repositório

```text
lab-agente-financeiro/
│
├── data/                          # Base de conhecimento local do agente
│   ├── historico_atendimento.csv  
│   ├── perfil_investidor.json     
│   ├── produtos_financeiros.json  
│   └── transacoes.csv             
│
├── docs/                          # Documentação arquitetural e de produto
│   ├── 01-documentacao-agente.md  
│   ├── 02-base-conhecimento.md    
│   ├── 03-prompts.md              
│   ├── 04-metricas.md             
│   └── 05-pitch.md                
│
├── src/                           # Código fonte da aplicação principal
│   └── app.py                     
│
├── .env                           # Variáveis de ambiente (não versionado)
├── README.md                      # Documentação principal
```

## ⚙️ Como Executar o Projeto Localmente

**1. Clone o repositório**
```bash
git clone [https://github.com/SEU_USUARIO/lab-agente-financeiro.git](https://github.com/SEU_USUARIO/lab-agente-financeiro.git)
cd lab-agente-financeiro
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install pandas streamlit groq python-dotenv
```

**4. Configure a chave da API**
Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API gratuita da Groq:
```text
GROQ_API_KEY=sua_chave_aqui
```

**5. Rode a aplicação Web**
```bash
cd src
streamlit run app.py
```
A aplicação abrirá automaticamente no seu navegador padrão.

## 📊 Exemplos de Uso
Experimente perguntar ao agente no chat:
* *"Quais são meus objetivos financeiros?"* (Teste de recuperação de dados)
* *"Quanto eu já gastei com alimentação e qual a sua dica para eu economizar?"* (Teste de análise e insight)
* *"Quais ações da bolsa americana você recomenda?"* (Teste de barreira de segurança)

---
*Projeto desenvolvido para fins educacionais e de portfólio.*