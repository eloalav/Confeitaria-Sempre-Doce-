from flask import Flask, render_template

app = Flask(__name__)

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




if __name__ == '__main__':
    app.run(debug=True)
