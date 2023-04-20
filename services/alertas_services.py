from db import get_database
import datetime
import time

db = get_database()


# Traer a todos los clientes
async def get_alertas(dias:int):
    try:
        faenas = []
        # Obtiene todos los documentos de la colección "compras"
        fecha = fecha_milisegundos(dias)
        docs = db.collection('faenas').where('kg_stock', '>', 0).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            faena = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            faenas.append(faena)
        response = list(filter(lambda x:x['fecha']<fecha, faenas))
        return get_stock_reses(response)
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}
    

def fecha_milisegundos(dias):
    fecha_actual = datetime.datetime.now()
    fecha_dias_atras = fecha_actual - datetime.timedelta(days=dias)
    fecha_ms_js = int(time.mktime(fecha_dias_atras.timetuple())) * 1000
    return fecha_ms_js

def get_stock_reses(faenas):
    stock_reses = []
    for faena in faenas:
        for res in faena['detalle']:
            if res['stock'] == True:
                stock_reses.append({'res':res,'fecha':faena['fecha'], 'tropa':faena['tropa'], 'friogorifico':faena['frigorifico']})
    return stock_reses


