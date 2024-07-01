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
    try:
        vehiculos = leer_datos()
        for value in vehiculos:
            if value['id_vehiculo'] == id_vehiculo:
                value['dominio'] = vehiculo.dominio
                value['marca'] = vehiculo.marca
                value['modelo'] = vehiculo.modelo
                value['tipo'] = vehiculo.tipo
                value['anio'] = vehiculo.anio
                value['kilometraje'] = vehiculo.kilometraje
                value['precio_venta'] = vehiculo.precio_venta
                value['estado'] = vehiculo.estado
        escribir_datos(vehiculos)
        return 200
    except Exception as e:
        return 500

#Eliminar:
def borrado_logico(id_vehiculo):
    try:
        vehiculos = leer_datos()
        for value in vehiculos:
            if(value['id_vehiculo']==id_vehiculo):
                value['delete']=1
        escribir_datos(vehiculos)
        return 200
    except Exception as e:
        return 500            

#Listados de búsqueda por (patente, marca, modelo y precios de compra/venta).
def mostrar_inventario():
    datos = leer_datos()
    vehiculos = [mapear_vehiculo(dato) for dato in datos]

    print(vehiculos)
    vehiculos_disponibles = []
    for vehiculo in vehiculos:
        if(vehiculo.delete != 1):
            vehiculos_disponibles.append(vehiculo.to_dict())      
    return vehiculos_disponibles

def mapear_vehiculo(dato):
      return Vehiculo(
          id_vehiculo=dato['id_vehiculo'],
          dominio=dato['dominio'], 
          marca=dato['marca'],
          modelo=dato['modelo'],
          tipo=dato['tipo'],
          anio=dato['anio'],
          kilometraje=dato['kilometraje'],
          precio_compra= dato['precio_compra'],
          precio_venta=dato['precio_venta'],
          estado=dato['estado'],
          delete= dato.get('delete', None))


def busqueda_por_id(id):
    vehiculos = leer_datos()
    for value in vehiculos:
        if(value['id_vehiculo'] == id):
            value['estado']="vendido"
            value['delete']=1
    escribir_datos(vehiculos)

def reservar_vehiculo_por_id(id):
    try:
        vehiculos = leer_datos()
        for value in vehiculos:
            if(value['id_vehiculo'] == id):
                value['estado']="Reservado"
        escribir_datos(vehiculos)
        return 200
    except Exception as e:
        return 500         