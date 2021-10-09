from logging import debug
from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request




app = Flask(__name__)

lista_usuarios = ["Andres","Maria","Fernanda","luis"]
lista_noticias = {
    1: {'titulo' : "noticia 1" , 'cuerpo': "1 2 3", 'imagenes': ['img 1', 'img 1' , 'img 1']},
    2: {'titulo' : "noticia 2" , 'cuerpo': "1 2 3", 'imagenes': ['img 1', 'img 1' , 'img 1']},
    3: {'titulo' : "noticia 3" , 'cuerpo': "1 2 3 ", 'imagenes': ['img 1', 'img 1' , 'img 1']},

}

sesion_iniciada = False
@app.route("/",methods=["GET"])

@app.route("/inicio", methods = ["GET"])
def inicio():
    
    # si esta logeado o inicio sesion ingresa a las noticias
    # si no pagina de bienvenida
    return render(
        "index.html", 
        sesion_iniciada = sesion_iniciada,
        lista_noticias = lista_noticias
    )

@app.route("/registro", methods=["GET","POST"])
def registro():
    return "pagina de registro"

@app.route("/ingreso",methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    if request.method == "GET":
        return render ("ingreso.html")
    else:
        sesion_iniciada = True
        return redirect ("/inicio")
    

@app.route("/perfil",methods=["GET","POST"])
def perfil():
    return "pagina de perfil de usuario"

@app.route("/usuario/<id_usuario>",methods=["GET"])
def usuario_info(id_usuario):

    if id_usuario in lista_usuarios:
        return f"Estas viendo el eprfil de usuario : { id_usuario}"
    else:
        return f"Erro el usuario: { id_usuario} no existe"

@app.route("/noticias/<id_noticias>",methods=["GET"])
def noticias_detalles(id_noticias):
   
    try:
         id_noticias = int(id_noticias)
    except Exception as e:
        id_noticias = 0 

    if id_noticias in lista_noticias:
        return lista_noticias[id_noticias]
    else:
        return f"la noticias: { id_noticias} no existe"

@app.route('/salir', methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/inicio')

# los metodos y accione se peuden realizar
# de lado del servidor el debe identificar que tipo de informacion 
# si queiro mostrar informaicion y traer del servidor uso el GET

#SI del navegador requiero mandar informacion al servidor uso un POST



if __name__=="__main__":
    app.run(debug=True)