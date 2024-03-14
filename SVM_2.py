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

# Directorio de la carpeta imágenes
dir = "D:\BDnormalizada"
Catg = ['CULTIVO ENFERMO', 'CULTIVO SANO']
data = []

for category in Catg:
    path = os.path.join(dir, category)
    label = Catg.index(category)
    
    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        Br_img = cv2.imread(imgpath, 0)
        try:
            Br_img = cv2.resize(Br_img, (50, 50))
            image = np.array(Br_img).flatten()
            imagen_normalizada = image.astype(np.float32) / np.iinfo(image.dtype).max
            data.append([imagen_normalizada, label])
        except Exception as e:
            pass

print(len(data))

pick_in = open('BDnormalizada.pickle', 'wb')
pickle.dump(data, pick_in)
pick_in.close()

# --------------------------------------------------------------------------------------

pick_in = open('BDnormalizada.pickle', 'rb')
data = pickle.load(pick_in)
pick_in.close()

data_ab = data

random.shuffle(data)
features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

Catg = ['CULTIVO ENFERMO', 'CULTIVO SANO']


xtrain, xtest, ytrain, ytest = train_test_split(
    features, labels, test_size=0.7)

model = SVC(C=100, kernel='poly', gamma=1)
model.fit(xtrain, ytrain)

pick = open('modeloSVM.sav', 'wb')
pickle.dump(model, pick)
pick.close()

## ----------------------------- Hacer predicciones usando la bd de entrenamiento -----------------------------

pick = open('modeloSVM.sav', 'rb')
model = pickle.load(pick)
pick.close()

prediction = model.predict(xtest)
accuracy = model.score(xtest, ytest)

categories = ['CULTIVO ENFERMO', 'CULTIVO SANO']

print('Accuracy: ', accuracy)
print('prediction is: ', categories[prediction[5]])


# mypet = xtest[0].reshape(50,50)
# plt.imshow(xtest[0], cmap='gray')
# plt.show()

## ---------------- predicciones con una nueva imagen que no están en la bd de entrenamiento -------------------------------

# Cargar la nueva imagen
new_img_path = "D:\BD\DJI_20230606111929_0033_MS_R.TIF"

# Cargar en escala de grises
flattened_img = cv2.imread(new_img_path, 0) 

# Procesar la imagen
try:
    flattened_img = cv2.resize(flattened_img, (50, 50))
    array_img = np.array(flattened_img).flatten()
    imagen_normalizada = array_img.astype(np.float32) / np.iinfo(array_img.dtype).max
except Exception as e:
    pass

# Cargar el modelo SVM
pick = open('modeloSVM.sav', 'rb')
model = pickle.load(pick)
pick.close()

# Predecir la categoría de la nueva imagen
prediction = model.predict([imagen_normalizada])

# Mostrar la predicción
categories = ['CULTIVO ENFERMO', 'CULTIVO SANO']
print('La nueva imagen pertenece a la categoría:', categories[prediction[0]])

# Mostrar la nueva imagen
plt.imshow(flattened_img, cmap='gray')
plt.show()