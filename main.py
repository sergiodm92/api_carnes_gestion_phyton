from fastapi import FastAPI
from routers.users import router as users_router
from middlewares.response import custom_Response_Exito
from routers.clientes import router as clientes_router
from routers.proveedores import router as proveedores_router
from routers.faenas import router as faenas_router
from routers.compras import router as compras_router

app = FastAPI()


@app.get(("/"),tags=["Default"])
async def response_default():
    response = {"message": "API en funcionamiento"}
    return custom_Response_Exito(response)


# Registra el router de compras en la aplicación con un prefijo de ruta
app.include_router(users_router, prefix="/user", tags=["User"])

app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])

app.include_router(proveedores_router, prefix="/proveedores", tags=["Proveedores"])

app.include_router(faenas_router, prefix="/faenas", tags=["Faenas"])

app.include_router(compras_router, prefix="/compras", tags=["Compras"])


# Ejecuta la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



