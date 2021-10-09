from flask import Flask
from flask import Flask
from flask import render_template as render

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

@app.route('/', methods=["GET"])
def index():
    #si ya inicio sesion entonces ingresa a reservas y ver vuelos 
    #si no  se dirige a la pagina de menu principal
    return render("index.html")
    


@app.route('/registro', methods=["GET","POST"])
def registro():  
    return render ("registro.html")


@app.route('/login', methods=["GET","POST"])
def ingreso():
    return render ("login.html")


@app.route('/reservas', methods=["GET","POST"])
def reserva():
    return"pagina de reserva"


@app.route('/vuelos', methods=["GET"])
def vuelos():
    return"pagina para ver los vuelos "


@app.route('/calificacion', methods=["GET","POST"])
def calificacion():
    return"pagina para ver la calififcaciones de los usuarios "


@app.route('/compras', methods=["GET","POST"])
def compra():
    return"pagina para ver compras "



@app.route('/usuarios/<id_usuario>', methods=["GET","POST"])
def usuario_info(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Estas viendo el perfil del usauario{id_usuario}"
    else:
        return f"Error el usuario {id_usuario} no existe"



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
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
