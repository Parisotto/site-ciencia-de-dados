from flask import render_template
from siteciencia import app

@app.route("/")
def index():
  # return "<h1>Bom dia, professor Parisotto</h1>"
  return render_template("index.html")

@app.route("/analise", defaults={'usuario':'Visitante'})
@app.route("/analise/<usuario>")
def analise(usuario):
  return render_template('analise.html', usuario=usuario)
