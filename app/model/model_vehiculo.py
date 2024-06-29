class Vehiculo:
   
   def __init__(self,dominio:str, marca:str,modelo:str,
                tipo:str,anio:int,kilometraje:float,
                precio_compra:float,precio_venta:float,
                estado:str, delete:str):
      self.dominio = dominio
      self.marca = marca
      self.modelo = modelo
      self.tipo = tipo
      self.anio = anio
      self.kilometraje = kilometraje
      self.precio_compra = precio_compra
      self.precio_venta = precio_venta
      self.estado = estado
      self.delete = delete

   def setIdVehiculo(self,id_vehiculo):
      self.id_vehiculo = id_vehiculo

   def to_dict(self):
        return {
            'id_vehiculo': self.id_vehiculo,
            'dominio': self.dominio,
            'marca': self.marca,
            'modelo': self.modelo,
            'tipo': self.tipo,
            'anio': self.anio,
            'kilometraje': self.kilometraje,
            'precio_compra': self.precio_compra,
            'precio_venta': self.precio_venta,
            'estado': self.estado,
            'delete': self.delete
        }   

   def __str__(self):
      return f"""
**|ID: {self.id_vehiculo} |Dominio': {self.dominio} |Marca: {self.marca} |Modelo: {self.modelo} |Tipo: {self.tipo} |Año: {self.anio} |Kilometraje: {self.kilometraje} |Precio de Compra: {self.precio_compra} |Precio de Venta: {self.precio_venta} |Estado: {self.estado} |Delete: {self.delete}"""