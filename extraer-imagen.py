import mysql.connector
from io import BytesIO
from PIL import Image
import numpy as np

def extraer_todas_las_imagenes():
    # Conectar a MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="Imágenes"
    )

    cursor = connection.cursor()

    # Recuperar todas las filas de la base de datos
    query = "SELECT * FROM Imágenes"
    cursor.execute(query)
    resultados = cursor.fetchall()

    datos = []
    datos1 = []
    for resultado in resultados:
        # Obtener los valores de cada columna
        Id_imagen, Nombre, Imagen_blob, Estado_planta, Fecha_captura, Hora_captura, Ubicacion_geográfica, Condiciones_climáticas = resultado

        # Convertir los bytes a una imagen
        imagen_bytes = BytesIO(Imagen_blob)
        imagen = Image.open(imagen_bytes)
        imagen_np = np.array(imagen) # Sería la imagen multiespectral en forma de array 
        #imagen.show() # Mostrar imagen con programa del pc

        # Imprimir otros datos
        print(f"""ID: {Id_imagen}
            Nombre: {Nombre}
            Imagen = {imagen}
            Estado de la Planta: {Estado_planta}
            Fecha de Captura: {Fecha_captura}
            Hora de Captura: {Hora_captura}
            Ubicación geográfica: {Ubicacion_geográfica}
            Condiciones Climáticas: {Condiciones_climáticas}
        """)
        
        datos.append(Nombre)
        datos1.append(Id_imagen)

    print(datos)
    print(datos1)
    # Cerrar la conexión
    cursor.close()
    connection.close()

# Extraer las imágenes
extraer_todas_las_imagenes()