from flask import Blueprint, request, render_template, redirect, url_for
from model.model_usuario import get_user_by_id, update_user

update = Blueprint('update', __name__, url_prefix='/update')

@update.route('/editar/<int:id>', methods=('GET', 'POST'))
def editar_usuario(id):
    usuario = get_user_by_id(id)
    if request.method == 'POST':
        # Procesa la edición del usuario aquí
        nombre = request.form['nombre']
        passwd = request.form['passwd']
        correo = request.form['correo']
        update_user(id, nombre, correo, passwd)  # Agregar la lógica para actualizar el usuario en la base de datos
        return redirect(url_for('user.main_view'))
    return render_template('user-edit.html', usuario=usuario)