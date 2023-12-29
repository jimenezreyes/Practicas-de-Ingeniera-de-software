from flask import Blueprint
from flask import Flask, render_template, url_for, redirect
from alchemyClasses import db
from controllers.UserController import user
from controllers.UserController import update
from controllers.UserController import delete
from controllers.controllerRenta import renta
from model.model_renta import Renta
from controllers.controllerMovie import movie  # Asegúrate de que la ruta sea correcta
from model.model_peliculas import Pelicula  # Importa el modelo de película si es necesario


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY='dev'
)

bp = Blueprint('bp1', __name__, url_prefix='/bp') #localhost:5000/bp/adssfgdjhgf

@bp.route('/')
def hello_controller():
    return render_template('new-controller.html')

@bp.route('/ejemplo')
def ej():
    return 'hola'

app.register_blueprint(bp) #esto agrega a un controlador a la aplicacion.
app.register_blueprint(user)
app.register_blueprint(update)
app.register_blueprint(delete)

app.register_blueprint(movie)

app.register_blueprint(renta)
db.init_app(app)


@app.route('/') #localhost:5000/ endpoints
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/another-route')
def another_world():
    return render_template('another-index.html')

#python -m flask run
@app.route('/redirect')
def not_here():
    return redirect(url_for('another_world')) #Nombre de la funcion donde se redirecciona

if __name__ == '__main__':
    app.run()
