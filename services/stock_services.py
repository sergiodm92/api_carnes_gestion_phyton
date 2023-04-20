from db import get_database

db = get_database()

async def get_stock():
    try:
        faenas_stock = await get_faenas_stock()
        stock = sumar_stock(faenas_stock)
        return stock
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Traer faenas
async def get_faenas_stock():
    try:
        faenas_stock_true = []
        # Obtiene todos los documentos de la colección "ventas"
        docs = db.collection('faenas').where('kg_stock', '>', 0).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            faena = doc.to_dict()
            # Agrega el diccionario a la lista de faenas con stock
            faenas_stock_true.append(faena)
        return faenas_stock_true
    except Exception as e:
        print(e)
        return {'error': 'Ocurrió un error inesperado: {}'.format(e)}


# Calcular Stock
def sumar_stock(faenas_stock):
    stock = {
        'total_kg_vaca' : {'kg':0},
        'total_kg_cerdo' : {'kg':0},
        'vaquillona' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'vaca' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'novillito' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'toro' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'novillo_pesado' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'capon' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
        'chancha' : {'res':0,'cuartoD':0,'cuartoT':0, 'kg':0},
    }
    
    for faena in faenas_stock:
        for res in faena['detalle']:
            categoria = res['categoria']
            cuartoT = res['cuartoT'] 
            cuartoD = res['cuartoD'] 
            kg = res['kg']
            if cuartoT==0 & cuartoD==0: 
                stock[categoria]['res']+= 1
                stock[categoria]['kg']+= kg
                if faena['type']=='vaca': 
                    stock['total_kg_vaca']['kg']+=kg
                if faena['type']=='cerdo': 
                    stock['total_kg_cerdo']['kg']+=kg
            if cuartoD > 0:
                stock[categoria]['cuartoD']+= 1
                stock[categoria]['kg']+= cuartoD
                if faena['type']=='vaca': 
                    stock['total_kg_vaca']['kg']+=cuartoD
                else: stock['total_kg_cerdo']['kg']+=cuartoD
            if cuartoT > 0:
                stock[categoria]['cuartoT']+= 1
                stock[categoria]['kg']+= cuartoT
                if faena['type']=='vaca': 
                    stock['total_kg_vaca']['kg']+=cuartoT
                else: stock['total_kg_cerdo']['kg']+=cuartoT
    return stock


