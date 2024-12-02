from flask import Flask, render_template, request, redirect
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder ="siteciencia/templates", static_folder = "siteciencia/static")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "cd.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=dt.now())
  def __repr__(self):
    return  f"Task: #{self.id}, description: {self.description}"

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

@app.route("/tarefas", methods=['POST', 'GET'])
def tarefas():
  if request.method == "POST":
    task = Task(description=request.form["description"])
    try:
      db.session.add((task))
      db.session.commit()
      return redirect("/tarefas")
    except:
      return "Houve um erro ao inserir a tarefa"
  else:
    tasks = Task.query.order_by(Task.date_created).all()
    return render_template("tarefas.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
  task = Task.query.get_or_404(id)
  try:
    db.session.delete(task)
    db.session.commit()
    return redirect("/tarefas")
  except:
    return "Houve um problema na remoção da tarefa"


@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
  task = Task.query.get_or_404(id)
  if request.method == "POST":
    task.description = request.form["description"]
    try:
      db.session.commit()
      return redirect("/tarefas")
    except:
      return "Houve um erro ao atualizar a tarefa"
  else:
    return render_template("update.html", task=task)



if __name__ == "__main__":
  app.run(debug=True, port=5001)
