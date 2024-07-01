import json
from model.model_cliente import Cliente


archivo_clientes_consumidores = "clientes_consumidores.json"

#Deserializa el obj JSON. 
def leer_datos_consumidor():
    try:
        with open(archivo_clientes_consumidores, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Serializa el Array a obj JSON
def escribir_datos(dato):
    with open(archivo_clientes_consumidores, 'w') as archivo:
        json.dump(dato, archivo, indent=4)

def agregar_cliente(cliente: Cliente):
    clientes = leer_datos_consumidor()
    cliente.set_id_cliente(len(clientes)) 
    clientes.append(cliente.to_dict())
    escribir_datos(clientes)
    return cliente.id_cliente

#Editar:
def editar_dato_cliente_consumidor(id_cliente, cliente: Cliente):
    try:
        clientes = leer_datos_consumidor()
        for value in clientes:
            if value['id_cliente'] == id_cliente:
                value['nombre'] = cliente.nombre
                value['apellido'] = cliente.apellido
                value['dni'] = cliente.dni
                value['direccion'] = cliente.direccion
                value['telefono'] = cliente.telefono
                value['email'] = cliente.email
        escribir_datos(clientes)
        return 200
    except Exception as e:
        return 500

#Eliminar:
def borrado_logico_cliente_consumidor(id_cliente):
    try:
        cliente = leer_datos_consumidor()
        for value in cliente:
            if(value['id_cliente'] == id_cliente):
                value['delete']=1
        escribir_datos(cliente)
        return 200
    except Exception as e:
        return 500        

#Listados.
def mostrar_clientes_consumidores():
    try:
        datos = leer_datos_consumidor()
        clientes_consumidor = []
        for value in datos:
            if(value['delete'] != 1):
                clientes_consumidor.append(value)
        return clientes_consumidor
    except Exception as e:
        return 500


def busqueda_por_dni_consumidor(dni):
    try:
        clientes = leer_datos_consumidor()
        for value in clientes:
            if(value['dni'] == dni):
                return value
    except Exception as e:
        return ''            