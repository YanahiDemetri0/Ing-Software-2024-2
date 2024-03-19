from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuario import Usuario

usuario_blueprint = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@usuario_blueprint.route('/') #localhost:5000/peliculas/
def menu_usuarios():
    return render_template('menu_usuario.html')


@usuario_blueprint.route('/ver_usuarios', methods=['GET']) #localhost:5000/peliculas/
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('ver_usuario.html', usuarios=usuarios)


@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuarios():
    if request.method == 'GET':
        return render_template('agregar_Usuario.html')
    else:
        #Obtengo la información del método post.
        nombre = request.form['nombre']
        idUsuario = request.form['idUsuario']
        password = request.form['password']
        email = request.form['email']
        profilePicture = request.form['profilePicture']
        superUser = request.form['superUser']

        usuarioNuevo = Usuario(nombre, idUsuario, password, email, profilePicture, superUser)
        db.session.add(usuarioNuevo)
        db.session.commit()
        flash('Usuario agregado correctamente a la base de datos')
        
        # Y regreso al flujo que me hayan especificado.
        return redirect(url_for('usuarios.ver_usuarios'))



@usuario_blueprint.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_usuarios(id):
    usuarios = Usuario.query.get(id)
    if usuarios:
        usuarios.nombre = request.form['nombre']
        usuarios.idUsuario = request.form['idUsuario']
        usuarios.password = request.form['password']
        usuarios.email = request.form['email']
        usuarios.superUser = request.form['superUser']
        
        db.session.commit()
        flash('Usuario actualizado correctamente')
    else:
        flash('El usuario no existe')

    return redirect(url_for('usuarios.ver_usuarios'))


@usuario_blueprint.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_pelicula(id):
    usuarios = Usuario.query.get(id)
    if usuarios:
        # Verifica si hay rentas asociadas a la película
        rentas_asociadas = Rentar.query.filter_by(idUsuario=id).first()
        if rentas_asociadas:
            flash('No se puede eliminar el usuario porque tiene rentas asociadas')
        else:
            db.session.delete(usuarios)
            db.session.commit()
            flash('Usuario eliminado correctamente')
    else:
        flash('El usuario no existe')
    
    # Redirecciona al usuario a la página donde se listan todas las películas
    return redirect(url_for('usuarios.ver_usuarios'))

@usuario_blueprint.route('/borrar_todos', methods=['POST'])
def borrar_todos_los_usuarios():
    # Selecciona todas las usuarips de la base de datos
    usuarios = Usuario.query.all()

    if usuarios:
        # Borra cada usuario individualmente
        for usuarios in usuarios:
            db.session.delete(usuarios)
        db.session.commit()
        flash('Todas los usuarios han sido borradas correctamente')
    else:
        flash('No hay usuarios para borrar')

    # Redirecciona al usuario a la página donde se listan todas los usuarios
    return redirect(url_for('usuarios.ver_usuarios'))




