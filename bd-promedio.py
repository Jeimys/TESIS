import os
import numpy as np
import tifffile
from PIL import Image

# Directorio que contiene las imágenes
directorio = "D:/bd"

# Enumerar archivos en el directorio
archivos = os.listdir(directorio)

# Cargar cada imagen
for imagen in archivos:
    ruta_imagen = os.path.join(directorio, imagen)
    with Image.open(ruta_imagen) as img:
        # Convertir la imagen a un arreglo numpy
        image = np.array(img)
        # Calcular el promedio de los valores de los píxeles
        average_pixel_value = np.mean(image)
        average_pixel_value_3f = float("{0:.3f}".format(average_pixel_value))
        print(f'{imagen} is: {average_pixel_value}') 
        print(average_pixel_value_3f)
        if average_pixel_value < 14000:
            label =  'CAT1'
        else:
            label = 'CAT2'
        print(label)
    print('-'*100)
