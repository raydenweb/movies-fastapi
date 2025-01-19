import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

nom_BD="pelis.sqlite"
dir=os.path.dirname(os.path.realpath(__file__))
bd_url=f"sqlite:///{os.path.join(dir,nom_BD)}"

bd=create_engine(bd_url, echo=True)
sesion=sessionmaker(bind=bd)

base=declarative_base()