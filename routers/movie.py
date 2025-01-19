from fastapi import FastAPI, Body, Request, HTTPException, Depends, Path, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional
from usr_jwt import crea_token, valida_token
from fastapi.security import HTTPBearer
from bd.database import sesion, bd, base
from models.models import Pelicula

ruta_pelucula=APIRouter()

class autentica(HTTPBearer):   
    async def __call__(self, req:Request):
        auth=await super().__call__(req)
        data=valida_token(auth.credentials)
        if data["email"] !="mario":
            raise HTTPException(status_code=403, detail="malas credenciales")

class Movies(BaseModel):
    id:Optional[int]=None
    titulo:str=Field(min_length=3, max_length=60,default="titulo pelicula")
    año:int=Field(default="1900")
    valoracion:float=Field(ge=1, le=10)
    pais:str=Field(min_length=3, max_length=60,default="chile")

@ruta_pelucula.get('/movies', tags=["pelis"], dependencies=[Depends(autentica())])
def da_movies():
    con =sesion()
    registros=con.query(Pelicula).all()
    #return {"hola":"mundo"}
    return JSONResponse(content=jsonable_encoder(registros))



@ruta_pelucula.get('/movies/{id}', tags=["pelis"])
def da_movie(id:int= Path(ge=1, le=100)):
    con=sesion()
    reg=con.query(Pelicula).filter(Pelicula.id==id).first()
    if not reg:
        return JSONResponse(status_code=404, content={"message":"No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(reg))
    #for i in pelis:
    #    if i["id"]==id:
    #         return i
    #return []
    #return {"hola":"mundo"}

@ruta_pelucula.post('/movies/', tags=["pelis"], status_code=201)
def crea(mov:Movies):
    con=sesion()
    reg=Pelicula(**mov.model_dump())
    con.add(reg)
    con.commit()
    #return JSONResponse(content={"message":"Se agrego nueva", "peliculilla":[mov.model_dump() for m in pelis]})
    return JSONResponse(content={"message":"Se agrego nueva"})

@ruta_pelucula.put('/movies/{id}', tags=["pelis"])
def actualiza(id:int, m:Movies):
    con=sesion()
    reg=con.query(Pelicula).filter(Pelicula.id==id).first()
    if not reg:
        return JSONResponse(status_code=404, content={"message":"No encontrado"})
    else:
        reg.titulo= m.titulo
        reg.año= m.año
        reg.valoracion= m.valoracion
        reg.pais= m.pais  
        con.commit() 
    return JSONResponse(status_code=200, content={"data":jsonable_encoder(reg)})

    #for item in pelis:
    #    if item["id"]==id:
    #        item["titulo"]= m.titulo,
    #        item["año"]= m.año,
    #        item["valoracion"]= m.valoracion,
    #        item["pais"]= m.pais,
    #        return pelis    


@ruta_pelucula.delete("/movies/{id}",tags=["pelis"])
def borra(id:int):
    con=sesion()
    reg=con.query(Pelicula).filter(Pelicula.id==id).first()
    if not reg:
        return JSONResponse(status_code=404, content={"message":"No encontrado"})
    con.delete(reg)
    con.commit()
    return JSONResponse(status_code=200, content={"message":"eliminado!!!!", "data":jsonable_encoder(reg)})

    
    


