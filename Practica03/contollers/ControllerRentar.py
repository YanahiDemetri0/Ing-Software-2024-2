from flask import Blueprint, request, flash, url_for, redirect, render_template
from alchemyClasses import db
from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula

rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

@rentar_blueprint.route('/') #localhost:5000/peliculas/
def menu_renta():
    return render_template('renta.html')

@rentar_blueprint.route('/nuevo', methods=['POST'])
def rentar_pelicula():
    idUsuario = request.form['idUsuario']
    idPelicula = request.form['idPelicula']

    usuario = Usuario.query.get(idUsuario)
    pelicula = Pelicula.query.get(idPelicula)

    if usuario and pelicula:
        nueva_renta = Rentar(idUsuario=idUsuario, idPelicula=idPelicula)
        db.session.add(nueva_renta)
        db.session.commit()
        flash('Película alquilada correctamente')
    else:
        flash('El usuario o la película no existen')

    return redirect(url_for('peliculas.ver_peliculas'))

@rentar_blueprint.route('/ver_rentas', methods=['GET'])
def ver_rentas():
    rentas = Rentar.query.all()
    return render_template('verRentas.html', rentas=rentas)

@rentar_blueprint.route('/actualizar_entrega/<int:id>', methods=['POST'])
def actualizar_entrega_renta(id):
    renta = Rentar.query.get(id)
    if renta:
        renta.entregada = not renta.entregada  # Cambiar el valor de entregada
        db.session.commit()
        flash('Estado de entrega actualizado correctamente')
    else:
        flash('La renta no existe')

    return redirect(url_for('rentar.ver_rentas'))


