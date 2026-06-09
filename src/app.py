import pandas as pd
import json
import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Configuração da página (deve ser a primeira chamada do Streamlit)
st.set_page_config(page_title="FinBot - Agente Financeiro", page_icon="💰", layout="wide")

# Carrega as variáveis de ambiente
load_dotenv()
CHAVE_API = os.getenv("GROQ_API_KEY")

# Inicializa o cliente da Groq
cliente = Groq(api_key=CHAVE_API)

# Função para carregar os dados (Cache para ficar mais rápido)
@st.cache_data
def carregar_dados():
    caminho_perfil = os.path.join(os.path.dirname(__file__), '../data/perfil_investidor.json')
    caminho_transacoes = os.path.join(os.path.dirname(__file__), '../data/transacoes.csv')

    with open(caminho_perfil, 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    
    transacoes = pd.read_csv(caminho_transacoes)
    return perfil, transacoes

def montar_contexto(perfil, transacoes):
    despesas = transacoes[transacoes['tipo'] == 'despesa']
    gasto_total = despesas['valor'].sum()
    gastos_por_categoria = despesas.groupby('categoria')['valor'].sum().to_dict()
    
    contexto = f"""
    Perfil do Cliente:
    Nome: {perfil['nome']}
    Renda Mensal Estimada: R$ {perfil['renda_mensal_estimada']}
    Objetivos: {', '.join(perfil['objetivos_financeiros'])}
    
    Resumo Financeiro do Mês:
    Gasto Total: R$ {gasto_total}
    Gastos por Categoria: {gastos_por_categoria}
    """
    return contexto, gasto_total

def consultar_agente(pergunta_usuario, contexto):
    system_prompt = f"""
    Você é um Consultor Financeiro Pessoal Inteligente. Seu objetivo é ajudar o usuário a gerenciar seus gastos de forma direta, educativa e em português do Brasil.
    Baseie-se APENAS nos dados fornecidos abaixo. Se não tiver a resposta nos dados, diga que não sabe.
    
    CONTEXTO DO USUÁRIO:
    {contexto}
    """
    
    resposta = cliente.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pergunta_usuario}
        ],
        model="llama-3.1-8b-instant",
        temperature=0.5,
    )
    return resposta.choices[0].message.content


# INTERFACE VISUAL COM STREAMLIT
try:
    perfil, transacoes = carregar_dados()
    contexto_preparado, gasto_total = montar_contexto(perfil, transacoes)
    
    # Barra lateral (Sidebar) com resumo dos dados
    with st.sidebar:
        st.header("📊 Painel de Controle")
        st.write(f"**Cliente:** {perfil['nome']}")
        st.metric(label="Renda Estimada", value=f"R$ {perfil['renda_mensal_estimada']}")
        st.metric(label="Total Gasto no Mês", value=f"R$ {gasto_total}")
        st.divider()
        st.subheader("🎯 Metas Atuais")
        for meta in perfil['objetivos_financeiros']:
            st.write(f"- {meta}")

    # Área principal do Chat
    st.title("🤖 FinBot - Seu Agente Inteligente")
    st.write("Converse com o seu assistente financeiro para analisar seus gastos ou pedir conselhos baseados nas suas metas.")

    # Inicializa o histórico do chat na sessão do navegador
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    # Exibe as mensagens antigas na tela
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Caixa de texto para o usuário digitar
    if prompt := st.chat_input("Pergunte sobre seus gastos..."):
        # Mostra a mensagem do usuário na tela e salva no histórico
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.mensagens.append({"role": "user", "content": prompt})

        # Consulta a IA e mostra a resposta com um efeito de carregamento
        with st.chat_message("assistant"):
            with st.spinner("Analisando seus dados..."):
                resposta_ia = consultar_agente(prompt, contexto_preparado)
                st.markdown(resposta_ia)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta_ia})

except Exception as e:
    st.error(f"Erro ao carregar o aplicativo: {e}")