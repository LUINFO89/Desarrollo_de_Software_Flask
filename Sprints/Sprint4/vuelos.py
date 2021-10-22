
from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, SelectField, SubmitField,TextField,TextAreaField
=======
from wtforms import StringField, SelectField, SubmitField,TextField
>>>>>>> 10f8323a5894a60206c85d9f718cff6667014b39
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
    botonVisualizar = SubmitField("Ver Vuelos ", render_kw={"onmouseover": "visualizarV()"})

class formularioC(FlaskForm):
<<<<<<< HEAD
    documento = StringField("Numero de Identificacion:", validators=[DataRequired(message="No dejar vacío este campo...")])
    nombre = StringField("Nombre pasajero:")
    lugar = SelectField("Lugar de Destino:", choices=[("Barranquilla"), ("Bogota"), ("Medellin"), ("Cali"), ("Cartagena")])
    mensaje = TextAreaField("Mensaje , sujerencia o reconocimiento:")
=======
    documento = StringField("Identificacion:", validators=[DataRequired(message="No dejar vacío este campo...")])
    nombre = StringField("Nombre:")
    lugar = SelectField("Lugar de Destino:", choices=[("Barranquilla"), ("Bogota"), ("Medellin"), ("Cali"), ("Cartagena")])
    mensaje = TextField("Mensaje , sujerencia o reconocimiento:")
>>>>>>> 10f8323a5894a60206c85d9f718cff6667014b39
    
    botonCrear = SubmitField("botonCrear", render_kw={"onmouseover": "guardarC()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover": "eliminarC()"})
    botonActualizar = SubmitField("botonActualizar", render_kw={"onmouseover": "actualizarC()"})
<<<<<<< HEAD
    botonVisualizar = SubmitField("Ver comentarios ", render_kw={"onmouseover": "visualizarC()"})

class formularioU(FlaskForm):
    documento = StringField("Identificacion:", validators=[DataRequired(message="No dejar vacío este campo...")])
    nombre = StringField("Nombre:")
    usuario = StringField("usuario:")
    correo = StringField("usuario:")
    contraseña = StringField("contraseña:")
    nacimiento = SelectField("Lugar de Nacimiento:", choices=[("Barranquilla"), ("Bogota"), ("Medellin"), ("Cali"), ("Cartagena")])
    telefono = TextField("Telefono:")
    direccion = TextField("Direccion:")
    rol = SelectField("rol:", choices=[("Pasajero"), ("Piloto")])

    botonCrear = SubmitField("botonCrear", render_kw={"onmouseover": "guardarU()"})
    botonEliminar = SubmitField("botonEliminar", render_kw={"onmouseover": "eliminarU()"})
    botonActualizar = SubmitField("botonActualizar", render_kw={"onmouseover": "actualizarU()"})
    botonVisualizar = SubmitField("Ver Usuario ", render_kw={"onmouseover": "visualizarU()"})

=======
    botonVisualizar = SubmitField("Ver Vuelos ", render_kw={"onmouseover": "visualizarC()"})
>>>>>>> 10f8323a5894a60206c85d9f718cff6667014b39



