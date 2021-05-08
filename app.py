from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)	

@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/potencia/<int:bp>/<int:ep>/', methods=["GET","POST"])
def potencia(bp, ep):
    if ep <= -1:
        ep2 = ep * -1
        return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep, solucion2=bp**ep2)
    else:
        return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep)

@app.route('/cuenta/<string:palabra>/<string:letra>/', methods=["GET","POST"])
def cuentaletras(palabra, letra):
    cont = 0

    for i in palabra:
        if i == letra:
            cont = cont + 1
    rels = (f"En la palabra {palabra} aparece {cont} veces el carácter {letra}")
    return render_template("cuentaletras.html", aparece=rels)

@app.route('/libro/<int:cod>/', methods=["GET","POST"])
def libros(cod):

    xmldoc = ET.parse('libros.xml')
    root = xmldoc.getroot()

    if cod == 123:
        a1 = root.find("./libro[1]/autor")
        t2 = root.find("./libro[1]/titulo")
    elif cod == 124:
        a1 = root.find("./libro[2]/autor")
        t2 = root.find("./libro[2]/titulo")
    elif cod == 125:
        a1 = root.find("./libro[3]/autor")
        t2 = root.find("./libro[3]/titulo")
    elif cod == 126:
        a1 = root.find("./libro[4]/autor")
        t2 = root.find("./libro[4]/titulo")
    elif cod == 127:
        a1 = root.find("./libro[5]/autor")
        t2 = root.find("./libro[5]/titulo")
        
    return render_template("libros.html", nombre=a1.text ,autor=t2.text)


app.run("0.0.0.0",5000,debug=True)