from flask import Flask

app = Flask(__name__)

@app.route("/")
def primera():
    return "<p>Hello, World primera ruta !</p>"

@app.route("/segunda")
def segundo():
    return "<h1>Hello, World segunda ruta !</h1>"

if __name__ == '__main__':
    app.run(debug = True)