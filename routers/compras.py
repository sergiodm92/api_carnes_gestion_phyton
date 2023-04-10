from fastapi import APIRouter, Depends
from models import Compra_Vacas, Compra_Cerdos
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.compras_services import (
    post_compra_vacas,
    post_compra_cerdos,
    get_compras, 
    get_compras_saldo, 
    delete_compra, 
    get_compra, 
    get_compras_by_proveedor
)

router = APIRouter()

# Ruta POST para cargar una compra
@router.post("/vaca")
async def new_compra_vacas(compra: Compra_Vacas, token_data=Depends(verify_token)):
    try:
        response = await post_compra_vacas(compra)
        if response:
            return custom_Response_Exito(compra)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta POST para cargar una compra
@router.post("/cerdo")
async def new_compra_cerdos(compra: Compra_Cerdos, token_data=Depends(verify_token)):
    try:
        response = await post_compra_cerdos(compra)
        if response:
            return custom_Response_Exito(compra)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta GET para obtener todas las Compras
@router.get("/all")
async def get_all_compras(token_data=Depends(verify_token)):
    try:
        compras = await get_compras()
        return custom_Response_Exito(compras)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae las compras con saldo > 0
@router.get("/saldo")
async def get_all_compras_saldo(token_data=Depends(verify_token)):
    try:
        faenas = await get_compras_saldo()
        return custom_Response_Exito(faenas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae una compra por ID
@router.get("/id/{id}")
async def get_compra_id(id: str, token_data=Depends(verify_token)):
    try:
        compra = await get_compra(id)
        return custom_Response_Exito(compra)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Ruta que trae una compra por ID
@router.get("/proveedor/{proveedor}")
async def get_compras_proveedor(proveedor: str, token_data=Depends(verify_token)):
    try:
        compras = await get_compras_by_proveedor(proveedor)
        return custom_Response_Exito(compras)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)


# Eliminar una compra por ID
@router.delete("/{id}")
async def delete_compra_id(id: str, token_data=Depends(verify_token)):
    try:
        response = await delete_compra(id)
        message = {"message": "La Compra se eliminó correctamente"}
        if response:
            return custom_Response_Exito(message)
        else:
            return custom_Response_Error(message="No se pudo eliminar la compra", status_code=400)

    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)
