from fastapi import APIRouter, Depends
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.stock_services import get_stock


router = APIRouter()


# Ruta para traer todos los pagos de un mismo tipo
@router.get("/", description="El type debe ser (compra, venta o faena)")
async def pagos_type(token_data=Depends(verify_token)):
    try:
        stock = await get_stock()
        if stock:
            return custom_Response_Exito(stock)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ", status_code=400)

