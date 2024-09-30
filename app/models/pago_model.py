from pydantic import BaseModel

class Pago(BaseModel):
    id: int= None
    id_usuario: int
    monto: float
    fecha_pago:str
    estado:bool