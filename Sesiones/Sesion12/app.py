from flask import Flask,redirect,url_for,render_template,request
import os
from Sesion12.formulario import formulary

app=Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def home():
    form = formulary()
    return render_template('formulario.html', form = form )

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)