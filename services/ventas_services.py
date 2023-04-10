from db import get_database
from models import Venta_Vacas, Venta_Cerdos, Venta_Achuras

db = get_database()

#crear una nueva venta de carne de vaca
async def post_venta_vacas(venta: Venta_Vacas):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('ventas').document(venta.id)
        doc_ref.set(venta.dict())
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
async def post_venta_cerdos(venta: Venta_Cerdos):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('ventas').document(venta.id)
        doc_ref.set(venta.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

#crear una nueva venta de achuras de vaca
async def post_venta_achuras(venta_achura: Venta_Achuras):
    try:
        # Crea el nuevo documento en Firestore con los datos de la venta
        doc_ref = db.collection('ventas').document(venta_achura.id)
        doc_ref.set(venta_achura.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# Traer a todas las ventas
async def get_ventas():
    try:
        ventas = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('ventas').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            venta = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            ventas.append(venta)
        return ventas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer las ventas con saldo > 0
async def get_ventas_saldo():
    try:
        ventas = []
        # Obtiene la faena por tropa
        docs = db.collection('ventas').where('saldo','>',0).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            venta = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            ventas.append(venta)
        return ventas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer las ventas por cliente
async def get_ventas_by_cliente(cliente:str):
    try:
        ventas = []
        # Obtiene la faena por tropa
        docs = db.collection('ventas').where('cliente','==',cliente).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            venta = doc.to_dict()
            # Agrega el diccionario a la lista de ventas
            ventas.append(venta)
        return ventas
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer una faena por tropa
async def get_venta(id:str):
    try:
        # Obtiene la faena por tropa
        venta = db.collection('ventas').document(id).get().to_dict()
        return venta
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Eliminar una venta por ID
async def delete_venta(id:str):
    try:
        doc_ref = db.collection('ventas').document(id)
        
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