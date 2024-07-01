from model.model_vehiculo import Vehiculo
from model.model_cliente import Cliente

class TransaccionFormModel:
    def __init__(self,cliente:Cliente, vehiculo:Vehiculo, tipo:str,fecha:str,observaciones:str):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha = fecha        
        self.tipo = tipo
        self.observaciones = observaciones

    def to_dict(self):
            return {
                "vehiculo": {
                    "id_vehiculo": self.vehiculo.id_vehiculo,
                    "dominio": self.vehiculo.dominio,
                    "marca": self.vehiculo.marca,
                    "modelo": self.vehiculo.modelo,
                    "tipo": self.vehiculo.tipo,
                    "anio": self.vehiculo.anio,
                    "kilometraje": self.vehiculo.kilometraje,
                    "precio_compra": self.vehiculo.precio_compra,
                    "precio_venta": self.vehiculo.precio_venta,
                    "estado": self.vehiculo.estado,
                    "delete": self.vehiculo.delete
                },
                "cliente": {
                    "id_cliente": self.cliente.id_cliente,
                    "nombre": self.cliente.nombre,
                    "apellido": self.cliente.apellido,
                    "dni": self.cliente.dni,
                    "direccion": self.cliente.direccion,
                    "telefono": self.cliente.telefono,
                    "email": self.cliente.email,
                    "delete": self.cliente.delete
                },
                "fecha": self.fecha,
                "tipo": self.tipo,
                "observaciones": self.observaciones
            }