import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from tkinter import Tk, Label, Button, Frame, filedialog, Entry
from PIL import ImageTk, Image
import numpy as np


## ---------------------------- Base de datos de entrenamiento -----------------------


#dir = "C:\\Users\\Jey Pérez\\OneDrive\\Documentos\\GitHub\\TESIS\\Imagenes"
# dir = "D:\\IMAGENES\\Imagenes"
# Categories = ['JPG', 'TIF']
# data = []

# for category in Categories:
#     path = os.path.join(dir, category)
#     label = Categories.index(category)
    
#     for img in os.listdir(path):
#         imgpath = os.path.join(path, img)
#         imagen_img = cv2.imread(imgpath, 0)
#         try:
#             imagen_img = cv2.resize(imagen_img, (50, 50))
#             image = np.array(imagen_img).flatten()
#             data.append([image, label])
#         except Exception as e:
#             pass

# print(len(data))

# pick_in = open('data1.pickle', 'wb')
# pickle.dump(data, pick_in)
# pick_in.close()


## ------------------------------- Entrenamiento con la base de datos ---------------------------------

pick_in = open('data1.pickle', 'rb')
data = pickle.load(pick_in)
pick_in.close()


random.shuffle(data)
features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.6)

# model = SVC(C=1, kernel='poly', gamma='auto')
# model.fit(xtrain, ytrain)

## ---------------------------------- Guardar el modelo entrenado -----------------------------------------------

# pick = open('model.sav', 'wb')
# pickle.dump(model, pick)
# pick.close()

## ----------------------------- Hacer predicciones usando la bd de entrenamiento -----------------------------

pick = open('model.sav', 'rb')
model = pickle.load(pick)
pick.close()

prediction = model.predict(xtest)
accuracy = model.score(xtest, ytest)

categories = ['JPG', 'TIF']

print('Accuracy: ', accuracy)
print('prediction is: ', categories[prediction[0]])


mypet = xtest[0].reshape(50,50)
plt.imshow(mypet, cmap='gray')
plt.show()


## ---------------- predicciones con una nueva imagen que no están en la bd de entrenamiento -------------------------------

# Cargar la nueva imagen
new_img_path = 'D:/NDVI_edited-testNDVI.jpg'
# new_img = cv2.imread(new_img_path, 0)  # Cargar en escala de grises
flattened_img = cv2.imread(new_img_path, 0) 

# Procesar la imagen
try:
    resized_img = cv2.resize(flattened_img, (50, 50))
    flattened_img = np.array(resized_img).flatten()
except Exception as e:
    pass


# Cargar el modelo SVM
pick = open('model.sav', 'rb')
model = pickle.load(pick)
pick.close()

# Predecir la categoría de la nueva imagen
prediction = model.predict([flattened_img])


# Mostrar la predicción
categories = ['JPG', 'TIF']
print('La nueva imagen pertenece a la categoría:', categories[prediction[0]])

# Mostrar la nueva imagen
plt.imshow(mypet, cmap='gray')
plt.imshow(resized_img, cmap='gray')
plt.show()