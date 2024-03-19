from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuario import Usuario

pelicula_blueprint = Blueprint('peliculas', __name__, url_prefix='/peliculas')


@pelicula_blueprint.route('/') #localhost:5000/peliculas/
def menu_pelicula():
    return render_template('pelicula.html')


@pelicula_blueprint.route('/verPeliculas', methods=['GET']) #localhost:5000/peliculas/
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('verPeliculas.html', peliculas=peliculas)


@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('peliculaAgregada.html')
    else:
        #Obtengo la información del método post.
        nombre = request.form['nombre']
        idPelicula = request.form['idPelicula']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        peliculaNueva = Pelicula(nombre, idPelicula, genero, duracion, inventario)
        db.session.add(peliculaNueva)
        db.session.commit()
        flash('Pelicula agregada correctamente a la base de datos')
        
        # Y regreso al flujo que me hayan especificado.
        return redirect(url_for('agregarPelicula.html', nombre=nombre,  idPelicula=idPelicula, genero=genero, duracion=duracion, inventario=inventario))


@pelicula_blueprint.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_pelicula(id):
    pelicula = Pelicula.query.get(id)
    if pelicula:
        pelicula.nombre = request.form['nombre']
        pelicula.genero = request.form['genero']
        pelicula.duracion = request.form['duracion']
        pelicula.inventario = request.form['inventario']
        
        db.session.commit()
        flash('Película actualizada correctamente')
    else:
        flash('La película no existe')

    return redirect(url_for('peliculas.ver_peliculas'))


@pelicula_blueprint.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_pelicula(id):
    pelicula = Pelicula.query.get(id)
    if pelicula:
        # Verifica si hay rentas asociadas a la película
        rentas_asociadas = Rentar.query.filter_by(idPelicula=id).first()
        if rentas_asociadas:
            flash('No se puede eliminar la película porque tiene rentas asociadas')
        else:
            db.session.delete(pelicula)
            db.session.commit()
            flash('Pelicula eliminada correctamente')
    else:
        flash('La pelicula no existe')
    
    # Redirecciona al usuario a la página donde se listan todas las películas
    return redirect(url_for('peliculas.ver_peliculas'))

@pelicula_blueprint.route('/borrar_todas', methods=['POST'])
def borrar_todas_las_peliculas():
    # Selecciona todas las películas de la base de datos
    peliculas = Pelicula.query.all()

    if peliculas:
        # Borra cada película individualmente
        for pelicula in peliculas:
            db.session.delete(pelicula)
        db.session.commit()
        flash('Todas las películas han sido borradas correctamente')
    else:
        flash('No hay películas para borrar')

    # Redirecciona al usuario a la página donde se listan todas las películas
    return redirect(url_for('peliculas.ver_peliculas'))




