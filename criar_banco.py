from siteciencia import bancodedados, app
from siteciencia.models import Usuario, Foto

with app.app_context():
  bancodedados.create_all()
