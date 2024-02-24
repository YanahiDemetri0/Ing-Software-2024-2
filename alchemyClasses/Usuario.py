from sqlalchemy import Column, Integer, String, Boolean
from alchemyClasses import db

#Demetrio Torres Yanahí

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    password = Column(String(64))
    email = Column(String(500), unique=True)
    profilePicture = Column(String, nullable=False)  # Cambiado a String para simplificar
    superUser = Column(Integer)

    # Inicializa  una instancia de la clases con los valores dados
    def __init__(self, nombre, password, email, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    
    # Imprime una cadena con los datos de un usuario
    def __str__(self):
        return f"ID: {self.idUsuario}, Nombre: {self.nombre}, Email: {self.email}, SuperUser: {self.superUser}"