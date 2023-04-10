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
    get_gasto_combustible, 
    get_gasto_transporte, 
    get_gasto_impositivo, 
    get_gasto_administrativo,
    delete_gasto_combustible, 
    delete_gasto_transporte, 
    delete_gasto_impositivo, 
    delete_gasto_administrativo
)

router = APIRouter()

# Ruta POST para cargar una venta
@router.post("/combustible")
async def new_venta_vacas(gasto_combustible: Gasto_Combustible, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_combustible(gasto_combustible)
        if response:
            return custom_Response_Exito(gasto_combustible)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.post("/transporte")
async def new_venta_vacas(gasto_transporte: Gasto_Transporte, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_transporte(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.post("/impositivo")
async def new_venta_vacas(gasto_combustible: Gasto_Impositivo, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_impositivo(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.post("/impositivo")
async def new_venta_vacas(gasto_combustible: Gasto_Administrativo, token_data=Depends(verify_token)):
    try:
        response = await post_gasto_administrativo(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.get("/combustible")
async def new_venta_vacas(gasto_combustible: Gasto_Combustible, token_data=Depends(verify_token)):
    try:
        response = await get_gasto_combustible(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.get("/transporte")
async def new_venta_vacas(gasto_combustible: Gasto_Transporte, token_data=Depends(verify_token)):
    try:
        response = await get_gasto_transporte(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.get("/impositivo")
async def new_venta_vacas(gasto_combustible: Gasto_Impositivo, token_data=Depends(verify_token)):
    try:
        response = await get_gasto_impositivo(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.get("/administrativo")
async def new_venta_vacas(gasto_combustible: Gasto_Administrativo, token_data=Depends(verify_token)):
    try:
        response = await get_gasto_administrativo(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

@router.delete("/combustible")
async def new_venta_vacas(gasto_combustible: Gasto_Combustible, token_data=Depends(verify_token)):
    try:
        response = await delete_gasto_combustible(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.delete("/transporte")
async def new_venta_vacas(gasto_combustible: Gasto_Combustible, token_data=Depends(verify_token)):
    try:
        response = await delete_gasto_transporte(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.delete("/impositivo")
async def new_venta_vacas(gasto_impositivo: Gasto_Impositivo, token_data=Depends(verify_token)):
    try:
        response = await delete_gasto_impositivo(gasto_impositivo)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.delete("/administrativo")
async def new_venta_vacas(gasto_combustible: Gasto_Administrativo, token_data=Depends(verify_token)):
    try:
        response = await delete_gasto_administrativo(gasto_combustible)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)