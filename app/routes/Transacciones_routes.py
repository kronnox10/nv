from fastapi import APIRouter, HTTPException
from app.controllers.transacciones_controller import *
from app.models.transacciones_model import Transacciones

router = APIRouter()

nueva_transaccion = TravesanoController()


@router.post("/create_transacciones")
async def create_transaccion(transacciones: Transacciones):
    rpta = nueva_transaccion.create_transaccion(transacciones)
    return rpta


@router.get("/get_transaccion/{transaccion_id}",response_model=Transacciones)
async def get_transaccion(transaccion_id: int):
    rpta = nueva_transaccion.get_transaccion(transaccion_id)
    return rpta

@router.get("/get_transacciones/")
async def get_transacciones():
    rpta = nueva_transaccion.get_transacciones()
    return rpta

    

@router.put("/actualizar_transacciones/{transaccion_id}")
async def update_transacciones(transaccion_id: int,transaccion: Transacciones,):
    rpta = nueva_transaccion.update_transacciones(transaccion_id,transaccion) 
    return rpta 

@router.delete("/eliminar_transacciones/{transaccion_id}")
async def delete_transacciones(transaccion_id: int):
    rpta = nueva_transaccion.delete_transacciones(transaccion_id)
    return rpta 