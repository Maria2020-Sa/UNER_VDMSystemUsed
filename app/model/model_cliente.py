
class Cliente:

   def __init__(self,id_cliente, nombre:str, apellido:str,dni:int,direccion:str,telefono:str,email:str,delete:str):
      self.id_cliente = id_cliente
      self.nombre = nombre
      self.apellido = apellido
      self.dni = dni
      self.direccion = direccion
      self.telefono = telefono
      self.email = email
      self.delete = delete

   def __str__(self):
      return f"""
**|Nombre: {self.nombre} |Apellido: {self.apellido} |DNI: {self.dni}  Direccion: {self.direccion} |Teléfono: {self.telefono} |Email: {self.email} |Delete: {self.delete}"""

   def set_id_cliente(self, id_cliente):
      self.id_cliente = id_cliente
   
   def to_dict(self):
      return {
         'id_cliente': self.id_cliente,
         'nombre': self.nombre,
         'apellido': self.apellido,
         'dni': self.dni,
         'direccion': self.direccion,
         'telefono': self.telefono,
         'email': self.email,
         'delete': self.delete
      }