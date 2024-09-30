from pydantic import BaseModel

class Atributoxusuario(BaseModel):
    id: int= None
    id_usuario: int
    id_atributo: int
    valor: str
    descripcion: str
    estado: bool