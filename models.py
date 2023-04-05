from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

class Proveedor(BaseModel):
    nombre: str
    email: str
    direccion: str
    cuil: str

class Cliente(BaseModel):
    nombre: str
    email: str
    direccion: str
    cuil: str

class Compra(BaseModel):
    id: str
    monto: float
    cantidad: int
    proveedor: str
    lugar: str
    kg: float



class Venta(BaseModel):
    monto: float
    cantidad: int
    proveedor: str
    lugar: str
    kg: float