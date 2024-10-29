from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'

@app.route("/")
def inicial():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    if username == "eloalav":
        if password == "eloa123":
            return redirect(url_for('upload'))

@app.route("/upload")
def upload():
    if request.method == "GET":
     return render_template("upload.html")
    elif request.method == "POST":
        file = request.files["file"]
        caminho = app.config["UPLOAD_FOLDER"] + "/" + file.filename
        file.save(caminho)

        return render_template("cardapio.html")


if __name__ == '__main__':
    app.run(debug=True)
