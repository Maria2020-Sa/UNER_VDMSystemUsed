import json
from model.model_vehiculo import Vehiculo


archivo_vehiculos = "vehiculos.json"

#Deserializa el obj JSON a Array Python
def leer_datos():
    try:
        with open(archivo_vehiculos, "r") as archivo:
            return (json.load(archivo))
    except FileNotFoundError:
        return []

#Serializa el Array a obj JSON
def escribir_datos(dato):
    with open(archivo_vehiculos, 'w') as archivo:
        json.dump(dato, archivo, indent=4)

def agregar_vehiculo(vehiculo: Vehiculo):
    vehiculos = leer_datos()
    vehiculo.setIdVehiculo(len(vehiculos)) 
    vehiculos.append(vehiculo.to_dict())
    escribir_datos(vehiculos)
    return vehiculo.id_vehiculo

#Editar:
def editar_dato(id_vehiculo, vehiculo: Vehiculo):
    vehiculos = leer_datos()
    for value in vehiculos:
        if value['id_vehiculo'] == id_vehiculo:
            value['dominio'] = vehiculo.dominio
            value['marca'] = vehiculo.marca
            value['modelo'] = vehiculo.modelo
            value['tipo'] = vehiculo.tipo
            value['anio'] = vehiculo.anio
            value['kilometraje'] = vehiculo.kilometraje
            value['precio_compra'] = vehiculo.precio_compra
            value['precio_venta'] = vehiculo.precio_venta
            value['estado'] = vehiculo.estado
    escribir_datos(vehiculos)

#Eliminar:
def borrado_logico(id_vehiculo):
    vehiculos = leer_datos()
    for value in vehiculos:
        if(value['id_vehiculo']==id_vehiculo):
            value['delete']=1
    escribir_datos(vehiculos)        

#Listados de búsqueda por (patente, marca, modelo y precios de compra/venta).
def mostrar_inventario():
    datos = leer_datos()
    vehiculos = [Vehiculo(**dato) for dato in datos]
    for vehiculo in vehiculos:
        if(vehiculo.delete != 1):
            print(vehiculo)