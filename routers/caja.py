from fastapi import APIRouter, Depends
from models import Cliente
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.caja_services import get_caja


router = APIRouter()

# Ruta GET para obtener todos los clientes
@router.get("/")
async def obtener_caja(token_data = Depends(verify_token)):
    try:
        clientes = await get_caja()
        return custom_Response_Exito(clientes)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)