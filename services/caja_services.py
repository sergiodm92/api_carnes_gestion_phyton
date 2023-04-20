# from db import get_database

# db = get_database()

# # Traer caja
# async def get_caja():
#     try:
#         caja = {
#             'total':0,
#             'fecha':0,
#             'ultimo_movimiento':{}
#         }
#         # Obtiene todos los documentos de la colección "compras"
#         docs = db.collection('caja').document('caja').get().to_dict()
#         caja['total']=docs['total']
#         caja['ultimo_movimiento']=docs['movimientos'][-1]
#         caja['fecha']=caja['ultimo_movimiento'].fecha
#         return caja
#     except Exception as e:
#         print(e)
#         return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    

# #nuevo post de caja
# async def update_caja(pago):
#     try:
#         # Crea el nuevo documento en Firestore con los datos de la compra
#         doc_ref = db.collection('caja').document('caja').get().to_dict()
#         if(pago.type == 'venta' | pago.type == 'iextra'):
#             doc_ref['total']+=pago.total
#         else: 
#             doc_ref['total']-=pago.total
#         doc_ref['movimientos'].append(pago)
#         db.collection('caja').document('caja').set(doc_ref)
#         # Verifica que el documento se haya creado correctamente
#         doc_snapshot = doc_ref.get()
#         if doc_snapshot.exists:
#             return True
#         else:
#             return False
#     except Exception as e:
#         print(e)
#         return False