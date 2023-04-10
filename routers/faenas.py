from fastapi import APIRouter, Depends
from models import Faena
from middlewares.response import custom_Response_Exito, custom_Response_Error
from middlewares.verify_token import verify_token
from services.faenas_services import( 
    post_faena, 
    get_faenas, 
    get_faena_tropa, 
    get_faena_frigorifico,
    get_faena_saldo, 
    delete_faena
    )

router = APIRouter()

# Ruta POST para cargar una faena
@router.post("/")
async def create_faena(faena: Faena, token_data = Depends(verify_token)):
    try:
        response = await post_faena(faena)
        if response : return custom_Response_Exito(faena)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


# Ruta GET para obtener todas las Faenas
@router.get("/all")
async def get_all_faenas(token_data = Depends(verify_token)):
    try:
        faenas = await get_faenas()
        return custom_Response_Exito(faenas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


# Ruta GET para obtener una Faenas por N de tropa por params
@router.get("/tropa/{tropa}")
async def get_faena(tropa, token_data = Depends(verify_token)):
    try:
        faena = await get_faena_tropa(tropa)
        return custom_Response_Exito(faena)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
# Ruta GET para obtener las faenas por frigorifico
@router.get("/frigorifico/{frigorifico}")
async def get_all_faenas_frigorifico(frigorifico:str,token_data = Depends(verify_token)):
    try:
        faenas = await get_faena_frigorifico(frigorifico)
        return custom_Response_Exito(faenas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


# Ruta que trae las faenas con saldo > 0
@router.get("/saldo")
async def get_all_faenas_saldo(token_data = Depends(verify_token)):
    try:
        faenas = await get_faena_saldo()
        return custom_Response_Exito(faenas)
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)
    
# Eliminar una Faena por tropa
@router.delete("/{tropa}")
async def eliminar_faena(tropa: str, token_data = Depends(verify_token)):
    try:
        response = await delete_faena(tropa)
        message = {"message": "La Faena se eliminó correctamente"}
        if response : return custom_Response_Exito(message)
        else: return custom_Response_Error(message="No se pudo eliminar la faena", status_code=400)
        
    except Exception as e:
        print(e)
        return custom_Response_Error(message="Ocurrió un error inesperado ",status_code=400)


