from fastapi import APIRouter, HTTPException
from app.services.user_service import authRegister, authLogin
from app.utils.custom_api_response import customResponseError, customResponseExito
from pydantic import BaseModel, ValidationError, validator

route = APIRouter()

class User(BaseModel):
    name: str
    password: str

    @validator('name')
    def name_length(cls, v):
        if len(v) < 6 or len(v) > 255:
            raise ValueError('El nombre debe tener entre 6 y 255 caracteres')
        return v

    @validator('password')
    def password_length(cls, v):
        if len(v) < 6 or len(v) > 1024:
            raise ValueError('La contraseña debe tener entre 6 y 1024 caracteres')
        return v

@route.post('/login')
async def login(user: User):
    try:
        token = await authLogin(user.dict())
        if len(token) > 100:
            return customResponseExito(token)
        else:
            raise HTTPException(status_code=400, detail="No se pudo iniciar sesión, reintente...")
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@route.post('/register')
async def register(user: User):
    try:
        result = await authRegister(user.dict())
        if isinstance(result, str):
            raise HTTPException(status_code=400, detail="No se ha podido registrar, reintente...")
        else:
            return customResponseExito(result)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

