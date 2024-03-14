import numpy as np
import tifffile
import os

# Ruta de las imágenes
ruta_imagenes = "D:\BD"

# Umbral para determinar si una imagen es "enferma"
umbral = 0.5  

# Recorrer todas las imágenes en la carpeta
for imagen_nombre in os.listdir(ruta_imagenes):
    # Leer la imagen
    imagen_tif = tifffile.imread(os.path.join(ruta_imagenes, imagen_nombre))

    # Normalizar la imagen
    imagen_normalizada = imagen_tif.astype(np.float32) / np.iinfo(imagen_tif.dtype).max
        
    # Determinar la etiqueta según la imagen normalizada
    if np.any(imagen_normalizada > umbral):
        print('-'*50)
        print(f'{imagen_nombre}: Cultivo enfermo')
        print(np.max(imagen_normalizada))
        print('-'*50)
    else:
        print('-'*50)
        print(f'{imagen_nombre}: Cultivo sano')
        print(np.max(imagen_normalizada))
        print('-'*50)
        