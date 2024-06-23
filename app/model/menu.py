from app.service.service_vehiculo import *
from model_vehiculo import Vehiculo

def solicitar_datos_vehiculos():
  dominio = input("Dominio: ")
  marca = input("Marca: ")
  modelo = input("Modelo: ")
  tipo = input("Tipo: ")
  anio = int(input("Año: "))
  kilometraje = float(input("Kilometraje: "))
  precio_compra = float(input("Precio de compra: "))
  precio_venta = float(input("Precio de Venta: "))
  estado = input("Estado actual: ")
  delete = input("<0-Activo | 1-No Activo>: ")
  return Vehiculo(dominio,marca,modelo,tipo,anio,kilometraje,precio_compra,precio_venta,estado,delete)



def gestionar_vehiculo():
    while True:
        print("""
    ___________MENÚ OPCIONES___________
    1. Agregar vehículo
    2. Editar/actualizar datos
    3. Eliminar vehículo
    4. Mostrar inventario disponible actualizado
    5. Salir""")
        opcion = input("**Selecciona una opción: ")

        match opcion:
            case "1":
                vehiculo = solicitar_datos_vehiculos()
                agregar_vehiculo(vehiculo)
                print("Vehículo agregado correctamente.")
            case "2":
                id_vehiculo = int(input("Ingrese el ID del vehículo que desea actualizar: "))
                vehiculo = solicitar_datos_vehiculos()
                editar_dato(id_vehiculo, vehiculo)
            case "3":
                id_vehiculo = int(input("Numero de la lista a borrar: "))
                borrado_logico(id_vehiculo)
            case "4":
                mostrar_inventario()
            case "5":
                break
            case _:
                print("Opción inválida. Inténtalo nuevamente.")
    
gestionar_vehiculo()