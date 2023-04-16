from db import get_database
from models import  Pago
from caja_services import post_caja

db = get_database()

#crear un nuevo pago
async def post_pago(pago: Pago):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('pagos').document(pago.id)
        doc_ref.set(pago.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            post_caja(pago.dict())
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False




# Traer pagos por type
async def get_pagos_type(type:str):
    try:
        pagos = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('pagos').where('type','==',type).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            pago = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            pagos.append(pago)
        return pagos
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer un  pago por ID
async def get_pago_id(id:str):
    try:
        # Obtiene todos los documentos de la colección "ventas"
        pago = db.collection('pagos').document(id).get().to_dict()
        return pago
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    
# Traer pagos por id de transaccion (id de venta,compra,faena)
async def get_pagos_transaccion(id:str):
    try:
        pagos = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('pagos').where('transaccion_id','==',id).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            pago = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            pagos.append(pago)
        return pagos
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    
# Traer pagos por contraparte (proveedor, cliente, frigorifico)
async def get_pagos_contraparte(contraparte:str):
    try:
        pagos = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('pagos').where('contraparte','==',contraparte).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            pago = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            pagos.append(pago)
        return pagos
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar pago
async def delete_pago(id:str):
    try:
        doc_ref = db.collection('pagos').document(id)
        
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
    
