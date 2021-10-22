import functools
import os
from re import X

from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file, current_app, g, make_response
from flask import render_template as render
from flask import *
from flask_wtf import form
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3

from reservas import formularioI
from vuelos import formularioV,formularioC
variable = None

app = Flask(__name__)
app.secret_key = os.urandom(24)

#----------------------------------------RUTA RAIZ--------------------------------------#

@app.route('/', methods=["GET","POST"])
def index():
    global variable
    if variable is not None:
        return redirect( url_for("login"))
    return render_template('index.html')
    
    
#----------------------------------------INICIO LOGIN--------------------------------------#
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            f"SELECT contraseña FROM usuarios WHERE usuario = '{username}'"
        ).fetchone()


        if user != None:
            variableInterna = user[0]
            session.clear()
            if check_password_hash(variableInterna, password):
                session["usuario"] = username
                form = formularioI()
                return render_template("menu.html", form=form, usuario2=username)#form = form significa todos los datos que van a pasar
            else: 
                return ("Usuario y clave falsas o inexactas, vuelva a intentar o llamamos a la policía :)")
        flash(error)

    return render_template('login.html')

#----------------------------------------RUTA CREAR USUARIO REGISTRO--------------------------------------#

@app.route('/registro', methods=["GET","POST"])
def registro():  
    if request.method == 'POST':
        name = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        email = request.form['correo']
        error = None
        db = get_db()
        db.execute(
            "INSERT INTO usuarios   (nombre, usuario,correo,contraseña) VALUES (?,?,?,?)",
            (name,username,email,generate_password_hash(password))
        )
        db.commit()
        return "alert('¡Datos guardados exitosamente!')"
    return render ("registro.html")


       

#----------------------------------------RUTA EDITAR USUARIO REGISTRO--------------------------------------#
#----------------------------------------RUTA VISUALIZAR USUARIO REGISTRO--------------------------------------#
#----------------------------------------RUTA CREAR USUARIO REGISTRO--------------------------------------#

#----------------------------------------RUTA MENU --------------------------------------#
@app.before_request
def load_logged_in_user():
    user_id = session.get( 'user_id' )

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps( view )
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect( url_for( 'login' ) )

        return view( **kwargs )

    return wrapped_view

@app.route('/menu', methods=["GET","POST"])
def menu():
    return render_template('menu.html')



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
            return render_template("vistaReserva.html", row = row)
    return "Error"
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
                return "Reserva borrada ^v^"
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
##################################################################################################################
#----------------------------------------INICIO CRUD VUELOS ------------------------------------------------#
@app.route('/vuelos', methods=["GET", "POST"])
def inicioV():
    form = formularioV()
    return render('vuelos.html', form = form)

#----------------------------------------CREAR CRUD VUELOS ------------------------------------------------#
@app.route('/vuelos/guardar/', methods=["GET","POST"])
def guardarv():
        form = formularioV()#Instancia de la clase en formulario.py
        if request.method == "POST":#Recupera datos
            docum = form.documento.data# docu es vuelos
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

#----------------------------------------VISUALIZAR CRUD VUELOS --------------------------------------------#
@app.route('/vuelos/visualizar/', methods=["POST"])
def visualizarV():
    form = formularioV()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:#conexion
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM vuelos WHERE ID = ?", [docum])
            row = cur.fetchone()
            if row is None:
                return "No se encontró el registro en la base de datos...... :'( "
            return render_template("vistaVuelos.html", row = row)
    return "Error"
#----------------------------------------EDITAR CRUD VUELOS ------------------------------------------------#
@app.route('/vuelo/actualizar/', methods=["POST"])
def actualizarV():
    
    form = formularioV()#Instancia de la clase en formulario.py
    if request.method == "POST":
        docum = form.documento.data# docu es vuelos
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
                "UPDATE vuelos SET AEROLINEA = ?, HORA = ?, DESTINO = ?, HORADESTINO = ?,OBSERVACION = ?,PILOTO = ?,CAPACIDAD = ? WHERE VUELO = ?;",
             [docum, aerolinea, hora, destino, horadestino, observacion, piloto,capacidad]
             )
            conn.commit()#Confirmación de inserción de datos :)
            return "¡Datos actualizados exitosamente ^v^!"
    return "No se pudo actualizar T_T"
#----------------------------------------BORRAR CRUD VUELOS ------------------------------------------------#
@app.route('/vuelos/eliminar/', methods=["POST"])
def eliminarV():
   
    form = formularioV()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM vuelos WHERE VUELO = ?", [docum])
            if conn.total_changes > 0:
                return "Vuelo borrado ^v^"
            return render_template("vuelos.html")
    return "Error"
#-----------------------------------------FIN CRUD VUELOS-------------------------------------------------#
##################################################################################################################
#----------------------------------------INICIO CRUD COMENTARIOS ------------------------------------------------#
@app.route('/comentarios', methods=["GET", "POST"])
def inicioC():
    form = formularioC()
    return render('comentarios.html', form = form)

@app.route('/comentarios/visualizar/', methods=["POST"])
def visualizarC():
    form = formularioV()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:#conexion
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("SELECT * FROM comentarios WHERE ID = ?", [docum])
            row = cur.fetchone()
            if row is None:
                return "No se encontró el registro en la base de datos...... :'( "
            return render_template("vistacomentarios.html", row = row)
    return "Error"
#----------------------------------------CREAR CRUD COMENTARIOS ------------------------------------------------#
@app.route('/comentarios/guardar/', methods=["GET","POST"])
def guardarC():
        form = formularioC()#Instancia de la clase en formulario.py
        if request.method == "POST":#Recupera datos
            docum = form.documento.data# docu es vuelos
            nombre = form.nombre.data
            lugar = form.lugar.data
            mensaje = form.mensaje.data
            

            with sqlite3.connect("database.db") as conn:#Manejador de contexto ->conexion
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO comentarios (idcomentarios, NOMBREVIAJERO, LUGARDEVUELO, MENSAJE) VALUES (?,?,?,?)", 
                (docum, nombre, lugar, mensaje)
                )
                conn.commit()
                return "<h1>¡Comentario guardado exitosamente!</h1>"
        return "No se pudo guardar T_T"    

#----------------------------------------EDITAR CRUD COMENTARIOS ------------------------------------------------#
@app.route('/comentarios/actualizar/', methods=["POST"])
def actualizarC():
    
    form = formularioC()
    if request.method == "POST":
        docum = form.documento.data# docu es vuelos
        nombre = form.nombre.data
        lugar = form.lugar.data
        mensaje = form.mensaje.data
        
        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE comentarios SET NOMBREVIAJERO = ?, LUGARDEVUELO = ?, MENSAJE = ? WHERE idcomentarios = ?",
             [docum, nombre, lugar, mensaje]
             )
            conn.commit()
            return "¡Datos actualizados exitosamente ^v^!"
    return "No se pudo actualizar T_T"
#----------------------------------------VISUALIZAR CRUD COMENTARIO ---------------------------------------------#
@app.route('/comentarios/eliminar/', methods=["POST"])
def eliminarC():
   
    form = formularioV()
    if request.method == "POST":
        docum = form.documento.data
        with sqlite3.connect("database.db") as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()#manipula la db
            cur.execute("DELETE FROM comentarios WHERE idcomentarios = ?", [docum])
            if conn.total_changes > 0:
                return "Comentario  borrado ^v^"
            return render_template("comentarios.html")
    return "Error"
#----------------------------------------BORRAR CRUD COMENTARIOS ------------------------------------------------#

@app.route( '/logout' )
def logout():
    session.clear()
    return redirect( url_for( 'index' ) )


'''@app.before_request
def load_logged_in_user():
    user_id = session.get( 'user_id' )

    if user_id is None:
        global variable
        variable = "login"
    else:
        variable = None '''



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
