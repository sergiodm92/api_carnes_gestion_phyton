from google.cloud import firestore
from models import Compra
from google.cloud.exceptions import GoogleCloudError

db =  firestore.Client.from_service_account_json('firebase.json')

#crear una nueva compra
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
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


async def getCompras():
    return {"mensaje": "prueba"}


async def sumar():
    return 2+5
