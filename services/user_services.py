import bcrypt
import random
from db import get_database
from models import User
import jwt

db = get_database()


async def auth_register(user: User):
    try:
        salt = bcrypt.gensalt(rounds=10)
        hashed_pass = bcrypt.hashpw(user.password.encode('utf-8'), salt).decode('utf-8')

        db.collection("users").document(user.name).set({"name": user.name, "password": hashed_pass})
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False


async def auth_login(user: User):
    try:
        auth_user = db.collection('users').document(user.name).get().to_dict()

        if auth_user is None:
            return {"mensaje": "Usuario no encontrado"}

        valid_password = bcrypt.checkpw(user.password.encode('utf-8'), auth_user['password'].encode('utf-8'))

        if valid_password :
            payload = {
                "name": auth_user["name"],
                "id": auth_user["name"]
            }

            secret = "Osjqbgk1brk1krncblqjgow91827461"

            token = jwt.encode(payload, secret, algorithm="HS256")

            return token
        else: 
            return {"mensaje": "Contraseña incorrecta"}
    except Exception as e:
        print(f"Error al autenticar usuario: {e}")
        return {"mensaje": "Error al autenticar usuario"}







