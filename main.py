from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=['Inicio'])
def home():
    return {"mensaje": "hola mundo."}

@app.get('/usuarios', tags=['Inicio'])
def usuario():
    return "muchos usuarios"