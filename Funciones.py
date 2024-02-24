import pymysql.cursors
import uuid
import random
import secrets
import string

from datetime import datetime, timedelta
from faker import Faker

#Demetrio Torres Yanahí


# Conexión a la base de datos
connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             cursorclass=pymysql.cursors.DictCursor)


# Crear una instancia de Faker
fake = Faker('es_ES')

#Funcion para crear contrasrñas de 12 caracteres
def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

# Función para generar oraciones de hasta tres palabras para nombar peliculas
def generar_nombre_pelicula():
    # Generar una lista de palabras aleatorias
    palabras = [fake.word() for _ in range(random.randint(1, 3))]
    # Unir las palabras en una oración
    oracion = ' '.join(palabras)
    return oracion

#Funcion para elegir un genero de peliculas random
def genero_pelicula():
    generos = [
        "Aciion", "Drama", "Terror", "Romantica", "Fantasia", "Ciencia ficción", "Musicales", "Suspenso"
        ]
    return random.choice(generos)

# Generar una fecha aleatoria dentro de un rango específico
def generar_fecha_aleatoria(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    random_days = random.randint(0, (end_datetime - start_datetime).days)
    return start_datetime + timedelta(days=random_days)


# Funcion para insertar registros aleatorios a las tablas Usuario, pelicula y renta
def insertar_registros():
    try:
        with connection.cursor() as cursor:
            #Insertar un usuario
            email_usuario = f'usuario{uuid.uuid4().hex[:8]}@demetrios.com'
            sql = "INSERT INTO usuarios (nombre, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (fake.name(), generar_contrasena(12), email_usuario))
            ultimo_idUsuario = cursor.lastrowid
            

            # Insertar películas
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (generar_nombre_pelicula(), genero_pelicula(), random.randint(90, 130), random.randint(1, 10)))
            ultimo_idPelicula = cursor.lastrowid

           
            # Insertar rentas
            fecha_renta = generar_fecha_aleatoria('2024-01-01', '2024-01-31')
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (ultimo_idUsuario, ultimo_idPelicula,fecha_renta , random.randint(1, 10)))
#datetime.now()
        connection.commit()
        print("Registros insertados correctamente.")
    except Exception as e:
        print("Error al insertar registros:", e)


# Funcion para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(apellido_termina_con):
    try:
        with connection.cursor() as cursor:
             # Consulta SQL para filtrar los usuarios por apellido que termine con la cadena especificada
            sql = "SELECT * FROM usuarios WHERE nombre LIKE %s"
            cursor.execute(sql, (f"%{apellido_termina_con}",))
            # Obtener los resultados de la consulta
            usuarios = cursor.fetchall()
            for row in usuarios:
                print(row)
            return usuarios
    except Exception as e:
        print("Error al filtrar usuarios por apellido:", e)


# FUnción para cambiar el género de una película
def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
            cursor.execute(sql, (nuevo_genero, nombre_pelicula))
        connection.commit()
        print("Género de la película actualizado correctamente.")
    except Exception as e:
        print("Error al cambiar el género de la película:", e)


# Función para eliminar rentas que tengan más de 3 días en la base
def eliminar_rentas_antiguas():
    try:
        with connection.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
        connection.commit()
        print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        print("Error al eliminar rentas antiguas:", e)


# Ejemplos de uso
insertar_registros()
# apellido_termina_con = input("Ingrese la cadena con la que desea filtrar los apellidos: ")
# filtrar_usuarios_por_apellido(apellido_termina_con)
# peliculaCambio = input("Ingrese el nombre de la película a la que le va a cambair el género: ")
# nuevoGenero = input("Ingrese el nuevo género que le va a asignar a la película que eligio: ")
# cambiar_genero_pelicula(peliculaCambio, nuevoGenero)
# eliminar_rentas_antiguas()

# Cerrar conexión
connection.close()
