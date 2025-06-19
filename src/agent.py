from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Inicializa o modelo LLM com Groq
llm = ChatGroq(temperature=0.7,
               model="llama-3.3-70b-versatile",
               api_key=groq_api_key)

prompt = PromptTemplate(
    input_variables=["proposito"],
    template="""
Você é um especialista em montagem de computadores. Com base no propósito informado pelo usuário, sugira uma configuração de hardware completa, incluindo:

- Processador
- Placa-Mãe
- Placa de Vídeo (se necessário)
- Memória RAM
- Armazenamento
- Fonte
- Gabinete
- Preço estimado total em Reais
- Links de lojas confiáveis para comprar no Brasil (Kabum, Terabyte, Amazon BR)

Objetivo do usuário: {proposito}

Ajuste a recomendação de acordo com o uso, priorizando custo-benefício.
Informe por quanto tempo a recomendação deve ser utilizada.
"""
)

pc_builder_chain = LLMChain(llm=llm, prompt=prompt)

def recomendar_pc(proposito):
    return pc_builder_chain.run(proposito)