import cv2
import numpy as np
from sklearn import svm
from sklearn.cluster import KMeans
from skimage import exposure
import matplotlib.pyplot as plt

# Ruta a la imagen multiespectral (reemplaza con tu propia ruta)
ruta_imagen = 'im.tif'

# Leer la imagen multiespectral utilizando OpenCV
imagen_multiespectral = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)

# Extraer las bandas necesarias (rojo e infrarrojo cercano)
banda_rojo = imagen_multiespectral[:, :, 2]
banda_infrarrojo = imagen_multiespectral[:, :, 3]

# Calcular el NDVI
ndvi = (banda_infrarrojo - banda_rojo) / (banda_infrarrojo + banda_rojo)

# Aplicar ajuste de contraste (opcional)
ndvi = exposure.equalize_hist(ndvi)

# Convertir la matriz 2D del NDVI a un vector 1D
ndvi_vector = ndvi.flatten()

# Definir zonas de interés (cultivos) basadas en umbrales NDVI
umbral_min = 0.2
umbral_max = 0.8

zonas_cultivo = np.where((ndvi >= umbral_min) & (ndvi <= umbral_max), 1, 0)

# Visualizar el NDVI y las zonas de cultivo
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(ndvi, cmap='RdYlGn')
plt.title('NDVI')
plt.subplot(1, 2, 2)
plt.imshow(zonas_cultivo, cmap='Blues')
plt.title('Zonas de Cultivo')
plt.show()

# Preparar datos para SVM
X = np.column_stack((banda_rojo.flatten(), banda_infrarrojo.flatten()))

# Entrenar el modelo SVM
modelo_svm = svm.SVC()
modelo_svm.fit(X, zonas_cultivo.flatten())

# Predicción de zonas de cultivo con SVM
prediccion_svm = modelo_svm.predict(X).reshape(banda_rojo.shape)

# Visualizar la predicción SVM
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(zonas_cultivo, cmap='Blues')
plt.title('Zonas de Cultivo (Real)')
plt.subplot(1, 2, 2)
plt.imshow(prediccion_svm, cmap='Blues')
plt.title('Zonas de Cultivo (SVM)')
plt.show()

# Preparar datos para k-means
X_flat = np.column_stack((ndvi_vector, banda_rojo.flatten(), banda_infrarrojo.flatten()))

# Entrenar el modelo k-means
k = 2  # Número de clusters
modelo_kmeans = KMeans(n_clusters=k)
modelo_kmeans.fit(X_flat)

# Asignar píxeles a los clusters
etiquetas_kmeans = modelo_kmeans.labels_.reshape(banda_rojo.shape)

# Visualizar la segmentación k-means
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(zonas_cultivo, cmap='Blues')
plt.title('Zonas de Cultivo (Real)')
plt.subplot(1, 2, 2)
plt.imshow(etiquetas_kmeans, cmap='viridis')
plt.title('Segmentación K-Means')
plt.show()
