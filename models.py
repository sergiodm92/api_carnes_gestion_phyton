from pydantic import BaseModel, validator
from typing import List

class User(BaseModel):
    name: str
    password: str

    @validator('name')
    def name_length(cls, v):
        if len(v) < 6 or len(v) > 255:
            raise ValueError('El nombre debe tener entre 6 y 255 caracteres')
        return v

    @validator('password')
    def password_length(cls, v):
        if len(v) < 6 or len(v) > 1024:
            raise ValueError('La contraseña debe tener entre 6 y 1024 caracteres')
        return v

class Proveedor(BaseModel):
    nombre: str
    email: str
    direccion: str
    telefono: str
    cuil: str

class Cliente(BaseModel):
    nombre: str
    email: str
    direccion: str
    telefono: str
    cuil: str

#definicion de Grupo de animales y compra

class Grupo_Vacas(BaseModel):
    cantidad: int
    tropa: str
    categoria: str
    comision: float
    costoVeps: float
    costo_faena: float
    costo_faena_kg: float
    costo_flete: float
    costo_hacienda: float
    costo_kg: float
    costo_kg_vivos_neto: float
    costo_total: float
    desbaste: float
    kg: float
    kg_vivos_brutos: float
    kg_vivos_netos: float
    recupero: float
    rinde: float
    kg_promedio: float
    

class Compra_Vacas(BaseModel):
    id: str
    type: str
    proveedor: str
    lugar: str
    fecha: int
    n_dte: str
    cantidad: int
    kg_total: float
    kg_brutos_total: float
    kg_netos_total: float
    precio_achuras_unitario: float
    recupero_precio_kg: float
    porcentaje_comision: float
    costo_flete: float
    costo_hacienda_total: float
    costo_veps_unitario: float
    grupos: List
    saldo: float

class Grupo_Cerdos(BaseModel):
    cantidad: int
    tropa: str
    categoria: str
    comision: float
    costoVeps: float
    costo_faena: float
    costo_faena_kg: float
    costo_flete: float
    costo_hacienda: float
    costo_kg: float
    costo_kg_vivos_neto: float
    costo_total: float
    desbaste: float
    kg: float
    kg_vivos_brutos: float
    kg_vivos_netos: float
    rinde: float
    kg_promedio: float


class Compra_Cerdos(BaseModel):
    id: str
    type: str
    proveedor: str
    lugar: str
    fecha: int
    n_dte: str
    cantidad: int
    kg_total: float
    kg_brutos_total: float
    kg_netos_total: float
    porcentaje_comision: float
    costo_flete: float
    costo_hacienda_total: float
    costo_veps_unitario: float
    grupos: List[Grupo_Cerdos]
    saldo: float

#definicion de Detalle de reses y venta

class Res_Vaca_Venta(BaseModel):
    categoria: str
    correlativo: str
    kg: float
    kg_total: float
    costo_kg: float
    cuartoD: float
    cuartoT: float
    total_media: str
    precio_kg: float

class Venta_Vaca(BaseModel):
    id: str
    cantidad: int
    cliente: str
    fecha: int
    costo: float
    detalle: List[Res_Vaca_Venta]
    kg: float
    total: float
    saldo: float

class Res_Cerdo(BaseModel):
    categoria: str
    correlativo: str
    kg: float
    kg_total: float
    costo_kg: float
    precio_kg: float

class Venta_Cerdo(BaseModel):
    id: str
    cantidad: int
    cliente: str
    fecha: int
    costo: float
    detalle: List[Res_Cerdo]
    kg: float
    total: float
    saldo: float

class Venta_Achura(BaseModel):
    id:str
    cliente: str
    fecha: int
    cantidad: int
    precio_unitario: float
    total: float
    saldo:float

#Faena y detalle de faena

# class Res_Vaca_Faena(BaseModel):
#     categoria: str
#     correlativo: str
#     kg: float
#     costo_kg: float
#     cuartoD: float
#     cuartoT: float
#     stock: bool
#     venta_id: str

# class Detalle(BaseModel):
#     res: List[Res_Vaca_Faena]

class Faena(BaseModel):
    id: str
    type: str
    tropa: str
    proveedor: str
    frigorifico: str
    fecha: int
    n_medias: int
    estado_compra: bool
    compra_id: str
    costo_faena_kg: float
    costo_total: float
    kg_total: float
    saldo: float
    detalle: List

# Pagos compra venta venta_achura faena

class Pago_Compra(BaseModel):
    id: str
    fecha:int
    proveedor: str
    forma_pago: str
    compra_id: str
    imagen_comprobante: str
    total: float

class Pago_Venta(BaseModel):
    id: str
    fecha:int
    cliente: str
    forma_pago: str
    venta_id: str
    imagen_comprobante: str
    total: float

class Pago_Faena(BaseModel):
    id: str
    fecha:int
    frigorifico: str
    forma_pago: str
    faena_id: str
    imagen_comprobante: str
    total: float

class Ingreso_Extra(BaseModel):
    id:str
    fecha: int
    concepto: str
    forma_pago: str
    total: float
    imagen_comprobante: str

class Extraccion(BaseModel):
    id:str
    fecha: int
    concepto: str
    forma_pago: str
    total: float
    imagen_comprobante: str

class Caja(BaseModel):
    fecha: int
    total: float

class Gasto_Combustible(BaseModel):
    id: str
    fecha: int
    type: str
    litros: float
    precio_litro: float
    total: float
    forma_pago: str
    imagen_comprobante: str

class Gasto_Transporte(BaseModel):
    id: str
    fecha: int
    concepto: str
    total: float
    forma_pago: str
    imagen_comprobante: str

class Gasto_Impositivo(BaseModel):
    id: str
    fecha: int
    type: str
    nota: str
    total: float
    forma_pago: str
    imagen_comprobante: str 