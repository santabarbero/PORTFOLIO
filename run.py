#Importar
from flask import Flask

 #Crear app mediante instancia
 app = Flask(__name__)

 #Crear rutas con sus correspondientes funciones
 @app.route("/")
 def holamundo():
     return "Hola mundo¡"

#Ejecutar nuestra app cuando ejecutemos este archivo rum.py
if __name__ == "__main__":
    app.run(debug=True)

 