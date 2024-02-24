from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Rentar import Rentar
from datetime import datetime

#Demetrio Torres Yanahi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

# Muestra los registros que se encuentran en la tabla
def mostrar_registros(tabla):
    with app.app_context():
        registros = Usuario.query.all()
        for registro in registros:
            print(registro)

# Filtra los registros de usuatio por su id
def filtrar_Usuario_por_id(id):
    with app.app_context():
        registro = Usuario.query.filter(Usuario.idUsuario == id).first()
        if registro:
            print(registro)
        else:
            print("No se encontró ningún registro con el ID proporcionado. \%" )


# Filtra los registros de una pelicla por su id
def filtrar_Pelicula_por_id(id):
    with app.app_context():
        registro = Pelicula.query.filter(Pelicula.idPelicula == id).first()
        if registro:
            print(registro)
        else:
            print("No se encontró ningún registro con el ID proporcionado. \%" )

# Filtra los registros de una renta por su id
def filtrar_Rentar_por_id(id):
    with app.app_context():
        registro = Rentar.query.filter(Rentar.idRentar == id).first()
        if registro:
            print(registro)
        else:
            print("No se encontró ningún registro con el ID proporcionado. \%" )

# Cambia el nombre de un usuario por otro de acuerdo a su id 
def actualizar_nUsuario(id_usuario, nuevo_nombre):
    with app.app_context():
        registro = Usuario.query.filter_by(idUsuario=id_usuario).first()
        if registro:
            registro.nombre = nuevo_nombre
            db.session.commit()
            print("Se actualizo el nombre del usuario con el id " + id_usuario)
        else:
            print("No se encontró ningún usuario con el ide " + id_usuario)

# Cambia el nombre de unq pelicula por otro de acuerdo a su id 
def actualizar_nPelicula(id_pelicula, nuevo_nombre):
    with app.app_context():
        registro = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
        if registro:
            registro.nombre = nuevo_nombre
            db.session.commit()
            print("Se actualizo el nombre de la pelicula con el id " + id_pelicula)
        else:
            print("No se encontró ningún usuario.")

# Cambia la feha de una renta por otra de acuerdo a su id 
def actualizar_fecha_renta(id_renta, nueva_fecha):
    with app.app_context():
        renta = Rentar.query.filter_by(idRentar=id_renta).first()
        renta.fecha_renta = nueva_fecha

def eliminar_reg_por_idUsuario(id):
    with app.app_context():
        registro = Usuario.query.filter(Usuario.idUsuario == id).first()
        if registro != None:
                #Elimina los registros de renta del usuario
                Rentar.query.filter_by(idUsuario=id).delete()
                db.session.commit()

                # Elimina el usuario después de eliminar los registros relacionados
                db.session.delete(registro)
                db.session.commit()
                print(f"Eliminación del usuario realizada")
        else:
            print(f'ID {id} no encontrado')

def eliminar_reg_por_idPelicula(id):
    with app.app_context():
        #Busca la película por su ID
        registro = Pelicula.query.filter(Pelicula.idPelicula == id).first()
        if registro != None:
                #Elimina los registros de renta de la pelicula
                Rentar.query.filter_by(idPelicula=id).delete()
                db.session.commit()

                # Elimina la pelicula después de eliminar los registros relacionados
                db.session.delete(registro)
                db.session.commit()
                print(f"Eliminación del usuario realizada")
        else:
            print(f'ID {id} no encontrado')


def eliminar_registro_por_idRenta(id):
    with app.app_context():
        registro = Rentar.query.filter_by(idRentar=id).first()
        db.session.delete(registro)
        db.session.commit()

def eliminar_todos_los_datos(tabla):
    with app.app_context():
        try:
            # Elimina todos los registros relacionados en la tabla Rentar
            Rentar.query.delete()
            db.session.commit()
            # Elimina todos los datos de la tabla
            tabla.query.delete()
            db.session.commit()
            print("Todos los datos de la tabla han sido eliminados")
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar todos los datos de la tabla: {str(e)}")


def mostrar_menu():
    print("Bienvenido al Menú, :")
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por id")
    print("3.  Actualizar la columna nombre de un registro")
    print("4. Eliminar un registro por id. ")
    print("5. Eliminar todos los registros.")
    print("6. Salir.")


def opcion_1_menu():
    with app.app_context():
        print("La tablas en tu base de datos son:")
        print("(1) Usuario    (2) Pelicula    (3) Rentar")
        eleccion = input("De que tabla quieres ver los registros:  ")

        if eleccion == "1":
            mostrar_registros(Usuario)
        elif eleccion == "2":
            mostrar_registros(Pelicula)
        elif eleccion == "3":
            mostrar_registros(Rentar)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def opcion2():
    with app.app_context():
        print("La tablas en tu base de datos son:")
        print("(1) Usuario    (2) Pelicula    (3) Rentar")
        eleccion = input("De que tabla quieres ver los registros?  ")
        id = input("¿Cúal es el id que deseas buscar? ")

        if eleccion == "1":
            filtrar_Usuario_por_id(id)
        elif eleccion == "2":
            filtrar_Pelicula_por_id(id)
        elif eleccion == "3":
            filtrar_Rentar_por_id(id)
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def opcion_3():
    with app.app_context():
        print("De que tabla quieres actualizar datos?  ")
        eleccion = input("1 Usuario    2 Pelicula    (3) Rentar  ")
        id = input("¿Cúal es el id del registro? ")

        if eleccion == "1":
            nombre = input("¿Cúal es el nuevo nombre que desea asignar? ")
            actualizar_nUsuario(id,nombre)
        elif eleccion == "2":
            nombre = input("¿Cúal es el nuevo nombre que desea asignar? ")
            actualizar_nPelicula(id,nombre)
        elif eleccion == "3":
            fecha = input("¿Cuál es la nueva fecha? (YYYY-MM-DD)")
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            actualizar_fecha_renta(id,fecha)
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def opcion_4():
    with app.app_context():
        print("De que tabla quieres eliminar registros?  ")
        eleccion = input("1 Usuario    2 Pelicula    (3) Rentar  ")
        id = input("¿Cúal es el id del registro? ")

        if eleccion == "1":
            eliminar_reg_por_idUsuario(id)
        elif eleccion == "2":
            eliminar_reg_por_idPelicula(id)
        elif eleccion == "3":
            eliminar_registro_por_idRenta(id)
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def opcion_5():
    with app.app_context():
        print("De que tabla quieres eliminar TODOS los registros?  ")
        eleccion = input("1 Usuario    2 Pelicula    (3) Rentar  ")
        if eleccion == "1":
            eliminar_todos_los_datos(Usuario)
        elif eleccion == "2":
            eliminar_todos_los_datos(Pelicula)
        elif eleccion == "3":
            eliminar_todos_los_datos(Rentar)
        
        db.session.commit()
        print(f"Tabla vaciada correctamente")

while True:
    mostrar_menu()
    opcion = input("¿Qué deseas hacer?  ")

    if opcion == "1":
        opcion_1_menu()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        opcion_4()
    elif opcion == "5":
        opcion_5()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
if __name__ == "__main__":
    app.run()