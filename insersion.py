import mysql.connector
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Conectar a la base de datos
db_connection = mysql.connector.connect(
    host='xxxxxxx',
    user='xxxxxxx',
    password='xxxxxxxxx',
    database='xxxxxxxx'
)


cursor = db_connection.cursor()

# Inserción en la tabla 'equipos'
equipos_ids = []  # Lista para almacenar los IDs de equipos

for _ in range(20):  # Generar 20 equipos
    nombre = fake.company()
    ciudad = fake.city()
    estadio = fake.company_suffix()
    fecha_fundacion = fake.date_of_birth(minimum_age=100)

    cursor.execute(
        "INSERT INTO equipos (nombre, ciudad, estadio, fechaFundacion) VALUES (%s, %s, %s, %s)",
        (nombre, ciudad, estadio, fecha_fundacion)
    )
    equipos_ids.append(cursor.lastrowid)  # Guardar el ID del último equipo insertado

print("IDs de equipos insertados:", equipos_ids)  # Verificar los IDs de equipos

# Inserción en la tabla 'jugadores'
for _ in range(10000):  # Generar 1000 jugadores
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha_nacimiento = fake.date_of_birth(minimum_age=18)
    
    nacionalidad = fake.country()[:50]  # Truncar a 50 caracteres
    posicion = random.choice(['Delantero', 'Mediocampista', 'Defensa', 'Portero'])
    numero_camiseta = random.randint(1, 99)
    
    # Elegir un equipo aleatorio que exista en la tabla 'equipos'
    equipo_actual = random.choice(equipos_ids)  # Usar IDs válidos
    print(f"Inserción de jugador: {nombre} {apellido}, Equipo ID: {equipo_actual}")  # Verificación

    cursor.execute(
        "INSERT INTO jugadores (nombre, apellido, fechaNacimiento, nacionalidad, posicion, numeroCamiseta, equipoActual) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nombre, apellido, fecha_nacimiento, nacionalidad, posicion, numero_camiseta, equipo_actual)
    )

# Inserción en la tabla 'arbitros'
for _ in range(20):  # Generar 20 árbitros
    nombre = fake.first_name()
    apellido = fake.last_name()
    nacionalidad = fake.country()[:50]  # Limitar a 50 caracteres
    experiencia = random.randint(1, 30)

    cursor.execute(
        "INSERT INTO arbitros (nombre, apellido, nacionalidad, experiencia) VALUES (%s, %s, %s, %s)",
        (nombre, apellido, nacionalidad, experiencia)
    )

# Commit para guardar los cambios
db_connection.commit()

# Cerrar la conexión
cursor.close()
db_connection.close()


