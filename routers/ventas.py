from fastapi import APIRouter, Depends
from models import Venta_Vacas, Venta_Cerdos, Venta_Achuras
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.ventas_services import (
    post_venta_vacas, 
    post_venta_cerdos, 
    get_ventas, 
    get_ventas_saldo, 
    delete_venta, 
    get_venta, 
    get_ventas_by_cliente,
    post_venta_achuras
)

router = APIRouter()


# Ruta POST para cargar una venta
@router.post("/vacas")
async def new_venta_vacas(venta: Venta_Vacas, token_data=Depends(verify_token)):
    try:
        response = await post_venta_vacas(venta)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta POST para cargar una venta
@router.post("/cerdos")
async def new_venta_cerdos(venta: Venta_Cerdos, token_data=Depends(verify_token)):
    try:
        response = await post_venta_cerdos(venta)
        if response:
            return custom_Response_Exito(venta)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta POST para cargar una venta
@router.post("/achuras")
async def new_venta_achuras(venta_achuras: Venta_Achuras, token_data=Depends(verify_token)):
    try:
        response = await post_venta_achuras(venta_achuras)
        if response:
            return custom_Response_Exito(venta_achuras)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

# Ruta GET para obtener todas las ventas
@router.get("/all")
async def get_all_ventas(token_data=Depends(verify_token)):
    try:
        ventas = await get_ventas()
        return custom_Response_Exito(ventas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae las ventas con saldo > 0
@router.get("/saldo")
async def get_all_ventas_saldo(token_data=Depends(verify_token)):
    try:
        ventas = await get_ventas_saldo()
        return custom_Response_Exito(ventas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae una venta por ID
@router.get("/id/{id}")
async def get_venta_id(id: str, token_data=Depends(verify_token)):
    try:
        venta = await get_venta(id)
        return custom_Response_Exito(venta)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae una venta por ID
@router.get("/cliente/{cliente}")
async def get_ventas_cliente(cliente: str, token_data=Depends(verify_token)):
    try:
        ventas = await get_ventas_by_cliente(cliente)
        return custom_Response_Exito(ventas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Eliminar una venta por ID
@router.delete("/{id}")
async def delete_venta_id(id: str, token_data=Depends(verify_token)):
    try:
        response = await delete_venta(id)
        message = {"message": "La venta se eliminó correctamente"}
        if response:
            return custom_Response_Exito(message)
        else:
            return custom_Response_Error(message="No se pudo eliminar la venta", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)