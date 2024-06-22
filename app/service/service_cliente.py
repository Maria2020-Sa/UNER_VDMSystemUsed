
from ..model.model_cliente import Cliente



nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el Nro. DNI: "))
direccion = input("Ingrese la dirección: ")
telefono = input("Insegre el Nro. Telefono: ")
email = input("Ingrese el email: ")

cliente = Cliente(nombre,apellido,dni,direccion,telefono,email)
print(cliente)
