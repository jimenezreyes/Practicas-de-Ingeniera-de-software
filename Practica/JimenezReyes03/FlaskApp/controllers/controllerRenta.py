from flask import Blueprint, render_template, redirect, url_for, flash, request
from alchemyClasses import db
from alchemyClasses.Renta import Renta
from datetime import date
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from datetime import datetime
from sqlalchemy.orm import relationship

renta = Blueprint('renta', __name__, url_prefix='/renta')

# Listar todas las rentas
@renta.route('/')
def listar_rentas():
    rentas = Renta.query.all()
    return render_template('renta-list.html', rentas=rentas)

# Crear una nueva renta
@renta.route('/crear', methods=['GET', 'POST'])
def crear_renta():
    if request.method == 'POST':
        idUsuario = request.form.get('idUsuario')
        idPelicula = request.form.get('idPelicula')
        fecha_renta = datetime.now()
        dias_de_renta = request.form.get('dias_de_renta')
        estatus = 0  # Por defecto, la renta no está vencida (puedes cambiarlo según tus necesidades)


        # Validar que existan el usuario y la película
        usuario = Usuario.query.get(idUsuario)
        pelicula = Pelicula.query.get(idPelicula)

        if not usuario or not pelicula:
            flash('Usuario o película no encontrados. Verifica los IDs.', 'danger')
            return redirect(url_for('renta.crear_renta'))

        nueva_renta = Renta(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)

        try:
            db.session.add(nueva_renta)
            db.session.commit()
            flash('Renta creada con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al crear renta', 'danger')

        return redirect(url_for('renta.listar_rentas'))
    
    return render_template('renta-create.html')

# Ver detalles de una renta
@renta.route('/ver/<int:id>')
def ver_renta(id):
    renta = Renta.query.get(id)
    return render_template('renta-detail.html', renta=renta)



# Actualizar una renta 
@renta.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_renta(id):
    renta = Renta.query.get(id)

    if renta:
        estatus_actual = int(request.form['estatus_actual'])
        renta.estatus = not estatus_actual  # Invierte el estado (entregado o no entregado)
        renta.fechaDevolucion = datetime.now()  # Actualiza la fecha de devolución


        try:
            db.session.commit()
            flash('Renta actualizada con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar la renta', 'danger')

    return redirect(url_for('renta.listar_rentas'))    


@renta.route('/actualizar/<int:id>', methods=['GET'])
def mostrar_pagina_actualizacion(id):
    renta = Renta.query.get(id)
    return render_template('actualizar-renta.html', renta=renta)    