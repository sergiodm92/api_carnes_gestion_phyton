from fastapi import APIRouter, HTTPException, status, Depends
from models import Compra_Vacas
from services.compra_services import getCompras, createNewCompra
from middlewares.verify_token import verify_token


router = APIRouter()

# Ruta GET para obtener todas las compras
@router.get("/all")
async def obtener_compras(token_data = Depends(verify_token)):
    try:
        compras = await getCompras()
        return compras
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Ruta POST para agregar una nueva compra
@router.post("/")
async def postCompra(compra: Compra_Vacas,token_data = Depends(verify_token)):
    try:
        response = await createNewCompra(compra)
        if(response):
            return {"mensaje": "compra cargada exitosamente", "status": status.HTTP_200_OK} 
        else: 
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocurrió un error y no se pudo cargar la compra")
    except Exception as e:
        print(e)
        return {"mensaje": "ocurrio un error con el servidor"}

compras = []
# Ruta GET para obtener una compra por ID
# @router.get("/{id}", response_model=str)
# async def obtener_compra_por_id(id: int):
#     # Lógica para obtener una compra por ID
#     if id >= len(compras):
#         raise HTTPException(status_code=404, detail="Compra no encontrada")
#     return compras[id]

@router.get("/sumar")
async def sum():
    suma = await sumar()
    return {"mensaje":suma}

# Ruta DELETE para eliminar una compra por ID
@router.delete("/{id}")
async def eliminar_compra(id: int):
    # Lógica para eliminar una compra por ID
    return {"mensaje": f"Eliminar compra con ID: {id}"}


