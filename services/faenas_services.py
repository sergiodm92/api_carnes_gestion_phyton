from db import get_database
from models import Faena

db = get_database()

#crear una nueva faena
async def post_faena(faena: Faena):
    try:
        # Crea el nuevo documento en Firestore con los datos de la faena
        doc_ref = db.collection('faenas').document(faena.tropa)
        doc_ref.set(faena.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# Traer a todas las Faenas
async def get_faenas():
    try:
        faenas = []
        # Obtiene todos los documentos de la colección "faenas"
        docs = db.collection('faenas').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            faena = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            faenas.append(faena)
        return faenas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer una faena por tropa
async def get_faena_tropa(tropa:str):
    try:
        # Obtiene la faena por tropa
        faena = db.collection('faenas').document(tropa).get().to_dict()
        return faena
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer las faenas por frigorifico
async def get_faena_frigorifico(frigorifico:str):
    try:
        faenas = []
        # Obtiene la faena por tropa
        docs = db.collection('faenas').where('frigorifico','==',frigorifico).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            faena = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            faenas.append(faena)
        return faenas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    
# Traer las faenas con saldo > 0

async def get_faena_saldo():
    try:
        faenas = []
        # Obtiene la faena por tropa
        docs = db.collection('faenas').where('saldo','>',0).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            faena = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            faenas.append(faena)
        return faenas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar una faena por tropa
async def delete_faena(tropa:str):
    try:
        # Obtiene la referencia al documento del proveedor
        proveedor_ref = db.collection('faenas').document(tropa)
        
        # Verifica si la faena existe
        if proveedor_ref.get().exists:
            # Elimina el documento de la faena
            proveedor_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}
