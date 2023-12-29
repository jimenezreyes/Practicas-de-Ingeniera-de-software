
from flask import Blueprint, request, redirect, url_for
from model.model_usuario import delete_user

delete = Blueprint('delete', __name__, url_prefix='/delete')

@delete.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    delete_user(id)  # Agregar la lógica para eliminar el usuario de la base de datos
    return redirect(url_for('user.main_view'))