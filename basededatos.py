import mysql.connector

conn = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    port = "3306", 
)

#print(conn)

# Crear base de datos
cursor = conn.cursor()

# Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS Imágenes")
cursor.execute("USE Imágenes")

# mostrar bases de datos ya creadas
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)

# Crear la tabla de imágenes

# Borrar tabla si existe 
cursor.execute("drop table if exists imágenes")
# Crear una nueva tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS imágenes (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Nombre VARCHAR(255) NOT NULL,
        Imagen LONGBLOB NOT NULL,
        Estado_planta VARCHAR(255) NOT NULL,
        Fecha_capture DATE NOT NULL,
        Hora_capture TIME NOT NULL,
        Ubicación_geográfica VARCHAR(255),
        Condiciones_climáticas TEXT,
        UNIQUE KEY nombre_archivo_unique (Nombre)              
    )
""")
#Estado_planta ENUM('Sana', 'Enferma') NOT NULL

# Cerrar la conexión
conn.commit()
cursor.close()
conn.close()

