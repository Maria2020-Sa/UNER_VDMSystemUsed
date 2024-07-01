from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length



class TransaccionVehiculoForm(FlaskForm):
    dominio = StringField('Dominio', validators=[DataRequired(), Length(min=4, max=25)])
    marca = StringField('Marca', validators=[DataRequired(), Length(min=4, max=25)])
    modelo = StringField('Modelo', validators=[DataRequired(), Length(min=4, max=25)])
    tipo = StringField('Tipo', validators=[DataRequired(), Length(min=4, max=25)])
    año = StringField('Año', validators=[DataRequired(), Length(min=4, max=25)])
    kilometraje = StringField('Kilometraje', validators=[DataRequired(), Length(min=4, max=25)])
    precioDeVenta = StringField('Precio de Venta', validators=[DataRequired(), Length(min=4, max=25)])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=4, max=25)])
