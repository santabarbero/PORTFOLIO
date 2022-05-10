from flask import Flask#Importar
app = Flask(__name__)#Crear app mediante instancia
@app.route("/")#Crear rutas con sus correspondientes funciones
def holamundo():
    return "Hola Mundo¡"
@app.route("/mis-proyectos")
def mostrarproyectos():
    return "Aquí se mostrarán mis proyectos"
#Ejecutar nuestra app cuando ejecutemos este archivo run.py
if __name__=="__main__":
    app.run(debug=False)
