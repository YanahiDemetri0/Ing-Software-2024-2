from sqlalchemy import Column, Integer, String, Boolean,  ForeignKey, DateTime, SmallInteger
from alchemyClasses import db
from sqlalchemy.orm import relationship


#Demetrio Torres Yanahí
class Rentar(db.Model):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(SmallInteger, default=0)


    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"ID Rentar: {self.idRentar}, Usuario: {self.idUsuario}, Película: {self.idPelicula}, Fecha de renta: {self.fecha_renta}, Días de renta: {self.dias_de_renta}, Estatus: {self.estatus}"