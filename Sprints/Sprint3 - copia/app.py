import os
import re
from sqlite3.dbapi2 import Date, Row
from flask import *
from flask import Flask,redirect,request,flash,url_for,jsonify,session
from flask import render_template as render
from db import get_db
import sqlite3

from reservas import formularioI
from vuelos import formularioV


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=["GET","POST"])
def index():
    return render("index.html")
    

@app.route( '/login', methods=('GET', 'POST') )
def login():
    try:
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['username']
            password = request.form['password']

            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render( 'login.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render( 'login.html' )

            user = db.execute(
                'SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ? ', (username, password)
            ).fetchone()

            # print('USER ')
            # print(user)

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                return redirect( 'menu.html' )
            flash( error )
        return render( 'login.html' )
    except:
        return render( 'menu.html' )
            

    # si el ususario se encuentra registrado ingresa al sistema principal 
    # cuando este dentro del sistema consultara los estados de los vuelos 
    # cuando este dentro del sistema consulata los comentarios 
    # cuando este dentro del sistema podra ver su perfil y editarlo 
    # cuando este dentro del sistema podra ver crear reserva 
    # si no esta loqeado se envia a menu principal donde tendra noticias generales del aeropuesto
    # si no esta logeado se solicitara crear un usuario ok


@app.route('/registro', methods=["GET","POST"])
def registro():  
    if request.method == 'POST':
        name = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        email = request.form['correo']
        error = None
        db = get_db()
        db.executescript(
            "INSERT INTO usuarios   (nombre, usuario,correo,contraseña) VALUES ('%s','%s','%s','%s')"%(name,username,email,password)
        )
        db.commit()
        return render ('login.html')
    return render ("registro.html")

# como el usuario no pudo ingresar al sistema , en esta pantalla se sealizara 
# el logeo y en la parte inferior del sistema se agrgara un espacio de comentario donde 
# informara al administrador e tipo de rol que cumplira el usuario
# el ususario registra sus datos y en un campo solicita al admin rol ok 


#----------------------------------------INICIO CRUD RESERVAS--------------------------------------#

@app.route('/reservas', methods=["GET", "POST"])
def inicio():
    form = formularioI()
    return render_template('reservas.html', form = form)

#---------------------------------------RESERVAS CREAR--------------------------------------------#
@app.route('/reservas/guardar/', methods=["POST"])
def guardar():
        form = formularioI()#Instancia de la clase en formulario.py
        if request.method == "POST":
            docum = form.documento.data#Recupera datos
            nombr = form.nombre.data
            lugar = form.lugardesde.data
            hasta = form.hasta.data
            salida = form.salida.data
            regreso = form.regreso.data
            cantidad = form.cantidadpasajeros.data

            with sqlite3.connect("database.db") as conn:#Manejador de contexto ->conexion
                cur = conn.cursor()#manipula la db
                #se va a usar el PreparedStatement
                #Acciones
                cur.execute(
                    "INSERT INTO reserva (documento, nombre, lugardesde, hasta, salida, regreso, cantidad) VALUES (?,?,?,?,?,?,?)", 
                (docum, nombr, lugar, hasta, salida,regreso, cantidad)
                )
                conn.commit()#Confirmación de inserción de datos :)
                return "¡Datos guardados exitosamente!"
        return "No se pudo guardar T_T"    

#-----------------------------------------RESERVAS VISUALIZAR ---------------------------------------#
@app.route('/vista', methods=["GET","POST"])
def vista():
     return render ("reservas.html")

@app.route('/reservas/visualizar/', methods=["POST"])
def visualizar():
    form = formularioI()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:#conexion
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM reserva WHERE Documento = ?", [docum])
            row = cur.fetchone()
            if row is None:
                return "No se encontró el registro en la base de datos...... :'( "
            return render_template("vistausuarios.html", row = row)
    return "Error"

# dentro del sistema el usuario realizara la reserva del vuelo a realizar 
# por medio de un codigo x , este sera clave para poder consultar su estado de vuelo
# si no tiene codigo y datos del vuelo , no podra hacer la reserva , tendra un boton de 
# regreso donde lo enviara a menu principal y escoger otra opcion. ok

#-----------------------------------------------RESERVAS ELIMINAR ------------------------------------#

@app.route('/reservas/eliminar/', methods=["POST"])
def eliminar():
   
    form = formularioI()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM reserva WHERE Documento = ?", [docum])
            if conn.total_changes > 0:
                return "Estudiante borrado ^v^"
            return render_template("reservas.html")
    return "Error"

#---------------------------------------RESERVAS ACTUALIZAR ----------------------------------------#

@app.route('/reservas/actualizar/', methods=["POST"])
def actualizar():
    
    form = formularioI()#Instancia de la clase en formulario.py
    if request.method == "POST":
        docum = form.documento.data#Recupera datos
        nombr = form.nombre.data
        lugar = form.lugardesde.data
        hasta = form.hasta.data
        salida = form.salida.data
        regreso = form.regreso.data
        cantidad = form.cantidadpasajeros.data
        with sqlite3.connect("database.db") as conn:#Manejador de contexto ->conexion
            cur = conn.cursor()#manipula la db
            #se va a usar el PreparedStatement
            #Acciones
            cur.execute(
                "UPDATE reserva SET nombre = ?, lugardesde = ?, hasta = ?, salida = ?,regreso = ?,cantidad = ? WHERE Documento = ?;",
             [docum, nombr, lugar, hasta, salida,regreso, cantidad]
             )
            conn.commit()#Confirmación de inserción de datos :)
            return "¡Datos actualizados exitosamente ^v^!"
    return "No se pudo actualizar T_T"
#-----------------------------------------FIN CRUD RESERVAS-------------------------------------------------#

####################################################################################################################################
######################################################################################################################
##################################################################################################################

#----------------------------------------INICIO CRUD VUELOS ------------------------------------------------#
@app.route('/vuelos', methods=["GET", "POST"])
def inicioV():
    form = formularioV()
    return render('vuelos.html', form = form)

#----------------------------------------INICIO CRUD VUELOS ------------------------------------------------#
@app.route('/vuelos/guardar/', methods=["GET","POST"])
def guardarv():
        form = formularioV()#Instancia de la clase en formulario.py
        if request.method == "POST":
            docum = form.documento.data#Recupera datos
            aerolinea = form.aerolinea.data
            hora = form.hora.data
            destino = form.destino.data
            horadestino = form.horadestino.data
            observacion = form.observacion.data
            piloto = form.piloto.data
            capacidad = form.capacidad.data

            with sqlite3.connect("database.db") as conn:#Manejador de contexto ->conexion
                cur = conn.cursor()#manipula la db
                #se va a usar el PreparedStatement
                #Acciones
                cur.execute(
                    "INSERT INTO vuelos (VUELO, AEROLINEA, HORA, DESTINO, HORADESTINO, OBSERVACION, PILOTO, CAPACIDAD) VALUES (?,?,?,?,?,?,?,?)", 
                (docum, aerolinea, hora, destino, horadestino,observacion, piloto,capacidad)
                )
                conn.commit()#Confirmación de inserción de datos :)
                return "<h1>¡Datos de Vuelo guardados exitosamente!</h1>"
        return "No se pudo guardar T_T"    


# esta pantalla solo estara diponible para los que tienen rol de admin y pilotos
# si no es piloto no podra ingresar
# tendra una lista de vuelos disponibles ok


#----------------------------------------CREAR CRUD VUELOS ------------------------------------------------#

@app.route('/menu', methods=["GET","POST"])
def menu():
        return render ("menu.html")
# este metodo permite tener de manera genral las opciones Lesser General Public
# que tendran los usuarios del sistema para realizar las tareas
# en la aplicacion` ok 

@app.route('/calificacion/', methods=["GET"])
def calificacion():
    global sesion_iniciada
    
    if request.method == "POST":
        return render ("login.html")
    else:
        sesion_iniciada = True
        return render ("calificacion.html")



# en esta pantalla el usario podra asignar una calificacion al vuelo establecido , saldra el
# nombre del vuelo , el comentario y el valor numerio de 1 a 100 dando calificacion al mismo
# solo podra calificar si esta registrado.
# si el usuario no esta logeado solo podra ver los comentarios 




# esta es la pantalla de perfiles , en esta pagina el usuario estara en la capacidad de ver y editar comentarios
# su usuario , siempre y cuando se encuentre logeado en el sistema podra editar datos generales
# el administrado sera el unico con acceso a borrar y asignar roles


   

@app.route('/salir', methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return render('index.html')

# metodo de salida para cerrar cesion de cualquier pantalla ok



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
