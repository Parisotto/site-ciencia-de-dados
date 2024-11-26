from flask import render_template, url_for
import random
from siteciencia import app
from flask_login import login_required

@app.route("/")
def index():
  # return "<h1>Bom dia, professor.</h1>"
  return render_template("index.html")

@app.route("/analise", defaults={'usuario':'Visitante'})
@app.route("/analise/<usuario>")
def analise(usuario):
  return render_template("analise.html", usuario=usuario)

@app.route("/galeria")
def galeria():
  numeros = random.sample(range(1, 26), 15)
  lista_imagens = [f"{num}.jpg" for num in numeros]
  return render_template("galeria.html", imagens=lista_imagens)

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
  return render_template("perfil.html", usuario=usuario)
