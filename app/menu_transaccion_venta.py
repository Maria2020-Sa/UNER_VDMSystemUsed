from service.venta.service_transaccion_venta import crear_archivo, agregar_transaccion_venta

formulario_venta = '''
{
    "id_vehiculo": 15,
    "id_cliente": 5,
    "tipo": "venta",
    "fecha": "fff",
    "monto": 2.0,
    "observaciones": "ff",
    "delete": 0
}'''

formulario_venta_2 = '''
{
    "id_vehiculo": 0,
    "id_cliente": null,
    "nombre": "aaa",
    "apellido": "aaa",
    "dni": 2,
    "direccion": "aaa",
    "telefono": 2,
    "email": "aa",
    "monto": 2.0,
    "observaciones": "ff",
    "delete": 0,
    "tipo": "venta",
    "fecha": "ll"
}'''

crear_archivo()
agregar_transaccion_venta(formulario_venta)