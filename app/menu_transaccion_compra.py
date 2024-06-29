from model.model_transaccion import *
from service.compra.sevice_transaccion_compra import agregar_transaccion_compra, crear_archivo

nuevo_json = '''
{
    "vehiculo": {
        "dominio": "ddd",
        "marca": "dd",
        "modelo": "d",
        "tipo": "d",
        "anio": 2,
        "kilometraje": 2.0,
        "precio_compra": 2.0,
        "precio_venta": 2.0,
        "estado": "d",
        "delete": 0
    },
    "cliente": {
        "nombre": "ddd",
        "apellido": "dd",
        "dni": 2,
        "direccion": "ddd",
        "telefono": 2,
        "email": "aa",
        "delete": 1
    },
    "fecha": "4545545",
    "tipo": "compra",
    "observaciones": "un año de uso"
}
'''

crear_archivo()
agregar_transaccion_compra(nuevo_json)