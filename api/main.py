from fastapi import FastAPI

app = FastAPI()

times = [
    {"id": 1, "nome": "time Nautico"},
    {"id": 2, "nome": "time çanta"},
    {"id": 3, "nome": "time Esporte"},
]

@app.get("/")
def raiz():
    return {"mensagem": "API do Racha funcionando!"}

@app.get("/times/{numero}")
def clubes(numero: int):
    for time in times:
        if numero == time["id"]:
            return time["nome"]