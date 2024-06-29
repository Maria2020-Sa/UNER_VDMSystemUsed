import json
import os
from model.model_cliente import *
from model.model_transaccion import *
from model.model_vehiculo import *
from service.venta.service_cliente import agregar_cliente
from service.venta.service_cliente import leer_datos_consumidor


archivo_transaccion_venta = "transaccion_venta.json"

def crear_archivo():
    if not os.path.exists(archivo_transaccion_venta):
        with open(archivo_transaccion_venta, 'w') as archivo:
            json.dump([], archivo)

#Deserializa el obj JSON a Array Python
def leer_datos():
    with open(archivo_transaccion_venta, "r") as archivo:
        return json.load(archivo)
    
def escribir_datos(dato):
    with open(archivo_transaccion_venta, 'w', encoding='utf-8') as archivo:
        json.dump(dato, archivo, ensure_ascii=False, indent=4)

def mapear_datos_cliente(formulario_venta):
    nombre = formulario_venta['nombre']
    apellido = formulario_venta['apellido']
    dni = formulario_venta['dni']
    direccion = formulario_venta['direccion']
    telefono = formulario_venta['telefono']
    email = formulario_venta['email']
    delete = formulario_venta['delete']
    return Cliente(nombre, apellido, dni, direccion, telefono, email, delete)

def mapear_datos_transaccion(id_transaccion, formulario_venta, id_cliente):
    id_transaccion_venta = id_transaccion
    id_vehiculo = formulario_venta['id_vehiculo']
    id_cliente = id_cliente
    monto = formulario_venta['monto']
    fecha = formulario_venta['fecha']
    tipo = formulario_venta['tipo']
    observaciones = formulario_venta['observaciones']
    return Transaccion(id_transaccion_venta, id_vehiculo, id_cliente, tipo, fecha, monto, observaciones)

def agregar_transaccion_venta(formulario_venta_json):
    transaccion_venta_bd = leer_datos()
    formulario_venta = json.loads(formulario_venta_json)

    if formulario_venta['id_cliente'] != None:
        id_cliente = formulario_venta['id_cliente']
        transaccion_venta = mapear_datos_transaccion(len(transaccion_venta_bd), formulario_venta, id_cliente)
        transaccion_venta_bd.append(transaccion_venta.to_dict())
        escribir_datos(transaccion_venta_bd)
    else:
        cliente = mapear_datos_cliente(formulario_venta)
        id_cliente = agregar_cliente(cliente)
        transaccion_venta = mapear_datos_transaccion(len(transaccion_venta_bd), formulario_venta, id_cliente)
        transaccion_venta_bd.append(transaccion_venta.to_dict())
        escribir_datos(transaccion_venta_bd)