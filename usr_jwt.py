import jwt 

def crea_token(data: dict):
    token:str=jwt.encode(payload=data, key="password", algorithm="HS256")
    # passwor hay que dejarla en var entorno ej dotenv
    return token

def valida_token(token:str)->dict:
    dara:dict=jwt.decode(token, key="password", algorithms=["HS256"])
    return dara
