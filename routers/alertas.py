from fastapi import APIRouter, Depends
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.alertas_services import get_alertas


router = APIRouter()

# Ruta GET para obtener todas las Compras
@router.get("/{dias}")
async def get_all_compras(dias:int,token_data=Depends(verify_token)):
    try:
        faenas = await get_alertas(dias)
        return custom_Response_Exito(faenas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)