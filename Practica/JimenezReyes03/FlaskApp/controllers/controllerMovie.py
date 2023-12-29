from flask import Blueprint, render_template, redirect, url_for, flash, request
from alchemyClasses import db
from model.model_peliculas import Pelicula
from model.model_usuario import Usuario  # Si necesitas relacionar películas con usuarios
from model.model_peliculas import get_all_peliculas
from model.model_peliculas import get_pelicula_by_id

movie = Blueprint('movie', __name__, url_prefix='/movie')

# Listar todas las películas
@movie.route('/')
def listar_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('movie-list.html', peliculas=peliculas)

# Ver detalles de una película
@movie.route('/ver/<int:id>')
def ver_pelicula(id):
    pelicula = Pelicula.query.get(id)
    return render_template('movie-detail.html', pelicula=pelicula)

# Crear una nueva película
@movie.route('/crear', methods=['GET', 'POST'])
def registrar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)

        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            flash('Película creada con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al crear película', 'danger')

        return redirect(url_for('movie.listar_peliculas'))
    
    return render_template('movie-registration.html')

# Editar una película existente
@movie.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pelicula(id):
    pelicula = Pelicula.query.get(id)

    if request.method == 'POST':
        # Procesa la edición de la película aquí
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        try:
            pelicula.nombre = nombre
            pelicula.genero = genero
            pelicula.duracion = duracion
            pelicula.inventario = inventario
            db.session.commit()
            flash('Película actualizada con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar película', 'danger')

        return redirect(url_for('movie.listar_peliculas'))
    
    return render_template('movie-edit.html', pelicula=pelicula)

# Eliminar una película
@movie.route('/eliminar/<int:id>', methods=['GET','POST'])
def eliminar_pelicula(id):
    pelicula = Pelicula.query.get(id)

    try:
        db.session.delete(pelicula)
        db.session.commit()
        flash('Película eliminada con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar película', 'danger')

    return redirect(url_for('movie.listar_peliculas'))