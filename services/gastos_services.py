from db import get_database
from models import (
    Gasto_Combustible,
    Gasto_Transporte, 
    Gasto_Impositivo, 
    Gasto_Administrativo
)

db = get_database()

#crear un nuevo gasto de combustible
async def post_gasto_combustible(gasto: Gasto_Combustible):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto.id)
        doc_ref.set(gasto.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

#crear una nueva venta de carne de cerdo
async def post_gasto_transporte(gasto: Gasto_Transporte):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto.id)
        doc_ref.set(gasto.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

#crear un nuevo gasto impositivo
async def post_gasto_impositivo(gasto: Gasto_Impositivo):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto.id)
        doc_ref.set(gasto.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
#crear un nuevo gasto administrativo
async def post_gasto_administrativo(gasto: Gasto_Administrativo):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto.id)
        doc_ref.set(gasto.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# Traer gastos de combustible
async def get_gastos_type(type:str):
    try:
        gastos_combustible = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('gastos').where('type','==',type).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            gasto = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            gastos_combustible.append(gasto)
        return gastos_combustible
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer un  gasto de combustible por ID
async def get_gasto_id(id:str):
    try:
        # Obtiene todos los documentos de la colección "ventas"
        gasto = db.collection('gastos').document(id).get().to_dict()
        return gasto
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar gasto de combustible
async def delete_gasto(id:str):
    try:
        doc_ref = db.collection('gastos').document(id)
        
        # Verifica si la venta existe
        if doc_ref.get().exists:
            # Elimina el documento de la venta
            doc_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}
    
