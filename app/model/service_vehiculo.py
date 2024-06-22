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

def agregar_vehiculo(marca, modelo, anio, precio):
    vehiculos = leer_datos()
    nuevo_vehiculo = {
        "id": (len(vehiculos)-1) + 1,
        "marca": marca,
        "modelo": modelo,
        "año": anio,
        "precio": precio,
        "delete": 0
    }
    vehiculos.append(nuevo_vehiculo)
    escribir_datos(vehiculos)








#Editar:
def editar_dato():
    print("En producción")

#Eliminar:
def borrado_logico(id):
    for value in archivo_vehiculos:
        if(value['id']==id):
            value['delete']=1

#Listados de búsqueda por (patente, marca, modelo y precios de compra/venta).
def mostrar_inventario():
    vehiculos = leer_datos()
    for vehiculo in vehiculos:
        print(vehiculo)
