import mysql.connector
from io import BytesIO
from PIL import Image

connection = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    port = "3306",
    database="Imágenes" 
)

print("-"*60)
if connection:
    print("Conexión exitosa")
else:
    print("Error de conexión")

# Crear base de datos
cursor = connection.cursor()

# Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS Imágenes")
cursor.execute("USE Imágenes")

print("-"*60)
# mostrar bases de datos ya creadas
cursor.execute("SHOW DATABASES")
print("Bases de datos existentes:")
for bd in cursor:
    print(f"Bd: {bd}")

# Crear la tabla de imágenes

# Borrar tabla si existe 
cursor.execute("drop table if exists imágenes")
# Crear una nueva tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS imágenes (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Nombre VARCHAR(255) NOT NULL,
        Imagen LONGBLOB NOT NULL,
        Estado_planta VARCHAR(255) NOT NULL, # Otra opción: Estado_planta ENUM('Sana', 'Enferma') NOT NULL
        Fecha_captura DATE NOT NULL, 
        Hora_captura TIME NOT NULL,
        Ubicación_geográfica VARCHAR(255),
        Condiciones_climáticas TEXT,
        UNIQUE KEY nombre_archivo_unique (Nombre)              
    )
""")


# -------------------------------------- Insertar imágenes -----------------------------------
def insertar_imagen(Nombre, Ruta_imagen, Estado_planta, Fecha_captura, Hora_captura, Ubicación_geográfica, Condiciones_climáticas):

    #cursor.execute("DELETE FROM Imágenes") # Borra todas las filas de la tabla

    # Leer la imagen como bytes
    with open(Ruta_imagen, "rb") as file:
        imagen_blob = file.read()

    # Insertar la imagen en la base de datos
    query = "INSERT INTO Imágenes (Nombre, Imagen, Estado_planta, Fecha_captura, Hora_captura, Ubicación_geográfica, Condiciones_climáticas) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (Nombre, imagen_blob, Estado_planta, Fecha_captura, Hora_captura, Ubicación_geográfica, Condiciones_climáticas)
    cursor.execute(query, data)


# Ingresar las imágenes
insertar_imagen("imagen1", "imagen1.jpg", "Enferma", "2024-01-01", "12:00:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Soleado y ventoso")
insertar_imagen("imagen2", "imagen2.jpg", "Sana", "2024-01-01", "12:30:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Nublado con lluvia")
insertar_imagen("imagen3", "imagen3.jpg", "Enferma", "2024-01-01", "01:00:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Soleado sin viento")

print("-"*60)

# Mostrar datos de la tabla
print("Datos de la tabla:")

# Forma 1: Todas las columnas
#query = "SELECT * FROM Imágenes"
#cursor.execute(query)
#resultados = cursor.fetchall()
#print(resultados)

# Forma 2: Columnas individuales
#cursor.execute("SELECT Nombre, Estado_planta, Ubicación_geográfica, Condiciones_climáticas FROM imágenes")
#resultados = cursor.fetchall()
#for resultado in resultados:
#    print(resultado)

# Forma 3: Todos, pero mejor organizados 
query = "SELECT * FROM Imágenes"
cursor.execute(query)
resultados = cursor.fetchall()
for resultado in resultados:
    # Obtener los valores de cada columna
    Id_imagen, Nombre, Imagen_blob, Estado_planta, Fecha_captura, Hora_captura, Ubicacion_geográfica, Condiciones_climáticas = resultado

    # Convertir los bytes a una imagen
    imagen_bytes = BytesIO(Imagen_blob)
    imagen = Image.open(imagen_bytes)
    #imagen.show() # Mostrar imagen

    # Imprimir otros datos
    print(f"""ID: {Id_imagen}
        Nombre: {Nombre}
        Imagen = {imagen_bytes}
        Estado de la Planta: {Estado_planta}
        Fecha de Captura: {Fecha_captura}
        Hora de Captura: {Hora_captura}
        Ubicación geográfica: {Ubicacion_geográfica}
        Condiciones Climáticas: {Condiciones_climáticas}
    """)

print("-"*60)
# Confirmar la transacción y cerrar la conexión
connection.commit()
cursor.close()
connection.close()

