import json
from flask import Flask, render_template, flash, redirect, request, url_for
from model.form.transaccion_form import TransaccionForm
from model.form.transaccion_vehiculo_form import TransaccionVehiculoForm
from model.form.transaccion_venta_form import TransaccionVentFormModel
from model.model_cliente import Cliente
from model.model_vehiculo import Vehiculo
from model.form.model_transaccion_form import TransaccionFormModel
from service.compra.sevice_transaccion_compra import agregar_transaccion_compra,busqueda_por_id_transaccion,mostrar_vehiculos_proveedores,busqueda_por_id_transaccion_vehiculo
from service.compra.service_cliente_proveedor import mostrar_clientes_proveedores, borrado_logico_cliente_proveedor, editar_dato_cliente_proveedor, busqueda_por_dni
from service.venta.service_transaccion_venta import agregar_transaccion_venta,busqueda_por_id_transaccion_venta
from service.venta.service_cliente import mostrar_clientes_consumidores,borrado_logico_cliente_consumidor, editar_dato_cliente_consumidor
from service.service_vehiculo  import mostrar_inventario, borrado_logico, editar_dato, reservar_vehiculo_por_id

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/form_page')
def form_page():
    form = TransaccionForm()
    return render_template('form.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = TransaccionForm()
    if form.validate_on_submit():
        cliente = ''
        response_cliente = busqueda_por_dni(form.dni.data)
        if(response_cliente != None):
            cliente = Cliente(**response_cliente)
        else:
            cliente = Cliente('a',form.nombre.data, form.apellido.data, form.dni.data, form.direccion.data, form.telefono.data, form.email.data, '0')
        vehiculo = Vehiculo('0',form.dominio.data, form.marca.data, form.modelo.data, form.tipo.data, form.año.data, form.kilometraje.data, form.precioDeCompra.data, form.precioDeVenta.data, form.estado.data, form.delete.data)
        fecha = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        tipo = 'compra'
        observaciones = 'form.observaciones'
        transaccionForm = TransaccionFormModel(cliente, vehiculo, tipo, fecha, observaciones).to_dict()
        json_resultado = json.dumps(transaccionForm)
        response = agregar_transaccion_compra(json_resultado)
        if int(response) == 200:
            flash(f'Guardado con exito!', 'success')
            return redirect(url_for('home'))
    else:
            return render_template('form.html', form=form)
    
    return render_template('form.html', form=form)

@app.route('/lista_venta')
def lista_venta():
    inventario_venta = mostrar_inventario()
    form_vehiculo = TransaccionVehiculoForm()

    return render_template('lista_venta.html', inventario_venta=inventario_venta, form_vehiculo=form_vehiculo)

# Ruta para manejar la eliminación de un vehículo
@app.route('/eliminar-vehiculo/<int:vehiculo_id>', methods=['POST', 'DELETE'])
def eliminar_vehiculo(vehiculo_id):
    if request.method == 'POST' or request.method == 'DELETE':
        response  = borrado_logico(vehiculo_id)
        if int(response) == 200:
            inventario_venta = mostrar_inventario()
            return render_template('lista_venta.html', inventario_venta=inventario_venta)
    else:
        return 'Método no permitido', 405

# Ruta para manejar la edición de un vehículo
@app.route('/editar_vehiculo/<int:id_vehiculo>', methods=['POST', 'UPDATE'])
def editar_vehiculo(id_vehiculo):
     # Obtener los datos del formulario
    marca = request.form['marca']
    modelo = request.form['modelo']
    tipo = request.form['tipo']
    dominio = request.form['dominio']
    anio = request.form['anio']
    kilometraje = request.form['kilometraje']
    precio_venta = request.form['precio_venta']
    precio_compra = request.form['precio_compra']
    estado = request.form['estado']
    vehiculo = Vehiculo(id_vehiculo,dominio,marca,modelo,tipo,anio,kilometraje,precio_compra,precio_venta,estado,'0')
    if request.method == 'POST':
        response  = editar_dato(id_vehiculo, vehiculo)
        if int(response) == 200:
            inventario_venta = mostrar_inventario()            
            return render_template('lista_venta.html', inventario_venta=inventario_venta)
    else:
        return 'Método no permitido', 405    

# Ruta para manejar la venta de un vehículo
@app.route('/vender_vehiculo/<int:id_vehiculo>', methods=['POST', 'UPDATE'])
def vender_vehiculo(id_vehiculo):



    nombre = None
    apellido = None
    direccion = None
    telefono = None
    email = None
    dni = request.form.get('dni')
    response_cliente = busqueda_por_dni(dni)
    id_cliente = ''
    if(response_cliente != ''):
        id_cliente = response_cliente['id_cliente']
    else:
        id_cliente = request.form.get('id_cliente')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        email = request.form.get('email') 


    # Obtener los datos del formulario
    id_vehiculo = id_vehiculo  
    monto = request.form.get('monto')
    observaciones = request.form.get('observaciones')
    delete = '0'
    tipo = 'Venta'
    fecha = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    transaccion_venta_vehiculo = TransaccionVentFormModel(id_vehiculo,id_cliente,nombre,apellido,dni,direccion,telefono,email,monto,observaciones,delete,tipo,fecha).to_dict()
    json_resultado = json.dumps(transaccion_venta_vehiculo)
    
    if request.method == 'POST':
        response = agregar_transaccion_venta(json_resultado)
        if int(response) == 200:
            inventario_venta = mostrar_inventario()            
            return render_template('lista_venta.html', inventario_venta=inventario_venta)
    else:
        return 'Método no permitido', 405
    inventario_venta = mostrar_inventario() 
    return render_template('lista_venta.html', inventario_venta=inventario_venta)   


# Ruta para manejar la venta de un vehículo
@app.route('/reservar_vehiculo/<int:id_vehiculo>', methods=['POST', 'UPDATE'])
def reservar_vehiculo(id_vehiculo):    
    if request.method == 'POST':
        
        response = reservar_vehiculo_por_id(id_vehiculo)
        if int(response) == 200:
            inventario_venta = mostrar_inventario()            
            return render_template('lista_venta.html', inventario_venta=inventario_venta)
    else:
        return 'Método no permitido', 405
    inventario_venta = mostrar_inventario() 
    return render_template('lista_venta.html', inventario_venta=inventario_venta)  


@app.route('/transaccion/<string:valor>',  methods=['POST','GET'])
def transaccion(valor):
    if request.method == 'POST' or request.method == 'GET':
        if(valor == 'cliente'):
            clientes_proveedores = mostrar_clientes_proveedores()
            return render_template('cliente_proveedor.html', clientes_proveedores=clientes_proveedores)
        elif valor == 'vehiculo':
            vehiculos_comprados = mostrar_vehiculos_proveedores()
            return render_template('lista_vehiculos_proveedor.html', inventario_lista_vehiculos=vehiculos_comprados, compra=1)
        elif valor == 'clientev':
            clientes_consumidores = mostrar_clientes_consumidores()
            return render_template('cliente_consumidor.html', clientes_consumidores=clientes_consumidores)
    else:
        return 'Método no permitido', 405    
    

# Ruta para manejar la eliminación de un cliente0
@app.route('/eliminar_cliente/<int:id_cliente>', methods=['POST', 'DELETE'])
def eliminar_cliente(id_cliente):
    if request.method == 'POST' or request.method == 'DELETE':
        response  = borrado_logico_cliente_proveedor(id_cliente)
        if int(response) == 200:
            clientes_proveedores = mostrar_clientes_proveedores()
            return render_template('cliente_proveedor.html', clientes_proveedores=clientes_proveedores)
    else:
        return 'Método no permitido', 405

# Ruta para manejar la edición de un cliente
@app.route('/editar_cliente/<int:id_cliente>', methods=['POST', 'UPDATE'])
def editar_cliente(id_cliente):
     # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    cliente = Cliente('0',nombre,apellido,dni,direccion,telefono,email,'0')
    if request.method == 'POST':
        response  = editar_dato_cliente_proveedor(id_cliente, cliente)
        if int(response) == 200:
            clientes_proveedores = mostrar_clientes_proveedores()
            return render_template('cliente_proveedor.html', clientes_proveedores=clientes_proveedores)
    else:
        return 'Método no permitido', 405    
    
# Ruta para manejar los vehiculos comprados por cliente
@app.route('/ver_vehiculos_comprados/<int:id_cliente>', methods=['POST'])
def ver_vehiculos_comprados(id_cliente):    
    if request.method == 'POST':
        response = busqueda_por_id_transaccion(id_cliente)
        if len(response) > 0:
            return render_template('lista_vehiculos_proveedor.html', inventario_lista_vehiculos=response)
    else:
        return 'Método no permitido', 405


# Ruta para manejar los clientes a los que se le compro el mismo modelo de vehiculos
@app.route('/ver_clientes_x_vehiculos/<int:id_vehiculo>', methods=['POST'])
def ver_clientes_x_vehiculos(id_vehiculo):
    if request.method == 'POST':
        response = busqueda_por_id_transaccion_vehiculo(id_vehiculo)
        if response != 500:
            return render_template('listado_clientes_x_vehiculos.html', cliente_response=response )
    else:
        return 'Método no permitido', 405


# Ruta para manejar la eliminación de un cliente para venta
@app.route('/eliminar_cliente_venta/<int:id_cliente>', methods=['POST', 'DELETE'])
def eliminar_cliente_venta(id_cliente):
    if request.method == 'POST' or request.method == 'DELETE':
        response  = borrado_logico_cliente_consumidor(id_cliente)
        if int(response) == 200:
            clientes_consumidores = mostrar_clientes_consumidores()
            return render_template('cliente_consumidor.html', clientes_consumidores=clientes_consumidores)
    else:
        return 'Método no permitido', 405
    
# Ruta para manejar la edición de un cliente consumidor
@app.route('/editar_cliente_venta/<int:id_cliente>', methods=['POST', 'UPDATE'])
def editar_cliente_venta(id_cliente):
     # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    cliente = Cliente('a',nombre,apellido,dni,direccion,telefono,email,'0')
    if request.method == 'POST':
        response  = editar_dato_cliente_consumidor(id_cliente, cliente)
        if int(response) == 200:
            clientes_consumidores = mostrar_clientes_consumidores()
            return render_template('cliente_consumidor.html', clientes_consumidores=clientes_consumidores)
    else:
        return 'Método no permitido', 405    
    

# Ruta para manejar los vehiculos vendido a un cliente
@app.route('/ver_vehiculos_vendidos/<int:id_cliente>', methods=['POST'])
def ver_vehiculos_vendidos(id_cliente):    
    if request.method == 'POST':
        response = busqueda_por_id_transaccion_venta(id_cliente)
        if len(response) > 0:
            return render_template('lista_vehiculos_proveedor.html', inventario_lista_vehiculos=response)
    else:
        return 'Método no permitido', 405
    

if __name__ == '__main__':
    app.run(debug=True)


