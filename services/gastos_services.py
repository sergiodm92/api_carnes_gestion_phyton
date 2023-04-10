from db import get_database
from models import (
    Gasto_Combustible,
    Gasto_Transporte, 
    Gasto_Impositivo, 
    Gasto_Administrativo
)

db = get_database()

#crear un nuevo gasto de combustible
async def post_gasto_combustible(gasto_combustible: Gasto_Combustible):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto_combustible.id)
        doc_ref.set(gasto_combustible.dict())
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
async def post_gasto_transporte(gasto_transporte: Gasto_Transporte):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto_transporte.id)
        doc_ref.set(gasto_transporte.dict())
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
async def post_gasto_impositivo(gasto_impositivo: Gasto_Impositivo):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto_impositivo.id)
        doc_ref.set(gasto_impositivo.dict())
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
async def post_gasto_administrativo(gasto_administrativo: Gasto_Administrativo):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('gastos').document(gasto_administrativo.id)
        doc_ref.set(gasto_administrativo.dict())
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
async def get_gasto_combustible():
    try:
        gastos_combustible = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('gastos').where('type','==','combustible').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            gasto = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            gastos_combustible.append(gasto)
        return gastos_combustible
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer gastos de transporte
async def get_gasto_transporte():
    try:
        gastos_transporte = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('gastos').where('type','==','transporte').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            gasto = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            gastos_transporte.append(gasto)
        return gastos_transporte
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer gastos impositivos
async def get_gasto_impositivo():
    try:
        gastos_impositivos = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('gastos').where('type','==','impositivo').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            gasto = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            gastos_impositivos.append(gasto)
        return gastos_impositivos
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    
# Traer gastos administrativos
async def get_gasto_administrativo():
    try:
        gastos_administrativos = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('gastos').where('type','==','administrativo').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            gasto = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            gastos_administrativos.append(gasto)
        return gastos_administrativos
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar gasto de combustible
async def delete_gasto_combustible(id:str):
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
    
# Eliminar gasto de transporte
async def delete_gasto_transporte(id:str):
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

# Eliminar gasto impositivo
async def delete_gasto_impositivo(id:str):
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
    
# Eliminar gasto administrativo
async def delete_gasto_administrativo(id:str):
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