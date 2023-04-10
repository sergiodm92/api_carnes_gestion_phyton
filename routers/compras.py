from fastapi import APIRouter, Depends
from models import Compra_Vacas
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.compras_services import post_compra

router = APIRouter()

# Ruta POST para cargar una compra
@router.post("/")
async def post_compra(compra: Compra_Vacas, token_data = Depends(verify_token)):
    try:
        response = await post_compra(compra)
        if response : return custom_Response_Exito(compra)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)