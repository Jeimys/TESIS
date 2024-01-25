import mysql.connector

def insertar_imagen(Nombre, Ruta_imagen, Estado_planta, Fecha_capture, Hora_capture, Ubicación_geográfica, Condiciones_climáticas):
    # Conectar a MySQL
    connection = mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "",
        port = "3306",
        database="Imágenes"
    )

    cursor = connection.cursor()

    #cursor.execute("DELETE FROM Imágenes") # Borra todas las filas de la tabla

    # Leer la imagen como bytes
    with open(Ruta_imagen, "rb") as file:
        imagen_blob = file.read()

    # Insertar la imagen en la base de datos
    query = "INSERT INTO Imágenes (Nombre, Imagen, Estado_planta, Fecha_capture, Hora_capture, Ubicación_geográfica, Condiciones_climáticas) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (Nombre, imagen_blob, Estado_planta, Fecha_capture, Hora_capture, Ubicación_geográfica, Condiciones_climáticas)
    cursor.execute(query, data)

    #cursor.execute("select ID from imágenes")
    #for fila in cursor:
    #    print(fila)

    query = "SELECT Id FROM Imágenes"
    cursor.execute(query)
    resultados = cursor.fetchall()
    print(resultados)

    print(cursor)

    # Confirmar la transacción y cerrar la conexión
    connection.commit()
    cursor.close()
    connection.close()

# Ejemplo de uso
insertar_imagen("imagen1", "C:/Users/Jey Pérez/OneDrive/Documentos/TESIS/imagen1.jpg", "Enferma", "2024-01-01", "12:00:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Soleado y ventoso")
insertar_imagen("imagen2", "C:/Users/Jey Pérez/OneDrive/Documentos/TESIS/imagen2.jpg", "Sana", "2024-01-01", "12:30:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Nublado con lluvia")
insertar_imagen("imagen3", "C:/Users/Jey Pérez/OneDrive/Documentos/TESIS/imagen3.jpg", "Enferma", "2024-01-01", "01:00:00", "Lat: XX.XXXX, Lon: YY.YYYY", "Soleado sin viento")
