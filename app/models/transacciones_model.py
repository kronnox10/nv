from pydantic import BaseModel

class Transacciones(BaseModel):
    
    id: int= None
    id_pago: int
    tipo_pago: str
    fecha_pago: str
    estado: bool