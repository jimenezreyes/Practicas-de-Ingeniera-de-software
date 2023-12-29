from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from random import randint
from flask import Blueprint, request, render_template, redirect, url_for, flash

from model.model_usuario import get_all_users

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def main_view():
    """s = ''
    for usuario in get_all_users():
        s += str(usuario)
    return s"""
    usuarios = get_all_users()
    return render_template('user-list.html', usuarios= usuarios)

@user.route('/registrar', methods=('GET', 'POST'))
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        passwd = request.form['passwd']
        correo = request.form['correo']
        nuevo_usuario = Usuario(nombre=nombre, email=correo, passwd=passwd)

        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario registrado con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar usuario', 'danger')
        #user = usuario(nombre, passwd, correo)
        #try si ya existe un usuario

        return redirect (url_for('user.main_view'))
        return f'{nombre}\n{correo}\n{passwd}'
    return render_template('user-registration.html')

@user.route('/error-message')
def example_flash():
    mensaje = 'Hola soy un mensaje'
    r = randint(0,2)
    if r == 0:
        flash(mensaje)
    return render_template('error.html')

# Define la función para obtener un usuario por su ID
def get_user_by_id(user_id):
    try:
        # Utiliza el método query para buscar un usuario por su ID
        usuario = Usuario.query.get(user_id)
        return usuario
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la búsqueda
        return None  # O devuelve un valor apropiado en caso de error


update = Blueprint('update', __name__, url_prefix='/update')

@update.route('/editar/<int:id>', methods=('GET', 'POST'))
def editar_usuario(id):
    usuario = get_user_by_id(id)
    if request.method == 'POST':
        # Procesa la edición del usuario aquí
        nombre = request.form['nombre']
        passwd = request.form['passwd']
        correo = request.form['correo']
        
        try:
            usuario.nombre = nombre
            usuario.email = correo
            usuario.password = passwd  # Aquí puedes aplicar el cifrado si es necesario
            db.session.commit()
            flash('Usuario actualizado con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar usuario', 'danger') # Agregar la lógica para actualizar el usuario en la base de datos
        return redirect(url_for('user.main_view'))
    return render_template('user-edit.html', usuario=usuario)



def delete_user(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuario eliminado con éxito', 'success')
        else:
            flash('No se encontró el usuario', 'danger')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar usuario', 'danger')

delete = Blueprint('delete', __name__, url_prefix='/delete')

@delete.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_usuario(id):
    delete_user(id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario eliminado con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar usuario', 'danger')

    return redirect(url_for('user.main_view'))