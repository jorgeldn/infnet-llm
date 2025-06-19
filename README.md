## Projeto da Disciplina: IA generativa para linguagem (LLM) [25E2_3]


# 🖥️ Assistente de Montagem de PC com IA

Este projeto é um aplicativo interativo desenvolvido com **Streamlit**, **LangChain** e **LLMs da Groq**, com o objetivo de auxiliar usuários a obter recomendações personalizadas de hardware para montagem de computadores, com base em seu propósito de uso (como jogar, estudar, editar vídeos, entre outros).


## 📌 Objetivos do Projeto

- Demonstrar o uso de **LLMs integrados via LangChain** para resolver um problema prático e específico.
- Ajudar usuários a escolherem **peças de computador compatíveis** com seu objetivo (custo-benefício).
- Fornecer uma **previsão de preço total** e **links de compra** em sites confiáveis no Brasil (ex: Kabum, Terabyte, Amazon BR).
- Aplicar conceitos de engenharia de prompt e agentes inteligentes em uma aplicação de fácil uso via navegador.


## 💡 Como Funciona

1. O usuário informa o **propósito** do computador (ex: “Jogar em Full HD”, “Trabalhar com AutoCAD”, “Edição de vídeos 4K”, etc.).
2. Um agente LLM é acionado para gerar uma **configuração ideal de peças**.
3. A resposta inclui:
   - Lista de peças recomendadas (CPU, GPU, RAM, etc.)
   - Estimativa de preço total
   - Links sugeridos para compra no Brasil


## 🧱 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) — para criação da interface web
- [LangChain](https://www.langchain.com/) — para orquestração de prompts e agentes LLM
- [Groq + Mixtral](https://console.groq.com/) — como backend LLM via `langchain_groq`
- Python 3.10+


## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
````

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Certifique-se de ter Python 3.10+ instalado.

### 4. Configure sua chave de API da Groq

Crie um arquivo `.env` dentro da pasta `src` do projeto com a seguinte variável:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Execute a aplicação

Dentro da pasta `src`, execute:

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` no navegador.


## 📷 Exemplo de Uso

Usuário informa:

```
"Quero um computador para editar vídeos em 4K usando Adobe Premiere."
```

Resposta da IA:

```
- Processador: AMD Ryzen 9 7900X
- Placa-mãe: ASUS B650
- Memória RAM: 32GB DDR5
- Armazenamento: SSD NVMe 1TB Gen4
- Placa de Vídeo: RTX 4070 Super
- Fonte: 750W 80 Plus Gold
- Gabinete: Médio com boa ventilação
- Preço estimado: R$ 9.500
- Links: www.kabum.com.br/produto1, www.amazon.com.br/produto2...
```


## 👨‍💻 Autor

Projeto desenvolvido por **\[Jorge Nascimento]** para fins acadêmicos.

