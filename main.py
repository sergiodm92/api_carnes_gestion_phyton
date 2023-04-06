from fastapi import FastAPI
from routers.users import router as users_router
from routers.compras import router as compras_router

app = FastAPI()

# Registra el router de compras en la aplicación con un prefijo de ruta
app.include_router(compras_router, prefix="/compras", tags=["Compras"])
app.include_router(users_router, prefix="/user", tags=["User"])


# Ejecuta la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
async def hello_world():
    return {"message": "API en funcionamiento"}



