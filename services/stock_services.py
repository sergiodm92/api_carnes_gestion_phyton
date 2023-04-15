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
        docs = db.collection('faenas').where('kg_stock', '>', 0).stream()
        # docs = db.collection('faenas').where('saldo', '>', 0).get()
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
    total_kg_vaca = 0
    vaquillona = 0
    vaca = 0
    novillito = 0
    toro = 0
    novillo_pesado = 0
    total_kg_cerdo = 0
    capon = 0
    chancha = 0
    
    for faena in faenas_stock:
        if faena['type'] == 'vaca':
            for res in faena['detalle']:
                categoria = res['categoria']
                kg = res['kg']
                if categoria == 'vaquillona':
                    vaquillona += 1
                elif categoria == 'Vaca':
                    vaca += 1
                elif categoria == 'novillito':
                    novillito += 1
                elif categoria == 'toro':
                    toro += 1
                elif categoria == 'novillo Pesado':
                    novillo_pesado += 1
                total_kg_vaca += kg
        elif faena['type'] == 'cerdo':
            for res in faena['detalle']:
                categoria = res['categoria']
                kg = res['kg']
                
                if categoria == 'capon':
                    capon += 1
                elif categoria == 'chancha':
                    chancha += 1
                
                total_kg_cerdo += kg
    return {
        'vaquillona': vaquillona,
        'vaca': vaca,
        'novillito': novillito,
        'toro': toro,
        'novillo pesado': novillo_pesado,
        'total kg vaca': total_kg_vaca,
        'capon': capon,
        'chancha': chancha,
        'total kg cerdo': total_kg_cerdo
    }



