# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:59:49 2022
@author: GLORIA GOMEZ
"""

import os
import numpy as np
import cv2
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Carga de datos
pick_in = open('data1.pickle', 'rb')
data = pickle.load(pick_in)
pick_in.close()

data_ab = data

# Barajar los datos
random.shuffle(data)
features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

Catg = ['isquemia', 'NMO', 'Normal', 'PRES']

# División de datos
xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.7)

# Carga del modelo SVM
pick = open('model.sav', 'rb')
model = pickle.load(pick)
pick.close()

# Predicción y evaluación
prediction = model.predict(xtest)
accuracy = model.score(xtest, ytest)

# Visualización de una imagen de prueba
Nbrain = xtest[0].reshape(50, 50)
plt.imshow(Nbrain, cmap='gray')
plt.show()

# Resultados
print('Accuracy', accuracy)
print('Anomalia real:', Catg[ytest[0]])
print('Anomalia identificada:', Catg[prediction[0]])
