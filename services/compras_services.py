from db import get_database
from models import Compra_Vacas

db = get_database()

#crear una nueva compra
async def post_compra(compra: Compra_Vacas):
    try:
        # Crea el nuevo documento en Firestore con los datos de la compra
        doc_ref = db.collection('compras').document(compra.id)
        doc_ref.set(compra.dict())
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


