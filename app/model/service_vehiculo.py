import json
import os


archivo_vehiculos = "vehiculos.json"

#Crear:
# Verifica si el archivo existe; si no, créalo
def crear_archivo():
    if not os.path.exists(archivo_vehiculos):
        with open(archivo_vehiculos, 'w') as archivo:
            json.dump([], archivo)
    else:
        with open(archivo_vehiculos, "r") as archivo:
            return (json.load(archivo))

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

def agregar_vehiculo(dominio, marca, modelo, tipo, anio, kilometraje, precio_compra, precio_venta, estado):
    vehiculos = leer_datos()
    nuevo_vehiculo = {
        "id_vehiculo": len(vehiculos),
        "dominio": dominio,
        "marca": marca,
        "modelo": modelo,
        "tipo": tipo,
        "anio": anio,
        "kilometraje": kilometraje,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta,
        "estado": estado,
        "delete": 0
    }
    vehiculos.append(nuevo_vehiculo)
    escribir_datos(vehiculos)

#Editar:
def editar_dato(id_vehiculo, dominio, marca, modelo, tipo, anio, kilometraje, precio_compra, precio_venta, estado):
    vehiculos = leer_datos()
    for value in vehiculos:
        if value['id_vehiculo'] == id_vehiculo:
            value['dominio'] = dominio
            value['marca'] = marca
            value['modelo'] = modelo
            value['tipo'] = tipo
            value['anio'] = anio
            value['kilometraje'] = kilometraje
            value['precio_compra'] = precio_compra
            value['precio_venta'] = precio_venta
            value['estado'] = estado
    escribir_datos(vehiculos)

#Eliminar:
def borrado_logico(id):
    vehiculos = leer_datos()
    for value in vehiculos:
        if(value['id']==id):
            value['delete']=1

#Listados de búsqueda por (patente, marca, modelo y precios de compra/venta).
def mostrar_inventario():
    vehiculos = leer_datos()
    for vehiculo in vehiculos:
        print(vehiculo)
