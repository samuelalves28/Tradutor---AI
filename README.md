# 🌐 API de Tradução com FastAPI + LangChain

Este projeto implementa uma API REST para tradução de textos usando modelos de linguagem da OpenAI, facilitada pelo framework LangChain. A API recebe um texto e o idioma alvo e retorna o texto traduzido.

---

## 🚀 O que faz este projeto

- Recebe requisições POST contendo um texto e um idioma alvo
- Envia o texto para o modelo GPT-3.5-turbo da OpenAI, solicitando tradução para o idioma desejado
- Retorna a tradução gerada pelo modelo como resposta JSON
- Permite integração simples para aplicações que precisam de tradução automática via API

---

## 🚀 Como rodar o projeto

### 1. Pré-requisitos

- Python 3.10+
- Chave de API da OpenAI

### 2. Instalar dependências

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows

pip install fastapi uvicorn python-dotenv langchain langchain-core langchain-openai langserve pydantic
