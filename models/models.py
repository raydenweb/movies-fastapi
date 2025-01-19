from bd.database import base
from sqlalchemy import Column, Integer, String, Float

class Pelicula(base):
    __tablename__="peliculas"
    id=Column(Integer, primary_key=True)
    titulo=Column(String)
    año=Column(String)
    valoracion=Column(Float)
    pais=Column(String)

