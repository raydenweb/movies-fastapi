from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from usr_jwt import crea_token, valida_token

ruta_usuario=APIRouter()

class usuario(BaseModel):
    email:str
    password:str



#########################################################3  
@ruta_usuario.post("/login", tags=["Autenticacion"])
def login(usr:usuario):
    if (usr.email=="mario", usr.password=="123"): # esto es lo que biene de la bd
        token:str = crea_token(usr.model_dump())
        return JSONResponse(content=token)
#########################################################3   