# Entre na pasta raiz do projeto.
# Criar um ambiente virtual: py -3 -m venv venv
# Ativar o ambiente virtual: venv\Scripts\Activate
# Instalar o flask: pip install flask
from siteciencia import app

if __name__ == "__main__":
  app.run(debug=True)
