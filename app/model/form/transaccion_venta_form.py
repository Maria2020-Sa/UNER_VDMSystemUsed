class TransaccionVentFormModel:
    def __init__(self,
                 id_vehiculo:int, 
                 id_cliente:int, 
                 nombre:str,
                 apellido:str,
                 dni:str,
                 direccion:str, 
                 telefono:str, 
                 email:str,
                 monto:str,
                 observaciones:str,
                 delete:str, 
                 tipo:str, 
                 fecha:str):
        self.id_vehiculo = id_vehiculo
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.monto = monto
        self.observaciones = observaciones
        self.delete = delete
        self.tipo = tipo
        self.fecha = fecha

    def to_dict(self):
            return {
                 "id_vehiculo": self.id_vehiculo,
                 "id_cliente": self.id_cliente,
                 "nombre": self.nombre,
                 "apellido": self.apellido,
                 "dni": self.dni,
                 "direccion": self.direccion,
                 "telefono": self.telefono,
                 "email": self.email,
                 "monto": self.monto,
                 "observaciones": self.observaciones,
                 "delete": self.delete,
                 "tipo": self.tipo,
                 "fecha": self.fecha
                 }