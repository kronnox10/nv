from fastapi import APIRouter, HTTPException
from controllers.pago_controller import *
from models.pago_model import Pago

router = APIRouter()

nuevo_pago = payController() #definido donde

@router.post("/create_pago/")
async def create_pay(pago: Pago):
    rpta = nuevo_pago.create_pay(pago)
    return rpta


@router.get("/get_pay/{pago_id}",response_model=Pago)
async def get_pay(pago_id: int):
    rpta = nuevo_pago.get_pay(pago_id)
    return rpta

@router.get("/get_pagos/")
async def get_pays():
    rpta = nuevo_pago.get_pays()
    return rpta

    

@router.put("/update_pay/{pago_id}")
async def update_pay(pago_id: int ,pago: Pago,):
    rpta = nuevo_pago.update_pay(pago_id, pago)
    return rpta 

@router.delete("/eliminarpay/{pago_id}")
async def delete_pay(pago_id: int):
    rpta = nuevo_pago.delete_pay(pago_id)
    
    return rpta 