from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length



class TransaccionForm(FlaskForm):
    dominio = StringField('Dominio', validators=[DataRequired(), Length(min=4, max=25)])
    marca = StringField('Marca', validators=[DataRequired(), Length(min=4, max=25)])
    modelo = StringField('Modelo', validators=[DataRequired(), Length(min=4, max=25)])
    tipo = StringField('Tipo', validators=[DataRequired(), Length(min=4, max=25)])
    año = StringField('Año', validators=[DataRequired(), Length(min=4, max=25)])
    kilometraje = StringField('Kilometraje', validators=[DataRequired(), Length(min=4, max=25)])
    precioDeCompra = StringField('Precio de Compra', validators=[DataRequired(), Length(min=4, max=25)])
    precioDeVenta = StringField('Precio de Venta', validators=[DataRequired(), Length(min=4, max=25)])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=4, max=25)])
    delete = RadioField('Delete', choices=[('Activo'), ('No Activo')], validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=4, max=25)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(min=4, max=25)])
    dni = StringField('DNI Nro.', validators=[DataRequired(), Length(min=4, max=25)])
    direccion = StringField('Dirección', validators=[DataRequired(), Length(min=4, max=25)])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=25)])