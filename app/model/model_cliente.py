
class Cliente:
   
   def __init__(self, nombre:str, apellido:str,dni:int,direccion:str,telefono:str,email:str):
      self.nombre = nombre
      self.apellido = apellido
      self.dni = dni
      self.direccion = direccion
      self.telefono = telefono
      self.email = email

   def __str__(self):
      return f"{{'nombre': {self.nombre}, 'apellido': {self.apellido}, 'dni': {self.dni}, 'direccion': {self.direccion}, 'telefono': {self.telefono}, 'email': {self.email}}}"
