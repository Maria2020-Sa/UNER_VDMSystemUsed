from service_vehiculo import *


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
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                anio = int(input("Año: "))
                precio = float(input("Precio: "))
                agregar_vehiculo(marca, modelo, anio, precio)
                print("Vehículo agregado correctamente.")
            case "2":
                editar_dato()
            case "3":
                id = int(input("Numero de la lista a borrar: "))
                borrado_logico(id)
            case "4":
                mostrar_inventario()
            case "5":
                break
            case _:
                print("Opción inválida. Inténtalo nuevamente.")
    
gestionar_vehiculo()