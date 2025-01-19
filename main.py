
from fastapi import FastAPI
from bd.database import sesion, bd, base
from routers.movie import ruta_pelucula
from routers.usuario import ruta_usuario

app=FastAPI(
    title="Comenzando",
    description="API primeros ensayos",
    version="0.0.1"
)
app.include_router(ruta_pelucula)
app.include_router(ruta_usuario)

base.metadata.create_all(bind=bd)



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
