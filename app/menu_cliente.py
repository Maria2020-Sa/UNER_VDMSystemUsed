from service.compra.service_cliente_proveedor import busqueda_por_dni
from service.venta.service_cliente import *
from model.model_cliente import Cliente

def solicitar_datos_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("DNI: "))
    direccion = input("Dirección: ")
    telefono = int(input("Teléfono: "))
    email = input("Email: ")
    delete = input("<0-Activo | 1-No Activo>: ")

    return Cliente('0',nombre,apellido,dni,direccion,telefono,email,delete)

def gestionar_clientes():
    while True:
        print("""
    ___________MENÚ OPCIONES___________
    1. Agregar cliente
    2. Editar/actualizar datos
    3. Eliminar cliente
    4. Mostrar clientes
    5. Salir""")
        opcion = input("    Selecciona una opción: ")

        match opcion:
            case "1":
                cliente = solicitar_datos_cliente()
                agregar_cliente(cliente)
            case "2":
                id_cliente = int(input("Número ID del cliente que desea actualizar: "))
                cliente = solicitar_datos_cliente()
                editar_dato_cliente(id_cliente, cliente)
            case "3":
                id_cliente = int(input("Numero de la lista a borrar: "))
                borrado_logico_cliente(id_cliente)
            case "4":
                print("\nLISTA DE CLIENTES ACTIVOS: ")
                mostrar_clientes()
            case "5":
                break
            case _:
                print("Opción inválida. Inténtalo nuevamente.")
    
print(busqueda_por_dni(98))
gestionar_clientes()
