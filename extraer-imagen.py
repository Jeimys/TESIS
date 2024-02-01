import mysql.connector
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

# Conectar a MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="Imágenes"
)

cursor = connection.cursor()

def extraer_todas_las_imagenes():
    # Recuperar todas las filas de la base de datos
    query = "SELECT * FROM Imágenes"
    cursor.execute(query)
    resultados = cursor.fetchall()
    return resultados


# Extraer las imágenes llamando la función
resultados = extraer_todas_las_imagenes()


# Mostrar IDs disponibles
print("IDs disponibles:")
for resultado in resultados:
    Id_imagen, Nombre, _, _, _, _, _, _ = resultado
    print(f"ID: {Id_imagen}, Nombre: {Nombre}")

# Preguntar al usuario por el ID de la imagen
id_elegido = int(input("Ingrese el ID de la imagen que desea ver: "))

for resultado in resultados:
# Obtener los valores de cada columna
    Id_imagen, Nombre, Imagen_blob, Estado_planta, Fecha_captura, Hora_captura, Ubicacion_geográfica, Condiciones_climáticas = resultado

    if Id_imagen == id_elegido:
        # Convertir los bytes a una una matriz NumPy
        imagen_bytes = BytesIO(Imagen_blob)
        imagen_array = np.frombuffer(imagen_bytes.getvalue(), dtype=np.uint8)

        # Decodificar la imagen con OpenCV
        imagen = cv2.imdecode(imagen_array, cv2.IMREAD_UNCHANGED)

        # Mostrar la imagen
        cv2.imshow("Imagen Multiespectral", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

 
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
        
        break  # Salir del bucle una vez que se encuentra la imagen

# Cerrar la conexión
cursor.close()
connection.close()