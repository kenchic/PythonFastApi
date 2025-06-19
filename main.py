from fastapi import FastAPI

app = FastAPI()

empleados = [
    {
        "nombre" : "German Alvarez",
        "descripcion" : "Desarrollador Web",
        "activo" : True,
        "usuario": "GALVAREZ",
        "rol" : "ventas",
        "clave" : "1234",
        "salario" : 2500,
        "tareasFinalizadas": 9
    },
    {
        "nombre" : "Daniel Rondon",
        "descripcion" : "Ing. DevOps",
        "activo" : True,
        "usuario": "DRONDON",
        "rol" : "compras",
        "clave" : "5678",
        "salario" : 4000,
        "tareasFinalizadas": 2
    }
]

@app.get('/', tags=['Inicio'])
def home():
    return {"mensaje": "hola mundo."}

@app.get('/empleados', tags=['Empleados'])
def get_empleados():
    return empleados

@app.get('/empleados/{id}', tags=['Empleados'])
def get_empleados(id: str):    
    for usu in empleados:
        if usu['usuario'] == id.upper():
            return usu        
    return []