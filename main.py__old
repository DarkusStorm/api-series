from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo!"}

@app.get("itens/{item_id}")
async def read_item(item_id: int, q: Optional[str]):
    return {"item_id": item_id, "q": q}

# Crie uma rota que retorne a soma de dois números passados por um caminho (path de URL). Extra: melhore a tipagem do código usando tipos do módulo typing onde for necessário.

@app.get("adicao/{a}/{b}")
async def adicao(a: int, b: int):
    return {"resultado": a + b}