import json
import os
from model.model_cliente import *
from model.model_transaccion import *
from model.model_vehiculo import *
from service.venta.service_cliente import agregar_cliente
from service.service_vehiculo import busqueda_por_id, busqueda_vehiculo_por_id

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
    return Cliente('a',nombre, apellido, dni, direccion, telefono, email, delete)

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
    crear_archivo()
    try:

        transaccion_venta_bd = leer_datos()
        formulario_venta = json.loads(formulario_venta_json)

        if formulario_venta['id_cliente'] != None:
            id_cliente = formulario_venta['id_cliente']
            transaccion_venta = mapear_datos_transaccion(len(transaccion_venta_bd), formulario_venta, id_cliente)
            transaccion_venta_bd.append(transaccion_venta.to_dict())
            escribir_datos(transaccion_venta_bd)
            busqueda_por_id(transaccion_venta.id_vehiculo)
        else:
            print("elseeeee")
            cliente = mapear_datos_cliente(formulario_venta)
            id_cliente = agregar_cliente(cliente)
            transaccion_venta = mapear_datos_transaccion(len(transaccion_venta_bd), formulario_venta, id_cliente)
            transaccion_venta_bd.append(transaccion_venta.to_dict())
            escribir_datos(transaccion_venta_bd)
            busqueda_por_id(transaccion_venta.id_vehiculo)
        return 200
    except Exception as e:
        print(e)
        return 500        

def busqueda_por_id_transaccion_venta(id_cliente):
        try:

            transaccion_compra_bd = leer_datos()

            id_transacciones_response = []
            for transaccion in transaccion_compra_bd:
                if(transaccion['id_cliente'] == id_cliente):
                    id_transacciones_response.append(transaccion['id_vehiculo'])

            vehiculos_response = []
            for id in id_transacciones_response:
                vehiculos_response.append(busqueda_vehiculo_por_id(id))

            return vehiculos_response
        except Exception as e:
            return [] 