import json
import os
from model.model_cliente import Cliente

archivo_clientes_proveedor = "clientes_proveedor.json"

#Deserializa el obj JSON. 
def leer_datos():
    try:
        with open(archivo_clientes_proveedor, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Serializa el Array a obj JSON
def escribir_datos(dato):
    with open(archivo_clientes_proveedor, 'w') as archivo:
        json.dump(dato, archivo, indent=4)

def agregar_cliente_proveedor(cliente_proveedor: Cliente):
    clientes_proveedores = leer_datos()
    cliente_proveedor.set_id_cliente(len(clientes_proveedores)) 
    clientes_proveedores.append(cliente_proveedor.to_dict())
    escribir_datos(clientes_proveedores)
    return cliente_proveedor.id_cliente

#Editar:
def editar_dato_cliente_proveedor(id_cliente, cliente_proveedor: Cliente):
    try:
        clientes_proveedores = leer_datos()
        for value in clientes_proveedores:
            if value['id_cliente'] == id_cliente:
                value['nombre'] = cliente_proveedor.nombre
                value['apellido'] = cliente_proveedor.apellido
                value['dni'] = cliente_proveedor.dni
                value['direccion'] = cliente_proveedor.direccion
                value['telefono'] = cliente_proveedor.telefono
                value['email'] = cliente_proveedor.email
        escribir_datos(clientes_proveedores)
        return 200
    except Exception as e:
        return 500

#Eliminar:
def borrado_logico_cliente_proveedor(id_cliente):
    try:
        clientes_proveedores = leer_datos()
        for value in clientes_proveedores:
            if(value['id_cliente'] == id_cliente):
                value['delete'] = 1
        escribir_datos(clientes_proveedores)
        return 200
    except Exception as e:
        return 500        

#Listados:
def mostrar_clientes_proveedores():
    datos = leer_datos()
    clientes_proveedores = []
    for value in datos:
        if(value['delete'] != 1):
            clientes_proveedores.append(value)
    return clientes_proveedores

def busqueda_por_dni(dni):
    clientes = leer_datos()
    cliente_response = []
    for value in clientes:
        if(value['dni'] == dni):
            cliente_response.append(value)
    return cliente_response