from fastapi import APIRouter, Depends
from models import Pago
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.pagos_services import (
    post_pago, 
    get_pagos_type,
    get_pago_id,
    get_pagos_transaccion,
    get_pagos_contraparte,
    delete_pago, 
)

router = APIRouter()

# Ruta POST para cargar una venta
@router.post("/")
async def New_pago(pago: Pago, token_data=Depends(verify_token)):
    try:
        response = await post_pago(pago)
        if response:
            return custom_Response_Exito(pago)
        else: custom_Response_Error(message="No se pudo cargar el gasto ", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta para traer todos los pagos de un mismo tipo
@router.get("/type/{type}", description="El type debe ser (compra, venta o faena)")
async def pagos_type(type:str, token_data=Depends(verify_token)):
    try:
        response = await get_pagos_type(type)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta para traer todos los pagos de una misma transaccion(compra, venta, faena)
@router.get("/transaccion/{id}", description="El type debe ser (compra, venta o faena)")
async def get_pagos_transaccion_id(id:str, token_data=Depends(verify_token)):
    try:
        response = await get_pagos_transaccion(id)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta para traer todos los pagos de una misma contraparte(cliente, proveedor, frigorifico)
@router.get("/contraparte/{name}")
async def get_pagos_transaccion_id(name:str, token_data=Depends(verify_token)):
    try:
        response = await get_pagos_contraparte(name)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Traer un pago  por ID
@router.get("/{id}")
async def pago_id(id: str, token_data=Depends(verify_token)):
    try:
        response = await get_pago_id(id)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)



@router.delete("/{id}")
async def delete_pago_id(id:str, token_data=Depends(verify_token)):
    try:
        response = await delete_pago(id)
        if response:
            messege = {"messege":"se elimino el gasto con id {id}"}
            return custom_Response_Exito(messege)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)