from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import datetime
from datetime import date
from sqlalchemy.orm import relationship
from model.model_peliculas import get_pelicula_by_id
from model.model_usuario import get_user_by_id

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)

    # Definir las relaciones con las tablas Usuario y Pelicula si es necesario
    usuario = relationship('Usuario', back_populates='rentas')
    pelicula = relationship('Pelicula', back_populates='rentas')


    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        usuario = get_user_by_id(self.idUsuario)
        peli = get_pelicula_by_id(self.idPelicula)
        return f'Renta: {self.idRentar}\nUsuario: {usuario.nombre}\nPelicula: {peli.nombre}'