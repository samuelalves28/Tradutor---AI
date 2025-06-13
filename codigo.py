from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap
from typing import TypedDict

# Carrega chave da OpenAI
load_dotenv(override=True)
chave = os.getenv("OPENAI_API_KEY")

# Prompt de tradução
template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])

modelo = ChatOpenAI(api_key=chave, model="gpt-3.5-turbo")
parser = StrOutputParser()

# Isso aqui é chamado de encadeamento (chain), e permite que a saída de um modelo seja passada para outro passo de processamento.
chain = template_mensagem | modelo | parser
