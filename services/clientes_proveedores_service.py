from db import get_database
from models import Cliente, Proveedor

db = get_database()

#crear un nuevo cliente
async def post_cliente(cliente: Cliente):
    try:
        # Crea el nuevo documento en Firestore con los datos de la compra
        doc_ref = db.collection('clientes').document(cliente.nombre)
        doc_ref.set(cliente.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

#crear un nuevo proveedor
async def post_proveedor(proveedor: Proveedor):
    try:
        # Crea el nuevo documento en Firestore con los datos de la compra
        doc_ref = db.collection('proveedores').document(proveedor.nombre)
        doc_ref.set(proveedor.dict())
        # Verifica que el documento se haya creado correctamente
        doc_snapshot = doc_ref.get()
        if doc_snapshot.exists:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# Traer a todos los clientes
async def get_clientes():
    try:
        clientes = []
        # Obtiene todos los documentos de la colección "compras"
        docs = db.collection('clientes').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            cliente = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            clientes.append(cliente)
        return clientes
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer a todos los proveedores
async def get_proveedores():
    try:
        proveedores = []
        # Obtiene todos los documentos de la colección "compras"
        docs = db.collection('proveedores').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            proveedor = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            proveedores.append(proveedor)
        return proveedores
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer un cliente por nombre
async def get_cliente(nombre:str):
    try:
        cliente = {}
        # Obtiene todos los documentos de la colección "compras"
        cliente = db.collection('clientes').document(nombre).get().to_dict()
        return cliente
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Traer un proveedor por nombre
async def get_proveedor(nombre:str):
    try:
        proveedor = {}
        # Obtiene todos los documentos de la colección "compras"
        proveedor = db.collection('proveedores').document(nombre).get().to_dict()

        return proveedor
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}

# Eliminar un cliente por nombre
async def delete_cliente(nombre:str):
    try:
        # Obtiene la referencia al documento del proveedor
        cliente_ref = db.collection('clientes').document(nombre)
        
        # Verifica si el proveedor existe
        if cliente_ref.get().exists:
            # Elimina el documento del proveedor
            cliente_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}

# Eliminar un proveedor por nombre
async def delete_proveedor(nombre:str):
    try:
        # Obtiene la referencia al documento del proveedor
        proveedor_ref = db.collection('proveedores').document(nombre)
        
        # Verifica si el proveedor existe
        if proveedor_ref.get().exists:
            # Elimina el documento del proveedor
            proveedor_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}

async def update_cliente(nombre: str, email: str, telefono: str, cuil:str, direccion:str):
    try:
        # Obtiene la referencia al documento del cliente
        cliente_ref = db.collection('clientes').document(nombre)

        # Verifica si el cliente existe
        if cliente_ref.get().exists:
            # Actualiza el correo electrónico del cliente
            cliente_ref.update({"email": email, "telefono":telefono, "cuil":cuil, "direccion":direccion})
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}

async def update_proveedor(nombre: str, email: str, telefono: str, cuil:str, direccion: str):
    try:
        # Obtiene la referencia al documento del cliente
        proveedor_ref = db.collection('proveedores').document(nombre)

        # Verifica si el cliente existe
        if proveedor_ref.get().exists:
            # Actualiza el correo electrónico del cliente
            proveedor_ref.update({"email": email, "telefono":telefono, "cuil":cuil, "direccion":direccion})
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return {'error': f'Ocurrió un error inesperado: {e}'}
    

