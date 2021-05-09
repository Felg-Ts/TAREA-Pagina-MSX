from flask import Flask, request,url_for,render_template
app = Flask(__name__)	

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html",titulo="principal")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html",titulo="juegos")


@app.route('/listajuegos',methods=["POST"])
def listajuegos():
	cadena=request.form.get("tjuego")
	return render_template("listajuegos.html",titulo="listajuegos",cadena=cadena)

@app.route('/juego/<int:cadena1>/',methods=["GET","POST"])
def juego(cadena1):
    return render_template("juego.html",titulo="juego", cadena1="cadena1")

#return render_template("potencia.html", base=bp, exponente=ep, solucion=bp**ep)

if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
