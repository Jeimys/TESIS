# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:59:49 2022

@author: GLORIA GOMEZ
"""

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


root = Tk()
root.title("GUI software de identificación de imagenes en base SVM")
root.iconbitmap('ico_Br.ico')
root.geometry("800x600")

root['background'] = '#19232d'

img_1 = Image.open("UPB_logo.jpg")


# dir = 'C:\\Users\\gloes\\Desktop\\Codigo\\BrIm'
# Catg = ['isquemia', 'NMO', 'Normal', 'PRES']
# data = []

# for category in Catg:
#     path = os.path.join(dir, category)
#     label = Catg.index(category)
    
#     for img in os.listdir(path):
#         imgpath = os.path.join(path, img)
#         Br_img = cv2.imread(imgpath, 0)
#         try:
#             Br_img = cv2.resize(Br_img, (50, 50))
#             image = np.array(Br_img).flatten()
#             data.append([image, label])
#         except Exception as e:
#             pass

# print(len(data))

# pick_in = open('data1.pickle', 'wb')
# pickle.dump(data, pick_in)
# pick_in.close()

pick_in = open('data1.pickle', 'rb')
data = pickle.load(pick_in)
pick_in.close()

data_ab = data

random.shuffle(data)
features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

Catg = ['isquemia', 'NMO', 'Normal', 'PRES']


xtrain, xtest, ytrain, ytest = train_test_split(
    features, labels, test_size=0.7)

# model = SVC(C=100, kernel='poly', gamma=1)
# model.fit(xtrain, ytrain)

pick = open('model.sav', 'rb')
model = pickle.load(pick)
#pickle.dump(model, pick)
pick.close()

prediction = model.predict(xtest)
accuracy = model.score(xtest, ytest)

Catg = ['isquemia', 'NMO', 'Normal', 'PRES']

# print('Accuracy', accuracy)
# print('Prediction is :', Catg[prediction[0]])
# print(str(accuracy))


# print('Anomality is :', Catg[ytest[0]])



Nbrain = xtest[0].reshape(50, 50)

# Nbraina = xtrain[0].reshape(50, 50)

plt.imshow(Nbrain, cmap='gray')
# plt.imshow(Nbraina, cmap='gray')
plt.show()

upFrame = Frame(root, width=200, height=600)
upFrame.grid(row=0, column=0, padx=70, pady=2)

upFrame1 = Frame(root, width=200, height=600, bg='#19232d')
upFrame1.grid(row=0, column=1, padx=70, pady=2)


rightFrame = Frame(root, width=200, height=600)
rightFrame.grid(row=1, column=1, padx=70, pady=2)

leftFrame = Frame(root, width=200, height=600)
leftFrame.grid(row=1, column=0, padx=50, pady=10)

img_1 = Image.open("UPB_logo.jpg")

rsz_img1 = img_1.resize((220, 110), Image.ANTIALIAS)
N_img1 = ImageTk.PhotoImage(rsz_img1)
imgtk = ImageTk.PhotoImage(image=Image.fromarray(Nbrain))
# N_img = ImageTk.PhotoImage(Nbrain)

e = Entry(rightFrame, width=20)
e_1 = Entry(rightFrame, width=20)

e.grid(row=0, column=1)

e_1.grid(row=1, column=1)


def getName():
    name = e.get()
    label_a = Label(rightFrame, text=name)
    label_a.grid(row=3, column=1, padx=20)


def getAge():
    name = e_1.get()
    label_e = Label(rightFrame, text=name)
    label_e.grid(row=4, column=1, padx=20)


accuracy_percent = accuracy*100

label_logo = Label(upFrame, image=N_img1).grid(row=0, column=0)
label_img = Label(leftFrame, image=imgtk).grid(row=0, column=0)
label_a = Label(rightFrame, text="Nombre: ").grid(row=3, column=0, padx=20)
label_e = Label(rightFrame, text="Edad: ").grid(row=4, column=0, padx=20)
label_1 = Label(
    rightFrame, text="Anomalia: "
    + str(Catg[ytest[0]]))
label_1.grid(row=5, column=0, padx=20)
label_2 = Label(rightFrame,
                text="Identificada: "
                + str(Catg[prediction[0]]))
label_2.grid(row=6, column=0, padx=20)
label_3 = Label(rightFrame, text="Porcentaje de confiabilidad: "
                + str(accuracy_percent) + '%')
label_3.grid(row=7, column=0, padx=20)
label_5 = Label(upFrame1,
                text="UNIVERSIDAD PONTIFICIA BOLIVARIANA",
                bg='#19232d', fg='#fff').grid(row=0, column=0, padx=20)
label_6 = Label(upFrame1,
                text="Programa de ingenieria electronica",
                bg='#19232d', fg='#fff').grid(row=1, column=0, padx=20)
label_7 = Label(upFrame1,
                text="Desarrollado por: Juan D.",
                bg='#19232d', fg='#fff').grid(row=3, column=0, padx=20)


data_img = []


def openf():
    global label_img
    global img_l
    global img_r
    global label_2
    global label_3
    root.filename = filedialog.askopenfilename(
        initialdir='C:\\Users\\GLORIA GOMEZ\\.spyder-py3\\BrIm',
        title="Selecciona una imagen", filetypes=(("png files", "*.png"),
                                                  ("all files", "*.*")))
    img_l = Image.open(root.filename)
    Br_imgtemp = cv2.imread(root.filename, 0)
    Br_imgtemp = cv2.resize(Br_imgtemp, (50, 50))
    imagetemp = np.array(Br_imgtemp).flatten()
    data_img.append(imagetemp)
    prediction_t = model.predict(data_img)
    rzs_img = img_l.resize((250, 250), Image.ANTIALIAS)
    img_r = ImageTk.PhotoImage(rzs_img)
    label_img = Label(leftFrame, image=img_r).grid(row=0, column=0)
    label_1.grid_forget()
    label_2.grid_forget()
    label_2 = Label(
        rightFrame, text="Identificada: "
        + str(Catg[int(prediction_t)])).grid(row=6, column=0, padx=20)


# Br_imgtemp = cv2.imread('C:/Users/GLORIA GOMEZ/.spyder-py3/S_BrN.png', 0)
# Br_imgtemp = cv2.resize(Br_imgtemp, (50, 50))
# imagetemp = np.array(Br_imgtemp).flatten()
# data_img.append(imagetemp)

# prediction_t = model.predict(data_img)
# sa = int(prediction_t)
# print('Prediction is :', Catg[int(prediction_t)])


button_name = Button(rightFrame, text="Ingresar nombre",
                      command=getName).grid(row=0, column=0)

button_age = Button(rightFrame, text="Ingresar edad",
                    command=getAge).grid(row=1, column=0)

button_open = Button(leftFrame, text="Open", bg="#6F7997", fg="white",
                      command=openf).grid(row=1, column=0)


root.mainloop()
