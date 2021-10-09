#documentos
#nombre sprintfield
#ciclo selection
#sexo\
#estado booleanfield
#botoncrear submitted
#botonactualizar submitted
#botoneliminar sub
#boton visualizar submitted

from flask import Flask,redirect,url_for,render_template,request
from flask_wtf import Flaskform
from wtforms import StringField,select,SubmitField,booleanfield
from wtforms import DataRequired

class formulary (Flaskform):
    documento = StringField("Documento",validators = [DataRequired(message="no dejar vacio")])
    nombre = StringField("nombre",validators = [DataRequired(message="no dejar vacio")])
    ciclo = StringField("ciclo",choice = [("ciclo1"),("ciclo2"),("ciclo3"),("ciclo4")])
    sexo = StringField("sexo",validators = [DataRequired(message="no dejar vacio")])
    estado = booleanfield("estado",validators = [DataRequired(message="no dejar vacio")])
    botoncrear = StringField("botoncrear", render_kw={ } )
    botoneliminar = StringField("botoneliminar",render_kw={ })
    botonactualizar = StringField("botonactualizar",render_kw={ })
    botonvisualizar = StringField("botonvisualizar",render_kw={ })

