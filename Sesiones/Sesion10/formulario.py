from flask_wtf import Flaskform

from wtforms import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class contacto(Flaskform):
    nombre = StringField("nombre", validators=[DataRequired(message="no dejar vacio")])
    correo = EmailField("correo", validators=[DataRequired(message="no dejar vacio")])
    mensaje = TextAreaField("mensaje", validators=[DataRequired(message="no dejar vacio")])
    enviar = SubmitField("enviar formulario")