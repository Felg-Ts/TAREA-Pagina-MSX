from flask import Flask, request,url_for,render_template
from jinja2 import Template
import json

app = Flask(__name__)	

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html",titulo="principal")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html",titulo="juegos")


@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    
    l1 = []

    f = open("MSX.json", "r")
    content = f.read()
    jsondecoded = json.loads(content)

    nombrej=request.form.get("tjuego")

    for i in jsondecoded:
        entityName = i["nombre"]
        if entityName.startswith(nombrej):
            l1.append(i)

    return render_template("listajuegos.html",titulo="listajuegos", l1=l1, i=i)

@app.route('/juego/<int:cadena1>/',methods=["GET","POST"])
def juego(nombrej):

    #f = open("MSX.json", "r")
    #content = f.read()
    #jsondecoded = json.loads(content)

    #for entity in jsondecoded:
        #entityName = entity["nombre"]
        #if entityName.startswith(nombrej) is True:
            #print(entityName)
            #print(entity["desarrollador"])

            return render_template("juego.html",titulo="juego",)

#return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep)

if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
