from db import get_database
from models import Compra_Vacas, Compra_Cerdos

db = get_database()

#crear una nueva compra
async def post_compra_vacas(compra: Compra_Vacas):
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

async def post_compra_cerdos(compra: Compra_Cerdos):
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


# Traer a todas las Compras
async def get_compras():
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


# Traer las compras con saldo > 0
async def get_compras_saldo():
    try:
        compras = []
        # Obtiene la faena por tropa
        docs = db.collection('compras').where('saldo','>',0).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            compra = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            compras.append(compra)
        return compras
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer las compras por proveedor
async def get_compras_by_proveedor(proveedor:str):
    try:
        compras = []
        # Obtiene la faena por tropa
        docs = db.collection('compras').where('proveedor','==',proveedor).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            compra = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            compras.append(compra)
        return compras
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer una faena por tropa
async def get_compra(id:str):
    try:
        # Obtiene la faena por tropa
        compra = db.collection('compras').document(id).get().to_dict()
        return compra
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar una compra por ID
async def delete_compra(id:str):
    try:
        # Obtiene la referencia al documento del proveedor
        doc_ref = db.collection('compras').document(id)
        
        # Verifica si la compra existe
        if doc_ref.get().exists:
            # Elimina el documento de la compra
            doc_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}