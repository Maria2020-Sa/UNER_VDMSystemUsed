import json
from flask import Flask, render_template, flash, redirect, request, url_for
from model.form.transaccion_form import TransaccionForm
from model.form.transaccion_vehiculo_form import TransaccionVehiculoForm
from model.form.transaccion_venta_form import TransaccionVentFormModel
from model.model_cliente import Cliente
from model.model_vehiculo import Vehiculo
from model.form.model_transaccion_form import TransaccionFormModel
from service.compra.sevice_transaccion_compra import agregar_transaccion_compra
from service.venta.service_transaccion_venta import agregar_transaccion_venta
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
        cliente = Cliente(form.nombre.data, form.apellido.data, form.dni.data, form.direccion.data, form.telefono.data, form.email.data, '0')
        vehiculo = Vehiculo('0',form.dominio.data, form.marca.data, form.modelo.data, form.tipo.data, form.año.data, form.kilometraje.data, form.precioDeCompra.data, form.precioDeVenta.data, form.estado.data, form.delete.data)
        fecha = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        tipo = 'compra'
        observaciones = 'form.observaciones'
        transaccionForm = TransaccionFormModel(cliente, vehiculo, tipo, fecha, observaciones).to_dict()
        json_resultado = json.dumps(transaccionForm)
        response = agregar_transaccion_compra(json_resultado)
        print("response", response)
        if int(response) == 200:
            flash(f'Guardado con exito!', 'success')
            return redirect(url_for('home'))
    else:
            print("Form validation failed")
            print(form.errors)
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
            flash(f'Vehículo con ID {vehiculo_id} eliminado correctamente', 'success')
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
     # Obtener los datos del formulario
    id_vehiculo = id_vehiculo
    id_cliente = request.form.get('id_cliente')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dni = request.form.get('dni')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    monto = request.form.get('monto')
    observaciones = request.form.get('observaciones')
    delete = '0'
    tipo = 'Venta'
    fecha = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    transaccion_venta_vehiculo = TransaccionVentFormModel(id_vehiculo,id_cliente,nombre,apellido,dni,direccion,telefono,email,monto,observaciones,delete,tipo,fecha).to_dict()
    json_resultado = json.dumps(transaccion_venta_vehiculo)
    
    if request.method == 'POST':
        print("holaaaa")
        response = agregar_transaccion_venta(json_resultado)
        print("holaaaa", response)
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
        print(response)
        if int(response) == 200:
            inventario_venta = mostrar_inventario()            
            return render_template('lista_venta.html', inventario_venta=inventario_venta)
    else:
        return 'Método no permitido', 405
    inventario_venta = mostrar_inventario() 
    return render_template('lista_venta.html', inventario_venta=inventario_venta)  


if __name__ == '__main__':
    app.run(debug=True)


