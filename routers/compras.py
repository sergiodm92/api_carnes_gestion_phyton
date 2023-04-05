from google.cloud import firestore
from fastapi import APIRouter, HTTPException
from google.cloud.exceptions import GoogleCloudError
from models import Compra


db =  firestore.Client.from_service_account_json('firebase.json')

router = APIRouter()

# Ruta GET para obtener todas las compras

@router.get("/all")
async def obtener_compras():
    try:
        compras = []
        # Obtiene todos los documentos de la colección "compras"
        docs = db.collection('compras').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            compra = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            compras.append(compra)
        return compras
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Ruta POST para agregar una nueva compra
@router.post("/")
async def createNewCompra(compra: Compra):
    try:
        # Crea el nuevo documento en Firestore con los datos de la compra
        doc_ref = db.collection('compras').document(compra.id)
        doc_ref.set({
            'id': compra.id,
            'monto': compra.monto,
            'cantidad': compra.cantidad,
            'proveedor': compra.proveedor,
            'lugar': compra.lugar,
            'kg': compra.kg,
        })
        
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return {"mensaje": "compra cargada con exito"}
        else:
            return {"mensaje": "error al cargar la compra"}
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
    suma = "sumar()"
    return {"mensaje":suma}

# Ruta DELETE para eliminar una compra por ID
@router.delete("/{id}")
async def eliminar_compra(id: int):
    # Lógica para eliminar una compra por ID
    return {"mensaje": f"Eliminar compra con ID: {id}"}


