import numpy as np
import tifffile
from sklearn import svm
import cv2

print('-'*100)

# Cargar la imagen .tif
image_path = ["imagenes/TIF/DJI_20231004102555_0001_MS_G.TIF", "imagenes/TIF/DJI_20231004102555_0001_MS_NIR.TIF", "imagenes/TIF/DJI_20231004102555_0001_MS_R.TIF", "imagenes/TIF/DJI_20231004102555_0001_MS_RE.TIF"]
for i in image_path:
    image = tifffile.imread(i)
    # Calcular el promedio de los valores de los píxeles
    average_pixel_value = np.mean(image)
    average_pixel_value_3f = float("{0:.3f}".format(average_pixel_value))
    print(f'average_pixel_value is: {average_pixel_value}') 
    print(average_pixel_value_3f)
    #print(image)
    if average_pixel_value < 14000:
        label =  'CAT1'
    else:
        label = 'CAT2'
    print(label)

print('-'*100)

# Cargar la imagen .jpg
image_path = ["imagenes/JPG/imagen1.jpg", "imagenes/JPG/imagen2.jpg", "imagenes/JPG/imagen3.jpg", "imagenes/JPG/ortomosaico.png"]
for i in image_path:
    image = cv2.imread(i)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = np.array(gray_image)
    # Calcular el promedio de los valores de los píxeles
    average_pixel_value = np.mean(gray_image)
    average_pixel_value_3f = float("{0:.3f}".format(average_pixel_value))
    print(f'average_pixel_value is: {average_pixel_value}') 
    print(average_pixel_value_3f)

print('-'*100)

# otra forma para jpg
from PIL import Image
import numpy as np

image_path = ["imagenes/JPG/imagen1.jpg", "imagenes/JPG/imagen2.jpg", "imagenes/JPG/imagen3.jpg", "imagenes/JPG/ortomosaico.png"]
for i in image_path:
    # Cargar la imagen
    imagen = Image.open(i)
    # Convertir la imagen a escala de grises
    imagen_gris = imagen.convert('L')
    # Convertir la imagen a un array numpy
    imagen_array = np.array(imagen_gris)
    # Calcular el promedio de los valores de los píxeles
    promedio_pixeles = np.mean(imagen_array)
    print(f"El promedio del valor de los píxeles de la imagen es: {promedio_pixeles}")
    promedio_pixeles_3f = float("{0:.3f}".format(promedio_pixeles))
    print(promedio_pixeles_3f)
    
print('-'*100)

# saber tipo de dato (tiff o jpg)
import imghdr
x = imghdr.what('imagenes/JPG/imagen1.jpg')
print(x)
