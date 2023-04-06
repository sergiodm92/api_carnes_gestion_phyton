from fastapi import FastAPI
from routers.compras import router as compras_router

app = FastAPI()

# Registra el router de compras en la aplicación con un prefijo de ruta
app.include_router(compras_router, prefix="/compras", tags=["Compras"])


# Ejecuta la aplicación FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

