from flask import Flask, request,url_for,render_template
app = Flask(__name__)	

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html",titulo="principal")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html",titulo="juegos")


@app.route("/listajuegos",methods=["POST"])
def listajuegos():
	cadena=request.form.get("juego")
	return render_template("listajuegos.html",titulo="listajuegos",cadena=cadena)


if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
