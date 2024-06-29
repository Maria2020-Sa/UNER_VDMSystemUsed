import datetime


class Transaccion:
    def __init__(self,id_transaccion: int,id_vehiculo:int,id_cliente:int,tipo:str,fecha:str,monto:float,observaciones:str):
        self.id_transaccion = id_transaccion
        self.id_vehiculo = id_vehiculo
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.fecha = fecha
        self.monto = monto
        self.observaciones = observaciones

    def set_id_transaccion(self, id_transaccion):
        self.id_transaccion_venta = id_transaccion,
    def to_dict(self):
            return {
                'id_transaccion': self.id_transaccion,
                'id_vehiculo': self.id_vehiculo,
                'id_cliente': self.id_cliente,
                'tipo': self.tipo,
                'fecha': self.fecha,
                'monto': self.monto,
                'observaciones': self.observaciones
            }

    def __str__(self):
            return f"""
    **|ID Transaccion: {self.id_transaccion}: 
        |ID Vehículo: {self.id_vehiculo} |ID Cliente: {self.id_cliente} |Tipo: {self.tipo}  |Fecha: {self.fecha}"""