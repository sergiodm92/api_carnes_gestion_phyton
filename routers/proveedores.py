from fastapi import APIRouter, HTTPException, status, Depends
from models import Proveedor
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.clientes_proveedores_service import get_proveedores, get_proveedor, post_proveedor, delete_proveedor, update_proveedor

router = APIRouter()

# Ruta GET para obtener todos los clientes
@router.get("/all")
async def obtener_clientes(token_data = Depends(verify_token)):
    try:
        proveedores = await get_proveedores()
        return custom_Response_Exito(proveedores)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
# Ruta POST para cargar un cliente
@router.post("/")
async def obtener_clientes(proveedor: Proveedor, token_data = Depends(verify_token)):
    try:
        response = await post_proveedor(proveedor)
        if response : return custom_Response_Exito(proveedor)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
# Ruta GET para obtener un cliente por nombre
@router.get("/{nombre}")
async def obtener_proveedor(nombre, token_data = Depends(verify_token)):
    try:
        proveedor = await get_proveedor(nombre)
        if proveedor : return custom_Response_Exito(proveedor)
        else: return custom_Response_Error(message="El cliente no existe",status_code=404)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)

# Ruta Delete para un cliente
@router.delete("/{nombre}")
async def eliminar_proveedor(nombre: str, token_data = Depends(verify_token)):
    try:
        response = await delete_proveedor(nombre)
        message = {"message": "El proveedor se eliminó correctamente"}
        if response : return custom_Response_Exito(message)
        else: return custom_Response_Error(message="No se pudo eliminar el proveedor", status_code=400)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
@router.put("/{nombre}")
async def actualizar_cliente(nombre: str, proveedor: Proveedor, token_data = Depends(verify_token)):
    try:
        response = await update_proveedor(nombre, proveedor.email, proveedor.telefono, proveedor.cuil, proveedor.direccion)
        message = {"message": "El correo electrónico del proveedor se actualizó correctamente"}
        if response : return custom_Response_Exito(message)
        else: return custom_Response_Error(message={"message": "No se pudo actualizar el correo electrónico del proveedor"}, status_code=400)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)

