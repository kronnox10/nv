from pydantic import BaseModel

class User(BaseModel):
    
    id: int= None
    usuario: str
    password: str
    nombre: str
    apellido: str
    documento: str
    telefono:str
    id_rol: int
    estado:bool
    