from fastapi import APIRouter, HTTPException, status, Depends
from models import Cliente
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.clientes_proveedores_service import get_clientes, get_cliente, post_cliente, delete_cliente, update_cliente

router = APIRouter()

# Ruta GET para obtener todos los clientes
@router.get("/all")
async def obtener_clientes(token_data = Depends(verify_token)):
    try:
        clientes = await get_clientes()
        return custom_Response_Exito(clientes)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)

# Ruta GET para obtener un cliente por nombre
@router.get("/{nombre}")
async def obtener_clientes(nombre, token_data = Depends(verify_token)):
    try:
        cliente = await get_cliente(nombre)
        if cliente : return custom_Response_Exito(cliente)
        else: return custom_Response_Error(message="El cliente no existe",status_code=404)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


# Ruta POST para cargar un cliente
@router.post("/")
async def obtener_clientes(cliente: Cliente, token_data = Depends(verify_token)):
    try:
        response = await post_cliente(cliente)
        if response : return custom_Response_Exito(cliente)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
# Ruta Delete para un cliente
@router.delete("/{nombre}")
async def eliminar_clientes(nombre: str, token_data = Depends(verify_token)):
    try:
        response = await delete_cliente(nombre)
        message = {"message": "El cliente se eliminó correctamente"}
        if response : return custom_Response_Exito(message)
        else: return custom_Response_Error(message="No se pudo eliminar el cliente", status_code=400)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


@router.put("/{nombre}")
async def actualizar_cliente(nombre: str, cliente: Cliente, token_data = Depends(verify_token)):
    try:
        response = await update_cliente(nombre, cliente.email, cliente.telefono, cliente.cuil, cliente.direccion)
        message = {"message": "El correo electrónico del cliente se actualizó correctamente"}
        if response : return custom_Response_Exito(message)
        else: return custom_Response_Error(message={"message": "No se pudo actualizar el correo electrónico del cliente"}, status_code=400)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)