import json
import os
from model.model_cliente import *
from model.model_transaccion import *
from model.model_vehiculo import *
from service.service_vehiculo import agregar_vehiculo
from service.compra.service_cliente_proveedor import agregar_cliente_proveedor

archivo_transaccion_compra = "transaccion_compra.json"

def crear_archivo():
    if not os.path.exists(archivo_transaccion_compra):
        with open(archivo_transaccion_compra, 'w') as archivo:
            json.dump([], archivo)

def leer_datos():
    try:
        with open(archivo_transaccion_compra, "r") as archivo:
            return (json.load(archivo))
    except FileNotFoundError:
        return []
    
def escribir_datos(dato):
    with open(archivo_transaccion_compra, 'w', encoding='utf-8') as archivo:
        json.dump(dato, archivo, ensure_ascii=False, indent=4)

def mapear_datos(id_transaccion, vehiculos: Vehiculo, cliente_proveedor, formulario_diccionario):
    id_transaccion_compra = id_transaccion
    id_vehiculo_compra = agregar_vehiculo(vehiculos)
    id_cliente_proveedor = agregar_cliente_proveedor(cliente_proveedor)
    monto = vehiculos.precio_compra
    fecha = formulario_diccionario["fecha"]
    tipo = formulario_diccionario["tipo"]
    observaciones = formulario_diccionario["observaciones"]
    return Transaccion(id_transaccion_compra, id_vehiculo_compra, id_cliente_proveedor, tipo, fecha, monto, observaciones).to_dict()

def agregar_transaccion_compra(formulario_json):
    try:
        crear_archivo()
        transaccion_compra_bd = leer_datos()
        formulario_diccionario = json.loads(formulario_json)
        print("formularios", formulario_diccionario)

        # Crear instancias de las clases
        vehiculos = Vehiculo(**formulario_diccionario["vehiculo"])
        cliente_proveedor = Cliente(**formulario_diccionario["cliente"])

        transaccion_compra = mapear_datos(len(transaccion_compra_bd), vehiculos, cliente_proveedor, formulario_diccionario)
        transaccion_compra_bd.append(transaccion_compra)
        escribir_datos(transaccion_compra_bd)
        return 200
    except Exception as e:
        print(e)
        return 500 