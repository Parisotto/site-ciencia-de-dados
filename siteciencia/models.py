from siteciencia import bancodedados, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
  return Usuario.query.get(int(id_usuario))

class Usuario(bancodedados.Model, UserMixin):
  id = bancodedados.Column(bancodedados.Integer, primary_key=True)
  username = bancodedados.Column(bancodedados.String, nullable=False)
  email = bancodedados.Column(bancodedados.String, nullable=False, unique=True)
  senha = bancodedados.Column(bancodedados.String, nullable=False)
  fotos = bancodedados.relationship("Foto", backref="usuario", lazy=True)

class Foto(bancodedados.Model):
  id = bancodedados.Column(bancodedados.Integer, primary_key=True)
  imagem = bancodedados.Column(bancodedados.String, default="default.png")
  data_criacao = bancodedados.Column(bancodedados.String, nullable=False, default=datetime.now())
  id_usuario = bancodedados.Column(bancodedados.Integer, bancodedados.ForeignKey('usuario.id'), nullable=False)
