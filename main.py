
from fastapi import FastAPI
from bd.database import sesion, bd, base
from routers.movie import ruta_pelucula
from routers.usuario import ruta_usuario
import os

app=FastAPI(
    title="Comenzando",
    description="API primeros ensayos",
    version="0.0.1"
)
app.include_router(ruta_pelucula)
app.include_router(ruta_usuario)

base.metadata.create_all(bind=bd)

if __name__=="__main__":
    port=int(os.environ.get("PORT",8000))
    uvicorn.run("main:app", host="0.0.0.0",port=port)

"""
pelis=[
    {
        "id":1,
        "titulo":"padrino",
        "año":1972,
        "valoracion":7,
        "pais":"chile"
    }
]


@app.get('/', tags=["inicio"])
def hola():
    #return {"hola":"mundo"}
    return HTMLResponse("<h2>hola world!!</h2>")

"""
