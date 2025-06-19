import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Inicializa o modelo ChatGroq
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile"  # Você pode trocar para "llama3-70b-8192" ou outros modelos suportados
)

# Criação da cadeia de conversação
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
    verbose=True
)

# Interface Streamlit
st.set_page_config(page_title="Agente de Viagem com LLM", layout="centered")
st.title("🧳 Agente Virtual de Viagens com IA")

st.markdown(
    "Faça perguntas como:\n"
    "- Quais são os melhores destinos na Europa no verão?\n"
    "- Monte um roteiro de 5 dias em Lisboa\n"
    "- Preciso de dicas para viajar com crianças\n"
)

# Histórico da conversa
if "history" not in st.session_state:
    st.session_state.history = []

# Input do usuário
user_input = st.text_input("Digite sua pergunta sobre viagens:")

if user_input:
    response = conversation.run(user_input)
    st.session_state.history.append((user_input, response))
    st.markdown(f"**Agente:** {response}")

# Exibe o histórico
for user, reply in st.session_state.history:
    st.markdown(f"**Você:** {user}")
    st.markdown(f"**Agente:** {reply}")
