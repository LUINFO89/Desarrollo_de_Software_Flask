
# Documento => StringField
# nombre => StringField
# lugardesde => SelectField
# hasta  => SelectField
# fecha => StringField
# salida => StringField
# regreso => StringField
# cantidadpasajeros => StringField

# BotonCrear => SubmitField
# BotonActualizar => SubmitField
# BotonEliminar => SubmitField
# BotonVisualizar => SubmitField
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired

class formularioI(FlaskForm):
    documento = StringField("Documento identidad", validators=[DataRequired(message="No dejar vacío este campo...")])
    nombre = StringField("Nombre")
    lugardesde = SelectField("lugardesde", choices=[("Bogota"), ("Medellin"), ("Cali"), ("Barranquilla"), ("Cartagena")])
    hasta = SelectField("hasta", choices=[("Barranquilla"), ("Medellin"), ("Cali"), ("Bogota"), ("Cartagena")])
    salida = StringField("salida")
    regreso = StringField("regreso")
    cantidadpasajeros = StringField("cantidad")

    botonCrear = SubmitField("botonCrear", render_kw={"onmouseover": "guardar()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover": "eliminar()"})
    botonActualizar = SubmitField("botonActualizar", render_kw={"onmouseover": "actualizar()"})
    botonVisualizar = SubmitField("Visualizar Reservas", render_kw={"onmouseover": "visualizar()"})