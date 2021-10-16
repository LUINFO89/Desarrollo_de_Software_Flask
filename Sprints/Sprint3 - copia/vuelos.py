
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired

class formularioV(FlaskForm):
    documento = StringField("Vuelo o Ticket:", validators=[DataRequired(message="No dejar vacío este campo...")])
    aerolinea = SelectField("Aerolinea:", choices=[("LATAM"), ("AVIANCA"), ("VIVACOLOMBIA"), ("SATENA"), ("VIVAAIR")])
    hora = StringField("Hora:")
    destino = StringField("Destino:")
    horadestino = StringField("Hora Destino:")
    observacion = SelectField("Observación:", choices=[("A tiempo"), ("Retrasado"), ("Aterrizado "), ("Despegado")])
    piloto = StringField("Piloto:")
    capacidad = StringField("Capacidad del avión:")


    botonCrear = SubmitField("botonCrear", render_kw={"onmouseover": "guardarV()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover": "eliminarV()"})
    botonActualizar = SubmitField("botonActualizar", render_kw={"onmouseover": "actualizarV()"})
    botonVisualizar = SubmitField("botonVisualizar", render_kw={"onmouseover": "visualizarV()"})
    Retroalimentacion = SubmitField("Retroalimentacion", render_kw={"onmouseover": "retroalimentacion()"})
