from flask import Flask
from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request


app = Flask(__name__)

lista_usuarios = {
    "Hellen",
    "Jose",
    "Juan",
    "LuisAmortegui",
    "LuisSoto",
    "Fabian"
}
lista_vuelos = {
   1: "Barranquilla",
   2: "Bogota",
   3: "SantaMarta"
}
lista_comentarios = {
   1: "Excelente",
   2: "Bueno",
   3: "Regular",
}

sesion_iniciada = False

@app.route('/', methods=["GET"])
def index():
    #si ya inicio sesion entonces ingresa a reservas y ver vuelos 
    #si no  se dirige a la pagina de menu principal
    return render("index.html" , sesion_iniciada=sesion_iniciada)


@app.route('/login', methods=["GET","POST"])
def ingreso():

    global sesion_iniciada

    if request.method == "GET":
        return render ("login.html")
    else:
        sesion_iniciada = True
        return render ("vuelos.html")

    # si el ususario se encuentra registrado ingresa al sistema principal 
    # cuando este dentro del sistema consultara los estados de los vuelos 
    # cuando este dentro del sistema consulata los comentarios 
    # cuando este dentro del sistema podra ver su perfil y editarlo 
    # cuando este dentro del sistema podra ver crear reserva 
    # si no esta loqeado se envia a menu principal donde tendra noticias generales del aeropuesto
    # si no esta logeado se solicitara crear un usuario


@app.route('/registro', methods=["GET","POST"])
def registro():  
    return render ("registro.html")

# como el usuario no pudo ingresar al sistema , en esta pantalla se sealizara 
# el logeo y en la parte inferior del sistema se agrgara un espacio de comentario donde 
# informara al administrador e tipo de rol que cumplira el usuario
# el ususario registra sus datos y en un campo solicita al admin rol


@app.route('/reservas', methods=["GET","POST"])
def reserva():
    return"pagina de reserva"

# dentro del sistema el usuario realizara la reserva del vuelo a realizar 
# por medio de un codigo x , este sera clave para poder consultar su estado de vuelo
# si no tiene codigo y datos del vuelo , no podra hacer la reserva , tendra un boton de 
# regreso donde lo enviara a menu principal y escoger otra opcion.

@app.route('/vuelos', methods=["GET"])
def vuelos():
    return"pagina para ver los vuelos "

# esta pantalla solo estara diponible para los que tienen rol de admin y pilotos
# si no es piloto no podra ingresar
# tendra una lista de vuelos disponibles


@app.route('/calificacion', methods=["GET","POST"])
def calificacion():
    return"pagina para ver la calififcaciones de los usuarios "

# en esta pantalla el usario podra asignar una calificacion al vuelo establecido , saldra el
# nombre del vuelo , el comentario y el valor numerio de 1 a 100 dando calificacion al mismo
# solo podra calificar si esta registrado.

@app.route('/comentarios/<id_comentario>', methods=["GET"])
def comentarios(id_comentario):
    try:
        id_comentario = int(id_comentario)
    except Exception as e:
        id_comentario = 0

    if id_comentario in lista_comentarios:
        return lista_comentarios[id_comentario]
    else:
        return f"el comentario que esta buscando ({id_comentario}) no fue digitado"

# si el usuario esta logeado podra ver y editar comentarios de os vuelos , esto como
# medida de retro alimentacion del servicio.
# si el usuario no esta logeado solo podra ver los comentarios 


@app.route('/usuarios/<id_usuario>', methods=["GET","POST"])
def usuario_info(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Estas viendo el perfil del usauario{id_usuario}"
    else:
        return f"Error el usuario {id_usuario} no existe"

# esta es la pantalla de perfiles , en esta pagina el usuario estara en la capacidad de ver y editar comentarios
# su usuario , siempre y cuando se encuentre logeado en el sistema podra editar datos generales
# el administrado sera el unico con acceso a borrar y asignar roles

@app.route('/salir', methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')

# metodo de salida para cerrar cesion de cualquier pantalla



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
