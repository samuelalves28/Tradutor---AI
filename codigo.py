from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

chave = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
  api_key=chave,
  model="gpt-3.5-turbo"
)

mensagens = [
  SystemMessage(content="Traduza o texto a seguir para frances"),
  HumanMessage(content="Bem vindo")
]

resposta = modelo.invoke(mensagens)

print(resposta.content)
