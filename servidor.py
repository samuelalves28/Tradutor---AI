from fastapi import FastAPI
from langserve import add_routes
from codigo import chain
from pydantic import BaseModel

# Usa BaseModel agora (Pydantic v2 compatível)
class InputData(BaseModel):
    idioma: str
    texto: str

app = FastAPI(
    title="Servidor de Tradução",
    description="API para traduzir textos usando modelos de linguagem",
    version="1.0.0"
)

# adiciona a rota
add_routes(app, chain, path="/traduza", input_type=InputData)

# executa localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
