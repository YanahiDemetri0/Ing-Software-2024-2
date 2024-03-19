from sqlalchemy import Column, Integer, String, Boolean
from alchemyClasses import db

#Demetrio Torres Yanahí

class Pelicula(db.Model):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, default=1)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario    
        
    def __str__(self):
        return f"ID: {self.idPelicula}, Nombre: {self.nombre}, Género: {self.genero}, Duración: {self.duracion}, Inventario: {self.inventario}"