from fastapi import APIRouter, Depends
from models import (
    Gasto_Combustible,
    Gasto_Transporte, 
    Gasto_Impositivo, 
    Gasto_Administrativo
)
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.gastos_services import (
    post_gasto_combustible, 
    post_gasto_transporte, 
    post_gasto_impositivo, 
    post_gasto_administrativo,
    get_gastos_type,
    get_gasto_id,
    delete_gasto, 
)

router = APIRouter()

# Ruta POST para cargar una venta
@router.post("/combustible")
async def new_gasto_combustible(gasto: Gasto_Combustible, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_combustible(gasto)
        if response:
            return custom_Response_Exito(gasto)
        else: custom_Response_Error(message="No se pudo cargar el gasto ", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar un gasto de transporte
@router.post("/transporte")
async def new_gasto_transporte(gasto_transporte: Gasto_Transporte, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_transporte(gasto_transporte)
        if response:
            return custom_Response_Exito(gasto_transporte)
        else: custom_Response_Error(message="No se pudo cargar el gasto ", status_code=400)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar un gasto impositivo
@router.post("/impositivo")
async def new_gasto_impositivo(gasto: Gasto_Impositivo, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_impositivo(gasto)
        if response:
            return custom_Response_Exito(gasto)
        else: custom_Response_Error(message="No se pudo cargar el gasto ", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)
    
# Ruta POST para cargar un gasto impositivo
@router.post("/administrativo")
async def new_gasto_administrativo(gasto: Gasto_Impositivo, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_administrativo(gasto)
        if response:
            return custom_Response_Exito(gasto)
        else: custom_Response_Error(message="No se pudo cargar el gasto ", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta para traer todos los gastos de combustible
@router.get("/{type}", description="El type debe ser (combustible, transporte, administrativo o impositivo)")
async def gastos_type(type:str, token_data=Depends(verify_token)):
    try:
        response = await get_gastos_type(type)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Traer un gasto  por ID
@router.get("/{id}")
async def gasto_id(id: str, token_data=Depends(verify_token)):
    try:
        response = await get_gasto_id(id)
        if response:
            return custom_Response_Exito(response)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

@router.delete("/{id}")
async def delete_gasto_id(id:str, token_data=Depends(verify_token)):
    try:
        response = await delete_gasto(id)
        if response:
            messege = {"messege":"se elimino el gasto con id {id}"}
            return custom_Response_Exito(messege)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

