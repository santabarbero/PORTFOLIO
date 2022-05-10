from flask import Flask
app = Flask("__name__")
@app.route("/")
def holamundo():
    return "holamundo"
#@app.route('/mis-proyectos')
def mostrarproyectos():
    return 'Aquí se mostrarán mis proyectos'
if __name__ == "__main__":
    app.run(debug=True)

    
    