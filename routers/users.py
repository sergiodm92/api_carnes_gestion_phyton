from fastapi import APIRouter
from services.user_services import auth_login, auth_register
from middlewares.response import custom_Response_Error, custom_Response_Exito
from models import User

router = APIRouter()

@router.post('/login')
async def login(user: User):
    try:
        token = await auth_login(user)
        if len(token) > 100:
            response = {"token": token}
            return custom_Response_Exito(response)
        else:
            return custom_Response_Error(message="No se pudo inicias sesion...", status_code=400)
    except Exception as e:
        return custom_Response_Error(message="Error del servidor...", status_code=500)

@router.post('/register')
async def register(user: User):
    try:
        result = await auth_register(user)
        if isinstance(result, str):
            return custom_Response_Error(message="No ha podido registrarse reintente...", status_code=400)
        else:
            if result:
                response = {"message":"Se registro correctamente"}
                return custom_Response_Exito(response)
    except Exception as e:
        return custom_Response_Error(message="Error del servidor...", status_code=500)
